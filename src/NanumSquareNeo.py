from . import wgetHandler
import os
import zipfile
import shutil
import math
from . import utility as Utility
import fontforge

link_NanumSquareNeo = "https://campaign.naver.com/nanumsquare_neo/download/NaverNanumSquareNeo.zip"
patchVersion = 2 # 업데이트 후 캐시를 무시하기 위해서 사용

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
            extractName = zip_ref.extract("NaverNanumSquareNeo/TTF/NanumSquareNeo-bRg.ttf","assets/NanumSquareNeoKr.extract")
            os.rename(extractName,"assets/NanumSquareNeoKr.ttf")
            shutil.rmtree('assets/NanumSquareNeoKr.extract')
        print(" [OK]")
    return "assets/NanumSquareNeoKr.ttf"

# 한글 범위의 글립을 선택함
def selectGlyphs(font):
    font.selection.none()
    font.selection.select(("more","ranges","unicode"),0x3131,0x32BF) # ㄱ ~ ㊿
    font.selection.select(("more","ranges","unicode"),0xAC00,0xD7A3) # 가 ~ 힣

# 굵기/폭 설정 캐시파일 만들기
def getCache(sourcePath,baseSize=550,weight=16):
    # 캐시된 파일을 확인하고 있으면 반환
    filename = "assets/cache/NanumSquareNeoKr.cache_{}.base_{}.weight_{}.sfd".format(patchVersion,baseSize,weight)
    if os.path.exists(filename):
        return fontforge.open(filename)

    # 새로운 캐시용 폰트 생성
    cache=fontforge.font()
    cache.encoding = 'UnicodeFull'

    # 소스 폰트를 패치시킴
    source=fontforge.open(sourcePath)
    selectGlyphs(source)
    source.changeWeight(weight) # 굵기 변경

    # 너비 지정
    Utility.setWidthWithSavingPosition(
        font=source,targetWidth=baseSize*2
    )

    # 캐시에 붇여넣기
    source.copy()
    selectGlyphs(cache)
    cache.paste()

    # 캐시 폰트 저장
    if not os.path.exists("assets/cache"): os.mkdir("assets/cache")
    cache.save(filename)
    return cache

# Regular 같은 문자열 weight 를 포인트 값으로 변경
weightStrToNum = {
    "Regular": 16,
}

# 캐시를 가져와서 글리프를 타겟 폰트에 붇여넣음
def pasteGlyphs(target,sourcePath,baseSize=550,weightStr="Regular"):

    # 캐시된 소스를 읽어드림
    source = getCache(
        sourcePath = sourcePath,
        baseSize = baseSize,
        weight = weightStrToNum.get(weightStr)
    )

    # 타겟으로 글리프 복사
    selectGlyphs(source)
    source.copy()
    selectGlyphs(target)
    target.paste()

    # 캐시 닫기
    source.close()
