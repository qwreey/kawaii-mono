import fontforge
import os

from . import NanumSquareNeo as NanumSquareNeoLoader
from . import NotoMono as NotoMonoLoader
from . import KawaiiMono as KawaiiMonoLoader

def build(config=None):
    # 메인 폰트 불러오기
    kawaii = fontforge.open(
        KawaiiMonoLoader.getFontPath())

    # 모든 글리프를 붇여넣을 수 있도록 인코딩을 utf full 로 변경
    kawaii.encoding = 'UnicodeFull'

    # 한글 글리프 붇여넣기
    if config.get("CopyKoreanGlyphs"):
        # 나눔 스퀘어 네오 다운로드/불러오기
        nanumSquareNeo = fontforge.open(
            NanumSquareNeoLoader.getFontPath())
        # 글리프 붇여넣기
        NanumSquareNeoLoader.pasteGlyphs(
            target=kawaii,baseSize=550,
            source=nanumSquareNeo)
        nanumSquareNeo.close()

    if (config.get("CopyJapaneseGlyphs") or
        config.get("CopyCJKUnifiedIdeographs")):
        # 노토 모노 다운로드/불러오기
        notoMono = fontforge.open(
            NotoMonoLoader.getFontPath())
        # 글리프 붇여넣기
        NotoMonoLoader.pasteGlyphs(
            JapaneseGlyphs=config.get("CopyJapaneseGlyphs") or False,
            CJKUnifiedIdeographs=config.get("CopyCJKUnifiedIdeographs") or False,
            target=kawaii,baseSize=550,
            source=notoMono)
        notoMono.close()

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
