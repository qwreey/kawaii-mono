import os
import wgetHandler

github_NotoSansMonoCJKkr = "https://github.com/googlefonts/noto-cjk/raw/main/Sans/Mono/NotoSansMonoCJKkr-Regular.otf"

# 폰트 다운로드와 열기
def download():
    if not os.path.exists("assets"): os.mkdir("assets")
    if not os.path.exists("assets/NotoMonoCJKkr.otf"):
        wgetHandler.download(github_NotoSansMonoCJKkr,"assets/NotoMonoCJKkr.otf")
    return "assets/NotoMonoCJKkr.otf"
