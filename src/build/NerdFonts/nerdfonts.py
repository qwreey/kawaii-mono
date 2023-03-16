import argparse
import utility as Utility

def callPatcher(font):

    import sys
    NerdFontPatcher = sys.modules.get("NerdFontPatcher",None)
    if not NerdFontPatcher:
        import importlib.util
        spec = importlib.util.spec_from_file_location("NerdFontPatcher", "assets/NerdFontPatcher_extract/fontPatcher.py")
        NerdFontPatcher = importlib.util.module_from_spec(spec)
        sys.modules["NerdFontPatcher"] = NerdFontPatcher
        spec.loader.exec_module(NerdFontPatcher)

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

    args.windows = True
    args.alsowindows = False
    args.nonmono = False
    # args.progressbars = False
    args.progressbars = True
    # args.quiet = True
    args.quiet = False
    args.adjustLineHeight = False
    # args.careful = True
    args.careful = False
    args.single = False
    args.removeligatures = False
    args.postprocess = False
    args.configfile = False
    args.custom = False
    args.glyphdir = "assets/NerdFontPatcher_extract/src/glyphs/"

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
