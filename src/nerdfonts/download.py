if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.realpath(os.path.dirname(os.path.realpath(__file__))+"/../"))
import os
import zipfile
import wgetHandler

link_FontPatcher = "https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FontPatcher.zip"

def downloadPatcher():
    if not os.path.exists("assets"): os.mkdir("assets")
    if not os.path.exists("assets/NerdFontPatcher_extract"):
        if not os.path.exists("assets/NerdFontPatcher.zip"):
            wgetHandler.download(link_FontPatcher,"assets/NerdFontPatcher.zip")
        print("Unzipping NerdFontPatcher.zip",end="")
        with zipfile.ZipFile("assets/NerdFontPatcher.zip", 'r') as zip_ref:
            extractName = zip_ref.extractall("assets/NerdFontPatcher_extract")
        print(" [OK]")
    return "assets/NanumSquareNeoKr.ttf"

if __name__ == "__main__": downloadPatcher()
