import argparse

def callPatcher(font):


    import sys
    NerdFontPatcher = sys.modules["NerdFontPatcher"]
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
    args.progressbars = True
    args.quiet = False
    args.adjustLineHeight = True
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
    font.selection.none()
    font.selection.select()
    deselectOriginalGlyphs()

def build(target,deselectOriginalGlyphs,NerdFontsAdjust=True,baseSize=550,weightStr="Regular"):
    # 용량적 이유로 Regular 폰트에만 패치를 적용함
    if weightStr != "Regular": return

    print("Patching: NerdFonts")

    # NerdFonts 공식 패처를 수행함
    callPatcher(target)

    # 적절한 크기를 위해서 크기조절을 수행함
    # if NerdFontsAdjust:
        # postScript(target,deselectOriginalGlyphs,baseSize)
