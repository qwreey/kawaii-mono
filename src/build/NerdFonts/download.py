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
        with open("assets/NerdFontPatcher_extract/__init__.py","w") as file:
            file.write("")
        with open("assets/NerdFontPatcher_extract/font-patcher") as file:
            patcherCode = file.read()
        patcherCode = patcherCode.replace(
            'sys.stdout.write("Adding " + str(max(1, glyphSetLength)) + " Glyphs from " + setName + " Set \\n")',
            'sys.stdout.write("\\x1b[2K\\r    Adding " + str(max(1, glyphSetLength)) + " Glyphs from " + setName + " Set \\n")')
        patcherCode = patcherCode.replace('text = "\\r╢{0}╟ {1}%"','text = "\\x1b[2K\\r    ╢{0}╟ {1}%"')
        patcherCode = patcherCode.replace('sys.stdout.write("\\n")','pass')
        patcherCode = patcherCode.replace('print("Very wide','print("    Very wide')
        patcherCode = patcherCode.replace('print("Redistributing line','print("    Redistributing line')
        with open("assets/NerdFontPatcher_extract/fontPatcher.py",mode="w") as file:
            file.write(patcherCode)
        print(" [OK]")
    return "assets/NerdFontPatcher_extract"

def isCached(): return os.path.exists("assets/NerdFontPatcher_extract")

def nerdFonts_Download_Test(): downloadPatcher()
