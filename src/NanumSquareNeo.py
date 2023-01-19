from . import wgetHandler
import os
import zipfile
import shutil
import math

link_NanumSquareNeo = "https://campaign.naver.com/nanumsquare_neo/download/NaverNanumSquareNeo.zip"

# 폰트 다운로드와 열기
# 배포 방식이 zip 으로 배포이기 때문에 zipfile 라이브러리로
# 다운로드 후 언팩함
def getFontPath():
    if not os.path.exists("assets"): os.mkdir("assets")
    if not os.path.exists("assets/NanumSquareNeoKr.ttf"):
        if not os.path.exists("assets/NanumSquareNeoKr.zip"):
            wgetHandler.download(link_NanumSquareNeo,"assets/NanumSquareNeoKr.zip")
        print("Unzipping NanumSquareNeoKr.zip",end="")
        with zipfile.ZipFile("assets/NanumSquareNeoKr.zip", 'r') as zip_ref:
            extractName = zip_ref.extract("NaverNanumSquareNeo/TTF/NanumSquareNeo-cBd.ttf","assets/NanumSquareNeoKr.extract")
            os.rename(extractName,"assets/NanumSquareNeoKr.ttf")
            shutil.rmtree('assets/NanumSquareNeoKr.extract')
        print(" [OK]")
    return "assets/NanumSquareNeoKr.ttf"

def pasteGlyphs(target,source,baseSize=550):
    def select(font):
        font.selection.none()
        font.selection.select(("more","ranges","unicode"),0x3131,0x32BF) # ㄱ ~ ㊿
        font.selection.select(("more","ranges","unicode"),0xAC00,0xD7A3) # 가 ~ 힣
    select(source)

    # 넓은 글자 크기 (한글에 모두 적용)
    wideWidth = baseSize*2
    for glyph in source.selection.byGlyphs:
        widthDiff = wideWidth-glyph.width # 타겟 너비와 얼마나 크기 차이가 나는지
        sideAdjust = widthDiff/2 # 좌우 사이드 조정해야하는 정도
        glyph.left_side_bearing = int(glyph.left_side_bearing + math.floor(sideAdjust)) # 좌우 베어링을 조정함
        glyph.right_side_bearing = int(glyph.right_side_bearing + math.ceil(sideAdjust))
        glyph.width = wideWidth # 타겟 너비로 정확하게 설정

    # 타겟으로 글리프 복사
    source.copy()
    select(target)
    target.paste()

if __name__ == "__main__":
    getFontPath()
