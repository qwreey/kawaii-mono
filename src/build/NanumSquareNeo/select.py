# 한글 범위의 글립을 선택함
def Korean(font):
    font.selection.none()
    font.selection.select(("more","ranges","unicode"),0x3131,0x32BF) # ㄱ ~ ㊿
    font.selection.select(("more","ranges","unicode"),0xAC00,0xD7A3) # 가 ~ 힣

def Clear(font):
    font.selection.none()
