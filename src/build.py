import fontforge

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
    if config.CopyKoreanGlyphs:
        # 나눔 스퀘어 네오 다운로드/불러오기
        nanumSquareNeo = fontforge.open(
            NanumSquareNeoLoader.getFontPath())
        # 글리프 붇여넣기
        NanumSquareNeoLoader.pasteGlyphs(
            target=kawaii,baseSize=550,
            source=nanumSquareNeo)

    if config.CopyJPGlyphs or config.Copy:
        # 노토 모노 다운로드/불러오기
        notoMono = fontforge.open(
            NotoMonoLoader.getFontPath())
            

    # 생성
    kawaii.generate("kawaiiPatched.ttf")

    # 파일 닫기
    notoMono.close()
    nanumSquareNeo.close()
    kawaii.close()

if __name__ == "__main__": build()
