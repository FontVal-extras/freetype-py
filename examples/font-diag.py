#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#  Diagnostics with FontVal's backend - Copyright 2017 Hin-Tak Leung
#  Distributed under the terms of the new BSD license.
#
# -----------------------------------------------------------------------------
from freetype import *

# prototype for diagnostics callback
DIAGFUNCptr = CFUNCTYPE(c_int, c_char_p, c_char_p, c_int, c_int, c_int, c_int, c_int, c_int)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: %s font_filename" % sys.argv[0])
        sys.exit()

    face = Face(sys.argv[1])

    print ('Family name:         {}'.format(face.family_name))
    print ('Style name:          {}'.format(face.style_name))
    print ('Face number:         {}'.format(face.num_faces))
    print ('Glyph number:        {}'.format(face.num_glyphs))
    print ('Available sizes:     {}'.format(face.available_sizes))
    print ('')

    library = get_handle()

    # default from FreeType 2.7 onwards is 40
    got_version = c_int(0)
    FT_Property_Get(library, "truetype", "interpreter-version", byref(got_version))
    print "truetype interpreter-version:", got_version

    # try setting to 38 and checking
    version = c_int(38)
    FT_Property_Set(library, "truetype", "interpreter-version", byref(version))

    got_version = c_int(0)
    FT_Property_Get(library, "truetype", "interpreter-version", byref(got_version))
    print "truetype interpreter-version:", got_version

    # try setting to 35 and checking
    version = c_int(35)
    FT_Property_Set(library, "truetype", "interpreter-version", byref(version))

    got_version = c_int(0)
    FT_Property_Get(library, "truetype", "interpreter-version", byref(got_version))
    print "truetype interpreter-version:", got_version

    # back to 40
    version = c_int(40)
    FT_Property_Set(library, "truetype", "interpreter-version", byref(version))

    got_version = c_int(0)
    FT_Property_Get(library, "truetype", "interpreter-version", byref(got_version))
    print "truetype interpreter-version:", got_version

    size = 10
    face.set_char_size( size * 64, 0, 96, 96 )
    lf = FT_LOAD_DEFAULT|FT_LOAD_NO_AUTOHINT|FT_LOAD_MONOCHROME|FT_LOAD_COMPUTE_METRICS
    lf |= FT_LOAD_TARGET_MONO
    for ig in range(face.num_glyphs):
        def py_diagfunc(message,
                        opcode,
                        range_base,
                        is_composite,
                        IP,
                        callTop,
                        opc,
                        start ):
            sDetails = "Size %d" % size + ", " + opcode
            # python does not have 'switch' statements.
            if ( range_base == 3 ):
                if (is_composite != 0):
                    sDetails += ", Composite Glyph ID %d" % ig
		else:
                    sDetails += ", Glyph ID %d" % ig
            elif (( range_base == 1 ) or ( range_base == 2)):
                sDetails += ", Pre-Program"
            else:
                sDetails += ", Unknown?"
            sDetails += ", At ByteOffset %d" % IP
            if (callTop > 0):
                sDetails += ", In function %d" % opc + " offsetted by %d" % (IP - start)
            print sDetails, ":", message
            return 0
        c_diagfunc = DIAGFUNCptr(py_diagfunc)
        TT_Diagnostics_Set(c_diagfunc)
        face.load_glyph(ig, lf)
        TT_Diagnostics_Unset()
