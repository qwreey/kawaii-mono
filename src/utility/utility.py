import math
import psMat

def setWidthWithSavingPosition(font,targetWidth):
    for glyph in font.selection.byGlyphs:
        widthDiff = targetWidth-glyph.width # 타겟 너비와 얼마나 크기 차이가 나는지
        sideAdjust = widthDiff/2 # 좌우 사이드 조정해야하는 정도
        glyph.left_side_bearing = int(glyph.left_side_bearing + math.floor(sideAdjust)) # 좌우 베어링을 조정함
        glyph.right_side_bearing = int(glyph.right_side_bearing + math.ceil(sideAdjust))
        glyph.width = targetWidth # 타겟 너비로 정확하게 설정

def width(font,targetWidth):
    for glyph in font.selection.byGlyphs: glyph.width = targetWidth

def scale(font,targetScale):
    font.transform(psMat.scale(targetScale))
    font.round()

def translate(font,targetX=0,targetY=0):
    font.transform(psMat.translate(targetX,targetY))

def centerX(font,targetWidth):
    for glyph in font.selection.byGlyphs:
        xmin,ymin, xmax,ymax = glyph.boundingBox()
        glyphWidth = xmax - xmin
        padding = (targetWidth - glyphWidth)//2
        foreground = glyph.foreground
        foreground.transform(psMat.translate(padding-xmin,0))
        glyph.foreground = foreground
