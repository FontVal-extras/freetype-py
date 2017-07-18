
# This file is derived from FontVal's GenerateFValData/OurData.xml
# and should stay in sync.

fv_diag = { 
    '_rast_A_ExceptionUnhandled' : 
    [ 'A6000', 'An exception occurred during rasterization testing' ],
    '_rast_E_3_USED_FOR_PERIOD' : 
    [ 'E6000', 'Reserved value of 3 used for period' ],
    '_rast_E_BITS_10_AND_13_SET' : 
    [ 'E6001', 'Bits 10 and 13 are set, they are mutually exclusive' ],
    '_rast_E_BITS_8_AND_11_SET' : 
    [ 'E6002', 'Bits 8 and 11 are set, they are mutually exclusive' ],
    '_rast_E_BITS_9_AND_12_SET' : 
    [ 'E6003', 'Bits 9 and 12 are set, they are mutually exclusive' ],
    '_rast_E_CONTOUR_OUT_OF_RANGE' : 
    [ 'E6004', 'Contour out of range' ],
    '_rast_E_CVT_OUT_OF_RANGE' : 
    [ 'E6005', 'CVT Out of range' ],
    '_rast_E_DIVIDE_BY_ZERO' : 
    [ 'E6006', 'Divide by zero' ],
    '_rast_E_EIF_WITHOUT_IF' : 
    [ 'E6007', 'EIF found without IF' ],
    '_rast_E_ELSE_WITHOUT_EIF' : 
    [ 'E6008', 'ELSE found without EIF' ],
    '_rast_E_ELSE_WITHOUT_IF' : 
    [ 'E6009', 'ELSE found without IF' ],
    '_rast_E_ENDF_BEYOND_64K_OF_FDEF' : 
    [ 'E6010', 'ENDF beyond 64K of FDEF' ],
    '_rast_E_ENDF_BEYOND_64K_OF_IDEF' : 
    [ 'E6011', 'ENDF beyond 64K of IDEF' ],
    '_rast_E_ENDF_EXECUTED' : 
    [ 'E6012', 'ENDF found without FDEF or IDEF' ],
    '_rast_E_EXCEEDS_INSTR_DEFS_IN_MAXP' : 
    [ 'E6013', 'IDEF exceeds max instruction defs in maxp' ],
    '_rast_E_FDEF_FOUND_IN_FDEF' : 
    [ 'E6014', 'FDEF found within FDEF - ENDF pair' ],
    '_rast_E_FDEF_FOUND_IN_IDEF' : 
    [ 'E6015', 'FDEF found within IDEF - ENDF pair' ],
    '_rast_E_FDEF_OUT_OF_RANGE' : 
    [ 'E6016', 'FDEF out of range' ],
    '_rast_E_FDEF_SPACE_NOT_DEFINED' : 
    [ 'E6017', 'Function definition space not defined' ],
    '_rast_E_FDEF_WITHOUT_ENDF' : 
    [ 'E6018', 'FDEF found without ENDF' ],
    '_rast_E_FUCOORDINATE_OUT_OF_RANGE' : 
    [ 'E6019', 'Funit coordinate out of range must be -16384 .. 16383' ],
    '_rast_E_FUNCTION_NOT_DEFINED' : 
    [ 'E6020', 'Function not defined' ],
    '_rast_E_IDEF_FOUND_IN_FDEF' : 
    [ 'E6021', 'IDEF found within FDEF - ENDF pair' ],
    '_rast_E_IDEF_FOUND_IN_IDEF' : 
    [ 'E6022', 'IDEF found within IDEF - ENDF pair' ],
    '_rast_E_IDEF_WITHOUT_ENDF' : 
    [ 'E6023', 'IDEF found without ENDF' ],
    '_rast_E_IF_WITHOUT_EIF' : 
    [ 'E6024', 'IF found without corresponding EIF' ],
    '_rast_E_INST_OPCODE_TO_LARGE' : 
    [ 'E6025', 'Instruction OpCode is to large. Must be between 0 and 255' ],
    '_rast_E_INSTR_DEFD_BY_FS' : 
    [ 'E6026', 'Instruction already defined by rasterizer' ],
    '_rast_E_INVALID_FLAG' : 
    [ 'E6027', 'Invalid Instruction flag' ],
    '_rast_E_INVALID_INSTRUCTION' : 
    [ 'E6028', 'Invalid Instruction' ],
    '_rast_E_INVALID_MAXZONES_IN_MAXP' : 
    [ 'E6029', 'Invalid maxZones in maxp table' ],
    '_rast_E_INVALID_STACK_ACCESS' : 
    [ 'E6030', 'Attempt to access stack element out of range' ],
    '_rast_E_INVALID_ZONE' : 
    [ 'E6031', 'Invalid zone' ],
    '_rast_E_INVALID_ZONE_IN_IUP' : 
    [ 'E6032', 'ZP2 in IUP does not point to zone 1' ],
    '_rast_E_INVALID_ZONE_NO_TWI' : 
    [ 'E6033', 'No twilight zone defined. Invalid zone' ],
    '_rast_E_JMP_BEFORE_BEGINNING' : 
    [ 'E6034', 'Jump before beginning of program or function' ],
    '_rast_E_JMP_BEYOND_2MORE_THAN_END' : 
    [ 'E6035', 'Jump beyond 2 bytes past end of function or program' ],
    '_rast_E_MATH_OVERFLOW' : 
    [ 'E6036', 'Math overflow' ],
    '_rast_E_NOT_CALLED_FROM_PREPROGRAM' : 
    [ 'E6037', 'Not called from pre-program' ],
    '_rast_E_OVERFLOW_INST_PTR' : 
    [ 'E6038', 'Overflow Instruction Stream' ],
    '_rast_E_POINT_OUT_OF_RANGE' : 
    [ 'E6039', 'Point out of range' ],
    '_rast_E_PREPROGAM_ZONE_NOT_TWI' : 
    [ 'E6040', 'Zone referenced in pre-program is not the twilight zone' ],
    '_rast_E_REFPOINT_USED_BUT_NOT_SET' : 
    [ 'E6041', 'Reference point used but not set' ],
    '_rast_E_RESERVED_BIT_SET' : 
    [ 'E6042', 'At least one reserved bit is set' ],
    '_rast_E_RP1_RP2_SAME_POS_ON_PROJ' : 
    [ 'E6043', 'RP1 and RP2 have the same position on the projection vector' ],
    '_rast_E_SELECTOR_INVALID' : 
    [ 'E6044', 'Selector invalid' ],
    '_rast_E_STACK_OVERFLOW' : 
    [ 'E6045', 'Stack Overflow' ],
    '_rast_E_STACK_UNDERFLOW' : 
    [ 'E6046', 'Stack Underflow' ],
    '_rast_E_STORAGE_OUT_OF_RANGE' : 
    [ 'E6047', 'Storage index out of range' ],
    '_rast_E_STORE_INDEX_NOT_WRITTEN_TO' : 
    [ 'E6048', 'Storage location not written to' ],
    '_rast_E_TWILIGHT_ZONE_PT_NOT_SET' : 
    [ 'E6049', 'Twilight zone point not set' ],
    '_rast_E_VALUE_INVALID_0_OR_1' : 
    [ 'E6050', 'Value invalid should be 0 or 1' ],
    '_rast_E_VALUE_INVALID_0_OR_2' : 
    [ 'E6051', 'Value invalid should be 0 or 2' ],
    '_rast_E_VALUE_OUT_OF_RANGE' : 
    [ 'E6052', 'Value out of range' ],
    '_rast_E_VALUE_TO_LARGE_FOR_INT16' : 
    [ 'E6053', 'Value exceeds capacity of 2 byte number' ],
    '_rast_E_VALUE_TO_LARGE_FOR_INT8' : 
    [ 'E6054', 'Value exceeds capacity of 1 byte number' ],
    '_rast_E_VALUE_TO_SMALL' : 
    [ 'E6055', 'Value too small' ],
    '_rast_E_VECTOR_XY_INVALID' : 
    [ 'E6056', 'X and Y components of vector are invalid. X^2 + Y^2 != 0x4000^2' ],
    '_rast_E_VECTOR_XY_ZERO' : 
    [ 'E6057', 'X and Y components of vector are 0' ],
    '_rast_E_ZONE_NOT_0_NOR_1' : 
    [ 'E6058', 'Zone not 0 nor 1' ],
    '_rast_E_rasterization' : 
    [ 'E6059', 'Could not perform rasterization' ],
    '_rast_E_FT_EXECUTION_TOO_LONG' : 
    [ 'E6070', 'Execution time too long and exceeds dynamic limit' ],
    '_rast_E_FT_EXECUTION_TOO_LONG_BACKWARD_JUMP' : 
    [ 'E6071', 'Execution time too long and exceeds dynamic limit in backward jump' ],
    '_rast_I_rasterization' : 
    [ 'I6059', 'Could not perform rasterization' ],
    '_rast_I_FT_Error_Supplymentary_Info' : 
    [ 'I6070', 'Supplementary Information' ],
    '_rast_P_rasterization' : 
    [ 'P6000', 'No problems were found during rasterization testing' ],
    '_rast_W_APPLE_ONLY_INSTR' : 
    [ 'W6000', 'GETVARIATION, GETDATA (Apple-specific) or IDEFs at opcode 0x91,0x92' ],
    '_rast_W_CALL_ZERO_LEN_FUNC' : 
    [ 'W6001', 'CALL to zero length function' ],
    '_rast_W_CALL_ZERO_LEN_UD_INSTR' : 
    [ 'W6002', 'Call to zero length user defined instruction' ],
    '_rast_W_DEBUG_FOUND' : 
    [ 'W6003', 'DEBUG found which should not be found in production code' ],
    '_rast_W_DELTAC_IN_GLYPH_PGM' : 
    [ 'W6004', 'Repeated executions in glyph programs can have unexpected results' ],
    '_rast_W_HI_PT_LESS_THAN_LOW_PT' : 
    [ 'W6005', 'High point is less than low point' ],
    '_rast_W_JMP_OFFSET_ZERO' : 
    [ 'W6006', 'Jump offset zero' ],
    '_rast_W_LOOP_NOT_1_AT_END_OF_PGM' : 
    [ 'W6007', 'Loop variable not 1 at end of program. This means it was set but not used' ],
    '_rast_W_LOOPCALL_COUNT_LESS_THAN_ONE' : 
    [ 'W6008', 'Value for count is less than 1. Function will not be called' ],
    '_rast_W_MPS_ALWAYS_12_ON_WINDOWS' : 
    [ 'W6009', 'Window 95 and Windows 3.1 always return 12' ],
    '_rast_W_PF_VECTORS_AT_OR_NEAR_PERP' : 
    [ 'W6010', 'Projection and freedom vectors at or near perpendicular' ],
    '_rast_W_PT_NOT_TOUCHED' : 
    [ 'W6011', 'Point not touched' ],
    '_rast_W_SANGW_OBSELETE' : 
    [ 'W6012', 'Function no longer needed because of dropped support of AA' ],
    '_rast_W_Need_Newer_FreeType' : 
    [ 'W6019', 'The Freetype version is too old' ],
    '_rast_W_FT_VALUE_OUT_OF_RANGE_SLOOP' : 
    [ 'W6020', 'Setting the loop variable to negative value' ],
    '_rast_W_FT_ZERO_LEN_FUNC' : 
    [ 'W6021', 'Defining zero-length function' ],
    '_rast_W_FT_ZERO_LEN_UD_INSTR' : 
    [ 'W6022', 'Defining zero-length user-defined instruction' ],
    '_rast_W_FT_InvalidOutline' : 
    [ 'W6023', 'Invalid Outline' ],
    '_rast_W_FT_InvalidArgument' : 
    [ 'W6024', 'Invalid Argument' ],
    '_rast_W_FT_InvalidPixelSize' : 
    [ 'W6025', 'Invalid PixelSize' ],
    '_rast_W_FT_InvalidSizeHandle' : 
    [ 'W6026', 'Invalid Size Handle' ],
    '_rast_W_FT_MAXP_maxComponentDepth_TOO_LOW' : 
    [ 'W6027', 'maxComponentDepth in maxp is too low' ],
    '_rast_W_FT_MAX_NUM_TWILIGHT_POINTS_CLAMP' : 
    [ 'W6028', 'number of twilight points unreasonably large' ],
    '_rast_W_FT_VALUE_OUT_OF_RANGE_SLOOP_ZERO' :
    [ 'W6029', 'Setting the loop variable to zero is an error' ],
    '_rast_W_FT_ALIGNRP_AFTER_IUP' :
    [ 'W6030', 'ALIGNRP after IUP in Subpixel-hinting mode' ]
}
