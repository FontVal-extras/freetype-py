# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#  CJK subfonts.py for Fontforge  - Copyright 2017 Hin-Tak Leung
#  Distributed under the terms of the new BSD license.
#
#  Usage:
#    fontforge -script subfonts.py master-font name-stem SFD-file
#
#  Example:
#    fontforge -script subfonts.py NotoSerifCJKtc-Medium.otf nose Unicode.sfd
#
#  This script requires freetype-py ( https://github.com/rougier/freetype-py ).
#  On Linux systems, the package may be called "python{,2,3}-freetype" instead.
#  Also fontforge needs to be built with
#  "./configure --enable-python-scripting --enable-python-extension" .
#  This is often the case on Linux, anyway.
#  The command "echo 'import fontforge' | python" indicates whether
#  the fontforge python extension is available. This command is silent on
#  success, but shows "ImportError: No module named fontforge" on failure.
#
#  *** Important ***:
#    To process many Adobe CFF OpenType fonts correctly (e.g. Source/Noto CJK),
#    the file "Adobe-Identity-0.cidmap" must be moved or renamed to be hidden
#    from being found by fontforge. On Linux, it is in "/usr/share/fontforge".
#    See https://github.com/fontforge/fontforge/issues/3084 .
#    On Ubuntu Linux, this file is in a separate "fontforge-extras" package.
#    i.e. The Ubuntu "fontforge-extras" package must NOT be installed.
#
#  Implementation Notes:
#    Except for the two blocks of freetype-py dependent code, this is roughly
#    a line-by-line translation of the "cjk/utils/subfonts/subfonts.pe" script
#    to fontforge's python API. Notable differences compared to the legacy
#    scripting interface are:
#
#    * Some Python API routines (e.g. "font.generate()" ) takes named
#      arguments, so there is no need to specify every argument up-to a last
#      non-default argument.
#    * The Python routines often take tuples i.e. named lists, for many of
#      the input arguments which are bit flags.
#    * The first two arguments to the Python "font.simplify()" is swapped
#      in position.
#    * "font.addExtrema()" (without any arguments) seems to have a different
#      default compared to the legacy interface; not or poorly documented.
#      See https://github.com/fontforge/fontforge/issues/3105
#    * Accessing unused encoding slots in Python throws TypeError, instead
#      of returning False for "font[slot].isWorthOutputting()".
#      See https://github.com/fontforge/fontforge/issues/3107
#
#    * The two blocks of freetype-py code is to work around fontforge's
#      problem coping with newer CJK fonts having glyphs at multiple encoding
#      slots.
#      See https://github.com/fontforge/fontforge/issues/3080 and references
#      therein.
#
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
