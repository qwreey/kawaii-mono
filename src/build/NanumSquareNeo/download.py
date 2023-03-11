import zipfile
import shutil
import wgetHandler
import os

link_NanumSquareNeo = "https://campaign.naver.com/nanumsquare_neo/download/NaverNanumSquareNeo.zip"

# 폰트 다운로드와 열기
# 배포 방식이 zip 으로 배포이기 때문에 zipfile 라이브러리로
# 다운로드 후 언팩함
def download():
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
