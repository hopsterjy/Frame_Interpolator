# Frame Interpolator (RIFE v2)

A clean, modern desktop GUI application for AI video frame rate upsampling and frame interpolation using RIFE (Real-Time Intermediate Flow Estimation) via NCNN Vulkan and FFmpeg.

Built with Python, CustomTkinter, and TkinterDnD2.

---

## Author

- **Jinu Yang** – [GitHub (@hopsterjy)](https://github.com/hopsterjy)

---

## Features

- **Modern Dark UI**: Powered by CustomTkinter with drag-and-drop file support (`.mp4`, `.mov`, `.mkv`, `.avi`).
- **Precision Timeline Trimming**: Interactive dual-slider timeline controls to isolate exact frame ranges.
- **Accurate FPS Conversion**: Automatic detection of native stream framerates (including standard NTSC fractions like 23.976, 29.97, 59.94) and arbitrary custom framerate inputs.
- **Auto-Naming Output**: Intelligently names output files with the target FPS appended (e.g., `clip_60fps.mp4`).
- **Model Preset Selector**: Support for Regular (`rife-v4.25`), Lite (`rife-v4.25-lite`), and Heavy (`rife-v4.25-heavy`) RIFE models.
- **Audio Synchronization**: Automatically trims and remuxes original audio tracks to match trimmed frame bounds without desync.
- **Auto-Cleanup**: Option to clean up temporary frame extraction directories automatically after encoding.

---

## Folder Structure

To run the application, ensure external binaries and model weights are placed inside the expected `./lib` hierarchy (these files are ignored by git to keep the repository lightweight):

```text
Frame_Interpolator/
├── rife_interpolator_v2.py
├── requirements.txt
├── README.md
├── .gitignore
└── lib/
    ├── rife/
    │   ├── rife-ncnn-vulkan.exe     # or rife-ncnn-vulkan-ex.exe / Linux/macOS binary
    │   └── models/
    │       ├── rife-v4.25/
    │       │   ├── flownet.bin
    │       │   └── flownet.param
    │       ├── rife-v4.25-lite/
    │       │   ├── flownet.bin
    │       │   └── flownet.param
    │       └── rife-v4.25-heavy/
    │           ├── flownet.bin
    │           └── flownet.param
    └── ffmpeg/
        └── bin/
            ├── ffmpeg.exe           # (Optional if ffmpeg is in your system PATH)
            └── ffprobe.exe          # (Optional if ffprobe is in your system PATH)