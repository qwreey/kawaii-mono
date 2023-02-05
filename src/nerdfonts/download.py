import os
import zipfile
# from .. import wgetHandler

import os
import importlib
basePath = os.path.realpath(os.path.dirname(__file__)+"/../")
wgetHandlerSpec = importlib.util.spec_from_file_location("wgetHandler",basePath+"/wgetHandler.py")
wgetHandler = importlib.util.module_from_spec(wgetHandlerSpec)
wgetHandlerSpec.loader.exec_module(wgetHandler)


# import wgetHandler

print("__file__ : {__file__}".format(__file__=__file__))
print("wgetHandler (spec)")
print(importlib.util.spec_from_file_location("wgetHandler",basePath))
print("wgetHandler [object]")
print(wgetHandler)
print(help(wgetHandler))
# import wgetHandler

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
