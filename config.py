
# TODO: 블록 글자 추가
# TODO: 기울임꼴(ah 같은 특수 기울임도) 추가
# TODO: 합자 추가

config = {
    # -------------------------------------------
    #               Base Settings
    # -------------------------------------------

    # TODO: 이 설정은 아직 동작하지 않습니다
    # 출력 파일의 이름을 지정합니다.
    # Array 형태로 여러 이름을 추가할 수 있습니다
    # 필요한 경우 otf 와 같은 다른 확장자를
    # 사용할 수도 있습니다
    "OutputNames": {
        "Bold": ["KawaiiPatched.ttf"],
        "Regular": [""],
    },

    # 일반적인 글자 (예: a) 의 너비입니다.
    # 작은 화면에 더많은 정보를 담아내려면
    # 이 값을 줄이세요. 단 스캐일이 조정되지
    # 않습니다
    # * 기본값 550
    "FontBaseWidth": 550,

    # TODO: 이 설정은 아직 동작하지 않습니다
    # 폰트의 X 축 스캐일 조정입니다.
    # 폰트의 width 를 줄이거나 늘렸을 때
    # 이 값을 변경하여 가로로 늘리거나
    # 작게 줄일 수 있습니다
    "FontScaleX": 1,

    # -------------------------------------------
    #            Glyphs and Features
    # -------------------------------------------

    # 한글 글리프를 나눔 스퀘어 네오 폰트에서
    # 복사할 지에 대한 여부입니다
    # 폰트 용량이 매우 커집니다!!
    "CopyKoreanGlyphs": True,

    # 노토 산스 모노에서 가타카나/히라가나
    # 글리프를 복사할 지에 대한 여부입니다
    # 한자는 포함하지 않습니다
    "CopyJapaneseGlyphs": True,

    # 노토 산스에서 단위관련 기호, 원형 기호
    # 글리프를 복사할 지에 대한 여부입니다
    # 폰트위 용량이 매우 커집니다!!
    "CopySymbols": True,

    # 노토 산스 모노에서 CJK 공용 한자 글리프를
    # 복사할 지에 대한 여부입니다.
    # 폰트 용량이 매우 커집니다!!
    # 웹용 폰트의 경우 끄는것을 추천합니다
    #! 최소 2분 이상 걸립니다!!
    "CopyCJKUnifiedIdeographs": True, # 일반적인 CJK Unified
    "CopyCJKUnifiedIdeographsExtension": False, # Extension A~F
    "CopyCJKCompatibilityIdeographs": False, # Compatibility Ideograph, Supplement
    #! 이 옵션들을 활성화시 ttf 포멧으로 저장에 실패할 수 있습니다
    #? ttf 의 글자수 제한 때문에 그런것이므로, 다른 포멧으로 저장해야합니다.

    # 라틴 글리프를 Hack 폰트에서 더 가져옵니다
    # (성조 표시된 라틴, ...)
    "CopyLatinExtra": True,

    # Nerd Fonts 패치를 적용할지에 대한
    # 여부입니다. 폰트 용량이 매우 커집니다!!
    # 웹용 폰트의 경우 끄는것을 추천합니다
    "NerdFonts": True,

    # TODO: 이 설정은 아직 동작하지 않습니다
    # Nerd Fonts 패치에 발견되는 크기 이슈를
    # 해결하기 위해 크기조절이 이루워집니다
    # Nerd Fonts 패치를 활성화 한 경우에만
    # 이 값이 사용됩니다.
    "NerdFontsAdjust": True,

    # TODO: 이 설정은 아직 동작하지 않습니다
    # Liga (합자) 를 추가할 지에 대한 여부입니다
    # 활성화시 <!-- 와 같은 문자를 합쳐줍니다
    # Vscode 의 경우 설정에
    # "editor.fontLigatures": true,
    # 가 되어있어야 표시됩니다.
    "Liga": True,
}
