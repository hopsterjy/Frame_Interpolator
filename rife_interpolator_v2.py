import os
import json
import tempfile
from fractions import Fraction
from pathlib import Path
import shutil
import subprocess
import threading
import customtkinter as ctk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES

# --- Create a compatible CustomTkinter root with Drag & Drop support ---
class TkinterDnD_CTk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

# PyInstaller sets __file__ inside its bundle directory, including one-file
# builds, where this directory is unpacked to a temporary location at launch.
BASE_DIR = Path(__file__).resolve().parent
RIFE_DIR = BASE_DIR / "lib" / "rife"
APP_SOURCE_REVISION = "ui-autonaming-2026-09-22"
MODELS = {
    "Regular": "rife-v4.25",
    "Lite": "rife-v4.25-lite",
    "Heavy": "rife-v4.25-heavy",
}

def find_model_dir(name):
    # Packaged layout first, then the folders beside the RIFE binary or script.
    candidates = (RIFE_DIR / "models" / name, RIFE_DIR / name,
                  BASE_DIR / "lib" / name, BASE_DIR / name)
    for folder in candidates:
        if all((folder / filename).is_file() for filename in ("flownet.bin", "flownet.param")):
            return folder
    raise FileNotFoundError(f"{name}: flownet.bin and flownet.param not found under ./lib or beside the app")

def find_rife_binary():
    for folder in (RIFE_DIR, BASE_DIR / "lib"):
        for filename in ("rife-ncnn-vulkan-ex.exe", "rife-ncnn-vulkan-ex",
                         "rife-ncnn-vulkan.exe", "rife-ncnn-vulkan"):
            candidate = folder / filename
            if candidate.is_file():
                return str(candidate)
    raise FileNotFoundError("RIFE executable missing: put it in ./lib/rife/ or ./lib/")

def find_ff_tool(name):
    if found := shutil.which(name):
        return found
    for filename in (name + ".exe", name):
        bundled = BASE_DIR / "lib" / "ffmpeg" / "bin" / filename
        if bundled.is_file():
            return str(bundled)
    raise FileNotFoundError(f"{name} missing from PATH and ./lib/ffmpeg/bin")

def parse_fps(value):
    value = value.strip()
    known = {"23.976": Fraction(24000, 1001), "29.97": Fraction(30000, 1001),
             "59.94": Fraction(60000, 1001), "119.88": Fraction(120000, 1001)}
    rate = known[value] if value in known else Fraction(value)
    if rate <= 0 or rate > 1000:
        raise ValueError("FPS must be between 0 and 1000")
    return rate

def target_count(source_count, source_fps, target_fps):
    if target_fps <= source_fps:
        raise ValueError("Target FPS must exceed source FPS")
    return round(Fraction(source_count) * target_fps / source_fps)

def suggested_output_path(input_path, fps):
    rate_label = f"{float(fps):.3f}".rstrip("0").rstrip(".")
    source = Path(input_path)
    return str(source.with_name(f"{source.stem}_{rate_label}fps.mp4"))

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class RifeApp(TkinterDnD_CTk):
    def __init__(self):
        super().__init__()

        self.title("Video Interpolator")
        self.geometry("650x850")
        self.resizable(False, False)
        
        self.detected_fps = None
        self.total_frames = 0
        
        self.start_frame_var = ctk.IntVar(value=0)
        self.end_frame_var = ctk.IntVar(value=0)
        self.custom_fps_var = ctk.StringVar()
        self.output_path_var = ctk.StringVar()
        self._output_is_auto = True
        self._setting_output_programmatically = False
        self.custom_fps_var.trace_add("write", self.on_custom_fps_change)
        self.output_path_var.trace_add("write", self.on_output_edit)

        # Reserve space before packing the main content so Windows display
        # scaling cannot compress the primary button at the bottom.
        self.footer = ctk.CTkFrame(self, fg_color="transparent", height=145)
        self.footer.pack(side="bottom", fill="x", padx=20, pady=(0, 10))
        self.footer.pack_propagate(False)

        # --- 1. INPUT UI ---
        self.lbl_input = ctk.CTkLabel(self, text="1. Input Video:")
        self.lbl_input.pack(pady=(20, 5), padx=20, anchor="w")
        
        self.frame_input = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_input.pack(fill="x", padx=20)
        self.entry_input = ctk.CTkEntry(self.frame_input, width=420)
        self.entry_input.pack(side="left", padx=(0, 10))
        self.btn_input = ctk.CTkButton(self.frame_input, text="Browse", width=100, command=self.select_input_file)
        self.btn_input.pack(side="left")

        # Drop Zone
        self.drop_zone = ctk.CTkFrame(self, height=60, fg_color="#2b2b2b", corner_radius=8, border_width=2, border_color="#565b5e")
        self.drop_zone.pack(fill="x", padx=20, pady=(10, 0))
        self.drop_zone.pack_propagate(False)
        
        self.lbl_drop = ctk.CTkLabel(self.drop_zone, text="Drag & Drop .mp4 / .mov file here", text_color="gray", font=("Arial", 14))
        self.lbl_drop.pack(expand=True)

        self.drop_zone.drop_target_register(DND_FILES)
        self.drop_zone.dnd_bind('<<Drop>>', self.handle_file_drop)

        self.lbl_fps = ctk.CTkLabel(self, text="Video Info: None", text_color="gray", font=("Arial", 12))
        self.lbl_fps.pack(pady=(10, 10), padx=25, anchor="w")

        # --- 2. TRIM UI ---
        self.lbl_trim = ctk.CTkLabel(self, text="2. Trim Timeline (Optional):")
        self.lbl_trim.pack(pady=(15, 0), padx=20, anchor="w")

        self.frame_trim = ctk.CTkFrame(self, fg_color="#1d1d1d", corner_radius=10, border_width=1, border_color="#3a3a3a")
        self.frame_trim.pack(fill="x", padx=20, pady=(5, 5))

        self.timeline_bar = ctk.CTkFrame(self.frame_trim, height=10, fg_color="#3a3a3a", corner_radius=5)
        self.timeline_bar.pack(fill="x", padx=15, pady=(15, 0))
        
        self.lbl_timeline_title = ctk.CTkLabel(self.frame_trim, text="TIMELINE CONTROL", text_color="gray", font=("Arial", 11, "bold"))
        self.lbl_timeline_title.pack(pady=(2, 10))

        self.trim_controls = ctk.CTkFrame(self.frame_trim, fg_color="transparent")
        self.trim_controls.pack(fill="x", padx=15, pady=10)

        # Start Slider
        self.lbl_start_val = ctk.CTkLabel(self.trim_controls, text="Start Frame: 0", width=120, anchor="w")
        self.lbl_start_val.grid(row=0, column=0, padx=5, pady=5)
        self.slider_start = ctk.CTkSlider(self.trim_controls, from_=0, to=100, width=450, command=self.on_start_drag)
        self.slider_start.grid(row=0, column=1, padx=5, pady=5)

        # End Slider
        self.lbl_end_val = ctk.CTkLabel(self.trim_controls, text="End Frame: 0", width=120, anchor="w")
        self.lbl_end_val.grid(row=1, column=0, padx=5, pady=5)
        self.slider_end = ctk.CTkSlider(self.trim_controls, from_=0, to=100, width=450, button_color="#C8504B", button_hover_color="#A0403C", command=self.on_end_drag)
        self.slider_end.grid(row=1, column=1, padx=5, pady=5)
        
        self.slider_start.configure(state="disabled")
        self.slider_end.configure(state="disabled")

        # --- 3. TARGET FRAMERATE UI ---
        self.lbl_target = ctk.CTkLabel(self, text="3. Target FPS:")
        self.lbl_target.pack(pady=(15, 5), padx=20, anchor="w")

        self.frame_target = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_target.pack(fill="x", padx=20)
        
        self.option_mode = ctk.CTkOptionMenu(self.frame_target, values=["30", "48", "60", "59.94", "120", "Custom FPS"], command=self.on_mode_change)
        self.option_mode.pack(side="left", padx=(0, 10))
        self.option_mode.set("60")
        
        self.entry_target_fps = ctk.CTkEntry(self.frame_target, width=110,
                                              textvariable=self.custom_fps_var,
                                              placeholder_text="24000/1001")
        self.entry_target_fps.pack(side="left", padx=(0, 5))
        self.entry_target_fps.configure(state="disabled")
        
        self.lbl_fps_unit = ctk.CTkLabel(self.frame_target, text="FPS", font=("Arial", 13))
        self.lbl_fps_unit.pack(side="left")

        self.lbl_model = ctk.CTkLabel(self.frame_target, text="Model:", width=55)
        self.lbl_model.pack(side="left", padx=(25, 5))
        self.option_model = ctk.CTkOptionMenu(self.frame_target, values=list(MODELS), width=140)
        self.option_model.pack(side="left")
        self.option_model.set("Regular")

        # --- 4. SAVE PATH UI ---
        self.lbl_output = ctk.CTkLabel(self, text="4. Save Output As:")
        self.lbl_output.pack(pady=(20, 5), padx=20, anchor="w")
        
        self.frame_output = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_output.pack(fill="x", padx=20)
        self.entry_output = ctk.CTkEntry(self.frame_output, width=420,
                                          textvariable=self.output_path_var)
        self.entry_output.pack(side="left", padx=(0, 10))
        self.btn_output = ctk.CTkButton(self.frame_output, text="Save As...", width=100, command=self.select_output_file)
        self.btn_output.pack(side="left")

        self.frame_options = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_options.pack(fill="x", padx=25, pady=10)

        self.chk_audio_var = ctk.IntVar(value=1)
        self.chk_audio = ctk.CTkCheckBox(self.frame_options, text="Include Original Audio Track", variable=self.chk_audio_var)
        self.chk_audio.pack(pady=5, anchor="w")

        self.chk_cleanup_var = ctk.IntVar(value=1)
        self.chk_cleanup = ctk.CTkCheckBox(self.frame_options, text="Delete temporary frames after completion", variable=self.chk_cleanup_var)
        self.chk_cleanup.pack(pady=5, anchor="w")

        # Status Bar & Start Button
        self.lbl_status = ctk.CTkLabel(self.footer, text="Ready", text_color="gray", font=("Arial", 14))
        self.lbl_status.pack(pady=(5, 4))

        self.progressbar = ctk.CTkProgressBar(self.footer, width=550)
        self.progressbar.pack(pady=5)
        self.progressbar.set(0)

        self.btn_start = ctk.CTkButton(self.footer, text="Start Interpolation", width=300,
                                        height=54, font=("Arial", 16, "bold"),
                                        command=self.start_processing)
        self.btn_start.pack(pady=(10, 5))

    # --- Slider Handlers ---
    def on_start_drag(self, value):
        val = int(value)
        end_val = self.end_frame_var.get()
        if val >= end_val:
            val = max(0, end_val - 1)
            self.slider_start.set(val)
            
        self.start_frame_var.set(val)
        self.lbl_start_val.configure(text=f"Start Frame: {val}")

    def on_end_drag(self, value):
        val = int(value)
        start_val = self.start_frame_var.get()
        if val <= start_val:
            val = min(self.total_frames - 1, start_val + 1)
            self.slider_end.set(val)
            
        self.end_frame_var.set(val)
        self.lbl_end_val.configure(text=f"End Frame: {val}")

    # --- Core Helpers ---
    def handle_file_drop(self, event):
        files = self.tk.splitlist(event.data)
        if files:
            file_path = files[0].strip('"\'')
            if file_path.lower().endswith(('.mp4', '.mov', '.mkv', '.avi')):
                self.load_video_data(file_path)
                return
        self.safe_update_status("❌ Please drop a valid video file (.mp4, .mov, etc.)", 0, "red")

    def select_input_file(self):
        filename = filedialog.askopenfilename(title="Select Input Video", filetypes=[("Video files", "*.mp4 *.mov *.mkv *.avi")])
        if filename:
            self.load_video_data(filename)

    def load_video_data(self, filepath):
        filepath = filepath.strip('"\' ')
        self.detected_fps = None
        self.total_frames = 0
        self.slider_start.configure(state="disabled")
        self.slider_end.configure(state="disabled")
        self.entry_input.delete(0, 'end')
        self.entry_input.insert(0, filepath)
        
        try:
            fps, frames = self.get_video_info(filepath)
        except (OSError, ValueError, KeyError, IndexError, subprocess.CalledProcessError) as exc:
            self.lbl_fps.configure(text="Could not inspect video", text_color="red")
            self.update_status(f"❌ {str(exc)[:95]}", 0, "red")
            return
        self.detected_fps = fps
        self.total_frames = frames
        self.lbl_fps.configure(text=f"Detected: {float(fps):.3f} FPS ({fps}) | Total Frames: {frames}", text_color="#2FA572")
            
        self.slider_start.configure(state="normal", to=frames - 1)
        self.slider_end.configure(state="normal", to=frames - 1)
        self.slider_start.set(0)
        self.slider_end.set(frames - 1)
        self.start_frame_var.set(0)
        self.end_frame_var.set(frames - 1)
        self.lbl_start_val.configure(text="Start Frame: 0")
        self.lbl_end_val.configure(text=f"End Frame: {frames - 1}")
        self._output_is_auto = True
        self.refresh_suggested_output()
        self.update_status("Ready", 0)

    def get_video_info(self, filepath):
        result = subprocess.run([find_ff_tool("ffprobe"), "-v", "error", "-select_streams", "v:0",
            "-count_frames", "-show_entries",
            "stream=avg_frame_rate,r_frame_rate,nb_frames,nb_read_frames,duration:format=duration",
            "-of", "json", filepath], capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        stream = data["streams"][0]
        rates = []
        for field in ("avg_frame_rate", "r_frame_rate"):
            try:
                rate = Fraction(stream.get(field, "0"))
            except (ValueError, ZeroDivisionError, TypeError):
                continue
            if rate > 0:
                rates.append(rate)
        fps = rates[0] if rates else None
        if fps is None:
            raise ValueError("Video has no valid frame rate")
        frames = next((int(value) for field in ("nb_read_frames", "nb_frames")
                       if (value := stream.get(field)) not in (None, "N/A", "0")), None)
        if frames is None:
            duration = stream.get("duration") or data.get("format", {}).get("duration")
            if not duration:
                raise ValueError("Could not determine video frame count")
            frames = round(Fraction(duration) * fps)
        if frames < 2:
            raise ValueError("Video needs at least two frames")
        return fps, frames

    def calculate_target_fps(self):
        custom = self.option_mode.get() == "Custom FPS"
        self.entry_target_fps.configure(state="normal" if custom else "disabled")
        if custom and not self.custom_fps_var.get().strip():
            self.custom_fps_var.set("60")
        self.refresh_suggested_output()

    def on_mode_change(self, choice):
        self.calculate_target_fps()

    def on_custom_fps_change(self, *_):
        if self.option_mode.get() == "Custom FPS":
            self.refresh_suggested_output()

    def on_output_edit(self, *_):
        if not self._setting_output_programmatically:
            self._output_is_auto = False

    def refresh_suggested_output(self):
        if not self._output_is_auto or not self.entry_input.get().strip():
            return
        selected = (self.custom_fps_var.get() if self.option_mode.get() == "Custom FPS"
                    else self.option_mode.get())
        try:
            path = suggested_output_path(self.entry_input.get().strip(), parse_fps(selected))
        except ValueError:
            return  # The user may still be typing a custom FPS.
        self._setting_output_programmatically = True
        try:
            self.output_path_var.set(path)
        finally:
            self._setting_output_programmatically = False

    def select_output_file(self):
        current = Path(self.entry_output.get().strip() or "output.mp4")
        filename = filedialog.asksaveasfilename(title="Save As", defaultextension=".mp4",
            initialdir=str(current.parent), initialfile=current.name,
            filetypes=[("MP4 video", "*.mp4")])
        if filename:
            self.output_path_var.set(filename)

    def safe_update_status(self, text, progress=None, color="gray"):
        self.after(0, lambda: self.update_status(text, progress, color))

    def update_status(self, text, progress=None, color="gray"):
        self.lbl_status.configure(text=text, text_color=color)
        if progress is not None:
            self.progressbar.set(progress)

    def start_processing(self):
        input_video = self.entry_input.get().strip().strip('"\'')
        output_video = self.entry_output.get().strip().strip('"\'')
        try:
            if not input_video or not os.path.isfile(input_video):
                raise ValueError("Choose an existing input video")
            if not output_video or Path(output_video).suffix.lower() != ".mp4":
                raise ValueError("Choose an MP4 output path")
            if Path(input_video).resolve() == Path(output_video).resolve():
                raise ValueError("Input and output must be different files")
            if not Path(output_video).parent.is_dir():
                raise ValueError("Output folder does not exist")
            if self.detected_fps is None or self.total_frames < 2:
                raise ValueError("Load a valid video first")
            selection = (self.entry_target_fps.get() if self.option_mode.get() == "Custom FPS"
                         else self.option_mode.get())
            target_fps = parse_fps(selection)
            start_f, end_f = self.start_frame_var.get(), self.end_frame_var.get()
            if not 0 <= start_f < end_f < self.total_frames:
                raise ValueError("Select at least two consecutive source frames")
            target_count(end_f - start_f + 1, self.detected_fps, target_fps)
            ffmpeg = find_ff_tool("ffmpeg")
            rife_bin = find_rife_binary()
            model_dir = find_model_dir(MODELS[self.option_model.get()])
            include_audio = bool(self.chk_audio_var.get())
            cleanup = bool(self.chk_cleanup_var.get())
        except (OSError, ValueError, KeyError, ZeroDivisionError) as exc:
            self.update_status(f"❌ {str(exc)[:100]}", 0, "red")
            return
        self.btn_start.configure(state="disabled")
        threading.Thread(target=self.run_pipeline,
            args=(input_video, output_video, target_fps, self.detected_fps,
                  start_f, end_f, ffmpeg, rife_bin, model_dir, include_audio, cleanup),
            daemon=True).start()

    def run_pipeline(self, input_video, output_video, target_fps, source_fps,
                     start_f, end_f, ffmpeg, rife_bin, model_dir, include_audio, cleanup):
        work = Path(tempfile.mkdtemp(prefix="rife-v2-"))
        input_frames, output_frames = work / "input", work / "output"
        input_frames.mkdir()
        output_frames.mkdir()
        video_only = work / "video.mp4"
        staged_output = None
        try:
            self.safe_update_status(f"1/4: Extracting frames {start_f}–{end_f}...", 0.1)
            extract = [ffmpeg, "-hide_banner", "-y", "-i", input_video, "-map", "0:v:0",
                "-vf", f"select=between(n\\,{start_f}\\,{end_f})", "-fps_mode", "passthrough",
                "-start_number", "0", str(input_frames / "%08d.png")]
            subprocess.run(extract, check=True, capture_output=True, text=True)
            extracted = sum(1 for _ in input_frames.glob("*.png"))
            if extracted < 2:
                raise ValueError("Fewer than two frames were extracted")
            target_total = target_count(extracted, source_fps, target_fps)

            self.safe_update_status(f"2/4: Interpolating {target_total} frames...", 0.3)
            print(f"RIFE executable: {rife_bin}\nRIFE model: {model_dir}")
            rife_cmd = [rife_bin, "-i", str(input_frames), "-o", str(output_frames),
                        "-n", str(target_total), "-m", str(model_dir)]
            result = subprocess.run(rife_cmd, cwd=str(Path(rife_bin).parent),
                                    capture_output=True, text=True)
            if "layer MemoryData not exists or registered" in (result.stderr + result.stdout):
                raise RuntimeError(
                    f"{Path(rife_bin).name} cannot load {model_dir.name}: its NCNN build lacks MemoryData. "
                    "Use a compatible RIFE 4.25 executable; see the setup guide.")
            if result.returncode != 0:
                raise RuntimeError(f"RIFE failed: {(result.stderr or result.stdout)[-700:]}")
            if (actual := sum(1 for _ in output_frames.glob("*.png"))) != target_total:
                raise RuntimeError(f"RIFE produced {actual} frames, expected {target_total}")

            fps_arg = f"{target_fps.numerator}/{target_fps.denominator}"
            self.safe_update_status("3/4: Encoding video...", 0.85)
            encode = [ffmpeg, "-hide_banner", "-y", "-framerate", fps_arg,
                "-start_number", "0", "-i", str(output_frames / "%08d.png"),
                "-frames:v", str(target_total), "-c:v", "libx264", "-crf", "18",
                "-pix_fmt", "yuv420p", str(video_only)]
            subprocess.run(encode, check=True, capture_output=True, text=True)

            with tempfile.NamedTemporaryFile(prefix="rife-result-", suffix=".mp4",
                    dir=str(Path(output_video).parent), delete=False) as tmp:
                staged_output = Path(tmp.name)
            self.safe_update_status("4/4: Finalizing audio and video...", 0.95)
            if include_audio:
                audio_start = float(Fraction(start_f) / source_fps)
                audio_length = float(Fraction(extracted) / source_fps)
                merge = [ffmpeg, "-hide_banner", "-y", "-i", str(video_only),
                    "-ss", str(audio_start), "-t", str(audio_length), "-i", input_video,
                    "-map", "0:v:0", "-map", "1:a:0?", "-c:v", "copy", "-c:a", "aac",
                    str(staged_output)]
                subprocess.run(merge, check=True, capture_output=True, text=True)
            else:
                shutil.copyfile(video_only, staged_output)
            os.replace(staged_output, output_video)
            staged_output = None
            self.safe_update_status("✅ Process finished successfully!", 1, "#2FA572")
        except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
            detail = exc.stderr if isinstance(exc, subprocess.CalledProcessError) else str(exc)
            print(f"Pipeline error: {detail}")
            self.safe_update_status(f"❌ Failed: {str(detail).strip()[-100:]}", 0, "red")
        finally:
            if staged_output is not None:
                staged_output.unlink(missing_ok=True)
            if cleanup:
                shutil.rmtree(work, ignore_errors=True)
            else:
                print(f"Temporary frames retained: {work}")
            self.after(0, lambda: self.btn_start.configure(state="normal"))

if __name__ == "__main__":
    app = RifeApp()
    app.mainloop()
