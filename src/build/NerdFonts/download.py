import os
import wgetHandler
import zipfile

link_FontPatcher = "https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FontPatcher.zip"

def downloadPatcher():
    if not os.path.exists("assets"): os.mkdir("assets")
    if not os.path.exists("assets/NerdFontPatcher_extract"):
        if not os.path.exists("assets/NerdFontPatcher.zip"):
            wgetHandler.download(link_FontPatcher,"assets/NerdFontPatcher.zip")
        print("Unzipping NerdFontPatcher.zip",end="")
        with zipfile.ZipFile("assets/NerdFontPatcher.zip", 'r') as zip_ref:
            extractName = zip_ref.extractall("assets/NerdFontPatcher_extract")
        os.rename("assets/NerdFontPatcher_extract/font-patcher","assets/NerdFontPatcher_extract/fontPatcher.py")
        with open("assets/NerdFontPatcher_extract/__init__.py","w") as file:
            file.write("")
        print(" [OK]")
    return "assets/NerdFontPatcher_extract"

def isCached(): return os.path.exists("assets/NerdFontPatcher_extract")

def nerdFonts_Download_Test(): downloadPatcher()
