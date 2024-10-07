import argparse
import utility as Utility
import logging
import sys

def callPatcher(font):
    NerdFontPatcher = sys.modules.get("NerdFontPatcher",None)
    if not NerdFontPatcher:
        import importlib.util
        spec = importlib.util.spec_from_file_location("NerdFontPatcher", "assets/NerdFontPatcher_extract/fontPatcher.py")
        NerdFontPatcher = importlib.util.module_from_spec(spec)
        sys.modules["NerdFontPatcher"] = NerdFontPatcher
        spec.loader.exec_module(NerdFontPatcher)
        logger = logging.getLogger("start") # Use start logger until we can set up something sane
        s_handler = logging.StreamHandler(stream=sys.stdout)
        s_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
        logger.addHandler(s_handler)
        NerdFontPatcher.logger = logger

    # NerdFontPatcher.patch(font)
    args = argparse.Namespace()

    # complete all options
    args.complete = True
    args.fontawesome = True
    args.fontawesomeextension = True
    args.fontlogos = True
    args.octicons = True
    args.codicons = True
    args.powersymbols = True
    args.pomicons = True
    args.powerline = True
    args.powerlineextra = True
    args.material = True
    args.weather = True
    args.nonmono = False
    args.progressbars = True
    args.quiet = False
    args.adjustLineHeight = False
    args.careful = True
    args.single = False
    args.removeligatures = False
    args.configfile = False
    args.custom = False
    args.glyphdir = "assets/NerdFontPatcher_extract/src/glyphs/"
    args.metrics = None
    args.xavgwidth = None
    args.forcebox = False
    args.dry_run = False
    # args.postprocess = False

#     'single' default=False, action='count',      help='Whether to generate the glyphs as single-width not double-width (default is double-width) (Nerd Font Mono)')
#     'nonmono' default=False, action='store_true', help='Do not adjust advance width (no "overhang") (Nerd Font Propo)')
#     'debugmode' default=0,     type=int, nargs='?', help='Verbose mode (optional: 1=just to file; 2*=just to terminal; 3=display and file)', const=2, choices=range(0, 3 + 1))
#     'quiet' default=False, action='store_true', help='Do not generate verbose output')
#     'careful' default=False, action='store_true', help='Do not overwrite existing glyphs if detected')
#     'extension' default="",    type=str,            help='Change font file type to create (e.g., ttf, otf)')
#     'outputdir' default=".",   type=str,            help='The directory to output the patched font file to')
#     'makegroups' default=1,     type=int, nargs='?', help='Use alternative method to name patched fonts (default=1)', const=1, choices=range(-1, 6 + 1))
#     'complete' default=False, action='store_true', help='Add all available Glyphs')
#     'codicons' default=False, action='store_true', help='Add Codicons Glyphs (https://github.com/microsoft/vscode-codicons)')
#     'fontawesome' default=False, action='store_true', help='Add Font Awesome Glyphs (http://fontawesome.io/)')
#     'fontawesomeextension' default=False, action='store_true', help='Add Font Awesome Extension Glyphs (https://andrelzgava.github.io/font-awesome-extension/)')
#     'fontlogos' default=False, action='store_true', help='Add Font Logos Glyphs (https://github.com/Lukas-W/font-logos)')
#     'material' default=False, action='store_true', help='Add Material Design Icons (https://github.com/templarian/MaterialDesign)')
#     'octicons' default=False, action='store_true', help='Add Octicons Glyphs (https://octicons.github.com)')
#     'powersymbols' default=False, action='store_true', help='Add IEC Power Symbols (https://unicodepowersymbol.com/)')
#     'pomicons' default=False, action='store_true', help='Add Pomicon Glyphs (https://github.com/gabrielelana/pomicons)')
#     'powerline' default=False, action='store_true', help='Add Powerline Glyphs')
#     'powerlineextra' default=False, action='store_true', help='Add Powerline Extra Glyphs (https://github.com/ryanoasis/powerline-extra-symbols)')
#     'weather' default=False, action='store_true', help='Add Weather Icons (https://github.com/erikflowers/weather-icons)')
#     'forcebox' default=False, action='store_true', help='Force patching in (over existing) box drawing glyphs')
#     'configfile' default=False, type=str,            help='Specify a file path for JSON configuration file (see sample: src/config.sample.json)')
#     'custom' default=False, type=str,            help='Specify a custom symbol font, all glyphs will be copied; absolute path suggested')
#     'dry_run' default=False, action='store_true', help='Do neither patch nor store the font, to check naming')
#     'glyphdir' default=__dir__ + "/src/glyphs/", type=str, help='Path to glyphs to be used for patching')
#     'noitalic' default=False, action='store_true', help='Font family does not have Italic (but Oblique), to help create correct RIBBI set')
#     'adjustLineHeight' default=False, action='store_true', help='Whether to adjust line heights (attempt to center powerline separators more evenly)')
#     'metrics' default=None, choices=get_metrics_names(), help='Select vertical metrics source (for problematic cases)')
#     'force_name' default=None, type=str,             help='Specify naming source (\'full\', \'postscript\', \'filename\', or concrete free name-string)')
#     'postprocess' default=False, type=str,            help='Specify a Script for Post Processing')
#     'removeligatures' default=False, action='store_true', help='Removes ligatures specificed in JSON configuration file (needs --configfile)')
#     'xavgwidth' default=None,  type=int, nargs='?', help='Adjust xAvgCharWidth (optional: concrete value)', const=True)

    patcher = NerdFontPatcher.font_patcher(args)
    patcher.patch(font)

selFlag = ("more","ranges","unicode")

def postScript(font,deselectOriginalGlyphs,baseSize):
    # Termux, Vscode 등에서 정의된 크기에 따라
    # 폰트 크기를 맞춥니다

    # 일반 크기
    font.selection.none()
    font.selection.select(selFlag,0xE200,0xF8FE)
    font.selection.select(selFlag,0xFADA,0xFD46)
    font.selection.select(selFlag,0xF8FF,0xF8FF)
    font.selection.select(selFlag,0xF0001,0xF1AF0)
    deselectOriginalGlyphs(font)
    Utility.setWidthWithSavingPosition(
        font=font,targetWidth=baseSize*2
    )
    Utility.width(font=font,targetWidth=baseSize)

    # 2배 크기
    font.selection.none()
    font.selection.select(selFlag,0xF8FF,0xFAD9)
    deselectOriginalGlyphs(font)
    Utility.setWidthWithSavingPosition(
        font=font,targetWidth=baseSize*2
    )

    # 몰라 그냥 다 2배로
    # font.selection.none()
    # font.selection.select(selFlag,0xF8FF,0xFAD9)
    # deselectOriginalGlyphs(font)
    # Utility.setWidthWithSavingPosition(
    #     font=font,targetWidth=baseSize*2
    # )

def build(target,deselectOriginalGlyphs,NerdFontsAdjust=True,baseSize=550,weightStr="Regular"):
    # 용량적 이유로 Regular 폰트에만 패치를 적용함
    if weightStr != "Regular": return

    print("Patching: NerdFonts")

    # NerdFonts 공식 패처를 수행함
    print("    Calling NerdFonts Patcher . . .",flush=True)
    callPatcher(target)
    print("\x1b[2K\r    [OK]")

    # 적절한 크기를 위해서 크기조절을 수행함
    if NerdFontsAdjust:
        print("    Adjusting size . . .",end="",flush=True)
        postScript(target,deselectOriginalGlyphs,baseSize)
        print(" [OK]")
