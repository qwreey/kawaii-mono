
for glyph in fontforge.activeFont().selection.byGlyphs:
    xmin,ymin, xmax,ymax = glyph.boundingBox()
    glyph.preserveLayerAsUndo()
    foreground = glyph.foreground
    for contour in foreground:
        if contour.isClockwise() == 0:
            contour.reverseDirection()
    glyph.foreground = foreground
    pen = glyph.glyphPen(replace=False)
    pen.moveTo((xmin-10,ymin-10))
    pen.lineTo((xmin-10,ymax+10))
    pen.lineTo((xmax+10,ymax+10))
    pen.lineTo((xmax+10,ymin-10))
    pen.closePath()
    pen = None
    glyph.intersect()
    glyph.simplify()