#!/usr/bin/env python3

from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).absolute().parent.parent.parent))

from color_range import ColorRange
from svg import text_color

out = ""

for size in (3, 5, 10, 15, 20):
    out += "<h2>%s</h2>\n" % size
    out += "<table>\n"
    for c in ColorRange.known_colors():
        out += "  <tr>\n"
        out += "    <td>%s</td>\n" % c
        color_range = ColorRange(c)
        for i in range(size):
            color = color_range.color_range(i, size)
            out += "    <td style='background: #%s; color:%s'>#%s</td>\n" % (color, text_color(color), color)
        out += "  </tr>\n"
    out += "</table>\n"

print(out)
