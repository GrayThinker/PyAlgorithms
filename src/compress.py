"""
Lossless:
    CCITT group 3 & 4 compression
    Gen purpose:
        Huffman coding
        Lempel Ziv encoding (LZ77,LZ78)
            Lempel_Ziv_Markov Chain (LZMA)
            Lempel-Ziv_Welch (LZW) compression 
            Lempel-Ziv-final state entropy (LZFSE)
            Lempel–Ziv–Oberhumer (LZO)
            Lempel–Ziv–Storer–Szymanski (LZSS)
                Flate/deflate compression
        RLE compression
        bzip2 (burrows-wheeler transform with RLE and huffman)
        Final state entropy (variant of ANS)
        Run-length encoding (RLE)
        Prediction by partial matching (PPM)
    
    Audio:
        Apple Lossless (ALAC codec)
        Adaptive transform acoustic coding (ATRAC)
        Audio Lossless Coding (also known as MPEG-4 ALS)
        Direct Stream Transfer (DST)
        Dolby TrueHD
        DTS-HD Master Audio
        Free Lossless Audio Codec (FLAC)
        Meridian Lossless Packing (MLP)
        Monkey's Audio (Monkey's Audio APE)
        MPEG-4 SLS (also known as HD-AAC)
        OptimFROG
        Original Sound Quality (OSQ)
        RealPlayer (RealAudio Lossless)
        Shorten (SHN)
        TTA (True Audio Lossless)
        WavPack (WavPack lossless)
        WMA Lossless (Windows Media Lossless)
    
    Raster Graphics:
        HEIF – High Efficiency Image File Format (lossless or lossy compression, using HEVC)
        ILBM – (lossless RLE compression of Amiga IFF images)
        LDCT – Lossless Discrete Cosine Transform[2][3]
        JBIG2 – (lossless or lossy compression of B&W images)
        JPEG 2000 – (includes lossless compression method via LeGall-Tabatabai 5/3[4][5][6] reversible integer wavelet transform)
        JPEG XR – formerly WMPhoto and HD Photo, includes a lossless compression method
        JPEG-LS – (lossless/near-lossless compression standard)
        PCX – PiCture eXchange
        PDF – Portable Document Format (lossless or lossy compression)
        PNG – Portable Network Graphics
        TIFF – Tagged Image File Format (lossless or lossy compression)
        TGA – Truevision TGA
        WebP – (lossless or lossy compression of RGB and RGBA images)
        FLIF – Free Lossless Image Format
        AVIF – AOMedia Video 1 Image File Format
    
    3D Graphics:
        OpenCTM – Lossless compression of 3D triangle meshes

Lossy:
    General:
        Modified discrete cosine transform (MDCT)
        Dolby Digital (AC-3)
        Adaptive Transform Acoustic Coding (ATRAC)
        MPEG Layer III (MP3)[11]
        Advanced Audio Coding (AAC / MP4 Audio)[12]
        Vorbis
        Windows Media Audio (WMA) (Standard and Pro profiles are lossy. WMA Lossless is also available.)
        LDAC[13][14]
        Opus (Notable for lack of patent restrictions, low delay, and high quality speech and general audio.)
        Adaptive differential pulse-code modulation (ADPCM)
        Master Quality Authenticated (MQA)
        MPEG-1 Audio Layer II (MP2)
        Musepack (based on Musicam)
        aptX/ aptX-HD[15]

    Image:
        Discrete cosine transform (DCT)
        JPEG[9]
        WebP (high-density lossless or lossy compression of RGB and RGBA images)
        High Efficiency Image Format (HEIF)
        Better Portable Graphics (BPG) (lossless or lossy compression)
        JPEG XR, a successor of JPEG with support for high dynamic range, wide gamut pixel formats (lossless or lossy compression)
        Wavelet compression
        JPEG 2000, JPEG's successor format that uses wavelets (lossless or lossy compression)
        DjVu
        ICER, used by the Mars Rovers, related to JPEG 2000 in its use of wavelets
        PGF, Progressive Graphics File (lossless or lossy compression)
        Cartesian Perceptual Compression, also known as CPC
        Fractal compression
        JBIG2 (lossless or lossy compression)
        S3TC texture compression for 3D computer graphics hardware
    3D graphics:
        gITF
    
    Video:
        Discrete cosine transform (DCT)
        H.261[9]
        Motion JPEG[9]
        MPEG-1 Part 2[10]
        MPEG-2 Part 2 (H.262)[10]
        MPEG-4 Part 2 (H.263)[9]
        Advanced Video Coding (AVC / H.264 / MPEG-4 AVC)[9] (may also be lossless, even in certain video sections)
        High Efficiency Video Coding (HEVC / H.265)[9]
        Ogg Theora (noted for its lack of patent restrictions)
        VC-1
        Wavelet compression
        Motion JPEG 2000
        Dirac
        Sorenson video codec
    
    Speech:
        Linear predictive coding (LPC)
        Adaptive predictive coding (APC)
        Code-excited linear prediction (CELP)
        Algebraic code-excited linear prediction (ACELP)
        Relaxed code-excited linear prediction (RCELP)
        Low-delay CELP (LD-CELP)
        Adaptive Multi-Rate (used in GSM and 3GPP)
        Codec2 (noted for its lack of patent restrictions)
        Speex (noted for its lack of patent restrictions)
        Modified discrete cosine transform (MDCT)
        AAC-LD
        Constrained Energy Lapped Transform (CELT)
        Opus (mostly for real-time applications)
"""