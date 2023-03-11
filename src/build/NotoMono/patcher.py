from . import selectGlyphs
from . import getCachedFont

# Regular 같은 문자열 weight 를 포인트 값으로 변경
weightStrToNum = {
    "Regular": 16,
}

def pasteGlyphs(target,sourcePath,deselectOriginalGlyphs,EnabledItems,baseSize=550,weightStr="Regular"):
    # 캐시된 소스를 읽어드림
    source = getCachedFont(
        sourcePath = sourcePath,
        baseSize = baseSize,
        weight = weightStrToNum.get(weightStr),
        EnabledItems = EnabledItems
    )

    selectGlyphs.Clear(source)
    selectGlyphs.Clear(target)

    # 타겟으로 글리프 복사
    selectGlyphs.SelectByEnabledList(source,EnabledItems)
    deselectOriginalGlyphs(source)
    source.copy()
    selectGlyphs.SelectByEnabledList(target,EnabledItems)
    deselectOriginalGlyphs(target)
    target.paste()

    # 캐시 닫기
    source.close()
