
import utility as Utility
import fontforge
import os
from . import selectGlyphs
from . import patchVersion

# 굵기/폭 설정 캐시파일 만들기
def getCachedFont(sourcePath,EnabledItems,baseSize=550,weight=16):
    # 캐시된 파일을 확인하고 있으면 반환
    filename = "assets/cache/NotoMono.cache_{}.base_{}.weight_{}{}{}{}{}{}.sfd".format(
        patchVersion,baseSize,weight,
        EnabledItems.get("JapaneseGlyphs") and ".jp" or "",
        EnabledItems.get("CJKUnifiedIdeographs") and ".id" or "",
        EnabledItems.get("CopyCJKUnifiedIdeographsExtension") and ".ide" or "",
        EnabledItems.get("CopyCJKCompatibilityIdeographs") and ".cid" or "",
        EnabledItems.get("Symbols") and ".sym" or "")
    if os.path.exists(filename):
        print("    Found build cache [CACHE HIT]")
        return fontforge.open(filename)
    print("    Creating new build cache",end="",flush=True)

    # 새로운 캐시용 폰트 생성
    cache=fontforge.font()
    cache.encoding = 'UnicodeFull'

    # 소스 폰트를 패치시킴
    source=fontforge.open(sourcePath)
    source.cidFlatten()
    source.encoding = 'UnicodeFull'
    if EnabledItems.get("JapaneseGlyphs"): selectGlyphs.JapaneseGlyphs(source)
    source.changeWeight(weight) # 굵기 변경
    selectGlyphs.SelectByEnabledList(source,EnabledItems)
    # 한자 글립은 냥많아서 크기조절하면 끝이 안난다냥

    # 너비 지정
    Utility.scale(font=source,targetScale=0.85)
    Utility.setWidthWithSavingPosition(
        font=source,targetWidth=baseSize*2
    )

    # 캐시에 붇여넣기
    source.copy()
    selectGlyphs.SelectByEnabledList(cache,EnabledItems)
    cache.paste()

    selectGlyphs.Clear(cache)
    selectGlyphs.Clear(source)

    # 캐시 폰트 저장
    if not os.path.exists("assets/cache"): os.mkdir("assets/cache")
    cache.save(filename)
    print(" [OK]")
    return cache
