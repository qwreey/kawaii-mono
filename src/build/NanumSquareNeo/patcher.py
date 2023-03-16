from . import getCachedFont
from . import selectGlyphs

# Regular 같은 문자열 weight 를 포인트 값으로 변경
weightStrToNum = {
    "Regular": 16,
}

# 캐시를 가져와서 글리프를 타겟 폰트에 붇여넣음
def pasteGlyphs(target,sourcePath,deselectOriginalGlyphs,baseSize=550,weightStr="Regular"):

    # 캐시된 소스를 읽어드림
    print("Patching: NanumSquareNeo")
    source = getCachedFont(
        sourcePath = sourcePath,
        baseSize = baseSize,
        weight = weightStrToNum.get(weightStr)
    )

    print("    Copying . . .",end="",flush=True)
    selectGlyphs.Clear(source)
    selectGlyphs.Clear(target)

    # 타겟으로 글리프 복사
    selectGlyphs.Korean(source)
    deselectOriginalGlyphs(source)
    source.copy()
    selectGlyphs.Korean(target)
    deselectOriginalGlyphs(target)
    target.paste()
    print(" [OK]")

    # 캐시 닫기
    source.close()
