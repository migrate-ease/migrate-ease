from cffi import FFI
ffi = FFI()
# ffi.cdef is a method in Python's CFFI (C Foreign Function Interface) library
# used to define C types, functions, constants, and global variables.
# It allows you to call C code from Python.
# aarch64 intinsics:
ffi.cdef("""
    unsigned int get_fpcr();
""")

ffi.set_source("_builtin_example", """
    unsigned int get_fpcr() {
        return __builtin_aarch64_get_fpcr();
    }
    """)

ffi.set_source("_test_example", """"
    // common intrinsic test
    * __builtin_apply_args ();
    * __builtin_apply ();
    __builtin_return ();
    __builtin_va_arg_pack ();
    __builtin_va_arg_pack_len ();
    * __builtin_return_address ();
    * __builtin_extract_return_addr ();
    * __builtin_frob_return_address ();
    * __builtin_frame_address ();
    __atomic_load_n (); //expect: PythonCPPStdCodes
    __atomic_load (); //expect: PythonCPPStdCodes
    __atomic_store_n (); //expect: PythonCPPStdCodes
    __atomic_store ();  // expect: PythonCPPStdCodes
    __atomic_exchange_n (); // expect: PythonCPPStdCodes
    __atomic_exchange (); // expect: PythonCPPStdCodes
    __atomic_compare_exchange_n (); // expect: PythonCPPStdCodes
    __atomic_compare_exchange (); // expect: PythonCPPStdCodes
    __atomic_add_fetch (); // expect: PythonCPPStdCodes
    __atomic_sub_fetch (); // expect: PythonCPPStdCodes
    __atomic_and_fetch (); // expect: PythonCPPStdCodes
    __atomic_xor_fetch (); // expect: PythonCPPStdCodes
    __atomic_or_fetch (); // expect: PythonCPPStdCodes
    __atomic_nand_fetch (); // expect: PythonCPPStdCodes
    __atomic_fetch_add (); // expect: PythonCPPStdCodes
    __atomic_fetch_sub (); // expect: PythonCPPStdCodes
    __atomic_fetch_and (); // expect: PythonCPPStdCodes
    __atomic_fetch_xor (); // expect: PythonCPPStdCodes
    __atomic_fetch_or (); // expect: PythonCPPStdCodes
    __atomic_fetch_nand (); // expect: PythonCPPStdCodes
    __atomic_test_and_set (); // expect: PythonCPPStdCodes
    __atomic_clear (); // expect: PythonCPPStdCodes
    __atomic_thread_fence ();
    __atomic_signal_fence ();
    __atomic_always_lock_free ();
    __atomic_is_lock_free ();
    __builtin_object_size ();
    __builtin_types_compatible_p ();
    __builtin_choose_expr ();
    __builtin_complex ();
    __builtin_constant_p ();
    __builtin_expect ();
    __builtin_trap ();
    __builtin_unreachable ();
    *__builtin_assume_aligned ();
    __builtin_LINE ();
    __builtin_FUNCTION ();
    __builtin_FILE ();
    __builtin___clear_cache ();
    __builtin_prefetch ();
    __builtin_huge_val ();
    __builtin_huge_valf ();
    __builtin_huge_vall ();
    __builtin_fpclassify ();
    __builtin_inf ();
    __builtin_infd32 ();
    __builtin_infd64 ();
    __builtin_infd128 ();
    __builtin_inff ();
    __builtin_infl ();
    __builtin_isinf_sign ();
    __builtin_nan ();
    __builtin_nand32 ();
    __builtin_nand64 ();
    __builtin_nand128 ();
    __builtin_nanf ();
    __builtin_nanl ();
    __builtin_nans ();
    __builtin_nansf ();
    __builtin_nansl ();
    __builtin_ffs ();
    __builtin_clz ();
    __builtin_ctz ();
    __builtin_clrsb ();
    __builtin_parity ();
    __builtin_ffsl ();
    __builtin_clzl ();
    __builtin_ctzl ();
    __builtin_clrsbl ();
    __builtin_parityl ();
    __builtin_ffsll ();
    __builtin_clzll ();
    __builtin_ctzll ();
    __builtin_clrsbll ();
    __builtin_parityll ();
    __builtin_powi ();
    __builtin_powif ();
    __builtin_powil ();
    __builtin_bswap16 ();
    __builtin_bswap32 ();
    __builtin_bswap64 ();
    *__builtin_alloca ();
    *__builtin_alloca_with_align ();
    *__builtin_alloca_with_align_and_max ();
    __builtin_has_attribute ();
    __builtin_speculation_safe_value ();
    __builtin_call_with_static_chain ();
    __builtin_tgmath ();
    __builtin_is_constant_evaluated ();
    __builtin_expect_with_probability ();
    * __builtin_assume_aligned ();
    * __builtin_FUNCTION ();
    * __builtin_FILE ();
    __builtin___clear_cache ();
    __builtin_object_size ();
    __builtin_huge_valfn ();
    __builtin_huge_valfnx ();
    __builtin_inffn ();
    __builtin_inffnx ();
    __builtin_nanfn ();
    __builtin_nanfnx ();
    __builtin_nansfn ();
    __builtin_nansfnx ();
    __builtin_ffs ();
    __builtin_ffsl ();
    __builtin_ffsll ();
    __builtin_bswap128 ();
    __builtin_extend_pointer ();
    __builtin_goacc_parlevel_id ();
    __builtin_goacc_parlevel_size ();
    __builtin_popcount ();
    __builtin_popcountl ();
    __builtin_popcountll ();
    __sync_synchronize ();
    __sync_lock_test_and_set ();
    __sync_lock_release ();
    __sync_fetch_and_add (); //expect: PythonCPPStdCodes
    __sync_fetch_and_sub (); //expect: PythonCPPStdCodes
    __sync_fetch_and_or (); //expect: PythonCPPStdCodes
    __sync_fetch_and_and (); //expect: PythonCPPStdCodes
    __sync_fetch_and_xor (); //expect: PythonCPPStdCodes
    __sync_fetch_and_nand (); //expect: PythonCPPStdCodes
    __sync_add_and_fetch (); //expect: PythonCPPStdCodes
    __sync_sub_and_fetch (); //expect: PythonCPPStdCodes
    __sync_or_and_fetch (); //expect: PythonCPPStdCodes
    __sync_and_and_fetch (); //expect: PythonCPPStdCodes
    __sync_xor_and_fetch (); //expect: PythonCPPStdCodes
    __sync_nand_and_fetch (); //expect: PythonCPPStdCodes
    __sync_bool_compare_and_swap (); //expect: PythonCPPStdCodes
    __sync_val_compare_and_swap (); //expect: PythonCPPStdCodes

    // shall not generate issue in aarch64.
    // aarch64 intrinsic test.
    __builtin_aarch64_get_fpcr(); 
    __builtin_aarch64_set_fpcr(); 
    __builtin_aarch64_get_fpsr(); 
    __builtin_aarch64_set_fpsr(); 
    __builtin_aarch64_get_fpcr64(); 
    __builtin_aarch64_set_fpcr64(); 
    __builtin_aarch64_get_fpsr64(); 
    __builtin_aarch64_set_fpsr64();
    // neon intrinsics.
    vadd_u32();
    vadd_u16();
    vadd_u8();
    vadd_s32();
    vadd_s16();
    vadd_s8();
    vadd_f32();
    vadd_u64();
    vadd_s64();
    vaddq_u32();
    vaddq_u16();
    vaddq_u8();
    vaddq_s32();
    vaddq_s16();
    vaddq_s8();
    vaddq_u64();
    vaddq_s64();
    vaddq_f32();
    vaddl_u32();
    vaddl_u16();
    vaddl_u8();
    vaddl_s32();
    vaddl_s16();
    vaddl_s8();
    vaddw_u32();
    vaddw_u16();
    vaddw_u8();
    vaddw_s32();
    vaddw_s16();
    vaddw_s8();
    vhadd_u32();
    vhadd_u16();
    vhadd_u8();
    vhadd_s32();
    vhadd_s16();
    vhadd_s8();
    vhaddq_u32();
    vhaddq_u16();
    vhaddq_u8();
    vhaddq_s32();
    vhaddq_s16();
    vhaddq_s8();
    vrhadd_u32();
    vrhadd_u16();
    vrhadd_u8();
    vrhadd_s32();
    vrhadd_s16();
    vrhadd_s8();
    vrhaddq_u32();
    vrhaddq_u16();
    vrhaddq_u8();
    vrhaddq_s32();
    vrhaddq_s16();
    vrhaddq_s8();
    vqadd_u32();
    vqadd_u16();
    vqadd_u8();
    vqadd_s32();
    vqadd_s16();
    vqadd_s8();
    vqadd_u64();
    vqadd_s64();
    vqaddq_u32();
    vqaddq_u16();
    vqaddq_u8();
    vqaddq_s32();
    vqaddq_s16();
    vqaddq_s8();
    vqaddq_u64();
    vqaddq_s64();
    vaddhn_u64();
    vaddhn_u32();
    vaddhn_u16();
    vaddhn_s64();
    vaddhn_s32();
    vaddhn_s16();
    vraddhn_u64();
    vraddhn_u32();
    vraddhn_u16();
    vraddhn_s64();
    vraddhn_s32();
    vraddhn_s16();
    vmul_u32();
    vmul_u16();
    vmul_u8();
    vmul_s32();
    vmul_s16();
    vmul_s8();
    vmul_f32();
    vmul_p8();
    vmulq_u32();
    vmulq_u16();
    vmulq_u8();
    vmulq_s32();
    vmulq_s16();
    vmulq_s8();
    vmulq_f32();
    vmulq_p8();
    vqdmulh_s32();
    vqdmulh_s16();
    vqdmulhq_s32();
    vqdmulhq_s16();
    vqrdmulh_s32();
    vqrdmulh_s16();
    vqrdmulhq_s32();
    vqrdmulhq_s16();
    vmull_u32();
    vmull_u16();
    vmull_u8();
    vmull_s32();
    vmull_s16();
    vmull_s8();
    vmull_p8();
    vqdmull_s32();
    vqdmull_s16();
    vmla_u32();
    vmla_u16();
    vmla_u8();
    vmla_s32();
    vmla_s16();
    vmla_s8();
    vmla_f32();
    vmlaq_u32();
    vmlaq_u16();
    vmlaq_u8();
    vmlaq_s32();
    vmlaq_s16();
    vmlaq_s8();
    vmlaq_f32();
    vmlal_u32();
    vmlal_u16();
    vmlal_u8(); 
    vmlal_s32(); 
    vmlal_s16(); 
    vmlal_s8(); 
    vqdmlal_s32(); 
    vqdmlal_s16(); 
    vmls_u32();
    vmls_u16();
    vmls_u8();
    vmls_s32();
    vmls_s16();
    vmls_s8();
    vmls_f32();
    vmlsq_u32();
    vmlsq_u16();
    vmlsq_u8();
    vmlsq_s32(); 
    vmlsq_s16(); 
    vmlsq_s8(); 
    vmlsq_f32(); 
    vmlsl_u32(); 
    vmlsl_u16(); 
    vmlsl_u8(); 
    vmlsl_s32(); 
    vmlsl_s16(); 
    vmlsl_s8(); 
    vqdmlsl_s32(); 
    vqdmlsl_s16(); 
    vfma_f32(); 
    vfmaq_f32(); 
    vfms_f32(); 
    vfmsq_f32(); 
    vrndn_f32(); 
    vrndqn_f32(); 
    vrnda_f32(); 
    vrndqa_f32(); 
    vrndp_f32(); 
    vrndqp_f32(); 
    vrndm_f32(); 
    vrndqm_f32(); 
    vrnd_f32(); 
    vrndq_f32(); 
    vsub_u32(); 
    vsub_u16(); 
    vsub_u8(); 
    vsub_s32(); 
    vsub_s16(); 
    vsub_s8(); 
    vsub_f32(); 
    vsub_u64(); 
    vsub_s64(); 
    vsubq_u32(); 
    vsubq_u16(); 
    vsubq_u8(); 
    vsubq_s32(); 
    vsubq_s16(); 
    vsubq_s8(); 
    vsubq_u64(); 
    vsubq_s64(); 
    vsubq_f32(); 
    vsubl_u32(); 
    vsubl_u16(); 
    vsubl_u8(); 
    vsubl_s32(); 
    vsubl_s16(); 
    vsubl_s8(); 
    vsubw_u32(); 
    vsubw_u16(); 
    vsubw_u8(); 
    vsubw_s32(); 
    vsubw_s16(); 
    vsubw_s8(); 
    vhsub_u32(); 
    vhsub_u16(); 
    vhsub_u8(); 
    vhsub_s32(); 
    vhsub_s16(); 
    vhsub_s8(); 
    vhsubq_u32(); 
    vhsubq_u16();
    vhsubq_u8(); 
    vhsubq_s32();
    vhsubq_s16();
    vhsubq_s8();
    vqsub_u32();
    vqsub_u16();
    vqsub_u8();
    vqsub_s32();
    vqsub_s16();
    vqsub_s8();
    vqsub_u64();
    vqsub_s64();
    vqsubq_u32();
    vqsubq_u16();
    vqsubq_u8();
    vqsubq_s32();
    vqsubq_s16();
    vqsubq_s8();
    vqsubq_u64();
    vqsubq_s64();
    vsubhn_u64();
    vsubhn_u32();
    vsubhn_u16();
    vsubhn_s64();
    vsubhn_s32();
    vsubhn_s16();
    vrsubhn_u64();
    vrsubhn_u32();
    vrsubhn_u16(); 
    vrsubhn_s64(); 
    vrsubhn_s32(); 
    vrsubhn_s16(); 
    vceq_u32(); 
    vceq_u16(); 
    vceq_u8(); 
    vceq_s32(); 
    vceq_s16(); 
    vceq_s8(); 
    vceq_f32(); 
    vceq_p8(); 
    vceqq_u32(); 
    vceqq_u16(); 
    vceqq_u8(); 
    vceqq_s32(); 
    vceqq_s16(); 
    vceqq_s8(); 
    vceqq_f32(); 
    vceqq_p8(); 
    vcge_s32(); 
    vcge_s16(); 
    vcge_s8(); 
    vcge_f32(); 
    vcge_u32(); 
    vcge_u16(); 
    vcge_u8(); 
    vcgeq_s32(); 
    vcgeq_s16(); 
    vcgeq_s8(); 
    vcgeq_f32(); 
    vcgeq_u32(); 
    vcgeq_u16(); 
    vcgeq_u8(); 
    vcle_s32(); 
    vcle_s16(); 
    vcle_s8(); 
    vcle_f32(); 
    vcle_u32(); 
    vcle_u16(); 
    vcle_u8(); 
    vcleq_s32(); 
    vcleq_s16(); 
    vcleq_s8(); 
    vcleq_f32(); 
    vcleq_u32(); 
    vcleq_u16(); 
    vcleq_u8(); 
    vcgt_s32(); 
    vcgt_s16(); 
    vcgt_s8(); 
    vcgt_f32(); 
    vcgt_u32(); 
    vcgt_u16(); 
    vcgt_u8(); 
    vcgtq_s32(); 
    vcgtq_s16(); 
    vcgtq_s8(); 
    vcgtq_f32(); 
    vcgtq_u32(); 
    vcgtq_u16(); 
    vcgtq_u8(); 
    vclt_s32(); 
    vclt_s16(); 
    vclt_s8(); 
    vclt_f32(); 
    vclt_u32(); 
    vclt_u16(); 
    vclt_u8(); 
    vcltq_s32(); 
    vcltq_s16(); 
    vcltq_s8(); 
    vcltq_f32(); 
    vcltq_u32(); 
    vcltq_u16(); 
    vcltq_u8(); 
    vcage_f32(); 
    vcageq_f32(); 
    vcale_f32(); 
    vcaleq_f32(); 
    vcagt_f32();  
    vcagtq_f32(); 
    vcalt_f32(); 
    vcaltq_f32(); 
    vtst_u32(); 
    vtst_u16(); 
    vtst_u8(); 
    vtst_s32(); 
    vtst_s16(); 
    vtst_s8(); 
    vtst_p8(); 
    vtstq_u32(); 
    vtstq_u16(); 
    vtstq_u8(); 
    vtstq_s32(); 
    vtstq_s16(); 
    vtstq_s8(); 
    vtstq_p8(); 
    vabd_u32(); 
    vabd_u16(); 
    vabd_u8(); 
    vabd_s32(); 
    vabd_s16(); 
    vabd_s8(); 
    vabd_f32(); 
    vabdq_u32(); 
    vabdq_u16(); 
    vabdq_u8(); 
    vabdq_s32(); 
    vabdq_s16(); 
    vabdq_s8(); 
    vabdq_f32(); 
    vabdl_u32(); 
    vabdl_u16(); 
    vabdl_u8(); 
    vabdl_s32(); 
    vabdl_s16(); 
    vabdl_s8(); 
    vaba_u32(); 
    vaba_u16(); 
    vaba_u8(); 
    vaba_s32(); 
    vaba_s16(); 
    vaba_s8(); 
    vabaq_u32(); 
    vabaq_u16(); 
    vabaq_u8(); 
    vabaq_s32(); 
    vabaq_s16(); 
    vabaq_s8(); 
    vabal_u32(); 
    vabal_u16(); 
    vabal_u8(); 
    vabal_s32(); 
    vabal_s16(); 
    vabal_s8(); 
    vmax_u32(); 
    vmax_u16(); 
    vmax_u8(); 
    vmax_s32(); 
    vmax_s16(); 
    vmax_s8(); 
    vmax_f32(); 
    vmaxq_u32(); 
    vmaxq_u16(); 
    vmaxq_u8(); 
    vmaxq_s32(); 
    vmaxq_s16(); 
    vmaxq_s8(); 
    vmaxq_f32(); 
    vmin_u32(); 
    vmin_u16(); 
    vmin_u8(); 
    vmin_s32(); 
    vmin_s16(); 
    vmin_s8(); 
    vmin_f32(); 
    vminq_u32(); 
    vminq_u16(); 
    vminq_u8(); 
    vminq_s32(); 
    vminq_s16(); 
    vminq_s8(); 
    vminq_f32(); 
    vpadd_u32(); 
    vpadd_u16(); 
    vpadd_u8(); 
    vpadd_s32(); 
    vpadd_s16(); 
    vpadd_s8(); 
    vpadd_f32(); 
    vpaddl_u32(); 
    vpaddl_u16(); 
    vpaddl_u8(); 
    vpaddl_s32(); 
    vpaddl_s16(); 
    vpaddl_s8(); 
    vpaddlq_u32(); 
    vpaddlq_u16(); 
    vpaddlq_u8(); 
    vpaddlq_s32(); 
    vpaddlq_s16(); 
    vpaddlq_s8(); 
    vpadal_u32(); 
    vpadal_u16(); 
    vpadal_u8(); 
    vpadal_s32(); 
    vpadal_s16(); 
    vpadal_s8(); 
    vpadalq_u32(); 
    vpadalq_u16(); 
    vpadalq_u8(); 
    vpadalq_s32(); 
    vpadalq_s16(); 
    vpadalq_s8(); 
    vpmax_u32(); 
    vpmax_u16(); 
    vpmax_u8(); 
    vpmax_s32(); 
    vpmax_s16(); 
    vpmax_s8(); 
    vpmax_f32(); 
    vpmin_u32(); 
    vpmin_u16(); 
    vpmin_u8(); 
    vpmin_s32(); 
    vpmin_s16(); 
    vpmin_s8(); 
    vpmin_f32(); 
    vrecps_f32(); 
    vrecpsq_f32(); 
    vrsqrts_f32(); 
    vrsqrtsq_f32(); 
    vshl_u32(); 
    vshl_u16(); 
    vshl_u8(); 
    vshl_s32(); 
    vshl_s16(); 
    vshl_s8(); 
    vshl_u64(); 
    vshl_s64(); 
    vshlq_u32(); 
    vshlq_u16(); 
    vshlq_u8(); 
    vshlq_s32(); 
    vshlq_s16(); 
    vshlq_s8(); 
    vshlq_u64(); 
    vshlq_s64(); 
    vrshl_u32(); 
    vrshl_u16(); 
    vrshl_u8(); 
    vrshl_s32(); 
    vrshl_s16(); 
    vrshl_s8(); 
    vrshl_u64(); 
    vrshl_s64(); 
    vrshlq_u32(); 
    vrshlq_u16(); 
    vrshlq_u8(); 
    vrshlq_s32(); 
    vrshlq_s16(); 
    vrshlq_s8(); 
    vrshlq_u64(); 
    vrshlq_s64(); 
    vqshl_u32(); 
    vqshl_u16(); 
    vqshl_u8(); 
    vqshl_s32(); 
    vqshl_s16(); 
    vqshl_s8(); 
    vqshl_u64(); 
    vqshl_s64(); 
    vqshlq_u32(); 
    vqshlq_u16(); 
    vqshlq_u8(); 
    vqshlq_s32(); 
    vqshlq_s16(); 
    vqshlq_s8(); 
    vqshlq_u64(); 
    vqshlq_s64(); 
    vqrshl_u32(); 
    vqrshl_u16(); 
    vqrshl_u8(); 
    vqrshl_s32(); 
    vqrshl_s16(); 
    vqrshl_s8(); 
    vqrshl_u64(); 
    vqrshl_s64(); 
    vqrshlq_u32(); 
    vqrshlq_u16(); 
    vqrshlq_u8(); 
    vqrshlq_s32(); 
    vqrshlq_s16(); 
    vqrshlq_s8(); 
    vqrshlq_u64(); 
    vqrshlq_s64(); 
    vshl_n_u32(); 
    vshl_n_u16(); 
    vshl_n_u8(); 
    vshl_n_s32(); 
    vshl_n_s16(); 
    vshl_n_s8(); 
    vshl_n_u64(); 
    vshl_n_s64(); 
    vshlq_n_u32(); 
    vshlq_n_u16(); 
    vshlq_n_u8(); 
    vshlq_n_s32(); 
    vshlq_n_s16(); 
    vshlq_n_s8(); 
    vshlq_n_u64(); 
    vshlq_n_s64(); 
    vqshl_n_u32(); 
    vqshl_n_u16(); 
    vqshl_n_u8(); 
    vqshl_n_s32(); 
    vqshl_n_s16(); 
    vqshl_n_s8(); 
    vqshl_n_u64(); 
    vqshl_n_s64(); 
    vqshlq_n_u32(); 
    vqshlq_n_u16(); 
    vqshlq_n_u8(); 
    vqshlq_n_s32(); 
    vqshlq_n_s16(); 
    vqshlq_n_s8(); 
    vqshlq_n_u64(); 
    vqshlq_n_s64(); 
    vqshlu_n_s64(); 
    vqshlu_n_s32(); 
    vqshlu_n_s16(); 
    vqshlu_n_s8(); 
    vqshluq_n_s64(); 
    vqshluq_n_s32(); 
    vqshluq_n_s16(); 
    vqshluq_n_s8(); 
    vshll_n_u32(); 
    vshll_n_u16(); 
    vshll_n_u8(); 
    vshll_n_s32(); 
    vshll_n_s16(); 
    vshll_n_s8(); 
    vshr_n_u32(); 
    vshr_n_u16(); 
    vshr_n_u8(); 
    vshr_n_s32(); 
    vshr_n_s16(); 
    vshr_n_s8(); 
    vshr_n_u64(); 
    vshr_n_s64(); 
    vshrq_n_u32(); 
    vshrq_n_u16(); 
    vshrq_n_u8(); 
    vshrq_n_s32(); 
    vshrq_n_s16(); 
    vshrq_n_s8(); 
    vshrq_n_u64(); 
    vshrq_n_s64(); 
    vrshr_n_u32(); 
    vrshr_n_u16(); 
    vrshr_n_u8(); 
    vrshr_n_s32(); 
    vrshr_n_s16(); 
    vrshr_n_s8(); 
    vrshr_n_u64(); 
    vrshr_n_s64(); 
    vrshrq_n_u32(); 
    vrshrq_n_u16(); 
    vrshrq_n_u8(); 
    vrshrq_n_s32(); 
    vrshrq_n_s16(); 
    vrshrq_n_s8(); 
    vrshrq_n_u64(); 
    vrshrq_n_s64(); 
    vshrn_n_u64(); 
    vshrn_n_u32(); 
    vshrn_n_u16(); 
    vshrn_n_s64(); 
    vshrn_n_s32(); 
    vshrn_n_s16(); 
    vrshrn_n_u64(); 
    vrshrn_n_u32(); 
    vrshrn_n_u16(); 
    vrshrn_n_s64(); 
    vrshrn_n_s32(); 
    vrshrn_n_s16(); 
    vqshrn_n_u64(); 
    vqshrn_n_u32(); 
    vqshrn_n_u16(); 
    vqshrn_n_s64(); 
    vqshrn_n_s32(); 
    vqshrn_n_s16(); 
    vqrshrn_n_u64(); 
    vqrshrn_n_u32(); 
    vqrshrn_n_u16(); 
    vqrshrn_n_s64(); 
    vqrshrn_n_s32(); 
    vqrshrn_n_s16(); 
    vqshrun_n_s64(); 
    vqshrun_n_s32(); 
    vqshrun_n_s16(); 
    vqrshrun_n_s64(); 
    vqrshrun_n_s32(); 
    vqrshrun_n_s16(); 
    vsra_n_u32(); 
    vsra_n_u16(); 
    vsra_n_u8(); 
    vsra_n_s32(); 
    vsra_n_s16(); 
    vsra_n_s8(); 
    vsra_n_u64(); 
    vsra_n_s64(); 
    vsraq_n_u32(); 
    vsraq_n_u16(); 
    vsraq_n_u8(); 
    vsraq_n_s32(); 
    vsraq_n_s16(); 
    vsraq_n_s8(); 
    vsraq_n_u64(); 
    vsraq_n_s64(); 
    vrsra_n_u32(); 
    vrsra_n_u16(); 
    vrsra_n_u8(); 
    vrsra_n_s32(); 
    vrsra_n_s16(); 
    vrsra_n_s8(); 
    vrsra_n_u64(); 
    vrsra_n_s64(); 
    vrsraq_n_u32(); 
    vrsraq_n_u16(); 
    vrsraq_n_u8(); 
    vrsraq_n_s32(); 
    vrsraq_n_s16(); 
    vrsraq_n_s8(); 
    vrsraq_n_u64(); 
    vrsraq_n_s64(); 
    vsri_n_u32(); 
    vsri_n_u16(); 
    vsri_n_u8(); 
    vsri_n_s32(); 
    vsri_n_s16(); 
    vsri_n_s8(); 
    vsri_n_u64(); 
    vsri_n_s64(); 
    vsri_n_p16(); 
    vsri_n_p8(); 
    vsriq_n_u32(); 
    vsriq_n_u16(); 
    vsriq_n_u8(); 
    vsriq_n_s32(); 
    vsriq_n_s16(); 
    vsriq_n_s8(); 
    vsriq_n_u64(); 
    vsriq_n_s64(); 
    vsriq_n_p16(); 
    vsriq_n_p8(); 
    vsli_n_u32(); 
    vsli_n_u16(); 
    vsli_n_u8(); 
    vsli_n_s32(); 
    vsli_n_s16(); 
    vsli_n_s8(); 
    vsli_n_u64(); 
    vsli_n_s64(); 
    vsli_n_p16(); 
    vsli_n_p8(); 
    vsliq_n_u32(); 
    vsliq_n_u16(); 
    vsliq_n_u8(); 
    vsliq_n_s32(); 
    vsliq_n_s16(); 
    vsliq_n_s8(); 
    vsliq_n_u64(); 
    vsliq_n_s64(); 
    vsliq_n_p16(); 
    vsliq_n_p8(); 
    vabs_f32(); 
    vabs_s32(); 
    vabs_s16(); 
    vabs_s8(); 
    vabsq_f32(); 
    vabsq_s32(); 
    vabsq_s16(); 
    vabsq_s8(); 
    vqabs_s32(); 
    vqabs_s16(); 
    vqabs_s8(); 
    vqabsq_s32(); 
    vqabsq_s16(); 
    vqabsq_s8(); 
    vneg_f32(); 
    vneg_s32(); 
    vneg_s16(); 
    vneg_s8(); 
    vnegq_f32(); 
    vnegq_s32(); 
    vnegq_s16(); 
    vnegq_s8(); 
    vqneg_s32(); 
    vqneg_s16(); 
    vqneg_s8(); 
    vqnegq_s32(); 
    vqnegq_s16(); 
    vqnegq_s8(); 
    vmvn_u32(); 
    vmvn_u16(); 
    vmvn_u8(); 
    vmvn_s32(); 
    vmvn_s16(); 
    vmvn_s8(); 
    vmvn_p8(); 
    vmvnq_u32(); 
    vmvnq_u16(); 
    vmvnq_u8(); 
    vmvnq_s32(); 
    vmvnq_s16(); 
    vmvnq_s8(); 
    vmvnq_p8(); 
    vcls_s32(); 
    vcls_s16(); 
    vcls_s8(); 
    vclsq_s32(); 
    vclsq_s16(); 
    vclsq_s8(); 
    vclz_u32(); 
    vclz_u16(); 
    vclz_u8(); 
    vclz_s32(); 
    vclz_s16(); 
    vclz_s8(); 
    vclzq_u32(); 
    vclzq_u16(); 
    vclzq_u8(); 
    vclzq_s32(); 
    vclzq_s16(); 
    vclzq_s8(); 
    vcnt_u8(); 
    vcnt_s8(); 
    vcnt_p8(); 
    vcntq_u8(); 
    vcntq_s8(); 
    vcntq_p8(); 
    vrecpe_f32(); 
    vrecpe_u32(); 
    vrecpeq_f32(); 
    vrecpeq_u32(); 
    vrsqrte_f32(); 
    vrsqrte_u32();
    vrsqrteq_f32();
    vrsqrteq_u32();
    vget_lane_u32();
    vget_lane_u16();
    vget_lane_u8();
    vget_lane_s32();
    vget_lane_s16();
    vget_lane_s8();
    vget_lane_f32();
    vget_lane_p16();
    vget_lane_p8();
    vget_lane_u64();
    vget_lane_s64();
    vgetq_lane_u32();
    vgetq_lane_u16();
    vgetq_lane_u8();
    vgetq_lane_s32();
    vgetq_lane_s16();
    vgetq_lane_s8();
    vgetq_lane_f32();
    vgetq_lane_p16();
    vgetq_lane_p8();
    vgetq_lane_u64();
    vgetq_lane_s64();
    vset_lane_u32();
    vset_lane_u16();
    vset_lane_u8();
    vset_lane_s32();
    vset_lane_s16();
    vset_lane_s8();
    vset_lane_f32();
    vset_lane_p16();
    vset_lane_p8();
    vset_lane_u64();
    vset_lane_s64();
    vsetq_lane_u32();
    vsetq_lane_u16();
    vsetq_lane_u8();
    vsetq_lane_s32();
    vsetq_lane_s16();  
    vsetq_lane_s8();  
    vsetq_lane_f32(); 
    vsetq_lane_p16(); 
    vsetq_lane_p8(); 
    vsetq_lane_u64(); 
    vsetq_lane_s64(); 
    vcreate_u32(); 
    vcreate_u16(); 
    vcreate_u8(); 
    vcreate_s32(); 
    vcreate_s16(); 
    vcreate_s8(); 
    vcreate_u64(); 
    vcreate_s64(); 
    vcreate_f32(); 
    vcreate_p16(); 
    vcreate_p8(); 
    vdup_n_u32(); 
    vdup_n_u16(); 
    vdup_n_u8(); 
    vdup_n_s32(); 
    vdup_n_s16(); 
    vdup_n_s8(); 
    vdup_n_f32(); 
    vdup_n_p16(); 
    vdup_n_p8(); 
    vdup_n_u64(); 
    vdup_n_s64(); 
    vdupq_n_u32(); 
    vdupq_n_u16(); 
    vdupq_n_u8(); 
    vdupq_n_s32(); 
    vdupq_n_s16(); 
    vdupq_n_s8(); 
    vdupq_n_f32(); 
    vdupq_n_p16(); 
    vdupq_n_p8(); 
    vdupq_n_u64(); 
    vdupq_n_s64(); 
    vmov_n_u32(); 
    vmov_n_u16(); 
    vmov_n_u8(); 
    vmov_n_s32(); 
    vmov_n_s16(); 
    vmov_n_s8(); 
    vmov_n_f32(); 
    vmov_n_p16(); 
    vmov_n_p8(); 
    vmov_n_u64(); 
    vmov_n_s64(); 
    vmovq_n_u32(); 
    vmovq_n_u16(); 
    vmovq_n_u8(); 
    vmovq_n_s32(); 
    vmovq_n_s16(); 
    vmovq_n_s8(); 
    vmovq_n_f32(); 
    vmovq_n_p16(); 
    vmovq_n_p8(); 
    vmovq_n_u64(); 
    vmovq_n_s64(); 
    vdup_lane_u32(); 
    vdup_lane_u16(); 
    vdup_lane_u8(); 
    vdup_lane_s32(); 
    vdup_lane_s16(); 
    vdup_lane_s8(); 
    vdup_lane_f32(); 
    vdup_lane_p16(); 
    vdup_lane_p8(); 
    vdup_lane_u64(); 
    vdup_lane_s64(); 
    vdupq_lane_u32(); 
    vdupq_lane_u16(); 
    vdupq_lane_u8(); 
    vdupq_lane_s32(); 
    vdupq_lane_s16(); 
    vdupq_lane_s8();
    vdupq_lane_f32(); 
    vdupq_lane_p16(); 
    vdupq_lane_p8(); 
    vdupq_lane_u64(); 
    vdupq_lane_s64(); 
    vcombine_u32(); 
    vcombine_u16(); 
    vcombine_u8(); 
    vcombine_s32(); 
    vcombine_s16(); 
    vcombine_s8(); 
    vcombine_u64(); 
    vcombine_s64(); 
    vcombine_f32(); 
    vcombine_p16(); 
    vcombine_p8(); 
    vget_high_u32(); 
    vget_high_u16(); 
    vget_high_u8(); 
    vget_high_s32(); 
    vget_high_s16(); 
    vget_high_s8(); 
    vget_high_u64(); 
    vget_high_s64(); 
    vget_high_f32(); 
    vget_high_p16(); 
    vget_high_p8(); 
    vget_low_u32(); 
    vget_low_u16(); 
    vget_low_u8(); 
    vget_low_s32(); 
    vget_low_s16(); 
    vget_low_s8(); 
    vget_low_f32(); 
    vget_low_p16(); 
    vget_low_p8(); 
    vget_low_u64(); 
    vget_low_s64(); 
    vcvt_f32_u32(); 
    vcvt_f32_s32(); 
    vcvt_u32_f32(); 
    vcvt_s32_f32(); 
    vcvtq_f32_u32(); 
    vcvtq_f32_s32(); 
    vcvtq_u32_f32(); 
    vcvtq_s32_f32(); 
    vcvt_n_f32_u32(); 
    vcvt_n_f32_s32(); 
    vcvt_n_u32_f32(); 
    vcvt_n_s32_f32(); 
    vcvtq_n_f32_u32(); 
    vcvtq_n_f32_s32(); 
    vcvtq_n_u32_f32(); 
    vcvtq_n_s32_f32(); 
    vmovn_u64(); 
    vmovn_u32(); 
    vmovn_u16(); 
    vmovn_s64(); 
    vmovn_s32(); 
    vmovn_s16(); 
    vqmovn_u64(); 
    vqmovn_u32(); 
    vqmovn_u16(); 
    vqmovn_s64(); 
    vqmovn_s32(); 
    vqmovn_s16(); 
    vqmovun_s64(); 
    vqmovun_s32(); 
    vqmovun_s16(); 
    vmovl_u32(); 
    vmovl_u16(); 
    vmovl_u8(); 
    vmovl_s32(); 
    vmovl_s16(); 
    vmovl_s8(); 
    vtbl1_p8(); 
    vtbl1_s8(); 
    vtbl1_u8(); 
    vtbl2_p8(); 
    vtbl2_s8(); 
    vtbl2_u8(); 
    vtbl3_p8(); 
    vtbl3_s8(); 
    vtbl3_u8(); 
    vtbl4_p8(); 
    vtbl4_s8(); 
    vtbl4_u8(); 
    vtbx1_p8(); 
    vtbx1_s8(); 
    vtbx1_u8(); 
    vtbx2_p8(); 
    vtbx2_s8(); 
    vtbx2_u8(); 
    vtbx3_p8(); 
    vtbx3_s8(); 
    vtbx3_u8(); 
    vtbx4_p8(); 
    vtbx4_s8(); 
    vtbx4_u8(); 
    vmul_lane_f32(); 
    vmul_lane_u32(); 
    vmul_lane_u16(); 
    vmul_lane_s32(); 
    vmul_lane_s16(); 
    vmulq_lane_f32(); 
    vmulq_lane_u32(); 
    vmulq_lane_u16(); 
    vmulq_lane_s32(); 
    vmulq_lane_s16(); 
    vmull_lane_u32(); 
    vmull_lane_u16(); 
    vmull_lane_s32(); 
    vmull_lane_s16(); 
    vqdmull_lane_s32(); 
    vqdmull_lane_s16(); 
    vqdmulhq_lane_s32(); 
    vqdmulhq_lane_s16(); 
    vqdmulh_lane_s32(); 
    vqdmulh_lane_s16(); 
    vqrdmulhq_lane_s32(); 
    vqrdmulhq_lane_s16(); 
    vqrdmulh_lane_s32(); 
    vqrdmulh_lane_s16(); 
    vmla_lane_f32(); 
    vmla_lane_u32(); 
    vmla_lane_u16(); 
    vmla_lane_s32(); 
    vmla_lane_s16(); 
    vmlaq_lane_f32(); 
    vmlaq_lane_u32(); 
    vmlaq_lane_u16(); 
    vmlaq_lane_s32(); 
    vmlaq_lane_s16(); 
    vmlal_lane_u32(); 
    vmlal_lane_u16(); 
    vmlal_lane_s32(); 
    vmlal_lane_s16(); 
    vqdmlal_lane_s32(); 
    vqdmlal_lane_s16(); 
    vmls_lane_f32(); 
    vmls_lane_u32(); 
    vmls_lane_u16(); 
    vmls_lane_s32(); 
    vmls_lane_s16(); 
    vmlsq_lane_f32(); 
    vmlsq_lane_u32(); 
    vmlsq_lane_u16(); 
    vmlsq_lane_s32(); 
    vmlsq_lane_s16(); 
    vmlsl_lane_u32(); 
    vmlsl_lane_u16(); 
    vmlsl_lane_s32(); 
    vmlsl_lane_s16(); 
    vqdmlsl_lane_s32(); 
    vqdmlsl_lane_s16(); 
    vmul_n_f32(); 
    vmul_n_u32(); 
    vmul_n_u16(); 
    vmul_n_s32(); 
    vmul_n_s16(); 
    vmulq_n_f32(); 
    vmulq_n_u32(); 
    vmulq_n_u16(); 
    vmulq_n_s32(); 
    vmulq_n_s16(); 
    vmull_n_u32(); 
    vmull_n_u16(); 
    vmull_n_s32(); 
    vmull_n_s16(); 
    vqdmull_n_s32(); 
    vqdmull_n_s16(); 
    vqdmulhq_n_s32(); 
    vqdmulhq_n_s16(); 
    vqdmulh_n_s32(); 
    vqdmulh_n_s16(); 
    vqrdmulhq_n_s32(); 
    vqrdmulhq_n_s16(); 
    vqrdmulh_n_s32(); 
    vqrdmulh_n_s16(); 
    vmla_n_f32(); 
    vmla_n_u32(); 
    vmla_n_u16(); 
    vmla_n_s32(); 
    vmla_n_s16(); 
    vmlaq_n_f32(); 
    vmlaq_n_u32(); 
    vmlaq_n_u16(); 
    vmlaq_n_s32(); 
    vmlaq_n_s16(); 
    vmlal_n_u32(); 
    vmlal_n_u16(); 
    vmlal_n_s32(); 
    vmlal_n_s16(); 
    vqdmlal_n_s32(); 
    vqdmlal_n_s16(); 
    vmls_n_f32(); 
    vmls_n_u32(); 
    vmls_n_u16(); 
    vmls_n_s32(); 
    vmls_n_s16(); 
    vmlsq_n_f32(); 
    vmlsq_n_u32(); 
    vmlsq_n_u16(); 
    vmlsq_n_s32(); 
    vmlsq_n_s16(); 
    vmlsl_n_u32(); 
    vmlsl_n_u16(); 
    vmlsl_n_s32(); 
    vmlsl_n_s16(); 
    vqdmlsl_n_s32(); 
    vqdmlsl_n_s16(); 
    vext_u32(); 
    vext_u16(); 
    vext_u8(); 
    vext_s32(); 
    vext_s16(); 
    vext_s8(); 
    vext_u64(); 
    vext_s64(); 
    vext_f32(); 
    vext_p16(); 
    vext_p8(); 
    vextq_u32(); 
    vextq_u16(); 
    vextq_u8(); 
    vextq_s32(); 
    vextq_s16(); 
    vextq_s8(); 
    vextq_u64(); 
    vextq_s64(); 
    vextq_f32(); 
    vextq_p16(); 
    vextq_p8(); 
    vrev64_u32(); 
    vrev64_u16(); 
    vrev64_u8(); 
    vrev64_s32(); 
    vrev64_s16(); 
    vrev64_s8(); 
    vrev64_f32(); 
    vrev64_p16(); 
    vrev64_p8(); 
    vrev64q_u32(); 
    vrev64q_u16(); 
    vrev64q_u8(); 
    vrev64q_s32(); 
    vrev64q_s16(); 
    vrev64q_s8(); 
    vrev64q_f32(); 
    vrev64q_p16(); 
    vrev64q_p8(); 
    vrev32_u16(); 
    vrev32_s16(); 
    vrev32_u8(); 
    vrev32_s8(); 
    vrev32_p16(); 
    vrev32_p8(); 
    vrev32q_u16(); 
    vrev32q_s16(); 
    vrev32q_u8(); 
    vrev32q_s8(); 
    vrev32q_p16(); 
    vrev32q_p8(); 
    vrev16_u8(); 
    vrev16_s8(); 
    vrev16_p8(); 
    vrev16q_u8(); 
    vrev16q_s8(); 
    vrev16q_p8(); 
    vbsl_u32(); 
    vbsl_u16(); 
    vbsl_u8(); 
    vbsl_s32(); 
    vbsl_s16(); 
    vbsl_s8(); 
    vbsl_u64(); 
    vbsl_s64(); 
    vbsl_f32(); 
    vbsl_p16(); 
    vbsl_p8(); 
    vbslq_u32(); 
    vbslq_u16(); 
    vbslq_u8(); 
    vbslq_s32(); 
    vbslq_s16(); 
    vbslq_s8(); 
    vbslq_u64(); 
    vbslq_s64(); 
    vbslq_f32(); 
    vbslq_p16(); 
    vbslq_p8(); 
    vtrn_u16(); 
    vtrn_u8(); 
    vtrn_s16(); 
    vtrn_s8(); 
    vtrn_p16(); 
    vtrn_p8(); 
    vtrn_f32(); 
    vtrn_u32(); 
    vtrn_s32(); 
    vtrnq_u32(); 
    vtrnq_u16(); 
    vtrnq_u8(); 
    vtrnq_s32(); 
    vtrnq_s16(); 
    vtrnq_s8(); 
    vtrnq_f32(); 
    vtrnq_p16(); 
    vtrnq_p8(); 
    vzip_u16(); 
    vzip_u8(); 
    vzip_s16(); 
    vzip_s8(); 
    vzip_p16(); 
    vzip_p8(); 
    vzip_f32(); 
    vzip_u32(); 
    vzip_s32(); 
    vzipq_u32(); 
    vzipq_u16(); 
    vzipq_u8(); 
    vzipq_s32(); 
    vzipq_s16(); 
    vzipq_s8(); 
    vzipq_f32(); 
    vzipq_p16(); 
    vzipq_p8(); 
    vuzp_u32(); 
    vuzp_u16(); 
    vuzp_u8(); 
    vuzp_s32(); 
    vuzp_s16(); 
    vuzp_s8(); 
    vuzp_f32(); 
    vuzp_p16(); 
    vuzp_p8(); 
    vuzpq_u32(); 
    vuzpq_u16(); 
    vuzpq_u8(); 
    vuzpq_s32(); 
    vuzpq_s16(); 
    vuzpq_s8(); 
    vuzpq_f32(); 
    vuzpq_p16(); 
    vuzpq_p8(); 
    vld1_u32(); 
    vld1_u16(); 
    vld1_u8(); 
    vld1_s32(); 
    vld1_s16(); 
    vld1_s8(); 
    vld1_u64(); 
    vld1_s64(); 
    vld1_f32(); 
    vld1_p16(); 
    vld1_p8(); 
    vld1q_u32(); 
    vld1q_u16(); 
    vld1q_u8(); 
    vld1q_s32(); 
    vld1q_s16(); 
    vld1q_s8(); 
    vld1q_u64(); 
    vld1q_s64(); 
    vld1q_f32(); 
    vld1q_p16(); 
    vld1q_p8(); 
    vld1_lane_u32(); 
    vld1_lane_u16(); 
    vld1_lane_u8(); 
    vld1_lane_s32(); 
    vld1_lane_s16(); 
    vld1_lane_s8(); 
    vld1_lane_f32(); 
    vld1_lane_p16(); 
    vld1_lane_p8(); 
    vld1_lane_u64(); 
    vld1_lane_s64(); 
    vld1q_lane_u32(); 
    vld1q_lane_u16(); 
    vld1q_lane_u8(); 
    vld1q_lane_s32(); 
    vld1q_lane_s16(); 
    vld1q_lane_s8(); 
    vld1q_lane_f32(); 
    vld1q_lane_p16(); 
    vld1q_lane_p8(); 
    vld1q_lane_u64(); 
    vld1q_lane_s64(); 
    vld1_dup_u32(); 
    vld1_dup_u16(); 
    vld1_dup_u8(); 
    vld1_dup_s32(); 
    vld1_dup_s16(); 
    vld1_dup_s8(); 
    vld1_dup_f32(); 
    vld1_dup_p16(); 
    vld1_dup_p8(); 
    vld1_dup_u64(); 
    vld1_dup_s64(); 
    vld1q_dup_u32(); 
    vld1q_dup_u16(); 
    vld1q_dup_u8(); 
    vld1q_dup_s32(); 
    vld1q_dup_s16(); 
    vld1q_dup_s8(); 
    vld1q_dup_f32(); 
    vld1q_dup_p16(); 
    vld1q_dup_p8(); 
    vld1q_dup_u64(); 
    vld1q_dup_s64(); 
    vst1_u32(); 
    vst1_u16(); 
    vst1_u8(); 
    vst1_s32(); 
    vst1_s16(); 
    vst1_s8(); 
    vst1_u64(); 
    vst1_s64(); 
    vst1_f32(); 
    vst1_p16(); 
    vst1_p8(); 
    vst1q_u32(); 
    vst1q_u16(); 
    vst1q_u8(); 
    vst1q_s32(); 
    vst1q_s16(); 
    vst1q_s8(); 
    vst1q_u64(); 
    vst1q_s64(); 
    vst1q_f32(); 
    vst1q_p16(); 
    vst1q_p8(); 
    vst1_lane_u32(); 
    vst1_lane_u16(); 
    vst1_lane_u8(); 
    vst1_lane_s32(); 
    vst1_lane_s16(); 
    vst1_lane_s8(); 
    vst1_lane_f32(); 
    vst1_lane_p16(); 
    vst1_lane_p8(); 
    vst1_lane_s64(); 
    vst1_lane_u64(); 
    vst1q_lane_u32(); 
    vst1q_lane_u16(); 
    vst1q_lane_u8(); 
    vst1q_lane_s32(); 
    vst1q_lane_s16(); 
    vst1q_lane_s8(); 
    vst1q_lane_f32(); 
    vst1q_lane_p16(); 
    vst1q_lane_p8(); 
    vst1q_lane_s64(); 
    vst1q_lane_u64(); 
    vld2_u32(); 
    vld2_u16(); 
    vld2_u8(); 
    vld2_s32(); 
    vld2_s16(); 
    vld2_s8(); 
    vld2_f32(); 
    vld2_p16(); 
    vld2_p8(); 
    vld2_u64(); 
    vld2_s64(); 
    vld2q_u32(); 
    vld2q_u16(); 
    vld2q_u8(); 
    vld2q_s32(); 
    vld2q_s16(); 
    vld2q_s8(); 
    vld2q_f32(); 
    vld2q_p16(); 
    vld2q_p8(); 
    vld2_lane_u32(); 
    vld2_lane_u16(); 
    vld2_lane_u8(); 
    vld2_lane_s32(); 
    vld2_lane_s16(); 
    vld2_lane_s8(); 
    vld2_lane_f32(); 
    vld2_lane_p16(); 
    vld2_lane_p8(); 
    vld2q_lane_s32(); 
    vld2q_lane_s16(); 
    vld2q_lane_u32(); 
    vld2q_lane_u16(); 
    vld2q_lane_f32(); 
    vld2q_lane_p16(); 
    vld2_dup_u32(); 
    vld2_dup_u16(); 
    vld2_dup_u8(); 
    vld2_dup_s32(); 
    vld2_dup_s16(); 
    vld2_dup_s8(); 
    vld2_dup_f32(); 
    vld2_dup_p16(); 
    vld2_dup_p8(); 
    vld2_dup_u64(); 
    vld2_dup_s64(); 
    vst2_u32(); 
    vst2_u16(); 
    vst2_u8(); 
    vst2_s32(); 
    vst2_s16(); 
    vst2_s8(); 
    vst2_f32(); 
    vst2_p16(); 
    vst2_p8(); 
    vst2_u64(); 
    vst2_s64(); 
    vst2q_u32(); 
    vst2q_u16(); 
    vst2q_u8(); 
    vst2q_s32(); 
    vst2q_s16(); 
    vst2q_s8(); 
    vst2q_f32(); 
    vst2q_p16(); 
    vst2q_p8(); 
    vst2_lane_u32(); 
    vst2_lane_u16(); 
    vst2_lane_u8(); 
    vst2_lane_s32(); 
    vst2_lane_s16(); 
    vst2_lane_s8(); 
    vst2_lane_f32(); 
    vst2_lane_p16(); 
    vst2_lane_p8(); 
    vst2q_lane_s32(); 
    vst2q_lane_s16(); 
    vst2q_lane_u32(); 
    vst2q_lane_u16(); 
    vst2q_lane_f32(); 
    vst2q_lane_p16(); 
    vld3_u32(); 
    vld3_u16(); 
    vld3_u8(); 
    vld3_s32(); 
    vld3_s16(); 
    vld3_s8(); 
    vld3_f32(); 
    vld3_p16(); 
    vld3_p8(); 
    vld3_u64(); 
    vld3_s64(); 
    vld3q_u32(); 
    vld3q_u16(); 
    vld3q_u8(); 
    vld3q_s32(); 
    vld3q_s16(); 
    vld3q_s8(); 
    vld3q_f32(); 
    vld3q_p16(); 
    vld3q_p8(); 
    vld3_lane_u32(); 
    vld3_lane_u16(); 
    vld3_lane_u8(); 
    vld3_lane_s32(); 
    vld3_lane_s16(); 
    vld3_lane_s8(); 
    vld3_lane_f32(); 
    vld3_lane_p16(); 
    vld3_lane_p8(); 
    vld3q_lane_s32(); 
    vld3q_lane_s16(); 
    vld3q_lane_u32(); 
    vld3q_lane_u16(); 
    vld3q_lane_f32(); 
    vld3q_lane_p16(); 
    vld3_dup_u32(); 
    vld3_dup_u16(); 
    vld3_dup_u8(); 
    vld3_dup_s32(); 
    vld3_dup_s16(); 
    vld3_dup_s8(); 
    vld3_dup_f32(); 
    vld3_dup_p16(); 
    vld3_dup_p8(); 
    vld3_dup_u64(); 
    vld3_dup_s64(); 
    vst3_u32(); 
    vst3_u16(); 
    vst3_u8(); 
    vst3_s32(); 
    vst3_s16(); 
    vst3_s8(); 
    vst3_f32(); 
    vst3_p16(); 
    vst3_p8(); 
    vst3_u64(); 
    vst3_s64(); 
    vst3q_u32(); 
    vst3q_u16(); 
    vst3q_u8(); 
    vst3q_s32(); 
    vst3q_s16(); 
    vst3q_s8(); 
    vst3q_f32(); 
    vst3q_p16(); 
    vst3q_p8(); 
    vst3_lane_u32(); 
    vst3_lane_u16(); 
    vst3_lane_u8(); 
    vst3_lane_s32(); 
    vst3_lane_s16(); 
    vst3_lane_s8(); 
    vst3_lane_f32(); 
    vst3_lane_p16(); 
    vst3_lane_p8(); 
    vst3q_lane_s32(); 
    vst3q_lane_s16(); 
    vst3q_lane_u32(); 
    vst3q_lane_u16(); 
    vst3q_lane_f32(); 
    vst3q_lane_p16(); 
    vld4_u32(); 
    vld4_u16(); 
    vld4_u8(); 
    vld4_s32(); 
    vld4_s16(); 
    vld4_s8(); 
    vld4_f32(); 
    vld4_p16(); 
    vld4_p8(); 
    vld4_u64(); 
    vld4_s64(); 
    vld4q_u32(); 
    vld4q_u16(); 
    vld4q_u8(); 
    vld4q_s32(); 
    vld4q_s16(); 
    vld4q_s8(); 
    vld4q_f32(); 
    vld4q_p16(); 
    vld4q_p8(); 
    vld4_lane_u32(); 
    vld4_lane_u16(); 
    vld4_lane_u8(); 
    vld4_lane_s32(); 
    vld4_lane_s16(); 
    vld4_lane_s8(); 
    vld4_lane_f32(); 
    vld4_lane_p16(); 
    vld4_lane_p8(); 
    vld4q_lane_s32(); 
    vld4q_lane_s16(); 
    vld4q_lane_u32(); 
    vld4q_lane_u16(); 
    vld4q_lane_f32(); 
    vld4q_lane_p16(); 
    vld4_dup_u32(); 
    vld4_dup_u16(); 
    vld4_dup_u8(); 
    vld4_dup_s32(); 
    vld4_dup_s16(); 
    vld4_dup_s8(); 
    vld4_dup_f32(); 
    vld4_dup_p16(); 
    vld4_dup_p8(); 
    vld4_dup_u64(); 
    vld4_dup_s64(); 
    vst4_u32(); 
    vst4_u16(); 
    vst4_u8(); 
    vst4_s32(); 
    vst4_s16(); 
    vst4_s8(); 
    vst4_f32(); 
    vst4_p16(); 
    vst4_p8(); 
    vst4_u64(); 
    vst4_s64(); 
    vst4q_u32(); 
    vst4q_u16(); 
    vst4q_u8(); 
    vst4q_s32(); 
    vst4q_s16(); 
    vst4q_s8(); 
    vst4q_f32(); 
    vst4q_p16(); 
    vst4q_p8(); 
    vst4_lane_u32(); 
    vst4_lane_u16(); 
    vst4_lane_u8(); 
    vst4_lane_s32(); 
    vst4_lane_s16(); 
    vst4_lane_s8(); 
    vst4_lane_f32(); 
    vst4_lane_p16(); 
    vst4_lane_p8(); 
    vst4q_lane_s32(); 
    vst4q_lane_s16(); 
    vst4q_lane_u32(); 
    vst4q_lane_u16(); 
    vst4q_lane_f32(); 
    vst4q_lane_p16(); 
    vand_u32(); 
    vand_u16(); 
    vand_u8(); 
    vand_s32(); 
    vand_s16(); 
    vand_s8(); 
    vand_u64(); 
    vand_s64(); 
    vandq_u32(); 
    vandq_u16(); 
    vandq_u8(); 
    vandq_s32(); 
    vandq_s16(); 
    vandq_s8(); 
    vandq_u64(); 
    vandq_s64(); 
    vorr_u32(); 
    vorr_u16(); 
    vorr_u8(); 
    vorr_s32(); 
    vorr_s16(); 
    vorr_s8(); 
    vorr_u64(); 
    vorr_s64(); 
    vorrq_u32(); 
    vorrq_u16(); 
    vorrq_u8(); 
    vorrq_s32(); 
    vorrq_s16(); 
    vorrq_s8(); 
    vorrq_u64(); 
    vorrq_s64(); 
    veor_u32(); 
    veor_u16(); 
    veor_u8(); 
    veor_s32(); 
    veor_s16(); 
    veor_s8(); 
    veor_u64(); 
    veor_s64(); 
    veorq_u32(); 
    veorq_u16(); 
    veorq_u8(); 
    veorq_s32(); 
    veorq_s16(); 
    veorq_s8(); 
    veorq_u64(); 
    veorq_s64(); 
    vbic_u32(); 
    vbic_u16(); 
    vbic_u8(); 
    vbic_s32(); 
    vbic_s16(); 
    vbic_s8(); 
    vbic_u64(); 
    vbic_s64(); 
    vbicq_u32(); 
    vbicq_u16(); 
    vbicq_u8(); 
    vbicq_s32(); 
    vbicq_s16(); 
    vbicq_s8(); 
    vbicq_u64(); 
    vbicq_s64(); 
    vorn_u32(); 
    vorn_u16(); 
    vorn_u8(); 
    vorn_s32(); 
    vorn_s16(); 
    vorn_s8(); 
    vorn_u64(); 
    vorn_s64(); 
    vornq_u32(); 
    vornq_u16(); 
    vornq_u8(); 
    vornq_s32(); 
    vornq_s16(); 
    vornq_s8(); 
    vornq_u64(); 
    vornq_s64(); 
    vreinterpret_p8_u32(); 
    vreinterpret_p8_u16(); 
    vreinterpret_p8_u8(); 
    vreinterpret_p8_s32(); 
    vreinterpret_p8_s16(); 
    vreinterpret_p8_s8(); 
    vreinterpret_p8_u64(); 
    vreinterpret_p8_s64(); 
    vreinterpret_p8_f32(); 
    vreinterpret_p8_p16(); 
    vreinterpretq_p8_u32(); 
    vreinterpretq_p8_u16(); 
    vreinterpretq_p8_u8(); 
    vreinterpretq_p8_s32(); 
    vreinterpretq_p8_s16(); 
    vreinterpretq_p8_s8(); 
    vreinterpretq_p8_u64(); 
    vreinterpretq_p8_s64(); 
    vreinterpretq_p8_f32(); 
    vreinterpretq_p8_p16(); 
    vreinterpret_p16_u32(); 
    vreinterpret_p16_u16(); 
    vreinterpret_p16_u8(); 
    vreinterpret_p16_s32(); 
    vreinterpret_p16_s16(); 
    vreinterpret_p16_s8(); 
    vreinterpret_p16_u64(); 
    vreinterpret_p16_s64(); 
    vreinterpret_p16_f32(); 
    vreinterpret_p16_p8(); 
    vreinterpretq_p16_u32(); 
    vreinterpretq_p16_u16(); 
    vreinterpretq_p16_u8(); 
    vreinterpretq_p16_s32(); 
    vreinterpretq_p16_s16(); 
    vreinterpretq_p16_s8(); 
    vreinterpretq_p16_u64(); 
    vreinterpretq_p16_s64(); 
    vreinterpretq_p16_f32(); 
    vreinterpretq_p16_p8(); 
    vreinterpret_f32_u32(); 
    vreinterpret_f32_u16(); 
    vreinterpret_f32_u8(); 
    vreinterpret_f32_s32(); 
    vreinterpret_f32_s16(); 
    vreinterpret_f32_s8(); 
    vreinterpret_f32_u64(); 
    vreinterpret_f32_s64(); 
    vreinterpret_f32_p16(); 
    vreinterpret_f32_p8(); 
    vreinterpretq_f32_u32(); 
    vreinterpretq_f32_u16(); 
    vreinterpretq_f32_u8(); 
    vreinterpretq_f32_s32(); 
    vreinterpretq_f32_s16(); 
    vreinterpretq_f32_s8(); 
    vreinterpretq_f32_u64(); 
    vreinterpretq_f32_s64(); 
    vreinterpretq_f32_p16(); 
    vreinterpretq_f32_p8(); 
    vreinterpret_s64_u32(); 
    vreinterpret_s64_u16(); 
    vreinterpret_s64_u8(); 
    vreinterpret_s64_s32(); 
    vreinterpret_s64_s16(); 
    vreinterpret_s64_s8(); 
    vreinterpret_s64_u64(); 
    vreinterpret_s64_f32(); 
    vreinterpret_s64_p16(); 
    vreinterpret_s64_p8(); 
    vreinterpretq_s64_u32(); 
    vreinterpretq_s64_u16(); 
    vreinterpretq_s64_u8(); 
    vreinterpretq_s64_s32(); 
    vreinterpretq_s64_s16(); 
    vreinterpretq_s64_s8(); 
    vreinterpretq_s64_u64(); 
    vreinterpretq_s64_f32(); 
    vreinterpretq_s64_p16(); 
    vreinterpretq_s64_p8(); 
    vreinterpret_u64_u32(); 
    vreinterpret_u64_u16(); 
    vreinterpret_u64_u8(); 
    vreinterpret_u64_s32(); 
    vreinterpret_u64_s16(); 
    vreinterpret_u64_s8(); 
    vreinterpret_u64_s64(); 
    vreinterpret_u64_f32(); 
    vreinterpret_u64_p16(); 
    vreinterpret_u64_p8(); 
    vreinterpretq_u64_u32(); 
    vreinterpretq_u64_u16(); 
    vreinterpretq_u64_u8(); 
    vreinterpretq_u64_s32(); 
    vreinterpretq_u64_s16(); 
    vreinterpretq_u64_s8(); 
    vreinterpretq_u64_s64(); 
    vreinterpretq_u64_f32(); 
    vreinterpretq_u64_p16(); 
    vreinterpretq_u64_p8(); 
    vreinterpret_s8_u32(); 
    vreinterpret_s8_u16(); 
    vreinterpret_s8_u8(); 
    vreinterpret_s8_s32(); 
    vreinterpret_s8_s16(); 
    vreinterpret_s8_u64(); 
    vreinterpret_s8_s64(); 
    vreinterpret_s8_f32(); 
    vreinterpret_s8_p16(); 
    vreinterpret_s8_p8(); 
    vreinterpretq_s8_u32(); 
    vreinterpretq_s8_u16(); 
    vreinterpretq_s8_u8(); 
    vreinterpretq_s8_s32(); 
    vreinterpretq_s8_s16(); 
    vreinterpretq_s8_u64(); 
    vreinterpretq_s8_s64(); 
    vreinterpretq_s8_f32(); 
    vreinterpretq_s8_p16(); 
    vreinterpretq_s8_p8(); 
    vreinterpret_s16_u32(); 
    vreinterpret_s16_u16(); 
    vreinterpret_s16_u8(); 
    vreinterpret_s16_s32(); 
    vreinterpret_s16_s8(); 
    vreinterpret_s16_u64(); 
    vreinterpret_s16_s64(); 
    vreinterpret_s16_f32(); 
    vreinterpret_s16_p16(); 
    vreinterpret_s16_p8(); 
    vreinterpretq_s16_u32(); 
    vreinterpretq_s16_u16(); 
    vreinterpretq_s16_u8(); 
    vreinterpretq_s16_s32(); 
    vreinterpretq_s16_s8(); 
    vreinterpretq_s16_u64(); 
    vreinterpretq_s16_s64(); 
    vreinterpretq_s16_f32(); 
    vreinterpretq_s16_p16(); 
    vreinterpretq_s16_p8(); 
    vreinterpret_s32_u32(); 
    vreinterpret_s32_u16(); 
    vreinterpret_s32_u8(); 
    vreinterpret_s32_s16(); 
    vreinterpret_s32_s8(); 
    vreinterpret_s32_u64(); 
    vreinterpret_s32_s64(); 
    vreinterpret_s32_f32(); 
    vreinterpret_s32_p16(); 
    vreinterpret_s32_p8(); 
    vreinterpretq_s32_u32(); 
    vreinterpretq_s32_u16(); 
    vreinterpretq_s32_u8(); 
    vreinterpretq_s32_s16(); 
    vreinterpretq_s32_s8(); 
    vreinterpretq_s32_u64(); 
    vreinterpretq_s32_s64(); 
    vreinterpretq_s32_f32(); 
    vreinterpretq_s32_p16(); 
    vreinterpretq_s32_p8(); 
    vreinterpret_u8_u32(); 
    vreinterpret_u8_u16(); 
    vreinterpret_u8_s32(); 
    vreinterpret_u8_s16(); 
    vreinterpret_u8_s8(); 
    vreinterpret_u8_u64(); 
    vreinterpret_u8_s64(); 
    vreinterpret_u8_f32(); 
    vreinterpret_u8_p16(); 
    vreinterpret_u8_p8(); 
    vreinterpretq_u8_u32(); 
    vreinterpretq_u8_u16(); 
    vreinterpretq_u8_s32(); 
    vreinterpretq_u8_s16(); 
    vreinterpretq_u8_s8(); 
    vreinterpretq_u8_u64(); 
    vreinterpretq_u8_s64(); 
    vreinterpretq_u8_f32(); 
    vreinterpretq_u8_p16(); 
    vreinterpretq_u8_p8(); 
    vreinterpret_u16_u32(); 
    vreinterpret_u16_u8(); 
    vreinterpret_u16_s32(); 
    vreinterpret_u16_s16(); 
    vreinterpret_u16_s8(); 
    vreinterpret_u16_u64(); 
    vreinterpret_u16_s64(); 
    vreinterpret_u16_f32(); 
    vreinterpret_u16_p16(); 
    vreinterpret_u16_p8(); 
    vreinterpretq_u16_u32(); 
    vreinterpretq_u16_u8(); 
    vreinterpretq_u16_s32(); 
    vreinterpretq_u16_s16(); 
    vreinterpretq_u16_s8(); 
    vreinterpretq_u16_u64(); 
    vreinterpretq_u16_s64(); 
    vreinterpretq_u16_f32(); 
    vreinterpretq_u16_p16(); 
    vreinterpretq_u16_p8(); 
    vreinterpret_u32_u16(); 
    vreinterpret_u32_u8(); 
    vreinterpret_u32_s32(); 
    vreinterpret_u32_s16(); 
    vreinterpret_u32_s8(); 
    vreinterpret_u32_u64(); 
    vreinterpret_u32_s64(); 
    vreinterpret_u32_f32(); 
    vreinterpret_u32_p16(); 
    vreinterpret_u32_p8(); 
    vreinterpretq_u32_u16(); 
    vreinterpretq_u32_u8(); 
    vreinterpretq_u32_s32(); 
    vreinterpretq_u32_s16(); 
    vreinterpretq_u32_s8(); 
    vreinterpretq_u32_u64(); 
    vreinterpretq_u32_s64(); 
    vreinterpretq_u32_f32(); 
    vreinterpretq_u32_p16(); 
    vreinterpretq_u32_p8(); 

    // non-aarch64 intrinsic test.
    __builtin_arm_getwcgr0(); //expect: PythonIntrinsicIssue
    __builtin_arm_setwcgr0(); //expect: PythonIntrinsicIssue
    __builtin_arm_getwcgr1(); //expect: PythonIntrinsicIssue
    __builtin_arm_setwcgr1(); //expect: PythonIntrinsicIssue
    __builtin_arm_getwcgr2(); //expect: PythonIntrinsicIssue
    __builtin_arm_setwcgr2(); //expect: PythonIntrinsicIssue
    __builtin_arm_getwcgr3(); //expect: PythonIntrinsicIssue
    __builtin_arm_setwcgr3(); //expect: PythonIntrinsicIssue
    __builtin_arm_textrmsb(); //expect: PythonIntrinsicIssue
    __builtin_arm_textrmsh(); //expect: PythonIntrinsicIssue
    __builtin_arm_textrmsw(); //expect: PythonIntrinsicIssue
    __builtin_arm_textrmub(); //expect: PythonIntrinsicIssue
    __builtin_arm_textrmuh(); //expect: PythonIntrinsicIssue
    __builtin_arm_textrmuw(); //expect: PythonIntrinsicIssue
    __builtin_arm_tinsrb(); //expect: PythonIntrinsicIssue
    __builtin_arm_tinsrh(); //expect: PythonIntrinsicIssue
    __builtin_arm_tinsrw(); //expect: PythonIntrinsicIssue
    __builtin_arm_tmia(); //expect: PythonIntrinsicIssue
    __builtin_arm_tmiabb(); //expect: PythonIntrinsicIssue
    __builtin_arm_tmiabt(); //expect: PythonIntrinsicIssue
    __builtin_arm_tmiaph(); //expect: PythonIntrinsicIssue
    __builtin_arm_tmiatb(); //expect: PythonIntrinsicIssue
    __builtin_arm_tmiatt(); //expect: PythonIntrinsicIssue
    __builtin_arm_tmovmskb(); //expect: PythonIntrinsicIssue
    __builtin_arm_tmovmskh(); //expect: PythonIntrinsicIssue
    __builtin_arm_tmovmskw(); //expect: PythonIntrinsicIssue
    __builtin_arm_waccb(); //expect: PythonIntrinsicIssue
    __builtin_arm_wacch(); //expect: PythonIntrinsicIssue
    __builtin_arm_waccw(); //expect: PythonIntrinsicIssue
    __builtin_arm_waddb(); //expect: PythonIntrinsicIssue
    __builtin_arm_waddbss(); //expect: PythonIntrinsicIssue
    __builtin_arm_waddbus(); //expect: PythonIntrinsicIssue
    __builtin_arm_waddh(); //expect: PythonIntrinsicIssue
    __builtin_arm_waddhss(); //expect: PythonIntrinsicIssue
    __builtin_arm_waddhus(); //expect: PythonIntrinsicIssue
    __builtin_arm_waddw(); //expect: PythonIntrinsicIssue
    __builtin_arm_waddwss(); //expect: PythonIntrinsicIssue
    __builtin_arm_waddwus(); //expect: PythonIntrinsicIssue
    __builtin_arm_walign(); //expect: PythonIntrinsicIssue
    __builtin_arm_wand(); //expect: PythonIntrinsicIssue
    __builtin_arm_wandn(); //expect: PythonIntrinsicIssue
    __builtin_arm_wavg2b(); //expect: PythonIntrinsicIssue
    __builtin_arm_wavg2br(); //expect: PythonIntrinsicIssue
    __builtin_arm_wavg2h(); //expect: PythonIntrinsicIssue
    __builtin_arm_wavg2hr(); //expect: PythonIntrinsicIssue
    __builtin_arm_wcmpeqb(); //expect: PythonIntrinsicIssue
    __builtin_arm_wcmpeqh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wcmpeqw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wcmpgtsb(); //expect: PythonIntrinsicIssue
    __builtin_arm_wcmpgtsh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wcmpgtsw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wcmpgtub(); //expect: PythonIntrinsicIssue
    __builtin_arm_wcmpgtuh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wcmpgtuw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmacs(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmacsz(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmacu(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmacuz(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmadds(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmaddu(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmaxsb(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmaxsh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmaxsw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmaxub(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmaxuh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmaxuw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wminsb(); //expect: PythonIntrinsicIssue
    __builtin_arm_wminsh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wminsw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wminub(); //expect: PythonIntrinsicIssue
    __builtin_arm_wminuh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wminuw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmulsm(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmulul(); //expect: PythonIntrinsicIssue
    __builtin_arm_wmulum(); //expect: PythonIntrinsicIssue
    __builtin_arm_wor(); //expect: PythonIntrinsicIssue
    __builtin_arm_wpackdss(); //expect: PythonIntrinsicIssue
    __builtin_arm_wpackdus(); //expect: PythonIntrinsicIssue
    __builtin_arm_wpackhss(); //expect: PythonIntrinsicIssue
    __builtin_arm_wpackhus(); //expect: PythonIntrinsicIssue
    __builtin_arm_wpackwss(); //expect: PythonIntrinsicIssue
    __builtin_arm_wpackwus(); //expect: PythonIntrinsicIssue
    __builtin_arm_wrord(); //expect: PythonIntrinsicIssue
    __builtin_arm_wrordi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wrorh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wrorhi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wrorw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wrorwi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsadb(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsadbz(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsadh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsadhz(); //expect: PythonIntrinsicIssue
    __builtin_arm_wshufh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wslld(); //expect: PythonIntrinsicIssue
    __builtin_arm_wslldi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsllh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsllhi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsllw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsllwi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsrad(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsradi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsrah(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsrahi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsraw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsrawi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsrld(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsrldi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsrlh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsrlhi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsrlw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsrlwi(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsubb(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsubbss(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsubbus(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsubh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsubhss(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsubhus(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsubw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsubwss(); //expect: PythonIntrinsicIssue
    __builtin_arm_wsubwus(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckehsb(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckehsh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckehsw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckehub(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckehuh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckehuw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckelsb(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckelsh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckelsw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckelub(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckeluh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckeluw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckihb(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckihh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckihw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckilb(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckilh(); //expect: PythonIntrinsicIssue
    __builtin_arm_wunpckilw(); //expect: PythonIntrinsicIssue
    __builtin_arm_wxor(); //expect: PythonIntrinsicIssue
    __builtin_arm_wzero(); //expect: PythonIntrinsicIssue
    _arm_smlal(); //expect: PythonIntrinsicIssue
    _arm_umlal(); //expect: PythonIntrinsicIssue
    _arm_clz(); //expect: PythonIntrinsicIssue
    _arm_qadd(); //expect: PythonIntrinsicIssue
    _arm_qdadd(); //expect: PythonIntrinsicIssue
    _arm_qdsub(); //expect: PythonIntrinsicIssue
    _arm_qsub(); //expect: PythonIntrinsicIssue
    _arm_smlabb(); //expect: PythonIntrinsicIssue
    _arm_smlabt(); //expect: PythonIntrinsicIssue
    _arm_smlatb(); //expect: PythonIntrinsicIssue
    _arm_smlatt(); //expect: PythonIntrinsicIssue
    _arm_smlalbb(); //expect: PythonIntrinsicIssue
    _arm_smlalbt(); //expect: PythonIntrinsicIssue
    _arm_smlaltb(); //expect: PythonIntrinsicIssue
    _arm_smlaltt(); //expect: PythonIntrinsicIssue
    _arm_smlawb(); //expect: PythonIntrinsicIssue
    _arm_smlawt(); //expect: PythonIntrinsicIssue
    _arm_smulbb(); //expect: PythonIntrinsicIssue
    _arm_smulbt(); //expect: PythonIntrinsicIssue
    _arm_smultb(); //expect: PythonIntrinsicIssue
    _arm_smultt(); //expect: PythonIntrinsicIssue
    _arm_smulwb(); //expect: PythonIntrinsicIssue
    _arm_smulwt(); //expect: PythonIntrinsicIssue
    _arm_sadd16(); //expect: PythonIntrinsicIssue
    _arm_sadd8(); //expect: PythonIntrinsicIssue
    _arm_sasx(); //expect: PythonIntrinsicIssue
    _arm_ssax(); //expect: PythonIntrinsicIssue
    _arm_ssub16(); //expect: PythonIntrinsicIssue
    _arm_ssub8(); //expect: PythonIntrinsicIssue
    _arm_shadd16(); //expect: PythonIntrinsicIssue
    _arm_shadd8(); //expect: PythonIntrinsicIssue
    _arm_shasx(); //expect: PythonIntrinsicIssue
    _arm_shsax(); //expect: PythonIntrinsicIssue
    _arm_shsub16(); //expect: PythonIntrinsicIssue
    _arm_shsub8(); //expect: PythonIntrinsicIssue
    _arm_qadd16(); //expect: PythonIntrinsicIssue
    _arm_qadd8(); //expect: PythonIntrinsicIssue
    _arm_qasx(); //expect: PythonIntrinsicIssue
    _arm_qsax(); //expect: PythonIntrinsicIssue
    _arm_qsub16(); //expect: PythonIntrinsicIssue
    _arm_qsub8(); //expect: PythonIntrinsicIssue
    _arm_uadd16(); //expect: PythonIntrinsicIssue
    _arm_uadd8(); //expect: PythonIntrinsicIssue
    _arm_uasx(); //expect: PythonIntrinsicIssue
    _arm_usax(); //expect: PythonIntrinsicIssue
    _arm_usub16(); //expect: PythonIntrinsicIssue
    _arm_usub8(); //expect: PythonIntrinsicIssue
    _arm_uhadd16(); //expect: PythonIntrinsicIssue
    _arm_uhadd8(); //expect: PythonIntrinsicIssue
    _arm_uhasx(); //expect: PythonIntrinsicIssue
    _arm_uhsax(); //expect: PythonIntrinsicIssue
    _arm_uhsub16(); //expect: PythonIntrinsicIssue
    _arm_uhsub8(); //expect: PythonIntrinsicIssue
    _arm_uqadd16(); //expect: PythonIntrinsicIssue
    _arm_uqadd8(); //expect: PythonIntrinsicIssue
    _arm_uqasx(); //expect: PythonIntrinsicIssue
    _arm_uqsax(); //expect: PythonIntrinsicIssue
    _arm_uqsub16(); //expect: PythonIntrinsicIssue
    _arm_uqsub8(); //expect: PythonIntrinsicIssue
    _arm_sxtab(); //expect: PythonIntrinsicIssue
    _arm_sxtab16(); //expect: PythonIntrinsicIssue
    _arm_sxtah(); //expect: PythonIntrinsicIssue
    _arm_uxtab(); //expect: PythonIntrinsicIssue
    _arm_uxtab16(); //expect: PythonIntrinsicIssue
    _arm_uxtah(); //expect: PythonIntrinsicIssue
    _arm_sxtb(); //expect: PythonIntrinsicIssue
    _arm_sxtb16(); //expect: PythonIntrinsicIssue
    _arm_sxth(); //expect: PythonIntrinsicIssue
    _arm_uxtb(); //expect: PythonIntrinsicIssue
    _arm_uxtb16(); //expect: PythonIntrinsicIssue
    _arm_uxth(); //expect: PythonIntrinsicIssue
    _arm_pkhbt(); //expect: PythonIntrinsicIssue
    _arm_pkhtb(); //expect: PythonIntrinsicIssue
    _arm_usad8(); //expect: PythonIntrinsicIssue
    _arm_usada8(); //expect: PythonIntrinsicIssue
    _arm_ssat(); //expect: PythonIntrinsicIssue
    _arm_usat(); //expect: PythonIntrinsicIssue
    _arm_ssat16(); //expect: PythonIntrinsicIssue
    _arm_usat16(); //expect: PythonIntrinsicIssue
    _arm_rev(); //expect: PythonIntrinsicIssue
    _arm_rev16(); //expect: PythonIntrinsicIssue
    _arm_revsh(); //expect: PythonIntrinsicIssue
    _arm_smlad(); //expect: PythonIntrinsicIssue
    _arm_smladx(); //expect: PythonIntrinsicIssue
    _arm_smlsd(); //expect: PythonIntrinsicIssue
    _arm_smlsdx(); //expect: PythonIntrinsicIssue
    _arm_smmla(); //expect: PythonIntrinsicIssue
    _arm_smmlar(); //expect: PythonIntrinsicIssue
    _arm_smmls(); //expect: PythonIntrinsicIssue
    _arm_smmlsr(); //expect: PythonIntrinsicIssue
    _arm_smmul(); //expect: PythonIntrinsicIssue
    _arm_smmulr(); //expect: PythonIntrinsicIssue
    _arm_smlald(); //expect: PythonIntrinsicIssue
    _arm_smlaldx(); //expect: PythonIntrinsicIssue
    _arm_smlsld(); //expect: PythonIntrinsicIssue
    _arm_smlsldx(); //expect: PythonIntrinsicIssue
    _arm_smuad(); //expect: PythonIntrinsicIssue
    _arm_smuadx(); //expect: PythonIntrinsicIssue
    _arm_smusd(); //expect: PythonIntrinsicIssue
    _arm_smusdx(); //expect: PythonIntrinsicIssue
    _arm_smull(); //expect: PythonIntrinsicIssue
    _arm_umaal(); //expect: PythonIntrinsicIssue
    _arm_bfc(); //expect: PythonIntrinsicIssue
    _arm_bfi(); //expect: PythonIntrinsicIssue
    _arm_rbit(); //expect: PythonIntrinsicIssue
    _arm_sbfx(); //expect: PythonIntrinsicIssue
    _arm_ubfx(); //expect: PythonIntrinsicIssue
    _arm_sdiv(); //expect: PythonIntrinsicIssue
    _arm_udiv(); //expect: PythonIntrinsicIssue
    __cps(); //expect: PythonIntrinsicIssue
    __dmb(); //expect: PythonIntrinsicIssue
    __dsb(); //expect: PythonIntrinsicIssue
    __isb(); //expect: PythonIntrinsicIssue
    __emit(); //expect: PythonIntrinsicIssue
    __hvc(); //expect: PythonIntrinsicIssue
    __iso_volatile_load16(); //expect: PythonIntrinsicIssue
    __iso_volatile_load32(); //expect: PythonIntrinsicIssue
    __iso_volatile_load64(); //expect: PythonIntrinsicIssue
    __iso_volatile_load8(); //expect: PythonIntrinsicIssue
    __iso_volatile_store16(); //expect: PythonIntrinsicIssue
    __iso_volatile_store32(); //expect: PythonIntrinsicIssue
    __iso_volatile_store64(); //expect: PythonIntrinsicIssue
    __iso_volatile_store8(); //expect: PythonIntrinsicIssue
    __ldrexd(); //expect: PythonIntrinsicIssue
    __prefetch(); //expect: PythonIntrinsicIssue
    __rdpmccntr64(); //expect: PythonIntrinsicIssue
    __sev(); //expect: PythonIntrinsicIssue
    __static_assert(); //expect: PythonIntrinsicIssue
    __swi(); //expect: PythonIntrinsicIssue
    __trap(); //expect: PythonIntrinsicIssue
    __wfe(); //expect: PythonIntrinsicIssue
    __wfi(); //expect: PythonIntrinsicIssue
    _AddSatInt(); //expect: PythonIntrinsicIssue
    _CopyDoubleFromInt64(); //expect: PythonIntrinsicIssue
    _CopyFloatFromInt32(); //expect: PythonIntrinsicIssue
    _CopyInt32FromFloat(); //expect: PythonIntrinsicIssue
    _CopyInt64FromDouble(); //expect: PythonIntrinsicIssue
    _CountLeadingOnes(); //expect: PythonIntrinsicIssue
    _CountLeadingOnes64(); //expect: PythonIntrinsicIssue
    _CountLeadingSigns(); //expect: PythonIntrinsicIssue
    _CountLeadingSigns64(); //expect: PythonIntrinsicIssue
    _CountLeadingZeros(); //expect: PythonIntrinsicIssue
    _CountLeadingZeros64(); //expect: PythonIntrinsicIssue
    _CountOneBits(); //expect: PythonIntrinsicIssue
    _CountOneBits64(); //expect: PythonIntrinsicIssue
    _DAddSatInt(); //expect: PythonIntrinsicIssue
    _DSubSatInt(); //expect: PythonIntrinsicIssue
    _isunordered(); //expect: PythonIntrinsicIssue
    _isunorderedf(); //expect: PythonIntrinsicIssue
    _MoveFromCoprocessor(); //expect: PythonIntrinsicIssue
    _MoveFromCoprocessor2(); //expect: PythonIntrinsicIssue
    _MoveFromCoprocessor64(); //expect: PythonIntrinsicIssue
    _MoveToCoprocessor(); //expect: PythonIntrinsicIssue
    _MoveToCoprocessor2(); //expect: PythonIntrinsicIssue
    _MoveToCoprocessor64(); //expect: PythonIntrinsicIssue
    _MulHigh(); //expect: PythonIntrinsicIssue
    _MulUnsignedHigh(); //expect: PythonIntrinsicIssue
    _ReadBankedReg(); //expect: PythonIntrinsicIssue
    _ReadStatusReg(); //expect: PythonIntrinsicIssue
    _SubSatInt(); //expect: PythonIntrinsicIssue
    _WriteBankedReg(); //expect: PythonIntrinsicIssue
    _WriteStatusReg(); //expect: PythonIntrinsicIssue

    __assume(); //expect: PythonIntrinsicIssue
    __code_seg(); //expect: PythonIntrinsicIssue
    __debugbreak(); //expect: PythonIntrinsicIssue
    __fastfail(); //expect: PythonIntrinsicIssue
    __nop(); //expect: PythonIntrinsicIssue
    __yield(); //expect: PythonIntrinsicIssue
    _AddressOfReturnAddress(); //expect: PythonIntrinsicIssue
    _BitScanForward(); //expect: PythonIntrinsicIssue
    _BitScanForward64(); //expect: PythonIntrinsicIssue
    _BitScanReverse(); //expect: PythonIntrinsicIssue
    _BitScanReverse64(); //expect: PythonIntrinsicIssue
    _bittest(); //expect: PythonIntrinsicIssue
    _bittest64(); //expect: PythonIntrinsicIssue
    _bittestandcomplement(); //expect: PythonIntrinsicIssue
    _bittestandreset(); //expect: PythonIntrinsicIssue
    _bittestandset(); //expect: PythonIntrinsicIssue
    _byteswap_uint64(); //expect: PythonIntrinsicIssue
    _byteswap_ulong(); //expect: PythonIntrinsicIssue
    _byteswap_ushort(); //expect: PythonIntrinsicIssue
    _disable(); //expect: PythonIntrinsicIssue
    _enable(); //expect: PythonIntrinsicIssue
    _lrotl(); //expect: PythonIntrinsicIssue
    _lrotr(); //expect: PythonIntrinsicIssue
    _ReadBarrier(); //expect: PythonIntrinsicIssue
    _ReadWriteBarrier(); //expect: PythonIntrinsicIssue
    _ReturnAddress(); //expect: PythonIntrinsicIssue
    _rotl(); //expect: PythonIntrinsicIssue
    _rotl16(); //expect: PythonIntrinsicIssue
    _rotl64(); //expect: PythonIntrinsicIssue
    _rotl8(); //expect: PythonIntrinsicIssue
    _rotr(); //expect: PythonIntrinsicIssue
    _rotr16(); //expect: PythonIntrinsicIssue
    _rotr64(); //expect: PythonIntrinsicIssue
    _rotr8(); //expect: PythonIntrinsicIssue
    _setjmpex(); //expect: PythonIntrinsicIssue
    _WriteBarrier(); //expect: PythonIntrinsicIssue

    _InterlockedAdd(); //expect: PythonIntrinsicIssue
    _InterlockedAdd64(); //expect: PythonIntrinsicIssue
    _InterlockedAdd64_acq(); //expect: PythonIntrinsicIssue
    _InterlockedAdd64_nf(); //expect: PythonIntrinsicIssue
    _InterlockedAdd64_rel(); //expect: PythonIntrinsicIssue
    _InterlockedAdd_acq(); //expect: PythonIntrinsicIssue
    _InterlockedAdd_nf(); //expect: PythonIntrinsicIssue
    _InterlockedAdd_rel(); //expect: PythonIntrinsicIssue
    _InterlockedAnd(); //expect: PythonIntrinsicIssue
    _InterlockedAnd16(); //expect: PythonIntrinsicIssue
    _InterlockedAnd16_acq(); //expect: PythonIntrinsicIssue
    _InterlockedAnd16_nf(); //expect: PythonIntrinsicIssue
    _InterlockedAnd16_rel(); //expect: PythonIntrinsicIssue
    _InterlockedAnd64(); //expect: PythonIntrinsicIssue
    _InterlockedAnd64_acq(); //expect: PythonIntrinsicIssue
    _InterlockedAnd64_nf(); //expect: PythonIntrinsicIssue
    _InterlockedAnd64_rel(); //expect: PythonIntrinsicIssue
    _InterlockedAnd8(); //expect: PythonIntrinsicIssue
    _InterlockedAnd8_acq(); //expect: PythonIntrinsicIssue
    _InterlockedAnd8_nf(); //expect: PythonIntrinsicIssue
    _InterlockedAnd8_rel(); //expect: PythonIntrinsicIssue
    _InterlockedAnd_acq(); //expect: PythonIntrinsicIssue
    _InterlockedAnd_nf(); //expect: PythonIntrinsicIssue
    _InterlockedAnd_rel(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange16(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange16_acq(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange16_nf(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange16_rel(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange64(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange64_acq(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange64_nf(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange64_rel(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange8(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange8_acq(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange8_nf(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange8_rel(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchangePointer(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchangePointer_acq(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchangePointer_nf(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchangePointer_rel(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange_acq(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange_nf(); //expect: PythonIntrinsicIssue
    _InterlockedCompareExchange_rel(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement16(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement16_acq(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement16_nf(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement16_rel(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement64(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement64_acq(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement64_nf(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement64_rel(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement_acq(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement_nf(); //expect: PythonIntrinsicIssue
    _InterlockedDecrement_rel(); //expect: PythonIntrinsicIssue
    _InterlockedExchange(); //expect: PythonIntrinsicIssue
    _InterlockedExchange16(); //expect: PythonIntrinsicIssue
    _InterlockedExchange16_acq(); //expect: PythonIntrinsicIssue
    _InterlockedExchange16_nf(); //expect: PythonIntrinsicIssue
    _InterlockedExchange64(); //expect: PythonIntrinsicIssue
    _InterlockedExchange64_acq(); //expect: PythonIntrinsicIssue
    _InterlockedExchange64_nf(); //expect: PythonIntrinsicIssue
    _InterlockedExchange8(); //expect: PythonIntrinsicIssue
    _InterlockedExchange8_acq(); //expect: PythonIntrinsicIssue
    _InterlockedExchange8_nf(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd16(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd16_acq(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd16_nf(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd16_rel(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd64(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd64_acq(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd64_nf(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd64_rel(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd8(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd8_acq(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd8_nf(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd8_rel(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd_acq(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd_nf(); //expect: PythonIntrinsicIssue
    _InterlockedExchangeAdd_rel(); //expect: PythonIntrinsicIssue
    _InterlockedExchangePointer(); //expect: PythonIntrinsicIssue
    _InterlockedExchangePointer_acq(); //expect: PythonIntrinsicIssue
    _InterlockedExchangePointer_nf(); //expect: PythonIntrinsicIssue
    _InterlockedExchange_acq(); //expect: PythonIntrinsicIssue
    _InterlockedExchange_nf(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement16(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement16_acq(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement16_nf(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement16_rel(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement64(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement64_acq(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement64_nf(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement64_rel(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement_acq(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement_nf(); //expect: PythonIntrinsicIssue
    _InterlockedIncrement_rel(); //expect: PythonIntrinsicIssue
    _InterlockedOr(); //expect: PythonIntrinsicIssue
    _InterlockedOr16(); //expect: PythonIntrinsicIssue
    _InterlockedOr16_acq(); //expect: PythonIntrinsicIssue
    _InterlockedOr16_nf(); //expect: PythonIntrinsicIssue
    _InterlockedOr16_rel(); //expect: PythonIntrinsicIssue
    _InterlockedOr64(); //expect: PythonIntrinsicIssue
    _InterlockedOr64_acq(); //expect: PythonIntrinsicIssue
    _InterlockedOr64_nf(); //expect: PythonIntrinsicIssue
    _InterlockedOr64_rel(); //expect: PythonIntrinsicIssue
    _InterlockedOr8(); //expect: PythonIntrinsicIssue
    _InterlockedOr8_acq(); //expect: PythonIntrinsicIssue
    _InterlockedOr8_nf(); //expect: PythonIntrinsicIssue
    _InterlockedOr8_rel(); //expect: PythonIntrinsicIssue
    _InterlockedOr_acq(); //expect: PythonIntrinsicIssue
    _InterlockedOr_nf(); //expect: PythonIntrinsicIssue
    _InterlockedOr_rel(); //expect: PythonIntrinsicIssue
    _InterlockedXor(); //expect: PythonIntrinsicIssue
    _InterlockedXor16(); //expect: PythonIntrinsicIssue
    _InterlockedXor16_acq(); //expect: PythonIntrinsicIssue
    _InterlockedXor16_nf(); //expect: PythonIntrinsicIssue
    _InterlockedXor16_rel(); //expect: PythonIntrinsicIssue
    _InterlockedXor64(); //expect: PythonIntrinsicIssue
    _InterlockedXor64_acq(); //expect: PythonIntrinsicIssue
    _InterlockedXor64_nf(); //expect: PythonIntrinsicIssue
    _InterlockedXor64_rel(); //expect: PythonIntrinsicIssue
    _InterlockedXor8(); //expect: PythonIntrinsicIssue
    _InterlockedXor8_acq(); //expect: PythonIntrinsicIssue
    _InterlockedXor8_nf(); //expect: PythonIntrinsicIssue
    _InterlockedXor8_rel(); //expect: PythonIntrinsicIssue
    _InterlockedXor_acq(); //expect: PythonIntrinsicIssue
    _InterlockedXor_nf(); //expect: PythonIntrinsicIssue
    _InterlockedXor_rel(); //expect: PythonIntrinsicIssue
    _interlockedbittestandreset(); //expect: PythonIntrinsicIssue
    _interlockedbittestandreset_acq(); //expect: PythonIntrinsicIssue
    _interlockedbittestandreset_nf(); //expect: PythonIntrinsicIssue
    _interlockedbittestandreset_rel(); //expect: PythonIntrinsicIssue
    _interlockedbittestandset(); //expect: PythonIntrinsicIssue
    _interlockedbittestandset_acq(); //expect: PythonIntrinsicIssue
    _interlockedbittestandset_nf(); //expect: PythonIntrinsicIssue
    _interlockedbittestandset_rel(); //expect: PythonIntrinsicIssue

    // x86 intrinsic test
    _mm_srli_epi64(); //expect: PythonIntrinsicIssue 
    _mm_shuffle_epi8(); //expect: PythonIntrinsicIssue 
    _mm_extract_ps(); //expect: PythonIntrinsicIssue 
    _mm_set1_epi64x(); //expect: PythonIntrinsicIssue 
    _mm_mul_epu32(); //expect: PythonIntrinsicIssue 
    _mm_add_epi64(); //expect: PythonIntrinsicIssue 

    _InterlockedAnd8_np(); //expect: PythonIntrinsicIssue 
    _InterlockedOr8_np(); //expect: PythonIntrinsicIssue 
    _InterlockedXor8_np(); //expect: PythonIntrinsicIssue 

    __builtin_ia32_pand(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pandn(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_por(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pxor(); //expect: PythonIntrinsicIssue 

    _mm_cvtsd_f64(); //expect: PythonIntrinsicIssue 
    __builtin_copysignq(); //expect: PythonIntrinsicIssue 
    __builtin_huge_valq(); //expect: PythonIntrinsicIssue 
    __builtin_infq(); //expect: PythonIntrinsicIssue 
    __builtin_fabsq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vec_ext_v4sf(); //expect: PythonIntrinsicIssue 
    _mm_cvtss_f32(); //expect: PythonIntrinsicIssue 
    _m_to_float(); //expect: PythonIntrinsicIssue 
    _div128(); //expect: PythonIntrinsicIssue 
    _InterlockedAnd64_HLEAcquire(); //expect: PythonIntrinsicIssue   
    _InterlockedAnd64_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedAnd64_np(); //expect: PythonIntrinsicIssue 
    _InterlockedCompareExchange64_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _InterlockedCompareExchange64_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedCompareExchange64_np(); //expect: PythonIntrinsicIssue 
    _InterlockedExchange64_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _InterlockedExchange64_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedExchangeAdd64_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _InterlockedExchangeAdd64_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedOr64_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _InterlockedOr64_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedOr64_np(); //expect: PythonIntrinsicIssue 
    _InterlockedXor64_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _InterlockedXor64_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedXor64_np(); //expect: PythonIntrinsicIssue 
    _loadbe_i64(); //expect: PythonIntrinsicIssue 
    _mm_cvtsd_si64(); //expect: PythonIntrinsicIssue 
    _mm_cvtsd_si64x(); //expect: PythonIntrinsicIssue 
    _mm_cvtsi128_si64(); //expect: PythonIntrinsicIssue 
    _mm_cvtsi128_si64x(); //expect: PythonIntrinsicIssue 
    _mm_cvtss_si64(); //expect: PythonIntrinsicIssue 
    _mm_cvtss_si64x(); //expect: PythonIntrinsicIssue 
    _mm_cvttsd_si64(); //expect: PythonIntrinsicIssue 
    _mm_cvttsd_si64x(); //expect: PythonIntrinsicIssue 
    _mm_cvttss_si64(); //expect: PythonIntrinsicIssue 
    _mm_cvttss_si64x(); //expect: PythonIntrinsicIssue 
    _mm_extract_epi64(); //expect: PythonIntrinsicIssue 
    _mm_popcnt_u64(); //expect: PythonIntrinsicIssue 
    _mul128(); //expect: PythonIntrinsicIssue 
    __mulh(); //expect: PythonIntrinsicIssue 
    __emul(); //expect: PythonIntrinsicIssue 
    __ll_rshift(); //expect: PythonIntrinsicIssue 
    _sarx_i64(); //expect: PythonIntrinsicIssue 
    __builtin_cpu_is(); //expect: PythonIntrinsicIssue 
    __builtin_cpu_supports(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_comieq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_comige(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_comigt(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_comile(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_comilt(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_comineq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_comisdeq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_comisdge(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_comisdgt(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_comisdle(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_comisdlt(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_comisdneq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtsd2si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtss2si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvttsd2si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvttss2si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movmskpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movmskpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movmskps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movmskps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpestri128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpestria128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpestric128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpestrio128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpestris128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpestriz128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpistri128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpistria128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpistric128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpistrio128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpistris128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpistriz128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pextrw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovmskb128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovmskb256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovmskb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ptestc128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ptestc256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ptestnzc128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ptestnzc256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ptestz128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ptestz256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomieq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomige(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomigt(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomile(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomilt(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomineq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomisdeq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomisdge(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomisdgt(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomisdle(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomisdlt(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ucomisdneq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vec_ext_v16qi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vec_ext_v4si(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_vtestcpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vtestcpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vtestcps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vtestcps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vtestnzcpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vtestnzcpd(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_vtestnzcps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vtestnzcps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vtestzpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vtestzpd(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_vtestzps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vtestzps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_xbegin(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_xtest(); //expect: PythonIntrinsicIssue 
    _div64(); //expect: PythonIntrinsicIssue 
    _loadbe_i32(); //expect: PythonIntrinsicIssue  
    _mm256_movemask_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_movemask_pd(); //expect: PythonIntrinsicIssue 
    _mm256_movemask_ps(); //expect: PythonIntrinsicIssue 
    _mm256_testc_pd(); //expect: PythonIntrinsicIssue 
    _mm256_testc_ps(); //expect: PythonIntrinsicIssue 
    _mm256_testc_si256(); //expect: PythonIntrinsicIssue 
    _mm256_testnzc_pd(); //expect: PythonIntrinsicIssue 
    _mm256_testnzc_ps(); //expect: PythonIntrinsicIssue 
    _mm256_testnzc_si256(); //expect: PythonIntrinsicIssue 
    _mm256_testz_pd(); //expect: PythonIntrinsicIssue 
    _mm256_testz_ps(); //expect: PythonIntrinsicIssue 
    _mm256_testz_si256(); //expect: PythonIntrinsicIssue 
    _mm_cmpestra(); //expect: PythonIntrinsicIssue 
    _mm_cmpestrc(); //expect: PythonIntrinsicIssue 
    _mm_cmpestri(); //expect: PythonIntrinsicIssue 
    _mm_cmpestro(); //expect: PythonIntrinsicIssue 
    _mm_cmpestrs(); //expect: PythonIntrinsicIssue 
    _mm_cmpestrz(); //expect: PythonIntrinsicIssue 
    _mm_cmpistra(); //expect: PythonIntrinsicIssue 
    _mm_cmpistrc(); //expect: PythonIntrinsicIssue 
    _mm_cmpistri(); //expect: PythonIntrinsicIssue 
    _mm_cmpistro(); //expect: PythonIntrinsicIssue 
    _mm_cmpistrs(); //expect: PythonIntrinsicIssue 
    _mm_cmpistrz(); //expect: PythonIntrinsicIssue 
    _mm_comieq_sd(); //expect: PythonIntrinsicIssue 
    _mm_comieq_ss(); //expect: PythonIntrinsicIssue 
    _mm_comige_sd(); //expect: PythonIntrinsicIssue 
    _mm_comige_ss(); //expect: PythonIntrinsicIssue 
    _mm_comigt_sd(); //expect: PythonIntrinsicIssue 
    _mm_comigt_ss(); //expect: PythonIntrinsicIssue 
    _mm_comile_sd(); //expect: PythonIntrinsicIssue 
    _mm_comile_ss(); //expect: PythonIntrinsicIssue 
    _mm_comilt_sd(); //expect: PythonIntrinsicIssue 
    _mm_comilt_ss(); //expect: PythonIntrinsicIssue 
    _mm_comineq_sd(); //expect: PythonIntrinsicIssue 
    _mm_comineq_ss(); //expect: PythonIntrinsicIssue 
    _mm_cvtsd_si32(); //expect: PythonIntrinsicIssue 
    _mm_cvtsi128_si32(); //expect: PythonIntrinsicIssue 
    _mm_cvt_ss2si(); //expect: PythonIntrinsicIssue 
    _mm_cvttsd_si32(); //expect: PythonIntrinsicIssue 
    _mm_cvtt_ss2si(); //expect: PythonIntrinsicIssue 
    _mm_extract_epi16(); //expect: PythonIntrinsicIssue 
    _mm_extract_epi32(); //expect: PythonIntrinsicIssue 
    _mm_extract_epi8(); //expect: PythonIntrinsicIssue 
    _mm_extract_ps(); //expect: PythonIntrinsicIssue 
    _mm_movemask_epi8(); //expect: PythonIntrinsicIssue 
    _mm_movemask_pd(); //expect: PythonIntrinsicIssue 
    _mm_movemask_ps(); //expect: PythonIntrinsicIssue 
    _mm_popcnt_u32(); //expect: PythonIntrinsicIssue
    _mm_testc_pd(); //expect: PythonIntrinsicIssue 
    _mm_testc_ps(); //expect: PythonIntrinsicIssue 
    _mm_testc_si128(); //expect: PythonIntrinsicIssue 
    _mm_testnzc_pd(); //expect: PythonIntrinsicIssue 
    _mm_testnzc_ps(); //expect: PythonIntrinsicIssue  
    _mm_testnzc_si128(); //expect: PythonIntrinsicIssue 
    _mm_testz_pd(); //expect: PythonIntrinsicIssue 
    _mm_testz_ps(); //expect: PythonIntrinsicIssue 
    _mm_testz_si128(); //expect: PythonIntrinsicIssue 
    _mm_ucomieq_sd(); //expect: PythonIntrinsicIssue 
    _mm_ucomieq_ss(); //expect: PythonIntrinsicIssue 
    _mm_ucomige_sd(); //expect: PythonIntrinsicIssue 
    _mm_ucomige_ss(); //expect: PythonIntrinsicIssue 
    _mm_ucomigt_sd(); //expect: PythonIntrinsicIssue 
    _mm_ucomigt_ss(); //expect: PythonIntrinsicIssue 
    _mm_ucomile_sd(); //expect: PythonIntrinsicIssue 
    _mm_ucomile_ss(); //expect: PythonIntrinsicIssue 
    _mm_ucomilt_sd(); //expect: PythonIntrinsicIssue 
    _mm_ucomilt_ss(); //expect: PythonIntrinsicIssue 
    _mm_ucomineq_sd(); //expect: PythonIntrinsicIssue 
    _mm_ucomineq_ss(); //expect: PythonIntrinsicIssue 
    _m_pextrw(); //expect: PythonIntrinsicIssue 
    _m_pmovmskb(); //expect: PythonIntrinsicIssue 
    _m_to_int(); //expect: PythonIntrinsicIssue 
    _rdrand16_step(); //expect: PythonIntrinsicIssue 
    _rdrand32_step(); //expect: PythonIntrinsicIssue 
    _rdrand64_step(); //expect: PythonIntrinsicIssue 
    _rdseed16_step(); //expect: PythonIntrinsicIssue 
    _rdseed32_step(); //expect: PythonIntrinsicIssue 
    _rdseed64_step(); //expect: PythonIntrinsicIssue 
    _sarx_i32(); //expect: PythonIntrinsicIssue
    _InterlockedAddLargeStatistic(); //expect: PythonIntrinsicIssue 
    _InterlockedAnd_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _InterlockedAnd_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedAnd_np(); //expect: PythonIntrinsicIssue 
    _InterlockedCompareExchange_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _InterlockedCompareExchange_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedCompareExchange_np(); //expect: PythonIntrinsicIssue 
    _InterlockedExchangeAdd_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _InterlockedExchangeAdd_HLERelease(); //expect: PythonIntrinsicIssue  
    _InterlockedExchange_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _InterlockedExchange_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedOr_HLEAcquire(); //expect: PythonIntrinsicIssue
    _InterlockedOr_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedOr_np(); //expect: PythonIntrinsicIssue 
    _InterlockedXor_HLEAcquire(); //expect: PythonIntrinsicIssue  
    _InterlockedXor_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedXor_np(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_cvtsd2si64(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvttsd2si64(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vec_ext_v2di(); //expect: PythonIntrinsicIssue 
    _mm256_castpd256_pd128(); //expect: PythonIntrinsicIssue 
    _mm256_extractf128_pd(); //expect: PythonIntrinsicIssue 
    _mm_add_pd(); //expect: PythonIntrinsicIssue 
    _mm_add_sd(); //expect: PythonIntrinsicIssue 
    _mm_addsub_pd(); //expect: PythonIntrinsicIssue 
    _mm_andnot_pd(); //expect: PythonIntrinsicIssue 
    _mm_and_pd(); //expect: PythonIntrinsicIssue 
    _mm_blend_pd(); //expect: PythonIntrinsicIssue 
    _mm_blendv_pd(); //expect: PythonIntrinsicIssue 
    _mm_broadcastsd_pd(); //expect: PythonIntrinsicIssue 
    _mm_castps_pd(); //expect: PythonIntrinsicIssue 
    _mm_castsi128_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmpeq_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmpeq_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmpge_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmpge_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmpgt_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmpgt_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmple_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmple_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmplt_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmplt_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmpneq_pd(); //expect: PythonIntrinsicIssue  
    _mm_cmpneq_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmpnge_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmpnge_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmpngt_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmpngt_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmpnle_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmpnle_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmpnlt_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmpnlt_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmpord_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmpord_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmp_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmp_sd(); //expect: PythonIntrinsicIssue 
    _mm_cmpunord_pd(); //expect: PythonIntrinsicIssue 
    _mm_cmpunord_sd(); //expect: PythonIntrinsicIssue 
    _mm_cvtepi32_pd(); //expect: PythonIntrinsicIssue 
    _mm_cvtpi32_pd(); //expect: PythonIntrinsicIssue 
    _mm_cvtps_pd(); //expect: PythonIntrinsicIssue 
    _mm_cvtsi32_sd(); //expect: PythonIntrinsicIssue 
    _mm_cvtsi64_sd(); //expect: PythonIntrinsicIssue 
    _mm_cvtsi64x_sd(); //expect: PythonIntrinsicIssue 
    _mm_cvtss_sd(); //expect: PythonIntrinsicIssue 
    _mm_div_pd(); //expect: PythonIntrinsicIssue 
    _mm_div_sd(); //expect: PythonIntrinsicIssue 
    _mm_dp_pd(); //expect: PythonIntrinsicIssue 
    _mm_fmadd_pd(); //expect: PythonIntrinsicIssue 
    _mm_fmadd_sd(); //expect: PythonIntrinsicIssue 
    _mm_fmaddsub_pd(); //expect: PythonIntrinsicIssue 
    _mm_fmsubadd_pd(); //expect: PythonIntrinsicIssue 
    _mm_fmsub_pd(); //expect: PythonIntrinsicIssue 
    _mm_fmsub_sd(); //expect: PythonIntrinsicIssue 
    _mm_fnmadd_pd(); //expect: PythonIntrinsicIssue 
    _mm_fnmadd_sd(); //expect: PythonIntrinsicIssue 
    _mm_fnmsub_pd(); //expect: PythonIntrinsicIssue 
    _mm_fnmsub_sd(); //expect: PythonIntrinsicIssue 
    _mm_frcz_pd(); //expect: PythonIntrinsicIssue  
    _mm_frcz_sd(); //expect: PythonIntrinsicIssue 
    _mm_hadd_pd(); //expect: PythonIntrinsicIssue  
    _mm_hsub_pd(); //expect: PythonIntrinsicIssue 
    _mm_i32gather_pd(); //expect: PythonIntrinsicIssue 
    _mm_i64gather_pd(); //expect: PythonIntrinsicIssue 
    _mm_load1_pd(); //expect: PythonIntrinsicIssue 
    _mm_loaddup_pd(); //expect: PythonIntrinsicIssue 
    _mm_loadh_pd(); //expect: PythonIntrinsicIssue 
    _mm_loadl_pd(); //expect: PythonIntrinsicIssue 
    _mm_load_pd(); //expect: PythonIntrinsicIssue 
    _mm_loadr_pd(); //expect: PythonIntrinsicIssue 
    _mm_load_sd(); //expect: PythonIntrinsicIssue  
    _mm_loadu_pd(); //expect: PythonIntrinsicIssue  
    _mm_macc_pd(); //expect: PythonIntrinsicIssue  
    _mm_macc_sd(); //expect: PythonIntrinsicIssue  
    _mm_macc_sd(); //expect: PythonIntrinsicIssue  
    _mm_maddsub_pd(); //expect: PythonIntrinsicIssue  
    _mm_mask_i32gather_pd(); //expect: PythonIntrinsicIssue  
    _mm_mask_i64gather_pd(); //expect: PythonIntrinsicIssue  
    _mm_maskload_pd(); //expect: PythonIntrinsicIssue  
    _mm_max_pd(); //expect: PythonIntrinsicIssue  
    _mm_max_sd(); //expect: PythonIntrinsicIssue   
    _mm_min_pd(); //expect: PythonIntrinsicIssue  
    _mm_min_sd(); //expect: PythonIntrinsicIssue  
    _mm_movedup_pd(); //expect: PythonIntrinsicIssue  
    _mm_move_sd(); //expect: PythonIntrinsicIssue  
    _mm_msubadd_pd(); //expect: PythonIntrinsicIssue  
    _mm_msub_pd(); //expect: PythonIntrinsicIssue  
    _mm_msub_sd(); //expect: PythonIntrinsicIssue  
    _mm_mul_pd(); //expect: PythonIntrinsicIssue  
    _mm_mul_sd(); //expect: PythonIntrinsicIssue  
    _mm_nmacc_pd(); //expect: PythonIntrinsicIssue 
    _mm_nmacc_sd(); //expect: PythonIntrinsicIssue  
    _mm_nmsub_pd(); //expect: PythonIntrinsicIssue  
    _mm_nmsub_sd(); //expect: PythonIntrinsicIssue 
    _mm_or_pd(); //expect: PythonIntrinsicIssue  
    _mm_permute2_pd(); //expect: PythonIntrinsicIssue  
    _mm_permute_pd(); //expect: PythonIntrinsicIssue  
    _mm_permutevar_pd(); //expect: PythonIntrinsicIssue  
    _mm_round_pd(); //expect: PythonIntrinsicIssue  
    _mm_round_sd(); //expect: PythonIntrinsicIssue  
    _mm_set1_pd(); //expect: PythonIntrinsicIssue  
    _mm_set_pd(); //expect: PythonIntrinsicIssue  
    _mm_setr_pd(); //expect: PythonIntrinsicIssue  
    _mm_set_sd(); //expect: PythonIntrinsicIssue  
    _mm_setzero_pd(); //expect: PythonIntrinsicIssue  
    _mm_shuffle_pd(); //expect: PythonIntrinsicIssue  
    _mm_sqrt_pd(); //expect: PythonIntrinsicIssue  
    _mm_sqrt_sd(); //expect: PythonIntrinsicIssue  
    _mm_sub_pd(); //expect: PythonIntrinsicIssue  
    _mm_sub_sd(); //expect: PythonIntrinsicIssue  
    _mm_unpackhi_pd(); //expect: PythonIntrinsicIssue  
    _mm_unpacklo_pd(); //expect: PythonIntrinsicIssue  
    _mm_xor_pd(); //expect: PythonIntrinsicIssue  
    _mm256_castsi256_si128(); //expect: PythonIntrinsicIssue  
    _mm256_cvtpd_epi32(); //expect: PythonIntrinsicIssue  
    _mm256_cvtps_ph(); //expect: PythonIntrinsicIssue  
    _mm256_cvttpd_epi32(); //expect: PythonIntrinsicIssue  
    _mm256_extractf128_si256(); //expect: PythonIntrinsicIssue  
    _mm256_extracti128_si256(); //expect: PythonIntrinsicIssue  
    _mm256_mask_i64gather_epi32(); //expect: PythonIntrinsicIssue  
     _mm_abs_epi16(); //expect: PythonIntrinsicIssue  
    _mm_abs_epi32(); //expect: PythonIntrinsicIssue  
    _mm_abs_epi8(); //expect: PythonIntrinsicIssue  
    _mm_add_epi16(); //expect: PythonIntrinsicIssue  
    _mm_add_epi32(); //expect: PythonIntrinsicIssue  
    _mm_add_epi64(); //expect: PythonIntrinsicIssue   
    _mm_add_epi8(); //expect: PythonIntrinsicIssue  
    _mm_adds_epi16(); //expect: PythonIntrinsicIssue  
    _mm_adds_epi8(); //expect: PythonIntrinsicIssue  
    _mm_adds_epu16(); //expect: PythonIntrinsicIssue  
    _mm_adds_epu8(); //expect: PythonIntrinsicIssue  
    _mm_aesdeclast_si128(); //expect: PythonIntrinsicIssue  
    _mm_aesdec_si128(); //expect: PythonIntrinsicIssue  
    _mm_aesenclast_si128(); //expect: PythonIntrinsicIssue  
    _mm_aesenc_si128(); //expect: PythonIntrinsicIssue  
    _mm_aesimc_si128(); //expect: PythonIntrinsicIssue  
    _mm_aeskeygenassist_si128(); //expect: PythonIntrinsicIssue  
    _mm_alignr_epi8(); //expect: PythonIntrinsicIssue  
    _mm_andnot_si128(); //expect: PythonIntrinsicIssue  
    _mm_andnot_si128(); //expect: PythonIntrinsicIssue  
    _mm_and_si128(); //expect: PythonIntrinsicIssue  
    _mm_avg_epu16(); //expect: PythonIntrinsicIssue  
    _mm_avg_epu8(); //expect: PythonIntrinsicIssue  
    _mm_blend_epi16(); //expect: PythonIntrinsicIssue   
    _mm_blend_epi32(); //expect: PythonIntrinsicIssue  
    _mm_blendv_epi8(); //expect: PythonIntrinsicIssue  
    _mm_broadcastb_epi8(); //expect: PythonIntrinsicIssue  
    _mm_broadcastd_epi32(); //expect: PythonIntrinsicIssue  
    _mm_broadcastq_epi64(); //expect: PythonIntrinsicIssue  
    _mm_broadcastw_epi16(); //expect: PythonIntrinsicIssue  
    _mm_castpd_si128(); //expect: PythonIntrinsicIssue  
    _mm_castps_si128(); //expect: PythonIntrinsicIssue  
    _mm_clmulepi64_si128(); //expect: PythonIntrinsicIssue  
    _mm_cmov_si128(); //expect: PythonIntrinsicIssue  
    _mm_cmpeq_epi16(); //expect: PythonIntrinsicIssue  
    _mm_cmpeq_epi32(); //expect: PythonIntrinsicIssue  
    _mm_cmpeq_epi64(); //expect: PythonIntrinsicIssue   
    _mm_cmpeq_epi8(); //expect: PythonIntrinsicIssue  
    _mm_cmpestrm(); //expect: PythonIntrinsicIssue   
    _mm_cmpgt_epi16(); //expect: PythonIntrinsicIssue  
    _mm_cmpgt_epi32(); //expect: PythonIntrinsicIssue  
    _mm_cmpgt_epi64(); //expect: PythonIntrinsicIssue  
    _mm_cmpgt_epi8(); //expect: PythonIntrinsicIssue  
    _mm_cmpistrm(); //expect: PythonIntrinsicIssue  
    _mm_cmplt_epi16(); //expect: PythonIntrinsicIssue  
    _mm_cmplt_epi32(); //expect: PythonIntrinsicIssue  
    _mm_cmplt_epi8(); //expect: PythonIntrinsicIssue  
    _mm_com_epi16(); //expect: PythonIntrinsicIssue  
    _mm_com_epi32(); //expect: PythonIntrinsicIssue 
    _mm_com_epi64(); //expect: PythonIntrinsicIssue  
    _mm_com_epi8(); //expect: PythonIntrinsicIssue  
    _mm_com_epu16(); //expect: PythonIntrinsicIssue  
    _mm_com_epu32(); //expect: PythonIntrinsicIssue  
    _mm_com_epu64(); //expect: PythonIntrinsicIssue  
    _mm_com_epu8(); //expect: PythonIntrinsicIssue 
    _mm_cvtepi16_epi32(); //expect: PythonIntrinsicIssue  
    _mm_cvtepi16_epi64(); //expect: PythonIntrinsicIssue  
    _mm_cvtepi32_epi64(); //expect: PythonIntrinsicIssue  
    _mm_cvtepi8_epi16(); //expect: PythonIntrinsicIssue  
    _mm_cvtepi8_epi32(); //expect: PythonIntrinsicIssue 
    _mm_cvtepi8_epi64(); //expect: PythonIntrinsicIssue  
    _mm_cvtepu16_epi32(); //expect: PythonIntrinsicIssue  
    _mm_cvtepu16_epi64(); //expect: PythonIntrinsicIssue  
    _mm_cvtepu32_epi64(); //expect: PythonIntrinsicIssue  
    _mm_cvtepu8_epi16(); //expect: PythonIntrinsicIssue  
    _mm_cvtepu8_epi32(); //expect: PythonIntrinsicIssue  
    _mm_cvtepu8_epi64(); //expect: PythonIntrinsicIssue  
    _mm_cvtpd_epi32(); //expect: PythonIntrinsicIssue  
    _mm_cvtps_epi32(); //expect: PythonIntrinsicIssue  
    _mm_cvtps_ph(); //expect: PythonIntrinsicIssue  
    _mm_cvtsi32_si128(); //expect: PythonIntrinsicIssue  
    _mm_cvtsi64_si128(); //expect: PythonIntrinsicIssue  
    _mm_cvtsi64x_si128(); //expect: PythonIntrinsicIssue   
    _mm_cvttpd_epi32(); //expect: PythonIntrinsicIssue   
    _mm_cvttps_epi32(); //expect: PythonIntrinsicIssue  
    _mm_extracti_si64(); //expect: PythonIntrinsicIssue   
    _mm_extract_si64(); //expect: PythonIntrinsicIssue  
    _mm_haddd_epi16(); //expect: PythonIntrinsicIssue  
    _mm_haddd_epi8(); //expect: PythonIntrinsicIssue  
    _mm_haddd_epu16(); //expect: PythonIntrinsicIssue  
    _mm_haddd_epu8(); //expect: PythonIntrinsicIssue  
    _mm_hadd_epi16(); //expect: PythonIntrinsicIssue  
    _mm_hadd_epi32(); //expect: PythonIntrinsicIssue  
    _mm_haddq_epi16(); //expect: PythonIntrinsicIssue  
    _mm_haddq_epi32(); //expect: PythonIntrinsicIssue  
    _mm_haddq_epi8(); //expect: PythonIntrinsicIssue  
    _mm_haddq_epu16(); //expect: PythonIntrinsicIssue  
    _mm_haddq_epu32(); //expect: PythonIntrinsicIssue  
    _mm_haddq_epu8(); //expect: PythonIntrinsicIssue  
    _mm_hadds_epi16(); //expect: PythonIntrinsicIssue  
    _mm_haddw_epi8(); //expect: PythonIntrinsicIssue  
    _mm_haddw_epu8(); //expect: PythonIntrinsicIssue  
    _mm_hsubd_epi16(); //expect: PythonIntrinsicIssue  
    _mm_hsub_epi16(); //expect: PythonIntrinsicIssue  
    _mm_hsub_epi32(); //expect: PythonIntrinsicIssue  
    _mm_hsubq_epi32(); //expect: PythonIntrinsicIssue  
    _mm_hsubs_epi16(); //expect: PythonIntrinsicIssue  
    _mm_hsubw_epi8(); //expect: PythonIntrinsicIssue  
    _mm_i32gather_epi32(); //expect: PythonIntrinsicIssue  
    _mm_i32gather_epi64(); //expect: PythonIntrinsicIssue  
    _mm_i64gather_epi32(); //expect: PythonIntrinsicIssue  
    _mm_i64gather_epi64(); //expect: PythonIntrinsicIssue  
    _mm_insert_epi16(); //expect: PythonIntrinsicIssue  
    _mm_insert_epi32(); //expect: PythonIntrinsicIssue  
    _mm_insert_epi64(); //expect: PythonIntrinsicIssue 
    _mm_insert_epi8(); //expect: PythonIntrinsicIssue   
    _mm_inserti_si64(); //expect: PythonIntrinsicIssue  
    _mm_insert_si64(); //expect: PythonIntrinsicIssue  
    _mm_lddqu_si128(); //expect: PythonIntrinsicIssue  
    _mm_loadl_epi64(); //expect: PythonIntrinsicIssue  
    _mm_load_si128(); //expect: PythonIntrinsicIssue  
    _mm_loadu_si128(); //expect: PythonIntrinsicIssue  
    _mm_maccd_epi16(); //expect: PythonIntrinsicIssue  
    _mm_macc_epi16(); //expect: PythonIntrinsicIssue  
    _mm_macc_epi32(); //expect: PythonIntrinsicIssue  
    _mm_macchi_epi32(); //expect: PythonIntrinsicIssue  
    _mm_macclo_epi32(); //expect: PythonIntrinsicIssue  
    _mm_maccsd_epi16(); //expect: PythonIntrinsicIssue  
    _mm_maccs_epi16(); //expect: PythonIntrinsicIssue  
    _mm_maccs_epi32(); //expect: PythonIntrinsicIssue  
    _mm_maccshi_epi32(); //expect: PythonIntrinsicIssue  
    _mm_maccslo_epi32(); //expect: PythonIntrinsicIssue  
    _mm_maddd_epi16(); //expect: PythonIntrinsicIssue  
    _mm_madd_epi16(); //expect: PythonIntrinsicIssue  
    _mm_maddsd_epi16(); //expect: PythonIntrinsicIssue  
    _mm_maddubs_epi16(); //expect: PythonIntrinsicIssue  
    _mm_mask_i32gather_epi32(); //expect: PythonIntrinsicIssue  
    _mm_mask_i32gather_epi64(); //expect: PythonIntrinsicIssue  
    _mm_mask_i64gather_epi32(); //expect: PythonIntrinsicIssue   
    _mm_mask_i64gather_epi64(); //expect: PythonIntrinsicIssue  
    _mm_maskload_epi32(); //expect: PythonIntrinsicIssue  
    _mm_maskload_epi64(); //expect: PythonIntrinsicIssue  
    _mm_max_epi16(); //expect: PythonIntrinsicIssue  
    _mm_max_epi32(); //expect: PythonIntrinsicIssue  
    _mm_max_epi8 (); //expect: PythonIntrinsicIssue  
    _mm_max_epu16(); //expect: PythonIntrinsicIssue  
    _mm_max_epu32(); //expect: PythonIntrinsicIssue  
    _mm_max_epu8(); //expect: PythonIntrinsicIssue  
    _mm_min_epi16(); //expect: PythonIntrinsicIssue 
    _mm_min_epi32(); //expect: PythonIntrinsicIssue  
    _mm_min_epi8(); //expect: PythonIntrinsicIssue   
    _mm_min_epu16(); //expect: PythonIntrinsicIssue  
    _mm_min_epu32(); //expect: PythonIntrinsicIssue  
    _mm_min_epu8(); //expect: PythonIntrinsicIssue  
    _mm_minpos_epu16(); //expect: PythonIntrinsicIssue  
    _mm_move_epi64(); //expect: PythonIntrinsicIssue  
    _mm_movpi64_epi64(); //expect: PythonIntrinsicIssue  
    _mm_mpsadbw_epu8(); //expect: PythonIntrinsicIssue  
    _mm_mul_epi32(); //expect: PythonIntrinsicIssue  
    _mm_mul_epu32(); //expect: PythonIntrinsicIssue  
    _mm_mulhi_epi16(); //expect: PythonIntrinsicIssue  
    _mm_mulhi_epu16(); //expect: PythonIntrinsicIssue  
    _mm_mulhrs_epi16(); //expect: PythonIntrinsicIssue  
    _mm_mullo_epi16(); //expect: PythonIntrinsicIssue  
    _mm_mullo_epi32(); //expect: PythonIntrinsicIssue  
    _mm_or_si128(); //expect: PythonIntrinsicIssue  
    _mm_packs_epi16(); //expect: PythonIntrinsicIssue  
    _mm_packs_epi32(); //expect: PythonIntrinsicIssue  
    _mm_packus_epi16(); //expect: PythonIntrinsicIssue  
    _mm_packus_epi32(); //expect: PythonIntrinsicIssue  
    _mm_perm_epi8(); //expect: PythonIntrinsicIssue  
    _mm_rot_epi16(); //expect: PythonIntrinsicIssue  
    _mm_rot_epi16(); //expect: PythonIntrinsicIssue  
    _mm_rot_epi32(); //expect: PythonIntrinsicIssue  
    _mm_rot_epi32(); //expect: PythonIntrinsicIssue  
    _mm_rot_epi64(); //expect: PythonIntrinsicIssue  
    _mm_rot_epi64(); //expect: PythonIntrinsicIssue  
    _mm_rot_epi8(); //expect: PythonIntrinsicIssue  
    _mm_rot_epi8(); //expect: PythonIntrinsicIssue  
    _mm_roti_epi16(); //expect: PythonIntrinsicIssue  
    _mm_roti_epi32(); //expect: PythonIntrinsicIssue  
    _mm_roti_epi64(); //expect: PythonIntrinsicIssue  
    _mm_roti_epi8(); //expect: PythonIntrinsicIssue  
    _mm_sad_epu8(); //expect: PythonIntrinsicIssue  
    _mm_set1_epi16(); //expect: PythonIntrinsicIssue  
    _mm_set1_epi32(); //expect: PythonIntrinsicIssue  
    _mm_set1_epi64(); //expect: PythonIntrinsicIssue  
    _mm_set1_epi64x(); //expect: PythonIntrinsicIssue  
    _mm_set1_epi8(); //expect: PythonIntrinsicIssue  
    _mm_set_epi16(); //expect: PythonIntrinsicIssue  
    _mm_set_epi32(); //expect: PythonIntrinsicIssue  
    _mm_set_epi64(); //expect: PythonIntrinsicIssue  
    _mm_set_epi64x(); //expect: PythonIntrinsicIssue  
    _mm_set_epi8(); //expect: PythonIntrinsicIssue  
    _mm_setl_epi64(); //expect: PythonIntrinsicIssue 
    _mm_setr_epi16(); //expect: PythonIntrinsicIssue 
    _mm_setr_epi32(); //expect: PythonIntrinsicIssue 
    _mm_setr_epi64(); //expect: PythonIntrinsicIssue 
    _mm_setr_epi8(); //expect: PythonIntrinsicIssue 
    _mm_setzero_si128(); //expect: PythonIntrinsicIssue 
    _mm_sha_epi16(); //expect: PythonIntrinsicIssue 
    _mm_sha_epi32(); //expect: PythonIntrinsicIssue 
    _mm_sha_epi64(); //expect: PythonIntrinsicIssue 
    _mm_sha_epi8(); //expect: PythonIntrinsicIssue 
    _mm_shl_epi16(); //expect: PythonIntrinsicIssue 
    _mm_shl_epi32(); //expect: PythonIntrinsicIssue 
    _mm_shl_epi64(); //expect: PythonIntrinsicIssue
    _mm_shl_epi8(); //expect: PythonIntrinsicIssue 
    _mm_shuffle_epi32(); //expect: PythonIntrinsicIssue  
    _mm_shuffle_epi8(); //expect: PythonIntrinsicIssue 
    _mm_shufflehi_epi16(); //expect: PythonIntrinsicIssue 
    _mm_shufflelo_epi16(); //expect: PythonIntrinsicIssue 
    _mm_sign_epi16(); //expect: PythonIntrinsicIssue 
    _mm_sign_epi32(); //expect: PythonIntrinsicIssue 
    _mm_sign_epi8(); //expect: PythonIntrinsicIssue 
    _mm_sll_epi16(); //expect: PythonIntrinsicIssue 
    _mm_sll_epi32(); //expect: PythonIntrinsicIssue 
    _mm_sll_epi64(); //expect: PythonIntrinsicIssue 
    _mm_slli_epi16(); //expect: PythonIntrinsicIssue 
    _mm_slli_epi32(); //expect: PythonIntrinsicIssue 
    _mm_slli_epi64(); //expect: PythonIntrinsicIssue 
    _mm_slli_si128(); //expect: PythonIntrinsicIssue 
    _mm_sllv_epi32(); //expect: PythonIntrinsicIssue 
    _mm_sllv_epi64(); //expect: PythonIntrinsicIssue 
    _mm_sra_epi16(); //expect: PythonIntrinsicIssue 
    _mm_sra_epi32(); //expect: PythonIntrinsicIssue 
    _mm_srai_epi16(); //expect: PythonIntrinsicIssue 
    _mm_srai_epi32(); //expect: PythonIntrinsicIssue 
    _mm_srav_epi32(); //expect: PythonIntrinsicIssue 
    _mm_srl_epi16(); //expect: PythonIntrinsicIssue  
    _mm_srl_epi32(); //expect: PythonIntrinsicIssue  
    _mm_srl_epi64(); //expect: PythonIntrinsicIssue  
    _mm_srli_epi16(); //expect: PythonIntrinsicIssue 
    _mm_srli_epi32(); //expect: PythonIntrinsicIssue 
    _mm_srli_epi64(); //expect: PythonIntrinsicIssue 
    _mm_srli_si128(); //expect: PythonIntrinsicIssue 
    _mm_srlv_epi32(); //expect: PythonIntrinsicIssue 
    _mm_srlv_epi64(); //expect: PythonIntrinsicIssue 
    _mm_stream_load_si128(); //expect: PythonIntrinsicIssue 
    _mm_sub_epi16(); //expect: PythonIntrinsicIssue 
    _mm_sub_epi32(); //expect: PythonIntrinsicIssue 
    _mm_sub_epi64(); //expect: PythonIntrinsicIssue 
    _mm_sub_epi8(); //expect: PythonIntrinsicIssue 
    _mm_subs_epi16(); //expect: PythonIntrinsicIssue 
    _mm_subs_epi8(); //expect: PythonIntrinsicIssue 
    _mm_subs_epu16(); //expect: PythonIntrinsicIssue 
    _mm_subs_epu8(); //expect: PythonIntrinsicIssue 
    _mm_unpackhi_epi16(); //expect: PythonIntrinsicIssue 
    _mm_unpackhi_epi32(); //expect: PythonIntrinsicIssue 
    _mm_unpackhi_epi64(); //expect: PythonIntrinsicIssue 
    _mm_unpackhi_epi8(); //expect: PythonIntrinsicIssue
    _mm_unpacklo_epi16(); //expect: PythonIntrinsicIssue 
    _mm_unpacklo_epi32(); //expect: PythonIntrinsicIssue  
    _mm_unpacklo_epi64(); //expect: PythonIntrinsicIssue 
    _mm_unpacklo_epi8(); //expect: PythonIntrinsicIssue
    _mm_xor_si128(); //expect: PythonIntrinsicIssue 
    _mm256_castps256_ps128(); //expect: PythonIntrinsicIssue  
    _mm256_cvtpd_ps(); //expect: PythonIntrinsicIssue 
    _mm256_extractf128_ps(); //expect: PythonIntrinsicIssue 
    _mm256_i64gather_ps(); //expect: PythonIntrinsicIssue 
    _mm256_mask_i64gather_ps(); //expect: PythonIntrinsicIssue 
    _mm_add_ps(); //expect: PythonIntrinsicIssue 
    _mm_add_ss(); //expect: PythonIntrinsicIssue 
    _mm_addsub_ps(); //expect: PythonIntrinsicIssue 
    _mm_andnot_ps(); //expect: PythonIntrinsicIssue 
    _mm_and_ps(); //expect: PythonIntrinsicIssue
    _mm_blend_ps(); //expect: PythonIntrinsicIssue  
    _mm_blendv_ps(); //expect: PythonIntrinsicIssue 
    _mm_broadcast_ss(); //expect: PythonIntrinsicIssue  
    _mm_broadcastss_ps(); //expect: PythonIntrinsicIssue
    _mm_castpd_ps(); //expect: PythonIntrinsicIssue
    _mm_castsi128_ps(); //expect: PythonIntrinsicIssue
    _mm_cmpeq_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmpeq_ss(); //expect: PythonIntrinsicIssue 
    _mm_cmpge_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmpge_ss(); //expect: PythonIntrinsicIssue 
    _mm_cmpgt_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmpgt_ss(); //expect: PythonIntrinsicIssue 
    _mm_cmple_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmple_ss(); //expect: PythonIntrinsicIssue 
    _mm_cmplt_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmplt_ss(); //expect: PythonIntrinsicIssue 
    _mm_cmpneq_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmpneq_ss(); //expect: PythonIntrinsicIssue 
    _mm_cmpnge_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmpnge_ss(); //expect: PythonIntrinsicIssue 
    _mm_cmpngt_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmpngt_ss(); //expect: PythonIntrinsicIssue
    _mm_cmpnle_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmpnle_ss(); //expect: PythonIntrinsicIssue 
    _mm_cmpnlt_ps(); //expect: PythonIntrinsicIssue  
    _mm_cmpnlt_ss(); //expect: PythonIntrinsicIssue 
    _mm_cmpord_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmpord_ss(); //expect: PythonIntrinsicIssue 
    _mm_cmp_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmp_ss(); //expect: PythonIntrinsicIssue 
    _mm_cmpunord_ps(); //expect: PythonIntrinsicIssue 
    _mm_cmpunord_ss(); //expect: PythonIntrinsicIssue 
    _mm_cvtepi32_ps(); //expect: PythonIntrinsicIssue 
    _mm_cvtpd_ps(); //expect: PythonIntrinsicIssue 
    _mm_cvtph_ps(); //expect: PythonIntrinsicIssue 
    _mm_cvt_pi2ps(); //expect: PythonIntrinsicIssue 
    _mm_cvtsd_ss(); //expect: PythonIntrinsicIssue
    _mm_cvt_si2ss(); //expect: PythonIntrinsicIssue 
    _mm_cvtsi64_ss(); //expect: PythonIntrinsicIssue 
    _mm_cvtsi64x_ss(); //expect: PythonIntrinsicIssue 
    _mm_div_ps(); //expect: PythonIntrinsicIssue 
    _mm_div_ss(); //expect: PythonIntrinsicIssue  
    _mm_dp_ps(); //expect: PythonIntrinsicIssue 
    _mm_fmadd_ps(); //expect: PythonIntrinsicIssue 
    _mm_fmadd_ss(); //expect: PythonIntrinsicIssue 
    _mm_fmaddsub_ps(); //expect: PythonIntrinsicIssue 
    _mm_fmsubadd_ps(); //expect: PythonIntrinsicIssue 
    _mm_fmsub_ps(); //expect: PythonIntrinsicIssue 
    _mm_fmsub_ss(); //expect: PythonIntrinsicIssue 
    _mm_fnmadd_ps(); //expect: PythonIntrinsicIssue 
    _mm_fnmadd_ss(); //expect: PythonIntrinsicIssue 
    _mm_fnmsub_ps(); //expect: PythonIntrinsicIssue 
    _mm_fnmsub_ss(); //expect: PythonIntrinsicIssue 
    _mm_frcz_ps(); //expect: PythonIntrinsicIssue 
    _mm_frcz_ss(); //expect: PythonIntrinsicIssue 
    _mm_hadd_ps(); //expect: PythonIntrinsicIssue 
    _mm_hsub_ps(); //expect: PythonIntrinsicIssue 
    _mm_i32gather_ps(); //expect: PythonIntrinsicIssue 
    _mm_i64gather_ps(); //expect: PythonIntrinsicIssue 
    _mm_insert_ps(); //expect: PythonIntrinsicIssue 
    _mm_loadh_pi(); //expect: PythonIntrinsicIssue 
    _mm_loadl_pi(); //expect: PythonIntrinsicIssue 
    _mm_load_ps1(); //expect: PythonIntrinsicIssue 
    _mm_load_ps(); //expect: PythonIntrinsicIssue
    _mm_loadr_ps(); //expect: PythonIntrinsicIssue 
    _mm_load_ss(); //expect: PythonIntrinsicIssue 
    _mm_loadu_ps(); //expect: PythonIntrinsicIssue 
    _mm_macc_ps(); //expect: PythonIntrinsicIssue 
    _mm_macc_ss(); //expect: PythonIntrinsicIssue 
    _mm_maddsub_ps(); //expect: PythonIntrinsicIssue 
    _mm_mask_i32gather_ps(); //expect: PythonIntrinsicIssue 
    _mm_mask_i64gather_ps(); //expect: PythonIntrinsicIssue 
    _mm_maskload_ps(); //expect: PythonIntrinsicIssue 
    _mm_max_ps(); //expect: PythonIntrinsicIssue 
    _mm_max_ss(); //expect: PythonIntrinsicIssue 
    _mm_min_ps(); //expect: PythonIntrinsicIssue 
    _mm_min_ss(); //expect: PythonIntrinsicIssue 
    _mm_movehdup_ps(); //expect: PythonIntrinsicIssue 
    _mm_movehl_ps(); //expect: PythonIntrinsicIssue 
    _mm_moveldup_ps(); //expect: PythonIntrinsicIssue 
    _mm_movelh_ps(); //expect: PythonIntrinsicIssue 
    _mm_move_ss(); //expect: PythonIntrinsicIssue 
    _mm_msubadd_ps(); //expect: PythonIntrinsicIssue 
    _mm_msub_ps(); //expect: PythonIntrinsicIssue 
    _mm_msub_ss(); //expect: PythonIntrinsicIssue 
    _mm_mul_ps(); //expect: PythonIntrinsicIssue 
    _mm_mul_ss(); //expect: PythonIntrinsicIssue 
    _mm_nmacc_ps(); //expect: PythonIntrinsicIssue 
    _mm_nmacc_ss(); //expect: PythonIntrinsicIssue 
    _mm_nmsub_ps(); //expect: PythonIntrinsicIssue 
    _mm_nmsub_ss(); //expect: PythonIntrinsicIssue 
    _mm_or_ps(); //expect: PythonIntrinsicIssue 
    _mm_permute2_ps(); //expect: PythonIntrinsicIssue 
    _mm_permute_ps(); //expect: PythonIntrinsicIssue 
    _mm_permutevar_ps(); //expect: PythonIntrinsicIssue 
    _mm_rcp_ps(); //expect: PythonIntrinsicIssue 
    _mm_rcp_ss(); //expect: PythonIntrinsicIssue 
    _mm_round_ps(); //expect: PythonIntrinsicIssue 
    _mm_round_ss(); //expect: PythonIntrinsicIssue 
    _mm_rsqrt_ps(); //expect: PythonIntrinsicIssue 
    _mm_rsqrt_ss(); //expect: PythonIntrinsicIssue 
    _mm_set_ps1(); //expect: PythonIntrinsicIssue 
    _mm_set_ps(); //expect: PythonIntrinsicIssue 
    _mm_setr_ps(); //expect: PythonIntrinsicIssue 
    _mm_set_ss(); //expect: PythonIntrinsicIssue 
    _mm_setzero_ps(); //expect: PythonIntrinsicIssue 
    _mm_shuffle_ps(); //expect: PythonIntrinsicIssue 
    _mm_sqrt_ps(); //expect: PythonIntrinsicIssue 
    _mm_sqrt_ss(); //expect: PythonIntrinsicIssue 
    _mm_sub_ps(); //expect: PythonIntrinsicIssue 
    _mm_sub_ss(); //expect: PythonIntrinsicIssue 
    _mm_unpackhi_ps(); //expect: PythonIntrinsicIssue 
    _mm_unpacklo_ps(); //expect: PythonIntrinsicIssue 
    _mm_xor_ps(); //expect: PythonIntrinsicIssue 
    _mm256_add_pd(); //expect: PythonIntrinsicIssue 
    _mm256_addsub_pd(); //expect: PythonIntrinsicIssue 
    _mm256_andnot_pd(); //expect: PythonIntrinsicIssue 
    _mm256_and_pd(); //expect: PythonIntrinsicIssue  
    _mm256_blend_pd(); //expect: PythonIntrinsicIssue
    _mm256_blendv_pd(); //expect: PythonIntrinsicIssue 
    _mm256_broadcast_pd(); //expect: PythonIntrinsicIssue 
    _mm256_broadcast_sd(); //expect: PythonIntrinsicIssue 
    _mm256_broadcastsd_pd(); //expect: PythonIntrinsicIssue 
    _mm256_castpd128_pd256(); //expect: PythonIntrinsicIssue 
    _mm256_castps_pd(); //expect: PythonIntrinsicIssue 
    _mm256_castsi256_pd(); //expect: PythonIntrinsicIssue  
    _mm256_cmp_pd(); //expect: PythonIntrinsicIssue 
    _mm256_cvtepi32_pd(); //expect: PythonIntrinsicIssue 
    _mm256_cvtps_pd(); //expect: PythonIntrinsicIssue 
    _mm256_div_pd(); //expect: PythonIntrinsicIssue 
    _mm256_fmadd_pd(); //expect: PythonIntrinsicIssue  
    _mm256_fmaddsub_pd(); //expect: PythonIntrinsicIssue 
    _mm256_fmsubadd_pd(); //expect: PythonIntrinsicIssue 
    _mm256_fmsub_pd(); //expect: PythonIntrinsicIssue 
    _mm256_fnmadd_pd(); //expect: PythonIntrinsicIssue 
    _mm256_fnmsub_pd(); //expect: PythonIntrinsicIssue 
    _mm256_frcz_pd(); //expect: PythonIntrinsicIssue 
    _mm256_hadd_pd(); //expect: PythonIntrinsicIssue 
    _mm256_hsub_pd(); //expect: PythonIntrinsicIssue 
    _mm256_i32gather_pd(); //expect: PythonIntrinsicIssue 
    _mm256_i64gather_pd(); //expect: PythonIntrinsicIssue 
    _mm256_insertf128_pd(); //expect: PythonIntrinsicIssue 
    _mm256_load_pd(); //expect: PythonIntrinsicIssue 
    _mm256_loadu_pd(); //expect: PythonIntrinsicIssue 
     _mm256_macc_pd(); //expect: PythonIntrinsicIssue 
    _mm256_maddsub_pd(); //expect: PythonIntrinsicIssue 
    _mm256_mask_i32gather_pd(); //expect: PythonIntrinsicIssue 
    _mm256_mask_i64gather_pd(); //expect: PythonIntrinsicIssue 
    _mm256_maskload_pd(); //expect: PythonIntrinsicIssue 
    _mm256_max_pd(); //expect: PythonIntrinsicIssue 
    _mm256_min_pd(); //expect: PythonIntrinsicIssue 
    _mm256_movedup_pd(); //expect: PythonIntrinsicIssue 
    _mm256_msubadd_pd(); //expect: PythonIntrinsicIssue 
    _mm256_msub_pd(); //expect: PythonIntrinsicIssue 
    _mm256_mul_pd(); //expect: PythonIntrinsicIssue 
    _mm256_nmacc_pd(); //expect: PythonIntrinsicIssue   
    _mm256_nmsub_pd(); //expect: PythonIntrinsicIssue 
    _mm256_or_pd(); //expect: PythonIntrinsicIssue 
    _mm256_permute2f128_pd(); //expect: PythonIntrinsicIssue 
    _mm256_permute2_pd(); //expect: PythonIntrinsicIssue 
    _mm256_permute4x64_pd(); //expect: PythonIntrinsicIssue 
    _mm256_permute_pd(); //expect: PythonIntrinsicIssue 
    _mm256_permutevar_pd(); //expect: PythonIntrinsicIssue 
    _mm256_round_pd(); //expect: PythonIntrinsicIssue  
    _mm256_set1_pd(); //expect: PythonIntrinsicIssue
    _mm256_set_pd(); //expect: PythonIntrinsicIssue  
    _mm256_setr_pd(); //expect: PythonIntrinsicIssue 
    _mm256_setzero_pd(); //expect: PythonIntrinsicIssue 
    _mm256_shuffle_pd(); //expect: PythonIntrinsicIssue 
    _mm256_sqrt_pd(); //expect: PythonIntrinsicIssue 
    _mm256_sub_pd(); //expect: PythonIntrinsicIssue 
    _mm256_unpackhi_pd(); //expect: PythonIntrinsicIssue 
    _mm256_unpacklo_pd(); //expect: PythonIntrinsicIssue 
    _mm256_xor_pd(); //expect: PythonIntrinsicIssue 
    _mm_macc_pd(); //expect: PythonIntrinsicIssue 
    _mm_maddsub_pd(); //expect: PythonIntrinsicIssue 
    _mm_msubadd_pd(); //expect: PythonIntrinsicIssue 
    _mm_msub_pd(); //expect: PythonIntrinsicIssue 
    _mm_nmacc_pd(); //expect: PythonIntrinsicIssue 
    _mm_nmsub_pd(); //expect: PythonIntrinsicIssue 
    _mm256_abs_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_abs_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_abs_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_add_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_add_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_add_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_add_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_adds_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_adds_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_adds_epu16(); //expect: PythonIntrinsicIssue 
    _mm256_adds_epu8(); //expect: PythonIntrinsicIssue  
    _mm256_alignr_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_andnot_si256(); //expect: PythonIntrinsicIssue 
    _mm256_and_si256(); //expect: PythonIntrinsicIssue 
    _mm256_avg_epu16(); //expect: PythonIntrinsicIssue 
    _mm256_avg_epu8(); //expect: PythonIntrinsicIssue 
    _mm256_avg_epu8(); //expect: PythonIntrinsicIssue 
    _mm256_blend_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_blend_epi32(); //expect: PythonIntrinsicIssue  
    _mm256_blendv_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_broadcastb_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_broadcastd_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_broadcastq_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_broadcastsi128_si256(); //expect: PythonIntrinsicIssue 
    _mm256_broadcastw_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_castpd_si256(); //expect: PythonIntrinsicIssue 
    _mm256_castps_si256(); //expect: PythonIntrinsicIssue 
    _mm256_castsi128_si256(); //expect: PythonIntrinsicIssue 
    _mm256_cmov_si256(); //expect: PythonIntrinsicIssue 
    _mm256_cmpeq_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_cmpeq_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_cmpeq_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_cmpeq_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_cmpgt_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_cmpgt_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_cmpgt_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_cmpgt_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_cvtepi16_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_cvtepi16_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_cvtepi32_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_cvtepi8_epi16(); //expect: PythonIntrinsicIssue  
    _mm256_cvtepi8_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_cvtepi8_epi64(); //expect: PythonIntrinsicIssue
    _mm256_cvtepu16_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_cvtepu16_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_cvtepu32_epi64(); //expect: PythonIntrinsicIssue  
    _mm256_cvtepu8_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_cvtepu8_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_cvtepu8_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_cvtps_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_cvttps_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_hadd_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_hadd_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_hadds_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_hsub_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_hsub_epi32(); //expect: PythonIntrinsicIssue  
    _mm256_hsubs_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_i32gather_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_i32gather_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_i64gather_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_i64gather_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_insertf128_si256(); //expect: PythonIntrinsicIssue 
    _mm256_inserti128_si256(); //expect: PythonIntrinsicIssue 
    _mm256_lddqu_si256(); //expect: PythonIntrinsicIssue 
    _mm256_load_si256(); //expect: PythonIntrinsicIssue  
    _mm256_loadu_si256(); //expect: PythonIntrinsicIssue 
    _mm256_madd_epi16(); //expect: PythonIntrinsicIssue  
    _mm256_maddubs_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_mask_i32gather_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_mask_i32gather_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_mask_i64gather_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_maskload_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_maskload_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_max_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_max_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_max_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_max_epu16(); //expect: PythonIntrinsicIssue 
    _mm256_max_epu32(); //expect: PythonIntrinsicIssue 
    _mm256_max_epu8(); //expect: PythonIntrinsicIssue 
    _mm256_min_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_min_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_min_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_min_epu16(); //expect: PythonIntrinsicIssue 
    _mm256_min_epu32(); //expect: PythonIntrinsicIssue 
    _mm256_min_epu8(); //expect: PythonIntrinsicIssue  
    _mm256_mpsadbw_epu8(); //expect: PythonIntrinsicIssue
    _mm256_mul_epi32(); //expect: PythonIntrinsicIssue  
    _mm256_mul_epu32(); //expect: PythonIntrinsicIssue 
    _mm256_mulhi_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_mulhi_epu16(); //expect: PythonIntrinsicIssue 
    _mm256_mulhrs_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_mullo_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_mullo_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_or_si256(); //expect: PythonIntrinsicIssue 
    _mm256_packs_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_packs_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_packus_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_packus_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_permute2f128_si256(); //expect: PythonIntrinsicIssue 
    _mm256_permute2x128_si256(); //expect: PythonIntrinsicIssue  
    _mm256_permute4x64_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_permutevar8x32_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_sad_epu8(); //expect: PythonIntrinsicIssue  
    _mm256_set1_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_set1_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_set1_epi64x(); //expect: PythonIntrinsicIssue 
    _mm256_set1_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_set_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_set_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_set_epi64x(); //expect: PythonIntrinsicIssue 
    _mm256_set_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_setr_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_setr_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_setr_epi64x(); //expect: PythonIntrinsicIssue 
    _mm256_setr_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_setzero_si256(); //expect: PythonIntrinsicIssue 
    _mm256_shuffle_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_shuffle_epi8(); //expect: PythonIntrinsicIssue  
    _mm256_shufflehi_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_shufflelo_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_sign_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_sign_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_sign_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_sll_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_sll_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_sll_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_slli_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_slli_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_slli_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_slli_si256(); //expect: PythonIntrinsicIssue 
    _mm256_sllv_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_sllv_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_sra_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_sra_epi32(); //expect: PythonIntrinsicIssue  
    _mm256_srai_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_srai_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_srav_epi32(); //expect: PythonIntrinsicIssue  
    _mm256_srl_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_srl_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_srl_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_srli_epi16(); //expect: PythonIntrinsicIssue  
    _mm256_srli_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_srli_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_srli_si256(); //expect: PythonIntrinsicIssue 
    _mm256_srlv_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_srlv_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_stream_load_si256(); //expect: PythonIntrinsicIssue 
    _mm256_sub_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_sub_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_sub_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_sub_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_subs_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_subs_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_subs_epu16(); //expect: PythonIntrinsicIssue 
    _mm256_subs_epu8(); //expect: PythonIntrinsicIssue 
    _mm256_unpackhi_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_unpackhi_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_unpackhi_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_unpackhi_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_unpacklo_epi16(); //expect: PythonIntrinsicIssue 
    _mm256_unpacklo_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_unpacklo_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_unpacklo_epi8(); //expect: PythonIntrinsicIssue 
    _mm256_xor_si256(); //expect: PythonIntrinsicIssue 
    _mm256_add_ps(); //expect: PythonIntrinsicIssue 
    _mm256_addsub_ps(); //expect: PythonIntrinsicIssue 
    _mm256_andnot_ps(); //expect: PythonIntrinsicIssue 
    _mm256_and_ps(); //expect: PythonIntrinsicIssue 
    _mm256_blend_ps(); //expect: PythonIntrinsicIssue 
    _mm256_blendv_ps(); //expect: PythonIntrinsicIssue 
    _mm256_broadcast_ps(); //expect: PythonIntrinsicIssue 
    _mm256_broadcast_ss(); //expect: PythonIntrinsicIssue 
    _mm256_broadcastss_ps(); //expect: PythonIntrinsicIssue 
    _mm256_castpd_ps(); //expect: PythonIntrinsicIssue 
    _mm256_castps128_ps256(); //expect: PythonIntrinsicIssue 
    _mm256_castsi256_ps(); //expect: PythonIntrinsicIssue 
    _mm256_cmp_ps(); //expect: PythonIntrinsicIssue 
    _mm256_cvtepi32_ps(); //expect: PythonIntrinsicIssue 
    _mm256_cvtph_ps(); //expect: PythonIntrinsicIssue 
    _mm256_div_ps(); //expect: PythonIntrinsicIssue 
    _mm256_dp_ps(); //expect: PythonIntrinsicIssue 
    _mm256_fmadd_ps(); //expect: PythonIntrinsicIssue 
    _mm256_fmaddsub_ps(); //expect: PythonIntrinsicIssue 
    _mm256_fmsubadd_ps(); //expect: PythonIntrinsicIssue 
    _mm256_fmsub_ps(); //expect: PythonIntrinsicIssue 
    _mm256_fnmadd_ps(); //expect: PythonIntrinsicIssue 
    _mm256_fnmsub_ps(); //expect: PythonIntrinsicIssue 
    _mm256_frcz_ps(); //expect: PythonIntrinsicIssue 
    _mm256_hadd_ps(); //expect: PythonIntrinsicIssue 
    _mm256_hsub_ps(); //expect: PythonIntrinsicIssue 
    _mm256_i32gather_ps(); //expect: PythonIntrinsicIssue 
    _mm256_insertf128_ps(); //expect: PythonIntrinsicIssue 
    _mm256_load_ps(); //expect: PythonIntrinsicIssue 
    _mm256_loadu_ps(); //expect: PythonIntrinsicIssue 
    _mm256_macc_ps(); //expect: PythonIntrinsicIssue 
    _mm256_maddsub_ps(); //expect: PythonIntrinsicIssue 
    _mm256_mask_i32gather_ps(); //expect: PythonIntrinsicIssue 
    _mm256_maskload_ps(); //expect: PythonIntrinsicIssue 
    _mm256_max_ps(); //expect: PythonIntrinsicIssue 
    _mm256_min_ps(); //expect: PythonIntrinsicIssue 
    _mm256_movehdup_ps(); //expect: PythonIntrinsicIssue 
    _mm256_moveldup_ps(); //expect: PythonIntrinsicIssue 
    _mm256_msubadd_ps(); //expect: PythonIntrinsicIssue 
    _mm256_msub_ps(); //expect: PythonIntrinsicIssue 
    _mm256_mul_ps(); //expect: PythonIntrinsicIssue 
    _mm256_nmacc_ps(); //expect: PythonIntrinsicIssue 
    _mm256_nmsub_ps(); //expect: PythonIntrinsicIssue 
    _mm256_or_ps(); //expect: PythonIntrinsicIssue 
    _mm256_permute2f128_ps(); //expect: PythonIntrinsicIssue 
    _mm256_permute2_ps(); //expect: PythonIntrinsicIssue 
    _mm256_permute_ps(); //expect: PythonIntrinsicIssue 
    _mm256_permutevar8x32_ps(); //expect: PythonIntrinsicIssue 
    _mm256_permutevar_ps(); //expect: PythonIntrinsicIssue 
    _mm256_rcp_ps(); //expect: PythonIntrinsicIssue 
    _mm256_round_ps(); //expect: PythonIntrinsicIssue 
    _mm256_rsqrt_ps(); //expect: PythonIntrinsicIssue 
    _mm256_set1_ps(); //expect: PythonIntrinsicIssue 
    _mm256_set_ps(); //expect: PythonIntrinsicIssue 
    _mm256_setr_ps(); //expect: PythonIntrinsicIssue 
    _mm256_setzero_ps(); //expect: PythonIntrinsicIssue 
    _mm256_shuffle_ps(); //expect: PythonIntrinsicIssue 
    _mm256_sqrt_ps(); //expect: PythonIntrinsicIssue  
    _mm256_sub_ps(); //expect: PythonIntrinsicIssue 
    _mm256_unpackhi_ps(); //expect: PythonIntrinsicIssue 
    _mm256_unpacklo_ps(); //expect: PythonIntrinsicIssue 
    _mm256_xor_ps(); //expect: PythonIntrinsicIssue 
    _mm_macc_ps(); //expect: PythonIntrinsicIssue 
    _mm_maddsub_ps(); //expect: PythonIntrinsicIssue 
    _mm_msubadd_ps(); //expect: PythonIntrinsicIssue  
    _mm_msub_ps(); //expect: PythonIntrinsicIssue 
    _mm_nmacc_ps(); //expect: PythonIntrinsicIssue 
    _mm_nmsub_ps(); //expect: PythonIntrinsicIssue 
    _m_from_float(); //expect: PythonIntrinsicIssue 
    _m_from_int(); //expect: PythonIntrinsicIssue 
    _mm_abs_pi16(); //expect: PythonIntrinsicIssue 
    _mm_abs_pi32(); //expect: PythonIntrinsicIssue 
    _mm_abs_pi8(); //expect: PythonIntrinsicIssue 
    _mm_add_si64(); //expect: PythonIntrinsicIssue 
    _mm_alignr_pi8(); //expect: PythonIntrinsicIssue 
    _mm_cvtpd_pi32(); //expect: PythonIntrinsicIssue 
    _mm_cvt_ps2pi(); //expect: PythonIntrinsicIssue 
    _mm_cvttpd_pi32(); //expect: PythonIntrinsicIssue 
    _mm_cvtt_ps2pi(); //expect: PythonIntrinsicIssue 
    _mm_hadd_pi16(); //expect: PythonIntrinsicIssue 
    _mm_hadd_pi32(); //expect: PythonIntrinsicIssue 
    _mm_hadds_pi16(); //expect: PythonIntrinsicIssue 
    _mm_hsub_pi16(); //expect: PythonIntrinsicIssue 
    _mm_hsub_pi32(); //expect: PythonIntrinsicIssue 
    _mm_hsubs_pi16(); //expect: PythonIntrinsicIssue 
    _mm_maddubs_pi16(); //expect: PythonIntrinsicIssue 
    _mm_movepi64_pi64(); //expect: PythonIntrinsicIssue 
    _mm_mulhrs_pi16(); //expect: PythonIntrinsicIssue 
    _mm_mul_su32(); //expect: PythonIntrinsicIssue 
    _mm_set1_pi16(); //expect: PythonIntrinsicIssue 
    _mm_set1_pi32(); //expect: PythonIntrinsicIssue 
    _mm_set1_pi8(); //expect: PythonIntrinsicIssue 
    _mm_set_pi16(); //expect: PythonIntrinsicIssue 
    _mm_set_pi32(); //expect: PythonIntrinsicIssue 
    _mm_set_pi8(); //expect: PythonIntrinsicIssue 
    _mm_setr_pi16(); //expect: PythonIntrinsicIssue 
    _mm_setr_pi32(); //expect: PythonIntrinsicIssue 
    _mm_setr_pi8(); //expect: PythonIntrinsicIssue 
    _mm_setzero_si64(); //expect: PythonIntrinsicIssue 
    _mm_shuffle_pi8(); //expect: PythonIntrinsicIssue 
    _mm_sign_pi16(); //expect: PythonIntrinsicIssue 
    _mm_sign_pi32(); //expect: PythonIntrinsicIssue 
    _mm_sign_pi8(); //expect: PythonIntrinsicIssue 
    _mm_sub_si64(); //expect: PythonIntrinsicIssue 
    _m_packssdw(); //expect: PythonIntrinsicIssue 
    _m_packsswb(); //expect: PythonIntrinsicIssue 
    _m_packuswb(); //expect: PythonIntrinsicIssue 
    _m_paddb(); //expect: PythonIntrinsicIssue 
    _m_paddd(); //expect: PythonIntrinsicIssue 
    _m_paddsb(); //expect: PythonIntrinsicIssue 
    _m_paddsw(); //expect: PythonIntrinsicIssue 
    _m_paddusb(); //expect: PythonIntrinsicIssue 
    _m_paddusw(); //expect: PythonIntrinsicIssue 
    _m_paddw(); //expect: PythonIntrinsicIssue 
    _m_pand(); //expect: PythonIntrinsicIssue 
    _m_pandn(); //expect: PythonIntrinsicIssue 
    _m_pavgb(); //expect: PythonIntrinsicIssue 
    _m_pavgusb(); //expect: PythonIntrinsicIssue 
    _m_pavgw(); //expect: PythonIntrinsicIssue 
    _m_pcmpeqb(); //expect: PythonIntrinsicIssue 
    _m_pcmpeqd(); //expect: PythonIntrinsicIssue 
    _m_pcmpeqw(); //expect: PythonIntrinsicIssue 
    _m_pcmpgtb(); //expect: PythonIntrinsicIssue 
    _m_pcmpgtd(); //expect: PythonIntrinsicIssue 
    _m_pcmpgtw(); //expect: PythonIntrinsicIssue 
    _m_pf2id(); //expect: PythonIntrinsicIssue 
    _m_pf2iw(); //expect: PythonIntrinsicIssue 
    _m_pfacc(); //expect: PythonIntrinsicIssue 
    _m_pfadd(); //expect: PythonIntrinsicIssue 
    _m_pfcmpeq(); //expect: PythonIntrinsicIssue 
    _m_pfcmpge(); //expect: PythonIntrinsicIssue 
    _m_pfcmpgt(); //expect: PythonIntrinsicIssue 
    _m_pfmax(); //expect: PythonIntrinsicIssue 
    _m_pfmin(); //expect: PythonIntrinsicIssue 
    _m_pfmul(); //expect: PythonIntrinsicIssue 
    _m_pfnacc(); //expect: PythonIntrinsicIssue 
    _m_pfpnacc(); //expect: PythonIntrinsicIssue 
    _m_pfrcpit1(); //expect: PythonIntrinsicIssue 
    _m_pfrcpit2(); //expect: PythonIntrinsicIssue
    _m_pfrcp(); //expect: PythonIntrinsicIssue
    _m_pfrsqit1(); //expect: PythonIntrinsicIssue 
    _m_pfrsqrt(); //expect: PythonIntrinsicIssue 
    _m_pfsub(); //expect: PythonIntrinsicIssue 
    _m_pfsubr(); //expect: PythonIntrinsicIssue 
    _m_pi2fd(); //expect: PythonIntrinsicIssue 
    _m_pi2fw(); //expect: PythonIntrinsicIssue
    _m_pinsrw(); //expect: PythonIntrinsicIssue 
    _m_pmaddwd(); //expect: PythonIntrinsicIssue
    _m_pmaxsw(); //expect: PythonIntrinsicIssue 
    _m_pmaxub(); //expect: PythonIntrinsicIssue
    _m_pminsw(); //expect: PythonIntrinsicIssue 
    _m_pminub(); //expect: PythonIntrinsicIssue 
    _m_pmulhrw(); //expect: PythonIntrinsicIssue 
    _m_pmulhuw(); //expect: PythonIntrinsicIssue 
    _m_pmulhw(); //expect: PythonIntrinsicIssue 
    _m_pmullw(); //expect: PythonIntrinsicIssue 
    _m_por(); //expect: PythonIntrinsicIssue  
    _m_psadbw(); //expect: PythonIntrinsicIssue 
    _m_pshufw(); //expect: PythonIntrinsicIssue 
    _m_pslldi(); //expect: PythonIntrinsicIssue 
    _m_pslld(); //expect: PythonIntrinsicIssue 
    _m_psllqi(); //expect: PythonIntrinsicIssue
    _m_psllq(); //expect: PythonIntrinsicIssue
    _m_psllwi(); //expect: PythonIntrinsicIssue 
    _m_psllw(); //expect: PythonIntrinsicIssue
    _m_psradi(); //expect: PythonIntrinsicIssue 
    _m_psrad(); //expect: PythonIntrinsicIssue 
    _m_psrawi(); //expect: PythonIntrinsicIssue 
    _m_psraw(); //expect: PythonIntrinsicIssue
    _m_psrldi(); //expect: PythonIntrinsicIssue
    _m_psrld(); //expect: PythonIntrinsicIssue 
    _m_psrlqi(); //expect: PythonIntrinsicIssue
    _m_psrlq(); //expect: PythonIntrinsicIssue 
    _m_psrlwi(); //expect: PythonIntrinsicIssue 
    _m_psrlw(); //expect: PythonIntrinsicIssue 
    _m_psubb(); //expect: PythonIntrinsicIssue 
    _m_psubd(); //expect: PythonIntrinsicIssue
    _m_psubsb(); //expect: PythonIntrinsicIssue 
    _m_psubsw(); //expect: PythonIntrinsicIssue 
    _m_psubusb(); //expect: PythonIntrinsicIssue 
    _m_psubusw(); //expect: PythonIntrinsicIssue
    _m_psubw(); //expect: PythonIntrinsicIssue  
    _m_pswapd(); //expect: PythonIntrinsicIssue 
    _m_punpckhbw(); //expect: PythonIntrinsicIssue 
    _m_punpckhdq(); //expect: PythonIntrinsicIssue 
    _m_punpckhwd(); //expect: PythonIntrinsicIssue 
    _m_punpcklbw(); //expect: PythonIntrinsicIssue 
    _m_punpckldq(); //expect: PythonIntrinsicIssue 
    _m_punpcklwd(); //expect: PythonIntrinsicIssue 
    _m_pxor(); //expect: PythonIntrinsicIssue 
    _InterlockedAnd16_np(); //expect: PythonIntrinsicIssue 
    _InterlockedCompareExchange16_np(); //expect: PythonIntrinsicIssue 
    _InterlockedOr16_np(); //expect: PythonIntrinsicIssue 
    _InterlockedXor16_np(); //expect: PythonIntrinsicIssue 
    _loadbe_i16(); //expect: PythonIntrinsicIssue 
    _addcarry_u16(); //expect: PythonIntrinsicIssue 
    _addcarry_u32(); //expect: PythonIntrinsicIssue 
    _addcarry_u64(); //expect: PythonIntrinsicIssue 
    _addcarry_u8(); //expect: PythonIntrinsicIssue 
    _addcarryx_u32(); //expect: PythonIntrinsicIssue 
    _addcarryx_u64(); //expect: PythonIntrinsicIssue 
    _bittestandcomplement64(); //expect: PythonIntrinsicIssue 
    _bittestandreset64(); //expect: PythonIntrinsicIssue 
    _bittestandset64(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_lwpins16(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_lwpins32(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_lwpins64(); //expect: PythonIntrinsicIssue 
    __inbyte(); //expect: PythonIntrinsicIssue 
    _interlockedbittestandreset64_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _interlockedbittestandreset64_HLERelease(); //expect: PythonIntrinsicIssue 
    _interlockedbittestandreset64(); //expect: PythonIntrinsicIssue 
    _interlockedbittestandreset_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _interlockedbittestandreset_HLERelease(); //expect: PythonIntrinsicIssue 
    _interlockedbittestandset64_HLEAcquire(); //expect: PythonIntrinsicIssue
    _interlockedbittestandset64_HLERelease(); //expect: PythonIntrinsicIssue 
    _interlockedbittestandset64(); //expect: PythonIntrinsicIssue 
    _interlockedbittestandset_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _interlockedbittestandset_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedCompareExchange128(); //expect: PythonIntrinsicIssue 
    __lwpins32(); //expect: PythonIntrinsicIssue 
    __lwpins64(); //expect: PythonIntrinsicIssue 
    __readfsbyte(); //expect: PythonIntrinsicIssue 
    __readgsbyte(); //expect: PythonIntrinsicIssue 
    _subborrow_u16(); //expect: PythonIntrinsicIssue 
    _subborrow_u32(); //expect: PythonIntrinsicIssue 
    _subborrow_u64(); //expect: PythonIntrinsicIssue 
    _subborrow_u8(); //expect: PythonIntrinsicIssue  
    __vmx_on(); //expect: PythonIntrinsicIssue 
    __vmx_vmclear(); //expect: PythonIntrinsicIssue 
    __vmx_vmlaunch(); //expect: PythonIntrinsicIssue 
    __vmx_vmptrld(); //expect: PythonIntrinsicIssue 
    __vmx_vmread(); //expect: PythonIntrinsicIssue 
    __vmx_vmresume(); //expect: PythonIntrinsicIssue 
    __vmx_vmwrite(); //expect: PythonIntrinsicIssue 
    _andn_u64(); //expect: PythonIntrinsicIssue 
    _bextri_u64(); //expect: PythonIntrinsicIssue 
    _bextr_u64(); //expect: PythonIntrinsicIssue 
    _blcfill_u64(); //expect: PythonIntrinsicIssue 
    _blcic_u64(); //expect: PythonIntrinsicIssue 
    _blci_u64(); //expect: PythonIntrinsicIssue 
    _blcmsk_u64(); //expect: PythonIntrinsicIssue 
    _blcs_u64(); //expect: PythonIntrinsicIssue 
    _blsfill_u64(); //expect: PythonIntrinsicIssue 
    _blsic_u64(); //expect: PythonIntrinsicIssue 
    _blsi_u64(); //expect: PythonIntrinsicIssue 
    _blsmsk_u64(); //expect: PythonIntrinsicIssue 
    _blsr_u64(); //expect: PythonIntrinsicIssue 
    _bzhi_u64(); //expect: PythonIntrinsicIssue 
    _load_be_u64(); //expect: PythonIntrinsicIssue 
    __lzcnt64(); //expect: PythonIntrinsicIssue 
    _lzcnt_u64(); //expect: PythonIntrinsicIssue 
    _mm_crc32_u64(); //expect: PythonIntrinsicIssue 
    _mulx_u64(); //expect: PythonIntrinsicIssue 
    __emulu(); //expect: PythonIntrinsicIssue  
    __ll_lshift(); //expect: PythonIntrinsicIssue 
    __ull_rshift(); //expect: PythonIntrinsicIssue 
    _pdep_u64(); //expect: PythonIntrinsicIssue 
    _pext_u64(); //expect: PythonIntrinsicIssue 
    __popcnt64(); //expect: PythonIntrinsicIssue 
    __rdtscp(); //expect: PythonIntrinsicIssue 
    __rdtsc(); //expect: PythonIntrinsicIssue 
    __readcr0(); //expect: PythonIntrinsicIssue 
    __readcr2(); //expect: PythonIntrinsicIssue 
    __readcr3(); //expect: PythonIntrinsicIssue 
    __readcr4(); //expect: PythonIntrinsicIssue 
    __readcr8(); //expect: PythonIntrinsicIssue 
    __readdr(); //expect: PythonIntrinsicIssue 
    __readeflags(); //expect: PythonIntrinsicIssue 
    _readfsbase_u64(); //expect: PythonIntrinsicIssue 
    _readgsbase_u64(); //expect: PythonIntrinsicIssue 
    __readgsqword(); //expect: PythonIntrinsicIssue  
    __readmsr(); //expect: PythonIntrinsicIssue 
    __readpmc(); //expect: PythonIntrinsicIssue 
    _rorx_u64(); //expect: PythonIntrinsicIssue 
    __shiftleft128(); //expect: PythonIntrinsicIssue 
    __shiftright128(); //expect: PythonIntrinsicIssue 
    _shlx_u64(); //expect: PythonIntrinsicIssue 
    _shrx_u64(); //expect: PythonIntrinsicIssue 
    _t1mskc_u64(); //expect: PythonIntrinsicIssue 
    _tzcnt_u64(); //expect: PythonIntrinsicIssue 
    _tzmsk_u64(); //expect: PythonIntrinsicIssue 
    _udiv128(); //expect: PythonIntrinsicIssue 
    _umul128(); //expect: PythonIntrinsicIssue 
    __umulh(); //expect: PythonIntrinsicIssue 
    _xgetbv(); //expect: PythonIntrinsicIssue 
    _andn_u32(); //expect: PythonIntrinsicIssue 
    _bextri_u32(); //expect: PythonIntrinsicIssue 
    _bextr_u32(); //expect: PythonIntrinsicIssue 
    _blcfill_u32(); //expect: PythonIntrinsicIssue 
    _blcic_u32(); //expect: PythonIntrinsicIssue 
    _blci_u32(); //expect: PythonIntrinsicIssue 
    _blcmsk_u32(); //expect: PythonIntrinsicIssue 
    _blcs_u32(); //expect: PythonIntrinsicIssue 
    _blsfill_u32(); //expect: PythonIntrinsicIssue 
    _blsic_u32(); //expect: PythonIntrinsicIssue 
    _blsi_u32(); //expect: PythonIntrinsicIssue 
    _blsmsk_u32(); //expect: PythonIntrinsicIssue 
    _blsr_u32(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_bextri_u32(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_bextr_u32(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_crc32hi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_crc32qi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_crc32si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_lzcnt_u32(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rdfsbase32(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rdgsbase32(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rdrand16_step(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rdrand32_step(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rdrand64_step(); //expect: PythonIntrinsicIssue  
    _bzhi_u32(); //expect: PythonIntrinsicIssue
    __getcallerseflags(); //expect: PythonIntrinsicIssue 
    _load_be_u32(); //expect: PythonIntrinsicIssue 
    _lzcnt_u32(); //expect: PythonIntrinsicIssue 
    __lzcnt(); //expect: PythonIntrinsicIssue 
    _mm_crc32_u16(); //expect: PythonIntrinsicIssue 
    _mm_crc32_u32(); //expect: PythonIntrinsicIssue 
    _mm_crc32_u8(); //expect: PythonIntrinsicIssue 
    _mm_getcsr(); //expect: PythonIntrinsicIssue 
    _mulx_u32(); //expect: PythonIntrinsicIssue 
    _pdep_u32(); //expect: PythonIntrinsicIssue 
    _pext_u32(); //expect: PythonIntrinsicIssue 
    __popcnt(); //expect: PythonIntrinsicIssue 
    _readfsbase_u32(); //expect: PythonIntrinsicIssue 
    _readgsbase_u32(); //expect: PythonIntrinsicIssue 
    _rorx_u32(); //expect: PythonIntrinsicIssue 
    _shlx_u32(); //expect: PythonIntrinsicIssue 
    _shrx_u32(); //expect: PythonIntrinsicIssue 
    _t1mskc_u32(); //expect: PythonIntrinsicIssue 
    _tzcnt_u32(); //expect: PythonIntrinsicIssue 
    _tzmsk_u32(); //expect: PythonIntrinsicIssue 
    _udiv64(); //expect: PythonIntrinsicIssue 
    __indword(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_bextri_u64(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_bextr_u64(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_crc32di(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_lzcnt_u64(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rdfsbase64(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rdgsbase64(); //expect: PythonIntrinsicIssue 
    _bzhi_u64(); //expect: PythonIntrinsicIssue 
    _pdep_u64(); //expect: PythonIntrinsicIssue 
    _pext_u64(); //expect: PythonIntrinsicIssue 
    __readcr0(); //expect: PythonIntrinsicIssue 
    __readcr2(); //expect: PythonIntrinsicIssue 
    __readcr3(); //expect: PythonIntrinsicIssue 
    __readcr4(); //expect: PythonIntrinsicIssue 
    __readcr8(); //expect: PythonIntrinsicIssue 
    __readfsdword(); //expect: PythonIntrinsicIssue 
    __readgsdword(); //expect: PythonIntrinsicIssue 
    __segmentlimit(); //expect: PythonIntrinsicIssue 
    __readdr(); //expect: PythonIntrinsicIssue 
    __readeflags(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_lzcnt_16(); //expect: PythonIntrinsicIssue 
    __inword(); //expect: PythonIntrinsicIssue 
    _load_be_u16(); //expect: PythonIntrinsicIssue 
    __lzcnt16(); //expect: PythonIntrinsicIssue 
    __popcnt16(); //expect: PythonIntrinsicIssue 
    __readfsword(); //expect: PythonIntrinsicIssue 
    __readgsword(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pabsw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_packssdw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_packusdw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddsw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddusw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pavgw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pblendw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pbroadcastw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpeqw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpgtw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phaddsw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phaddw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phsubsw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phsubw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaddwd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaxsw256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmaxuw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pminsw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pminuw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovsxbw256 (); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovzxbw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmulhrsw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmulhuw256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmulhw256(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_pmullw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psadbw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pshufhw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pshuflw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psignw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllwi256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psraw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrawi256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlwi256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubsw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubusw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckhwd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpcklwd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcmov_v16hi256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_lddqu(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loaddqu(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_mpsadbw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pabsb128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_packsswb128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_packuswb128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_paddb128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pavgb128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pblendvb128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pbroadcastb128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pcmpeqb128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pcmpestrm128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pcmpgtb128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pcmpistrm128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmaxsb128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmaxub128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pminsb128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pminub128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pshufb128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psignb128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubb128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckhbw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpcklbw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vec_set_v16qi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcmov_v16qi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomeqb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomequb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomfalseb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomfalseub(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgeb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgeub(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgtb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgtub(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_vpcomleb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomleub(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomltb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomltub(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomneb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomneub(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomtrueb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomtrueub(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpperm(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vprotb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpshab(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpshlb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_palignr(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmuludq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psadbw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllqi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlqi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_addpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_addsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_addsubpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_andnpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_andpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_blendpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_blendvpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpeqpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpeqsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpgepd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpgtpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmplepd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmplesd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpltpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpltsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpneqpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpneqsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpngepd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpngtpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpnlepd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpnlesd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpnltpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpnltsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpordpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpordsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmppd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpunordpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpunordsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtdq2pd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtpi2pd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtps2pd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtsi2sd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtsi642sd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtss2sd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_divpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_divsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_dppd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmaddpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmaddsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmaddsubpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmsubaddpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmsubpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmsubsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmaddpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmaddsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmsubpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmsubsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gatherdiv2df(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gathersiv2df(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_haddpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_hsubpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loadddup(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loadhpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loadlpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loadupd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskloadpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maxpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maxsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_minpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_minsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movddup(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movsd(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_mulpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_mulsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_orpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pd_pd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_roundpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_roundsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_shufpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_sqrtpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_sqrtsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_subpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_subsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_unpckhpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_unpcklpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vextractf128_pd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vfrczpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vfrczsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcmov_v2df(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermil2pd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermilpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermilvarpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_xorpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_aesdec128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_aesdeclast128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_aesenc128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_aesenclast128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_aesimc128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_aeskeygenassist128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_extrqi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_extrq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gatherdiv2di(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gathersiv2di(); //expect: PythonIntrinsicIssue
    __builtin_ia32_insertqi(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_insertq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskloadq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movntdqa(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_palignr128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pand128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pandn128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pbroadcastq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pclmulqdq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpeqq(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_pcmpgtq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovsxbq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovsxdq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovsxwq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovzxbq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovzxdq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovzxwq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmuldq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmuludq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_por128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psadbw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pslldqi128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllqi128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllv2di(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrldqi128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlqi128(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_psrlv2di(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckhqdq128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_punpcklqdq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pxor128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vec_set_v2di(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcmov(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vpcmov_v2di(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomeqq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomequq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomfalseq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomfalseuq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgeq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgeuq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgtq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgtuq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomleq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomleuq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomltq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomltuq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomneq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomneuq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomtrueq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomtrueuq(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_vphaddbq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphadddq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphaddubq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphaddudq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphadduwq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphaddwq(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vphsubdq(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vpmacsdqh(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vpmacsdql(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vpmacssdqh(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vpmacssdql(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vprotq(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vpshaq(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vpshlq(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pfacc(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pfadd(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pfmax(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pfmin(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pfmul(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pfnacc(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pfpnacc(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pfrcpit1(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pfrcpit2(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pfrcp(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pfrsqrtit1 (); //expect: PythonIntrinsicIssue
    __builtin_ia32_pfrsqrt(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pfsubr(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pfsub(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pi2fd(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pi2fw(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pswapdsf(); //expect: PythonIntrinsicIssue
    __builtin_ia32_cvtpd2pi(); //expect: PythonIntrinsicIssue
    __builtin_ia32_cvtps2pi(); //expect: PythonIntrinsicIssue
    __builtin_ia32_cvttpd2pi(); //expect: PythonIntrinsicIssue
    __builtin_ia32_cvttps2pi(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pabsd(); //expect: PythonIntrinsicIssue
    __builtin_ia32_paddd(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pcmpeqd(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pcmpgtd(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pf2id(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pf2iw(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pfcmpeq(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pfcmpge(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pfcmpgt(); //expect: PythonIntrinsicIssue
    __builtin_ia32_phaddd(); //expect: PythonIntrinsicIssue
    __builtin_ia32_phsubd(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psignd(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pslldi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pslld(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psradi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrad(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrldi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrld(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pswapdsi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckhdq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckldq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_lddqu256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loaddqu256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_mpsadbw256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pabsb256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_packsswb256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_packuswb256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddb256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddsb256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddusb256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pavgb256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pblendvb256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pbroadcastb256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pcmpeqb256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pcmpgtb256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmaddubsw256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmaxsb256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmaxub256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pminsb256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pminub256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pshufb256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psignb256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psubb256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psubsb256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psubusb256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_punpckhbw256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_punpcklbw256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vpcmov_v32qi256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_addpd256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_addsubpd256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_andnpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_andpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_blendpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_blendvpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmppd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtdq2pd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtps2pd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_divpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmaddpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmaddsubpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmsubaddpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmsubpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmaddpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmsubpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gatherdiv4df(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gathersiv4df(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_haddpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_hsubpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loadupd256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_maskloadpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maxpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_minpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movddup256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_mulpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_orpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pd256_pd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_permdf256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_roundpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_shufpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_sqrtpd256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_subpd256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_unpckhpd256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_unpcklpd256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vbroadcastf128_pd256(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_vbroadcastsd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vbroadcastsd_pd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vfrczpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vinsertf128_pd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcmov_v4df256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vperm2f128_pd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermil2pd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermilpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermilvarpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_xorpd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_andnotsi256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_andsi256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_extract128i256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gatherdiv4di(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gathersiv4di(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_insert128i256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskloadq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movntdqa256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_palignr256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pbroadcastq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpeqq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pcmpgtq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_permdi256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_permti256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmovsxbq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmovsxdq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmovsxwq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmovzxbq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmovzxdq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmovzxwq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmuldq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmuludq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_por256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pslldqi256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psllq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psllqi256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psllv4di(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psrldqi256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psrlq256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psrlqi256(); //expect: PythonIntrinsicIssue
    __builtin_ia32_psrlv4di(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckhqdq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpcklqdq256(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_pxor256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vbroadcastsi256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcmov_v4di256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pabsw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_packssdw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddsw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddusw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pavgw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpeqw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpgtw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phaddsw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phaddw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phsubsw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phsubw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pinsrw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaddubsw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaxsw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pminsw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmulhrsw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmulhrw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmulhuw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmulhw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmullw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psignw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllwi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrawi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psraw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlwi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubsw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubusw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckhwd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpcklwd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_addps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_addss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_addsubps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_andnps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_andps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_blendps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_blendvps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtdq2ps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtpd2ps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtpd2ps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtpi2ps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtsd2ss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtsi2ss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_divps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_divss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_dpps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmaddps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmaddss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmaddsubps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmsubaddps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmsubps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmsubss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmaddps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmaddss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmsubps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmsubss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gatherdiv4sf256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gatherdiv4sf(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gathersiv4sf(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_haddps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_hsubps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_insertps128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loadaps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loadhps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loadlps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loadsss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loadups(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskloadps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maxps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maxss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_minps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_minss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movhlps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movlhps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movshdup(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movsldup(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_mulps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_mulss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_orps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ps_ps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rcpps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rcpss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_roundps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_roundss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rsqrtps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rsqrtss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_shufps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_sqrtps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_sqrtss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_subps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_subss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_unpckhps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_unpcklps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vbroadcastss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vbroadcastss_ps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vec_set_v4sf(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vextractf128_ps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vfrczps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vfrczss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcmov_v4sf(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermil2ps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermilps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermilvarps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_xorps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpeqps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpeqss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpgeps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpgtps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpleps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpless(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpltps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpltss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpneqps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpneqss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpngeps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpngtps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpnleps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpnless(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpnltps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpnlts(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpordps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpordss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpunordps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpunordss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtpd2dq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtpd2dq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtps2dq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvttpd2dq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvttpd2dq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvttps2dq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gatherdiv4si256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gatherdiv4si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gathersiv4si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskloadd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pabsd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pblendd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pbroadcastd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpeqd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpgtd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phaddd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phsubd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaddwd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaxsd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaxud128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pminsd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pminud128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovsxbd128(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmovsxwd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovzxbd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovzxwd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmulld128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pshufd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psignd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pslld128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pslldi128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllv4si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrad128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psradi128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrav4si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrld128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrldi128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlv4si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckhdq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckldq128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_si_si256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vec_set_v4si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vextractf128_si256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcmov_v4si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomeqd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomequd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomfalsed(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomfalseud(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomged(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgeud(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgtd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgtud(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomled(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomleud(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomltd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomltud(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomned(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomneud(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomtrued(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomtrueud(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphaddbd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphaddubd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphadduwd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphaddwd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphsubwd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpmacsdd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpmacssdd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpmacsswd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpmacswd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpmadcsswd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpmadcswd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vprotd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpshad(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpshld(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pabsw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_packssdw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_packusdw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pavgw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pblendw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pbroadcastw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpeqw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpgtw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phaddsw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phaddw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phminposuw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phsubsw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phsubw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaddubsw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaxsw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaxuw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pminsw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pminuw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovsxbw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovzxbw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmulhrsw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmulhuw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmulhw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmullw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pshufhw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pshuflw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psignw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllwi128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psraw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrawi128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlwi128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubw128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckhwd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpcklwd128(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcmov_v8hi(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomequw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomeqw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomfalseuw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomfalsew(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgeuw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgew(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgtuw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomgtw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomleuw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomlew(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_vpcomltuw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomltw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomneuw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomnew(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomtrueuw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcomtruew(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphaddbw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphaddubw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vphsubbw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpmacssww(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpmacsww(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vprotw(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vpshaw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpshlw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pabsb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_packsswb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_packuswb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddsb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddusb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pavgb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pavgusb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpeqb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpgtb(); //expect: PythonIntrinsicIssue
    __builtin_ia32_pmaxub(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pminub(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pshufb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psignb(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_psubb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubsb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubusb(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckhbw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpcklbw(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_addps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_addsubps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_andnps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_andps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_blendps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_blendvps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cmpps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtdq2ps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_divps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_dpps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmaddps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmaddsubps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmsubaddps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fmsubps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmaddps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_fnmsubps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gathersiv8sf(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_haddps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_hsubps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_loadups256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskloadps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maxps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_minps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movshdup256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movsldup256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_mulps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_orps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_permvarsf256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_ps256_ps(); //expect: PythonIntrinsicIssue
    __builtin_ia32_rcpps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_roundps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rsqrtps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_rsqrtps_nr256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_shufps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_sqrtps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_sqrtps_nr256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_subps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_unpckhps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_unpcklps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vbroadcastf128_ps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vbroadcastss256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vbroadcastss_ps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vfrczps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vinsertf128_ps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcmov_v8sf256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vperm2f128_ps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermil2ps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermilps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpermilvarps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_xorps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvtps2dq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_cvttps2dq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_gathersiv8si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskloadd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pabsd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_paddd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pblendd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pbroadcastd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpeqd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pcmpgtd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_permvarsi256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phaddd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_phsubd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaxsd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmaxud256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pminsd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pminud256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovsxbd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovsxwd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovzxbd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmovzxwd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pmulld256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pshufd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psignd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pslld256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pslldi256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psllv8si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrad256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psradi256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrav8si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrld256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrldi256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psrlv8si(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_psubd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckhdq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_punpckldq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_si256_si(); //expect: PythonIntrinsicIssue
    __builtin_ia32_vinsertf128_si256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vpcmov_v8si256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vperm2f128_si256(); //expect: PythonIntrinsicIssue 
    __addfsbyte(); //expect: PythonIntrinsicIssue 
    __addfsdword(); //expect: PythonIntrinsicIssue 
    __addfsword(); //expect: PythonIntrinsicIssue 
    __addgsbyte(); //expect: PythonIntrinsicIssue 
    __addgsdword(); //expect: PythonIntrinsicIssue 
    __addgsqword(); //expect: PythonIntrinsicIssue 
    __addgsword(); //expect: PythonIntrinsicIssue 
    __builtin_cpu_init(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_clflush(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_femms(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_lfence(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_llwpcb16(); //expect: PythonIntrinsicIssue
    __builtin_ia32_llwpcb16(); //expect: PythonIntrinsicIssue
    __builtin_ia32_llwpcb32(); //expect: PythonIntrinsicIssue
    __builtin_ia32_llwpcb32(); //expect: PythonIntrinsicIssue
    __builtin_ia32_llwpcb64(); //expect: PythonIntrinsicIssue
    __builtin_ia32_llwpcb64(); //expect: PythonIntrinsicIssue
    __builtin_ia32_lwpval16(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_lwpval32(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_lwpval64(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskmovdqu(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskmovq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskstored256(); //expect: PythonIntrinsicIssue  
    __builtin_ia32_maskstored(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskstorepd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskstorepd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskstoreps256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskstoreps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskstoreq256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_maskstoreq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_mfence(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_monitor(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movntdq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movnti64(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movnti(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movntpd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movntps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movntq(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movntsd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_movntss(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_mwait(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_pause(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_sfence(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_storeaps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_storedqu256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_storedqu(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_storehps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_storelps(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_storess(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_storeupd256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_storeupd(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_storeups256(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_storeups(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vzeroall(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_vzeroupper(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_xabort(); //expect: PythonIntrinsicIssue 
    __builtin_ia32_xend(); //expect: PythonIntrinsicIssue 
    _clac(); //expect: PythonIntrinsicIssue 
    __cpuidex(); //expect: PythonIntrinsicIssue 
    __cpuid(); //expect: PythonIntrinsicIssue  
    __faststorefence(); //expect: PythonIntrinsicIssue 
    _fxrstor64(); //expect: PythonIntrinsicIssue 
    _fxrstor(); //expect: PythonIntrinsicIssue 
    _fxsave64(); //expect: PythonIntrinsicIssue 
    _fxsave(); //expect: PythonIntrinsicIssue 
    __halt(); //expect: PythonIntrinsicIssue 
    __inbytestring(); //expect: PythonIntrinsicIssue 
    __incfsbyte(); //expect: PythonIntrinsicIssue 
    __incfsdword(); //expect: PythonIntrinsicIssue 
    __incfsword(); //expect: PythonIntrinsicIssue 
    __incgsbyte(); //expect: PythonIntrinsicIssue 
    __incgsdword(); //expect: PythonIntrinsicIssue 
    __incgsqword(); //expect: PythonIntrinsicIssue 
    __incgsword(); //expect: PythonIntrinsicIssue 
    __indwordstring(); //expect: PythonIntrinsicIssue 
    __int2c(); //expect: PythonIntrinsicIssue 
    _InterlockedCompareExchangePointer_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _InterlockedCompareExchangePointer_HLERelease(); //expect: PythonIntrinsicIssue 
    _InterlockedCompareExchangePointer_np(); //expect: PythonIntrinsicIssue 
    _InterlockedExchangePointer_HLEAcquire(); //expect: PythonIntrinsicIssue 
    _InterlockedExchangePointer_HLERelease(); //expect: PythonIntrinsicIssue 
    __invlpg(); //expect: PythonIntrinsicIssue 
    _invpcid(); //expect: PythonIntrinsicIssue 
    __inwordstring(); //expect: PythonIntrinsicIssue 
    _lgdt(); //expect: PythonIntrinsicIssue 
    __lidt(); //expect: PythonIntrinsicIssue 
    __llwpcb(); //expect: PythonIntrinsicIssue 
    __lwpval32(); //expect: PythonIntrinsicIssue 
    __lwpval64(); //expect: PythonIntrinsicIssue 
    _m_empty(); //expect: PythonIntrinsicIssue 
    _m_femms(); //expect: PythonIntrinsicIssue 
    _mm256_maskstore_epi32(); //expect: PythonIntrinsicIssue 
    _mm256_maskstore_epi64(); //expect: PythonIntrinsicIssue 
    _mm256_maskstore_pd(); //expect: PythonIntrinsicIssue 
    _mm256_maskstore_ps(); //expect: PythonIntrinsicIssue 
    _mm256_store_pd(); //expect: PythonIntrinsicIssue 
    _mm256_store_ps(); //expect: PythonIntrinsicIssue 
    _mm256_store_si256(); //expect: PythonIntrinsicIssue 
    _mm256_storeu_pd(); //expect: PythonIntrinsicIssue 
    _mm256_storeu_ps(); //expect: PythonIntrinsicIssue 
    _mm256_storeu_si256(); //expect: PythonIntrinsicIssue 
    __mm256_stream_pd(); //expect: PythonIntrinsicIssue 
    _mm256_stream_ps(); //expect: PythonIntrinsicIssue 
    __mm256_stream_si256(); //expect: PythonIntrinsicIssue 
    _mm256_zeroall(); //expect: PythonIntrinsicIssue 
    _mm256_zeroupper(); //expect: PythonIntrinsicIssue 
    _m_maskmovq(); //expect: PythonIntrinsicIssue 
    _mm_clflush(); //expect: PythonIntrinsicIssue 
    _mm_lfence(); //expect: PythonIntrinsicIssue 
    _mm_maskmoveu_si128(); //expect: PythonIntrinsicIssue 
    _mm_maskstore_epi32(); //expect: PythonIntrinsicIssue 
    _mm_maskstore_epi64(); //expect: PythonIntrinsicIssue 
    _mm_maskstore_pd(); //expect: PythonIntrinsicIssue 
    _mm_maskstore_ps(); //expect: PythonIntrinsicIssue 
    _mm_mfence(); //expect: PythonIntrinsicIssue 
    _mm_monitor(); //expect: PythonIntrinsicIssue 
    _mm_mwait(); //expect: PythonIntrinsicIssue 
    _mm_pause(); //expect: PythonIntrinsicIssue 
    _mm_prefetch(); //expect: PythonIntrinsicIssue 
    _mm_setcsr(); //expect: PythonIntrinsicIssue 
    _mm_sfence(); //expect: PythonIntrinsicIssue  
    _mm_store1_pd(); //expect: PythonIntrinsicIssue 
    _mm_storeh_pd(); //expect: PythonIntrinsicIssue 
    _mm_storeh_pi(); //expect: PythonIntrinsicIssue 
    _mm_storel_epi64(); //expect: PythonIntrinsicIssue 
    _mm_storel_pd(); //expect: PythonIntrinsicIssue 
    _mm_storel_pi(); //expect: PythonIntrinsicIssue 
    _mm_store_pd(); //expect: PythonIntrinsicIssue 
    _mm_store_ps1(); //expect: PythonIntrinsicIssue 
    _mm_store_ps(); //expect: PythonIntrinsicIssue 
    _mm_storer_pd(); //expect: PythonIntrinsicIssue 
    _mm_storer_ps(); //expect: PythonIntrinsicIssue 
    _mm_store_sd(); //expect: PythonIntrinsicIssue 
    _mm_store_si128(); //expect: PythonIntrinsicIssue 
    _mm_store_ss(); //expect: PythonIntrinsicIssue 
    _mm_storeu_pd(); //expect: PythonIntrinsicIssue 
    _mm_storeu_ps(); //expect: PythonIntrinsicIssue 
    _mm_storeu_si128(); //expect: PythonIntrinsicIssue 
    _mm_stream_pd(); //expect: PythonIntrinsicIssue 
    _mm_stream_pd(); //expect: PythonIntrinsicIssue 
    _mm_stream_pi(); //expect: PythonIntrinsicIssue 
    _mm_stream_ps(); //expect: PythonIntrinsicIssue 
    _mm_stream_sd(); //expect: PythonIntrinsicIssue 
    _mm_stream_si128(); //expect: PythonIntrinsicIssue 
    _mm_stream_si32(); //expect: PythonIntrinsicIssue 
    _mm_stream_si64x(); //expect: PythonIntrinsicIssue 
    _mm_stream_ss(); //expect: PythonIntrinsicIssue 
    __movsb(); //expect: PythonIntrinsicIssue 
    __movsd(); //expect: PythonIntrinsicIssue 
    __movsq(); //expect: PythonIntrinsicIssue 
    __movsw(); //expect: PythonIntrinsicIssue 
    _m_prefetch(); //expect: PythonIntrinsicIssue 
    _m_prefetchw(); //expect: PythonIntrinsicIssue 
    __nvreg_restore_fence(); //expect: PythonIntrinsicIssue 
    __nvreg_save_fence(); //expect: PythonIntrinsicIssue 
    __outbytestring(); //expect: PythonIntrinsicIssue 
    __outbyte(); //expect: PythonIntrinsicIssue 
    __outdwordstring(); //expect: PythonIntrinsicIssue 
    __outdword(); //expect: PythonIntrinsicIssue 
    __outwordstring(); //expect: PythonIntrinsicIssue 
    __outword(); //expect: PythonIntrinsicIssue 
    _rsm(); //expect: PythonIntrinsicIssue 
    _sgdt(); //expect: PythonIntrinsicIssue 
    _sgdt(); //expect: PythonIntrinsicIssue 
    __sidt(); //expect: PythonIntrinsicIssue 
    * __slwpcb(); //expect: PythonIntrinsicIssue 
    _stac(); //expect: PythonIntrinsicIssue 
    _Store64_HLERelease(); //expect: PythonIntrinsicIssue 
    _storebe_i16(); //expect: PythonIntrinsicIssue 
    _storebe_i32(); //expect: PythonIntrinsicIssue 
    _storebe_i64(); //expect: PythonIntrinsicIssue 
    _store_be_u16(); //expect: PythonIntrinsicIssue 
    _store_be_u32(); //expect: PythonIntrinsicIssue 
    _store_be_u64(); //expect: PythonIntrinsicIssue 
    _Store_HLERelease(); //expect: PythonIntrinsicIssue 
    _StorePointer_HLERelease(); //expect: PythonIntrinsicIssue 
    __stosb(); //expect: PythonIntrinsicIssue 
    __stosd(); //expect: PythonIntrinsicIssue 
    __stosq(); //expect: PythonIntrinsicIssue 
    __stosw(); //expect: PythonIntrinsicIssue 
    __svm_clgi(); //expect: PythonIntrinsicIssue 
    __svm_invlpga(); //expect: PythonIntrinsicIssue 
    __svm_skinit(); //expect: PythonIntrinsicIssue 
    __svm_stgi(); //expect: PythonIntrinsicIssue 
    __svm_vmload(); //expect: PythonIntrinsicIssue 
    __svm_vmrun(); //expect: PythonIntrinsicIssue 
    __svm_vmsave(); //expect: PythonIntrinsicIssue 
    __ud2(); //expect: PythonIntrinsicIssue 
    __vmx_off(); //expect: PythonIntrinsicIssue  
    __vmx_vmptrst(); //expect: PythonIntrinsicIssue 
    __wbinvd(); //expect: PythonIntrinsicIssue 
    __writecr0(); //expect: PythonIntrinsicIssue 
    __writecr0(); //expect: PythonIntrinsicIssue 
    __writecr3(); //expect: PythonIntrinsicIssue 
    __writecr3(); //expect: PythonIntrinsicIssue 
    __writecr4(); //expect: PythonIntrinsicIssue 
    __writecr4(); //expect: PythonIntrinsicIssue 
    __writecr8(); //expect: PythonIntrinsicIssue 
    __writecr8(); //expect: PythonIntrinsicIssue 
    __writedr(); //expect: PythonIntrinsicIssue 
    __writedr(); //expect: PythonIntrinsicIssue 
    __writeeflags(); //expect: PythonIntrinsicIssue 
    __writeeflags(); //expect: PythonIntrinsicIssue 
    _writefsbase_u32(); //expect: PythonIntrinsicIssue 
    _writefsbase_u64(); //expect: PythonIntrinsicIssue 
    _writefsbase_u64(); //expect: PythonIntrinsicIssue 
    __writefsbyte(); //expect: PythonIntrinsicIssue 
    __writefsdword(); //expect: PythonIntrinsicIssue 
    __writefsword(); //expect: PythonIntrinsicIssue 
    _writegsbase_u32(); //expect: PythonIntrinsicIssue 
    _writegsbase_u64(); //expect: PythonIntrinsicIssue 
    _writegsbase_u64(); //expect: PythonIntrinsicIssue 
    __writegsbyte(); //expect: PythonIntrinsicIssue 
    __writegsdword(); //expect: PythonIntrinsicIssue 
    __writegsqword(); //expect: PythonIntrinsicIssue 
    __writegsword(); //expect: PythonIntrinsicIssue 
    __writemsr(); //expect: PythonIntrinsicIssue 
    _xrstor64(); //expect: PythonIntrinsicIssue 
    _xrstor(); //expect: PythonIntrinsicIssue 
    _xsave64(); //expect: PythonIntrinsicIssue 
    _xsaveopt64(); //expect: PythonIntrinsicIssue 
    _xsaveopt(); //expect: PythonIntrinsicIssue 
    _xsave(); //expect: PythonIntrinsicIssue 
    _xsetbv(); //expect: PythonIntrinsicIssue 

    // OTHER ARCH INTRINSICS
    _addcary(); //expect: PythonIntrinsicIssue 
    _allow_cpu_features(); //expect: PythonIntrinsicIssue 
    _bit_scan_(); //expect: PythonIntrinsicIssue 
    _bnd_(); //expect: PythonIntrinsicIssue 
    _rdpip_(); //expect: PythonIntrinsicIssue 
    _rotwa(); //expect: PythonIntrinsicIssue 
    vec_v(); //expect: PythonIntrinsicIssue 
    _otherarch_intrinsic_(); //expect: PythonIntrinsicIssue 

    // INCOMPATIBLE UCRT INTRINSICS
    _abs64(); //expect: PythonIntrinsicIssue
    _alloca(); //expect: PythonIntrinsicIssue
    _byteswap_uint64(); //expect: PythonIntrinsicIssue
    _byteswap_ulong(); //expect: PythonIntrinsicIssue
    _byteswap_ushort(); //expect: PythonIntrinsicIssue
    _lrotl(); //expect: PythonIntrinsicIssue
    _lrotr(); //expect: PythonIntrinsicIssue
    _rotl(); //expect: PythonIntrinsicIssue
    _rotl64(); //expect: PythonIntrinsicIssue
    _rotr(); //expect: PythonIntrinsicIssue
    _rotr64(); //expect: PythonIntrinsicIssue
    _strset(); //expect: PythonIntrinsicIssue
    _wcsset(); //expect: PythonIntrinsicIssue
    wcscat();
    strset(); //expect: PythonIntrinsicIssue
    wcscmp();
    wcslen();
      
    int printf(const char *format, ...);
""")

ffi.compile()

# Load shared library.
# None means loading the entire C namespace.
C = ffi.dlopen(None)
# Call a function from the shared library.
arg = ffi.new("char[]", b"dsklfsd")
C.printf(b"hello %s!\n", arg)