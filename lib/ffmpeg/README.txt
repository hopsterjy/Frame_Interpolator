FFmpeg 64-bit static Windows build from www.gyan.dev

Version: 2026-09-21-git-a9cbcc2bbb-essentials_build-www.gyan.dev

License: GPL v3

Source Code: https://github.com/FFmpeg/FFmpeg/commit/a9cbcc2bbb

git-essentials build configuration: 

ARCH                      x86 (generic)
big-endian                no
runtime cpu detection     yes
standalone assembly       yes
x86 assembler             nasm
MMX enabled               yes
MMXEXT enabled            yes
SSE enabled               yes
SSSE3 enabled             yes
AESNI enabled             yes
CLMUL enabled             yes
AVX enabled               yes
AVX2 enabled              yes
AVX-512 enabled           yes
AVX-512ICL enabled        yes
XOP enabled               yes
FMA3 enabled              yes
FMA4 enabled              yes
i686 features enabled     yes
CMOV is fast              yes
EBX available             yes
6 registers available     yes
7 registers available     yes
debug symbols             yes
strip symbols             yes
optimize for size         no
optimizations             yes
static                    yes
shared                    no
network support           yes
threading support         pthreads
safe bitstream reader     yes
texi2html enabled         no
perl enabled              yes
pod2man enabled           yes
makeinfo enabled          yes
makeinfo supports HTML    yes
experimental features     yes
xmllint enabled           yes

External libraries:
avisynth                libmp3lame              libvorbis
bzlib                   libopencore_amrnb       libvpx
cairo                   libopencore_amrwb       libwebp
gmp                     libopenjpeg             libx264
gnutls                  libopenmpt              libx265
iconv                   libopus                 libxml2
libaom                  librubberband           libxvid
libass                  libspeex                libzimg
libfontconfig           libsrt                  libzmq
libfreetype             libssh                  lzma
libfribidi              libtheora               mediafoundation
libgme                  libvidstab              openal
libgsm                  libvmaf                 sdl2
libharfbuzz             libvo_amrwbenc          zlib

External libraries providing hardware acceleration:
amf                     d3d12va                 nvdec
cuda                    dxva2                   nvenc
cuda_llvm               ffnvcodec               vaapi
cuvid                   libmfx
d3d11va                 libvpl

Libraries:
avcodec                 avformat                swscale
avdevice                avutil
avfilter                swresample

Programs:
ffmpeg                  ffplay                  ffprobe

Enabled decoders:
aac                     flac                    pcm_u8
aac_fixed               flashsv                 pcm_vidc
aac_latm                flashsv2                pcx
aasc                    flic                    pdv
ac3                     flv                     pfm
ac3_fixed               fmvc                    pgm
acelp_kelvin            fourxm                  pgmyuv
adpcm_4xm               fraps                   pgssub
adpcm_adx               frwu                    pgx
adpcm_afc               ftr                     phm
adpcm_agm               g2m                     photocd
adpcm_aica              g723_1                  pictor
adpcm_argo              g728                    pixlet
adpcm_circus            g729                    pjs
adpcm_ct                gdv                     png
adpcm_dtk               gem                     ppm
adpcm_ea                gif                     prores
adpcm_ea_maxis_xa       gremlin_dpcm            prores_raw
adpcm_ea_r1             gsm                     prosumer
adpcm_ea_r2             gsm_ms                  psd
adpcm_ea_r3             h261                    ptx
adpcm_ea_xas            h263                    qcelp
adpcm_g722              h263i                   qdm2
adpcm_g726              h263p                   qdmc
adpcm_g726le            h264                    qdraw
adpcm_ima_acorn         h264_amf                qoa
adpcm_ima_alp           h264_cuvid              qoi
adpcm_ima_amv           h264_qsv                qpeg
adpcm_ima_apc           hap                     qtrle
adpcm_ima_apm           hca                     r10k
adpcm_ima_cunning       hcom                    r210
adpcm_ima_dat4          hdr                     ra_144
adpcm_ima_dk3           hevc                    ra_288
adpcm_ima_dk4           hevc_amf                ralf
adpcm_ima_ea_eacs       hevc_cuvid              rasc
adpcm_ima_ea_sead       hevc_qsv                rawvideo
adpcm_ima_escape        hnm4_video              realtext
adpcm_ima_hvqm2         hq_hqa                  rka
adpcm_ima_hvqm4         hqx                     rl2
adpcm_ima_iss           huffyuv                 roq
adpcm_ima_magix         hymt                    roq_dpcm
adpcm_ima_moflex        iac                     rpza
adpcm_ima_mtf           idcin                   rscc
adpcm_ima_oki           idf                     rtv1
adpcm_ima_pda           iff_ilbm                rv10
adpcm_ima_qt            ilbc                    rv20
adpcm_ima_rad           imc                     rv30
adpcm_ima_smjpeg        imm4                    rv40
adpcm_ima_ssi           imm5                    rv60
adpcm_ima_wav           indeo2                  s302m
adpcm_ima_ws            indeo3                  sami
adpcm_ima_xbox          indeo4                  sanm
adpcm_ms                indeo5                  sbc
adpcm_mtaf              interplay_acm           scpr
adpcm_n64               interplay_dpcm          screenpresso
adpcm_psx               interplay_video         sdx2_dpcm
adpcm_psxc              ipu                     sga
adpcm_sanyo             jacosub                 sgi
adpcm_sbpro_2           jpeg2000                sgirle
adpcm_sbpro_3           jpegls                  sheervideo
adpcm_sbpro_4           jv                      shorten
adpcm_swf               kgv1                    simbiosis_imx
adpcm_thp               kmvc                    sipr
adpcm_thp_le            lagarith                siren
adpcm_vima              lead                    smackaud
adpcm_xa                libaom_av1              smacker
adpcm_xmd               libgsm                  smc
adpcm_yamaha            libgsm_ms               smvjpeg
adpcm_zork              libopencore_amrnb       snow
agm                     libopencore_amrwb       sol_dpcm
ahx                     libopus                 sp5x
aic                     libspeex                speedhq
alac                    libvorbis               speex
alias_pix               libvpx_vp8              srgc
als                     libvpx_vp9              srt
amrnb                   loco                    ssa
amrwb                   lscr                    stl
amv                     m101                    subrip
anm                     mace3                   subviewer
ansi                    mace6                   subviewer1
anull                   magicyuv                sunrast
apac                    mdec                    svq1
ape                     media100                svq3
apng                    metasound               tak
aptx                    microdvd                targa
aptx_hd                 mimic                   targa_y216
apv                     misc4                   tdsc
arbc                    mjpeg                   text
argo                    mjpeg_cuvid             theora
ass                     mjpeg_qsv               thp
asv1                    mjpegb                  tiertexseqvideo
asv2                    mlp                     tiff
atrac1                  mmvideo                 tmv
atrac3                  mobiclip                truehd
atrac3al                motionpixels            truemotion1
atrac3p                 movtext                 truemotion2
atrac3pal               mp1                     truemotion2rt
atrac9                  mp1float                truespeech
aura                    mp2                     tscc
aura2                   mp2float                tscc2
av1                     mp3                     tta
av1_amf                 mp3adu                  twinvq
av1_cuvid               mp3adufloat             txd
av1_qsv                 mp3float                ulti
avrn                    mp3on4                  utvideo
avrp                    mp3on4float             v210
avs                     mpc7                    v210x
avui                    mpc8                    vb
bethsoftvid             mpeg1_cuvid             vble
bfi                     mpeg1video              vbn
bink                    mpeg2_cuvid             vc1
binkaudio_dct           mpeg2_qsv               vc1_cuvid
binkaudio_rdft          mpeg2video              vc1_qsv
bintext                 mpeg4                   vc1image
bitpacked               mpeg4_cuvid             vcr1
bmp                     mpegvideo               vmdaudio
bmv_audio               mpl2                    vmdvideo
bmv_video               msa1                    vmix
bonk                    mscc                    vmnc
brender_pix             msmpeg4v1               vnull
c93                     msmpeg4v2               vorbis
cavs                    msmpeg4v3               vp3
cbd2_dpcm               msnsiren                vp4
ccaption                msp2                    vp5
cdgraphics              msrle                   vp6
cdtoons                 mss1                    vp6a
cdxl                    mss2                    vp6f
cfhd                    msvideo1                vp7
cinepak                 mszh                    vp8
clearvideo              mts2                    vp8_cuvid
cljr                    mv30                    vp8_qsv
cllc                    mvc1                    vp9
comfortnoise            mvc2                    vp9_amf
cook                    mvdv                    vp9_cuvid
cpia                    mvha                    vp9_qsv
cri                     mwsc                    vplayer
cscd                    mxpeg                   vqa
cyuv                    nellymoser              vqc
dca                     notchlc                 vvc
dds                     nuv                     vvc_qsv
derf_dpcm               on2avc                  wady_dpcm
dfa                     opus                    wavarc
dfpwm                   osq                     wavpack
dirac                   paf_audio               wbmp
dnxhd                   paf_video               wcmv
dolby_e                 pam                     webp
dpx                     pbm                     webp_anim
dsd_lsbf                pcm_alaw                webvtt
dsd_lsbf_planar         pcm_bluray              wmalossless
dsd_msbf                pcm_dvd                 wmapro
dsd_msbf_planar         pcm_dvda                wmav1
dsicinaudio             pcm_f16le               wmav2
dsicinvideo             pcm_f24le               wmavoice
dss_sp                  pcm_f32be               wmv1
dst                     pcm_f32le               wmv2
dvaudio                 pcm_f64be               wmv3
dvbsub                  pcm_f64le               wmv3image
dvdsub                  pcm_lxf                 wnv1
dvvideo                 pcm_mulaw               wrapped_avframe
dxa                     pcm_s16be               ws_snd1
dxtory                  pcm_s16be_planar        xan_dpcm
dxv                     pcm_s16le               xan_wc3
eac3                    pcm_s16le_planar        xan_wc4
eacmv                   pcm_s24be               xbin
eamad                   pcm_s24daud             xbm
eatgq                   pcm_s24le               xface
eatgv                   pcm_s24le_planar        xl
eatqi                   pcm_s32be               xma1
eightbps                pcm_s32le               xma2
eightsvx_exp            pcm_s32le_planar        xpm
eightsvx_fib            pcm_s64be               xsub
escape124               pcm_s64le               xwd
escape130               pcm_s8                  y41p
evrc                    pcm_s8_planar           ylc
exr                     pcm_sga                 yop
fastaudio               pcm_u16be               yuv4
ffv1                    pcm_u16le               zero12v
ffvhuff                 pcm_u24be               zerocodec
ffwavesynth             pcm_u24le               zlib
fic                     pcm_u32be               zmbv
fits                    pcm_u32le

Enabled encoders:
a64multi                h264_vaapi              pcm_s8
a64multi5               hdr                     pcm_s8_planar
aac                     hevc_amf                pcm_u16be
aac_mf                  hevc_d3d12va            pcm_u16le
ac3                     hevc_mf                 pcm_u24be
ac3_fixed               hevc_nvenc              pcm_u24le
ac3_mf                  hevc_qsv                pcm_u32be
adpcm_adx               hevc_vaapi              pcm_u32le
adpcm_argo              huffyuv                 pcm_u8
adpcm_g722              jpeg2000                pcm_vidc
adpcm_g726              jpegls                  pcx
adpcm_g726le            libaom_av1              pdv
adpcm_ima_alp           libgsm                  pfm
adpcm_ima_amv           libgsm_ms               pgm
adpcm_ima_apm           libmp3lame              pgmyuv
adpcm_ima_qt            libopencore_amrnb       phm
adpcm_ima_ssi           libopenjpeg             png
adpcm_ima_wav           libopus                 ppm
adpcm_ima_ws            libspeex                prores
adpcm_ms                libtheora               prores_aw
adpcm_swf               libvo_amrwbenc          prores_ks
adpcm_yamaha            libvorbis               qoi
alac                    libvpx_vp8              qtrle
alias_pix               libvpx_vp9              r10k
amv                     libwebp                 r210
anull                   libwebp_anim            ra_144
apng                    libx264                 rawvideo
aptx                    libx264rgb              roq
aptx_hd                 libx265                 roq_dpcm
ass                     libxvid                 rpza
asv1                    ljpeg                   rv10
asv2                    magicyuv                rv20
av1_amf                 mjpeg                   s302m
av1_d3d12va             mjpeg_qsv               sbc
av1_mf                  mjpeg_vaapi             sgi
av1_nvenc               mlp                     smc
av1_qsv                 movtext                 snow
av1_vaapi               mp2                     speedhq
avrp                    mp2fixed                srt
avui                    mp3_mf                  ssa
bitpacked               mpeg1video              subrip
bmp                     mpeg2_qsv               sunrast
cfhd                    mpeg2_vaapi             svq1
cinepak                 mpeg2video              targa
cljr                    mpeg4                   text
comfortnoise            msmpeg4v2               tiff
dca                     msmpeg4v3               truehd
dfpwm                   msrle                   tta
dnxhd                   msvideo1                ttml
dpx                     nellymoser              utvideo
dsd_msbf                opus                    v210
dvbsub                  pam                     vbn
dvdsub                  pbm                     vc2
dvvideo                 pcm_alaw                vnull
dxv                     pcm_bluray              vorbis
eac3                    pcm_dvd                 vp8_vaapi
exr                     pcm_f32be               vp9_qsv
ffv1                    pcm_f32le               vp9_vaapi
ffvhuff                 pcm_f64be               wavpack
fits                    pcm_f64le               wbmp
flac                    pcm_mulaw               webvtt
flashsv                 pcm_s16be               wmav1
flashsv2                pcm_s16be_planar        wmav2
flv                     pcm_s16le               wmv1
g723_1                  pcm_s16le_planar        wmv2
gif                     pcm_s24be               wrapped_avframe
h261                    pcm_s24daud             xbm
h263                    pcm_s24le               xface
h263p                   pcm_s24le_planar        xsub
h264_amf                pcm_s32be               xwd
h264_d3d12va            pcm_s32le               y41p
h264_mf                 pcm_s32le_planar        yuv4
h264_nvenc              pcm_s64be               zlib
h264_qsv                pcm_s64le               zmbv

Enabled hwaccels:
av1_d3d11va             hevc_vaapi              vc1_vaapi
av1_d3d11va2            mjpeg_nvdec             vp8_nvdec
av1_d3d12va             mjpeg_vaapi             vp8_nvdec_cuarray
av1_dxva2               mpeg1_nvdec             vp8_vaapi
av1_nvdec               mpeg1_nvdec_cuarray     vp9_d3d11va
av1_nvdec_cuarray       mpeg2_d3d11va           vp9_d3d11va2
av1_vaapi               mpeg2_d3d11va2          vp9_d3d12va
h263_vaapi              mpeg2_d3d12va           vp9_dxva2
h264_d3d11va            mpeg2_dxva2             vp9_nvdec
h264_d3d11va2           mpeg2_nvdec             vp9_nvdec_cuarray
h264_d3d12va            mpeg2_nvdec_cuarray     vp9_vaapi
h264_dxva2              mpeg2_vaapi             vvc_vaapi
h264_nvdec              mpeg4_nvdec             wmv3_d3d11va
h264_nvdec_cuarray      mpeg4_nvdec_cuarray     wmv3_d3d11va2
h264_vaapi              mpeg4_vaapi             wmv3_d3d12va
hevc_d3d11va            vc1_d3d11va             wmv3_dxva2
hevc_d3d11va2           vc1_d3d11va2            wmv3_nvdec
hevc_d3d12va            vc1_d3d12va             wmv3_nvdec_cuarray
hevc_dxva2              vc1_dxva2               wmv3_vaapi
hevc_nvdec              vc1_nvdec
hevc_nvdec_cuarray      vc1_nvdec_cuarray

Enabled parsers:
aac                     dvdsub                  mpegaudio
aac_latm                evc                     mpegvideo
ac3                     ffv1                    opus
adx                     flac                    png
ahx                     ftr                     pnm
amr                     g723_1                  prores
apv                     g729                    prores_raw
av1                     gif                     qoi
avs2                    gsm                     rv34
avs3                    h261                    sbc
bmp                     h263                    sipr
cavsvideo               h264                    tak
cook                    hdr                     vc1
cri                     hevc                    vorbis
dca                     ipu                     vp3
dirac                   jpeg2000                vp8
dnxhd                   jpegxl                  vp9
dnxuc                   jpegxs                  vvc
dolby_e                 lcevc                   webp
dpx                     misc4                   xbm
dvaudio                 mjpeg                   xma
dvbsub                  mlp                     xwd
dvd_nav                 mpeg4video

Enabled demuxers:
aa                      idcin                   pcm_f64le
aac                     idf                     pcm_mulaw
aax                     iff                     pcm_s16be
ac3                     ifv                     pcm_s16le
ac4                     ilbc                    pcm_s24be
ace                     image2                  pcm_s24le
acm                     image2_alias_pix        pcm_s32be
act                     image2_brender_pix      pcm_s32le
adf                     image2pipe              pcm_s8
adp                     image_bmp_pipe          pcm_u16be
ads                     image_cri_pipe          pcm_u16le
adx                     image_dds_pipe          pcm_u24be
aea                     image_dpx_pipe          pcm_u24le
afc                     image_exr_pipe          pcm_u32be
aiff                    image_gem_pipe          pcm_u32le
aix                     image_gif_pipe          pcm_u8
alp                     image_hdr_pipe          pcm_vidc
amr                     image_j2k_pipe          pdv
amrnb                   image_jpeg_pipe         pjs
amrwb                   image_jpegls_pipe       pmp
anm                     image_jpegxl_pipe       pp_bnk
apac                    image_jpegxs_pipe       pva
apc                     image_pam_pipe          pvf
ape                     image_pbm_pipe          qcp
apm                     image_pcx_pipe          qoa
apng                    image_pfm_pipe          r3d
aptx                    image_pgm_pipe          rawvideo
aptx_hd                 image_pgmyuv_pipe       rcwt
apv                     image_pgx_pipe          realtext
aqtitle                 image_phm_pipe          redspark
argo_asf                image_photocd_pipe      rka
argo_brp                image_pictor_pipe       rl2
argo_cvg                image_png_pipe          rm
asf                     image_ppm_pipe          roq
asf_o                   image_psd_pipe          rpl
ass                     image_qdraw_pipe        rsd
ast                     image_qoi_pipe          rso
astc                    image_sgi_pipe          rtp
au                      image_sunrast_pipe      rtsp
av1                     image_svg_pipe          s337m
avi                     image_tiff_pipe         sami
avisynth                image_vbn_pipe          sap
avr                     image_webp_pipe         sbc
avs                     image_xbm_pipe          sbg
avs2                    image_xpm_pipe          scc
avs3                    image_xwd_pipe          scd
bethsoftvid             imf                     sdns
bfi                     ingenient               sdp
bfstm                   ipmovie                 sdr2
bink                    ipu                     sds
binka                   ircam                   sdx
bintext                 iss                     segafilm
bit                     iv8                     ser
bitpacked               ivf                     sga
bmv                     ivr                     shorten
boa                     jacosub                 siff
bonk                    jpegxl_anim             simbiosis_imx
brstm                   jv                      sln
c93                     ktx                     smacker
caf                     kux                     smjpeg
cavsvideo               kvag                    smush
cdg                     laf                     sol
cdxl                    lc3                     sox
cine                    libgme                  spdif
codec2                  libopenmpt              srt
codec2raw               live_flv                stl
concat                  lmlm4                   str
dash                    loas                    subviewer
data                    lrc                     subviewer1
daud                    luodat                  sup
dcstr                   lvf                     svag
derf                    lxf                     svs
dfa                     m4v                     swf
dfpwm                   matroska                tak
dhav                    mca                     tedcaptions
dirac                   mcc                     thp
dnxhd                   mgsts                   threedostr
dsf                     microdvd                tiertexseq
dsicin                  mjpeg                   tmv
dss                     mjpeg_2000              truehd
dts                     mlp                     tta
dtshd                   mlv                     tty
dv                      mm                      txd
dvbsub                  mmf                     ty
dvbtxt                  mods                    usm
dxa                     moflex                  v210
ea                      mov                     v210x
ea_cdata                mp3                     vag
eac3                    mpc                     vc1
epaf                    mpc8                    vc1t
evc                     mpegps                  vividas
ffmetadata              mpegts                  vivo
filmstrip               mpegtsraw               vmd
fits                    mpegvideo               vobsub
flac                    mpjpeg                  voc
flic                    mpl2                    vpk
flv                     mpsub                   vplayer
fourxm                  msf                     vqf
frm                     msnwc_tcp               vvc
fsb                     msp                     w64
fwse                    mtaf                    wady
g722                    mtv                     wav
g723_1                  musx                    wavarc
g726                    mv                      wc3
g726le                  mvi                     webm_dash_manifest
g728                    mvr                     webp_anim
g729                    mxf                     webvtt
gdv                     mxg                     wsaud
genh                    nc                      wsd
gif                     nistsphere              wsvqa
gsm                     nsp                     wtv
gxf                     nsv                     wv
h261                    nut                     wve
h263                    nuv                     xa
h264                    obu                     xbin
hca                     ogg                     xmd
hcom                    oma                     xmv
hevc                    osq                     xvag
hls                     paf                     xwma
hnm                     pcm_alaw                yop
hxvs                    pcm_f32be               yuv4mpegpipe
iamf                    pcm_f32le
ico                     pcm_f64be

Enabled muxers:
a64                     h264                    pcm_s24be
ac3                     hash                    pcm_s24le
ac4                     hds                     pcm_s32be
adts                    hevc                    pcm_s32le
adx                     hls                     pcm_s8
aea                     iamf                    pcm_u16be
aiff                    ico                     pcm_u16le
alp                     ilbc                    pcm_u24be
amr                     image2                  pcm_u24le
amv                     image2pipe              pcm_u32be
apm                     ipod                    pcm_u32le
apng                    ircam                   pcm_u8
aptx                    ismv                    pcm_vidc
aptx_hd                 iterm2                  pdv
apv                     ivf                     psp
argo_asf                jacosub                 rawvideo
argo_cvg                ktx                     rcwt
asf                     kvag                    rm
asf_stream              latm                    roq
ass                     lc3                     rso
ast                     lrc                     rtp
astc                    m4v                     rtp_mpegts
au                      matroska                rtsp
avi                     matroska_audio          sap
avif                    mcc                     sbc
avm2                    md5                     scc
avs2                    microdvd                segafilm
avs3                    mjpeg                   segment
bit                     mkvtimestamp_v2         smjpeg
caf                     mlp                     smoothstreaming
cavsvideo               mmf                     sox
codec2                  mov                     spdif
codec2raw               mp2                     spx
crc                     mp3                     srt
dash                    mp4                     stream_segment
data                    mpeg1system             streamhash
daud                    mpeg1vcd                sup
dfpwm                   mpeg1video              swf
dirac                   mpeg2dvd                tee
dnxhd                   mpeg2svcd               tg2
dts                     mpeg2video              tgp
dv                      mpeg2vob                truehd
eac3                    mpegts                  tta
evc                     mpjpeg                  ttml
f4v                     mxf                     uncodedframecrc
ffmetadata              mxf_d10                 vc1
fifo                    mxf_opatom              vc1t
filmstrip               null                    voc
fits                    nut                     vvc
flac                    obu                     w64
flv                     oga                     wav
framecrc                ogg                     webm
framehash               ogv                     webm_chunk
framemd5                oma                     webm_dash_manifest
g722                    opus                    webp
g723_1                  pcm_alaw                webvtt
g726                    pcm_f32be               whip
g726le                  pcm_f32le               wsaud
gif                     pcm_f64be               wtv
gsm                     pcm_f64le               wv
gxf                     pcm_mulaw               yuv4mpegpipe
h261                    pcm_s16be
h263                    pcm_s16le

Enabled protocols:
async                   http                    rtmp
cache                   httpproxy               rtmpe
concat                  https                   rtmps
concatf                 icecast                 rtmpt
crypto                  ipfs_gateway            rtmpte
data                    ipns_gateway            rtmpts
dtls                    libsrt                  rtp
fd                      libssh                  srtp
ffrtmpcrypt             libzmq                  subfile
ffrtmphttp              md5                     tcp
file                    mmsh                    tee
ftp                     mmst                    tls
gopher                  pipe                    udp
gophers                 prompeg                 udplite

Enabled filters:
a3dscope                dcshift                 paletteuse
aap                     dctdnoiz                pan
abench                  ddagrab                 perlin
abitscope               deband                  perms
acompressor             deblock                 perspective
acontrast               decimate                phase
acopy                   deconvolve              photosensitivity
acrossfade              dedot                   pixdesctest
acrossover              deesser                 pixelize
acrusher                deflate                 pixscope
acue                    deflicker               pp7
addroi                  deinterlace_d3d12       premultiply
adeclick                deinterlace_qsv         premultiply_dynamic
adeclip                 deinterlace_vaapi       prewitt
adecorrelate            dejudder                procamp_vaapi
adelay                  delogo                  pseudocolor
adenorm                 denoise_vaapi           psnr
aderivative             deshake                 pullup
adrawgraph              despill                 qp
adrc                    detelecine              random
adynamicequalizer       dialoguenhance          readeia608
adynamicsmooth          dilation                readvitc
aecho                   displace                realtime
aemphasis               doubleweave             remap
aeval                   drawbox                 removegrain
aevalsrc                drawbox_vaapi           removelogo
aexciter                drawgraph               repeatfields
afade                   drawgrid                replaygain
afdelaysrc              drawtext                reverse
afftdn                  drawvg                  rgbashift
afftfilt                drmeter                 rgbtestsrc
afir                    dynaudnorm              roberts
afireqsrc               earwax                  rotate
afirsrc                 ebur128                 rubberband
aformat                 edgedetect              sab
afreqshift              elbg                    scale
afwtdn                  entropy                 scale2ref
agate                   epx                     scale_cuda
agraphmonitor           eq                      scale_d3d11
ahistogram              equalizer               scale_d3d12
aiir                    erosion                 scale_qsv
aintegral               estdif                  scale_vaapi
ainterleave             exposure                scdet
alatency                extractplanes           scharr
alimiter                extrastereo             scroll
allpass                 fade                    segment
allrgb                  feedback                select
allyuv                  fftdnoiz                selectivecolor
aloop                   fftfilt                 sendcmd
alphaextract            field                   separatefields
alphamerge              fieldhint               setdar
amerge                  fieldmatch              setfield
ametadata               fieldorder              setparams
amf_capture             fillborders             setpts
amix                    find_rect               setrange
amovie                  firequalizer            setsar
amplify                 flanger                 settb
amultiply               floodfill               sharpness_vaapi
anequalizer             format                  shear
anlmdn                  fps                     showcqt
anlmf                   framepack               showcwt
anlms                   framerate               showfreqs
anoisesrc               framestep               showinfo
anull                   frc_amf                 showpalette
anullsink               freezedetect            showspatial
anullsrc                freezeframes            showspectrum
apad                    fspp                    showspectrumpic
aperms                  fsync                   showvolume
aphasemeter             gblur                   showwaves
aphaser                 geq                     showwavespic
aphaseshift             gfxcapture              shuffleframes
apsnr                   gradfun                 shufflepixels
apsyclip                gradients               shuffleplanes
apulsator               graphmonitor            sidechaincompress
arealtime               grayworld               sidechaingate
aresample               greyedge                sidedata
areverse                guided                  sierpinski
arls                    haas                    signalstats
arnndn                  haldclut                signature
asdr                    haldclutsrc             silencedetect
asegment                hdcd                    silenceremove
aselect                 headphone               sinc
asendcmd                hflip                   sine
asetnsamples            highpass                siti
asetpts                 highshelf               smartblur
asetrate                hilbert                 smptebars
asettb                  histeq                  smptehdbars
ashowinfo               histogram               sobel
asidedata               hqdn3d                  spectrumsynth
asisdr                  hqx                     speechnorm
asoftclip               hstack                  split
aspectralstats          hstack_qsv              spp
asplit                  hstack_vaapi            sr_amf
ass                     hsvhold                 ssim
astats                  hsvkey                  ssim360
astreamselect           hue                     stereo3d
asubboost               huesaturation           stereotools
asubcut                 hwdownload              stereowiden
asupercut               hwmap                   streamselect
asuperpass              hwupload                subtitles
asuperstop              hwupload_cuda           super2xsai
atadenoise              hysteresis              superequalizer
atempo                  identity                surround
atilt                   idet                    swaprect
atrim                   il                      swapuv
avectorscope            inflate                 tblend
avgblur                 interlace               telecine
avsynctest              interleave              testsrc
axcorrelate             join                    testsrc2
azmq                    kerndeint               thistogram
backgroundkey           kirsch                  threshold
bandpass                lagfun                  thumbnail
bandreject              latency                 thumbnail_cuda
bass                    latticepal              tile
bbox                    lenscorrection          tiltandshift
bench                   libvmaf                 tiltshelf
bilateral               life                    tinterlace
bilateral_cuda          limitdiff               tlut2
biquad                  limiter                 tmedian
bitplanenoise           loop                    tmidequalizer
blackdetect             loudnorm                tmix
blackframe              lowpass                 tonemap
blend                   lowshelf                tonemap_vaapi
blockdetect             lumakey                 tpad
blurdetect              lut                     transpose
bm3d                    lut1d                   transpose_cuda
boxblur                 lut2                    transpose_vaapi
bwdif                   lut3d                   treble
bwdif_cuda              lutrgb                  tremolo
cas                     lutyuv                  trim
ccrepack                mandelbrot              unpremultiply
cellauto                maskedclamp             unsharp
channelmap              maskedmax               untile
channelsplit            maskedmerge             uspp
chorus                  maskedmin               v360
chromahold              maskedthreshold         vaguedenoiser
chromakey               maskfun                 varblur
chromakey_cuda          mcdeint                 vectorscope
chromanr                mcompand                vflip
chromashift             median                  vfrdet
ciescope                mergeplanes             vibrance
codecview               mestimate               vibrato
color                   mestimate_d3d12         vidstabdetect
colorbalance            metadata                vidstabtransform
colorchannelmixer       midequalizer            vif
colorchart              minterpolate            vignette
colorcontrast           mix                     virtualbass
colorcorrect            monochrome              vmafmotion
colordetect             morpho                  volume
colorhold               movie                   volumedetect
colorize                mpdecimate              vpp_amf
colorkey                mptestsrc               vpp_qsv
colorlevels             msad                    vqe_amf
colormap                multiply                vstack
colormatrix             negate                  vstack_qsv
colorspace              nlmeans                 vstack_vaapi
colorspace_cuda         nnedi                   w3fdif
colorspectrum           noformat                waveform
colortemperature        noise                   weave
compand                 normalize               xbr
compensationdelay       null                    xcorrelate
concat                  nullsink                xfade
convolution             nullsrc                 xmedian
convolve                oscilloscope            xpsnr
copy                    overlay                 xstack
corr                    overlay_cuda            xstack_qsv
cover_rect              overlay_qsv             xstack_vaapi
crop                    overlay_vaapi           yadif
cropdetect              owdenoise               yadif_cuda
crossfeed               pad                     yaepblur
crystalizer             pad_cuda                yuvtestsrc
cue                     pad_vaapi               zmq
curves                  pal100bars              zoneplate
datascope               pal75bars               zoompan
dblur                   palettegen              zscale

Enabled bsfs:
aac_adtstoasc           h264_metadata           pcm_rechunk
ahx_to_mp2              h264_mp4toannexb        pgs_frame_merge
apv_metadata            h264_redundant_pps      prores_metadata
av1_frame_merge         hapqa_extract           remove_extradata
av1_frame_split         hevc_metadata           setts
av1_metadata            hevc_mp4toannexb        showinfo
chomp                   imx_dump_header         smpte436m_to_eia608
dca_core                lcevc_merge             text2movsub
dovi_rpu                lcevc_metadata          trace_headers
dovi_split              media100_to_mjpegb      trim
dts2pts                 mjpeg2jpeg              truehd_core
dump_extradata          mjpega_dump_header      vp9_metadata
dv_error_marker         mov2textsub             vp9_raw_reorder
eac3_core               mpeg2_metadata          vp9_superframe
eia608_to_smpte436m     mpeg4_unpack_bframes    vp9_superframe_split
evc_frame_merge         noise                   vvc_metadata
extract_extradata       null                    vvc_mp4toannexb
filter_units            opus_metadata

Enabled indevs:
dshow                   lavfi                   vfwcap
gdigrab                 openal

Enabled outdevs:

git-essentials external libraries' versions: 

AMF v1.5.2-3-ga4c8f39
aom v3.15.0-42-g208e9c49db
AviSynthPlus v3.7.5-383-g5c82777b
cairo 1.18.5
ffnvcodec n13.1.15.0-1-geddcea9
freetype VER-2-14-3
fribidi v1.0.17
gsm 1.0.24
harfbuzz 14.4.0-115-g240a7d7b
lame 3.100
libass 0.17.5-11-gf61db56
libgme 0.6.6
libopencore-amrnb 0.1.6
libopencore-amrwb 0.1.6
libssh 0.12.2
libtheora v1.2.0
libwebp v1.6.0-261-gea0c620
openal-soft 1.25.2-48-g7532541
openjpeg2 2.5.4
openmpt libopenmpt-0.6.30-3-g6c0a06bc
opus v1.6.1-68-g503d81b1
rubberband v4.0.0
SDL release-2.32.0-234-gb90ac9502
speex Speex-1.2.1-51-g0589522
srt v1.5.7-8-gff8ab25
VAAPI 2.25.0.
vidstab v1.1.2-214-ge2445c4
vmaf v3.2.1-8-g86da14d0
vo-amrwbenc 0.1.3
vorbis v1.3.7-37-g1b75110b
VPL 2.17
vpx v1.17.0-61-g5e680f308
x264 v0.165.3223
x265 4.3-45-g116b875
xvid v1.3.7
zeromq 4.3.5
zimg release-3.0.6-253-g67e0603

