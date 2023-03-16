import os
import utility as Utility
import fontforge

from . import NerdFonts as NerdFontsLoader
from . import NanumSquareNeo as NanumSquareNeoLoader
from . import NotoMono as NotoMonoLoader
from . import KawaiiMono as KawaiiMonoLoader

deselectFlags = ("less","unicode")

def build(config=None):
    # 메인 폰트 불러오기 / 에셋 다운로드
    kawaii = fontforge.open(
        KawaiiMonoLoader.getFontPath())
    downloadContentHeader = False
    def printDownloadContentHeader():
        nonlocal downloadContentHeader
        if downloadContentHeader == False:
            downloadContentHeader = True
            print("-------------- DOWNLOAD PATCH CONTENTS --------------")
    # 나눔 스퀘어 네오 다운로드
    nanumSquareNeo = None
    if config.get("CopyKoreanGlyphs"):
        if not NanumSquareNeoLoader.isCached(): printDownloadContentHeader()
        nanumSquareNeo = NanumSquareNeoLoader.download()
    # 노토 모노 다운로드/불러오기
    notoMono = None
    if (config.get("CopyJapaneseGlyphs") or
        config.get("CopyCJKUnifiedIdeographs") or
        config.get("CopyCJKUnifiedIdeographsExtension") or
        config.get("CopyCJKCompatibilityIdeographs")):
        if not NotoMonoLoader.isCached(): printDownloadContentHeader()
        notoMono = NotoMonoLoader.download()
    # Nerd fonts 패치기 다운로드
    nerdFontsPatcherPath = None
    if config.get("NerdFonts"):
        if not NerdFontsLoader.isCached(): printDownloadContentHeader()
        nerdFontsPatcherPath = NerdFontsLoader.downloadPatcher()
    print("--------------------- Patching ----------------------")

    # 유지 목록 (덮어쓰기 금지) 만들기
    keepList = None
    def deselectOriginalGlyphs(target):
        nonlocal keepList
        for unicode in keepList:
            if unicode == -1: continue
            target.selection.select(deselectFlags,unicode)
    def updateOriginalGlyphs():
        nonlocal keepList
        kawaii.selection.all()
        keepList = [i.unicode for i in kawaii.selection.byGlyphs]
        kawaii.selection.none()
    updateOriginalGlyphs()

    # 모든 글리프를 붇여넣을 수 있도록 인코딩을 utf full 로 변경
    kawaii.encoding = 'UnicodeFull'

    # 폰트 가로폭 설정
    baseSize = config.get("FontBaseWidth")
    if baseSize != 550:
        Utility.setWidthWithSavingPosition(
            font=kawaii,targetWidth=baseSize
        )

    # 한글 글리프 붇여넣기
    if nanumSquareNeo:
        # 글리프 붇여넣기
        NanumSquareNeoLoader.pasteGlyphs(
            target=kawaii,baseSize=baseSize,weightStr="Regular",
            sourcePath=nanumSquareNeo,
            deselectOriginalGlyphs = deselectOriginalGlyphs)
        updateOriginalGlyphs()

    # 일어 글리프 혹은 한자 글리프 추가
    if notoMono:
        # 글리프 붇여넣기
        NotoMonoLoader.pasteGlyphs(
            EnabledItems = {
                "JapaneseGlyphs": config.get("CopyJapaneseGlyphs") or False,
                "CJKUnifiedIdeographs": config.get("CopyCJKUnifiedIdeographs") or False,
                "CJKUnifiedIdeographsExtension": config.get("CopyCJKUnifiedIdeographsExtension") or False,
                "CJKCompatibilityIdeographs": config.get("CopyCJKCompatibilityIdeographs") or False,
                "Symbols": config.get("CopySymbols") or False,
            },
            target=kawaii,baseSize=baseSize,
            sourcePath=notoMono,
            deselectOriginalGlyphs = deselectOriginalGlyphs)
        updateOriginalGlyphs()

    # NerdFonts 패치 적용
    if config.get("NerdFonts"):
        NerdFontsLoader.build(
            target=kawaii,
            NerdFontsAdjust=config.get("NerdFontsAdjust") or False,
            baseSize=baseSize,
            weightStr="Regular",
            deselectOriginalGlyphs = deselectOriginalGlyphs)
        updateOriginalGlyphs()

    # 생성
    if not os.path.exists("out"): os.mkdir("out")
    kawaii.generate("out/"+"KawaiiMonoRegularPatched.ttf")

    # KawaiiMonoRegularPatched.ttf
    # KawaiiMonoRegularPatched.otf
    # KawaiiMonoRegularPatched.woff
    # KawaiiMonoRegularPatched.eot

    # 파일 닫기
    kawaii.close()

if __name__ == "__main__": build()
