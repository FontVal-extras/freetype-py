# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#  CJK subfonts.py for Fontforge  - Copyright 2017 Hin-Tak Leung
#  Distributed under the terms of the new BSD license.
#
#  Usage:
#    fontforge -script subfonts.py NotoSerifCJKtc-Medium.otf nose Unicode.sfd
#
#  Must move /usr/share/fontforge/Adobe-Identity-0.cidmap!
# -----------------------------------------------------------------------------
import fontforge
from freetype import Face
import time
import locale

if ( fontforge.version() < "20071105" ):
    print( "Can't use FontForge version before 2007-11-05.  Aborting." )
    exit(1)

if ( len(sys.argv) != 4 ):
    print( "usage: [fontforge -script] ", sys.argv[0], " master-font name-stem SFD-file" )
    exit(1)

# Use freetype-py to remember the cmap:
face = Face(sys.argv[1])
face.set_charmap( face.charmap )
reverse_lookup = {}
charcode, gindex = face.get_first_char()
while ( gindex ):
    if ( gindex in reverse_lookup.keys() ):
        reverse_lookup[gindex].append( charcode )
    else:
        reverse_lookup[gindex] = [charcode]
    charcode, gindex = face.get_next_char( charcode, gindex )
del face
# first block of freetype-py code ends.

print("Loading ", sys.argv[1], "...")
font = fontforge.open(sys.argv[1])

if ( font.cidfontname != "" ):
    font.cidFlatten()

font.reencode("ucs4")

# 2nd block of freetype-py code:
for gindex in reverse_lookup.keys():
    if ( len(reverse_lookup[gindex]) > 1 ):
        for x in range( len(reverse_lookup[gindex]) - 1 ):
            font.selection.select( reverse_lookup[gindex][-1] )
            if ( not (font[reverse_lookup[gindex][-1]]).isWorthOutputting() ):
                print( 'Source Empty!' )
            font.copy()
            font.selection.select( reverse_lookup[gindex][x] )
            try:
                font[reverse_lookup[gindex][x]]
            except TypeError:
                # expect this!
                pass
            else:
                print( 'Destination Full!' )
            font.paste()
# 2nd block of freetype-py code ends.

locale.setlocale(locale.LC_ALL, "C")
copyright = font.copyright + "\n\nSubfont version " + time.strftime("%F", time.gmtime()) + "."
font.copyright = copyright

print("Ensure third order curves...")
font.is_quadratic = False

print("Scaling to PostScript units...")
font.em = 1000
font.ascent = 900
font.descent = 100

num_chars = len(font)
count = 0
delta = 100

while (count + delta < num_chars):
    print(count, "/", num_chars - 1, ":")
    # small "bug" in old script
    # redundant processing of the N*delta'th glyphs
    font.selection = range(count, count + delta)

    print("  Add extrema...")
    font.addExtrema()

    print("  Simplifying outlines...")
    font.simplify(2) # note opposite order

    count += delta

print(count, "/", num_chars - 1, ":")
font.selection = range(count, num_chars)

print("  Add extrema...")
font.addExtrema()

print("  Simplifying outlines...")
font.simplify(2) # note opposite order

font.selection.all()

print("Generating subfonts...")
font.generate(sys.argv[2] + "%s.pfb",
              flags=("afm", "tfm", "no-hints", "round"),
              subfont_directory=sys.argv[3])

font.close()
