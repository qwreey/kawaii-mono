selFlag = ("more","ranges","unicode")

# 일본어 글립 선택
def JapaneseGlyphs(font):
    # 사각문자 (Square)
    font.selection.select(selFlag,0x32FF,0x2271)
    font.selection.select(selFlag,0x337B,0x337F) # Missing one char
    font.selection.select(selFlag,0x1F200,0x1F200)

    # 히라가나/가타카나
    font.selection.select(selFlag,0x3041,0x30FF)
    font.selection.select(selFlag,0x31F0,0x31FF) # SMALL Katakana
    font.selection.select(selFlag,0xFF66,0xFF9F) # HalfWidth Katakana

    # 일어 기호
    font.selection.select(selFlag,0xFF5B,0xFF65)

# CJK 한자 글립 선택
def CJKUnifiedIdeographs(font):
    # CJK Stroke
    font.selection.select(selFlag,0x31C0,0x31E3)

    # Bopomofo
    font.selection.select(selFlag,0x3105,0x312F)
    font.selection.select(selFlag,0x31A0,0x31BB)

    # CJK Unified Ideograph
    font.selection.select(selFlag,0x4E00,0x9FFF)

def CJKUnifiedIdeographsExtension(font):
    font.selection.select(selFlag,0x3400,0x4DBF) # Extension A
    font.selection.select(selFlag,0x20000,0x2A6DF) # Extension B
    font.selection.select(selFlag,0x2A700,0x2B73F) # Extension C
    font.selection.select(selFlag,0x2B740,0x2B81F) # Extension D
    font.selection.select(selFlag,0x2B820,0x2CEAF) # Extension E
    font.selection.select(selFlag,0x2CEB0,0x2EBEF) # Extension F

def CJKCompatibilityIdeographs(font):
    # CJK Compatibility Ideograph
    font.selection.select(selFlag,0xF900,0xFAFF)
    # CJK Compatibility Ideographs Supplement
    font.selection.select(selFlag,0x2F800,0x2FA1F)

def Symbols(font):
    # 원형, 단위기호
    font.selection.select(selFlag,0x3220,0x3250)
    font.selection.select(selFlag,0x3220,0x3250)
    font.selection.select(selFlag,0x3280,0x32B0) # Missing ...
    font.selection.select(selFlag,0x32C0,0x32FE)

    # 단위 기호
    font.selection.select(selFlag,0x3358,0x337A)
    font.selection.select(selFlag,0x3380,0x33FF)

    # 로마 숫자
    # font.selection.select(selFlag,0x2160,0x217B)
    font.selection.select(selFlag,0x2150,0x218F) # Number Forms

    # Latin Ligature
    font.selection.select(selFlag,0xFB00,0xFB4F) # 	Alphabetic Presentation Forms

    # 특수기호/FULLWIDTH Latin
    font.selection.select(selFlag,0x2600,0x26FF) # Miscellaneous Symbols
    font.selection.select(selFlag,0x2700,0x27BF) # Dingbats
    font.selection.select(selFlag,0xFE10,0xFE1F) # Vertical Forms
    # font.selection.select(selFlag,0xFFE0,0xFFEE) # (Without kr) Halfwidth and Fullwidth Forms
    font.selection.select(selFlag,0xFF00,0xFFEF) # Halfwidth and Fullwidth Forms
    font.selection.select(selFlag,0x1F100,0x1F1FF) # Enclosed Alphanumeric Supplement
    font.selection.select(selFlag,0x1F200,0x1F2FF) # Enclosed Ideographic Supplement

def SelectByEnabledList(target,EnabledItems):
    if EnabledItems.get("JapaneseGlyphs"): JapaneseGlyphs(target)
    if EnabledItems.get("CJKUnifiedIdeographs"): CJKUnifiedIdeographs(target)
    if EnabledItems.get("CJKUnifiedIdeographsExtension"): CJKUnifiedIdeographsExtension(target)
    if EnabledItems.get("CJKCompatibilityIdeographs"): CJKCompatibilityIdeographs(target)
    if EnabledItems.get("Symbols"): Symbols(target)

def Clear(font):
    font.selection.none()
