#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#  Diagnostics with FontVal's backend - Copyright 2017 Hin-Tak Leung
#  Distributed under the terms of the new BSD license.
#
# -----------------------------------------------------------------------------
from freetype import *


def set_and_check_interpreter_version(x):
    library = get_handle()
    version = c_int(x)
    FT_Property_Set(library, "truetype", "interpreter-version", byref(version))

    got_version = c_int(0)
    FT_Property_Get(library, "truetype", "interpreter-version", byref(got_version))
    print("truetype interpreter-version:", got_version)


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


    # default from FreeType 2.7 onwards is 40
    set_and_check_interpreter_version(40)

    # try setting to 38 and checking
    set_and_check_interpreter_version(38)

    # try setting to 35 and checking
    set_and_check_interpreter_version(35)

    # back to 40
    set_and_check_interpreter_version(40)

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
            print(sDetails, ":", message)
            return 0
        c_diagfunc = DIAGFUNCptr(py_diagfunc)
        TT_Diagnostics_Set(c_diagfunc)
        face.load_glyph(ig, lf)
        TT_Diagnostics_Unset()
