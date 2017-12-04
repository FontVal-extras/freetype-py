# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#  CJK multi-encoding fix for Fontforge  - Copyright 2017 Hin-Tak Leung
#  Distributed under the terms of the new BSD license.
#
#  Usage:
#    fontforge -script cjk-multi-fix.py oldname newname
#
#  Example:
#    fontforge -script cjk-multi-fix.py NotoSerifCJKtc-Medium.otf NotoSerifCJKtc-Medium-fixed.otf
#
#  This script requires freetype-py ( https://github.com/rougier/freetype-py ).
#  On Linux systems, the package may be called "python{,2,3}-freetype" instead.
#  Also fontforge needs to be built with
#  "./configure --enable-python-scripting --enable-python-extension" .
#  This is often the case on Linux, anyway.
#
#  The command "echo 'import fontforge' | python" indicates whether
#  the fontforge python extension is available. This command is silent on
#  success, but shows "ImportError: No module named fontforge" on failure.
#
#  *** Important ***:
#    To process many Adobe CFF OpenType fonts correctly (e.g. Source/Noto CJK),
#    the file "Adobe-Identity-0.cidmap" must be moved or renamed to be hidden
#    from being found by fontforge. On Linux, it is in "/usr/share/fontforge".
#    See https://github.com/fontforge/fontforge/issues/3084 .
#
#    On Ubuntu Linux, this file is in a separate "fontforge-extras" package.
#    i.e. The Ubuntu "fontforge-extras" package must NOT be installed.
#
# -----------------------------------------------------------------------------
import fontforge
from freetype import Face
import time
import locale

if ( fontforge.version() < "20071105" ):
    print( "Can't use FontForge version before 2007-11-05.  Aborting." )
    exit(1)

if ( len(sys.argv) != 3 ):
    print( "usage: [fontforge -script] ", sys.argv[0], " oldname newname" )
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

font.selection.all()

font.generate(sys.argv[2])

font.close()
