// shall not generate issue in aarch64.
void common_intrinsic_test()
{
    * __builtin_apply_args ();
    * __builtin_apply ();
    __builtin_return ();
    __builtin_va_arg_pack ();
    __builtin_va_arg_pack_len ();
    * __builtin_return_address ();
    * __builtin_extract_return_addr ();
    * __builtin_frob_return_address ();
    * __builtin_frame_address ();
    __atomic_load_n (); //expect: CPPStdCodes
    __atomic_load (); //expect: CPPStdCodes
    __atomic_store_n (); //expect: CPPStdCodes
    __atomic_store ();  // expect: CPPStdCodes
    __atomic_exchange_n (); // expect: CPPStdCodes
    __atomic_exchange (); // expect: CPPStdCodes
    __atomic_compare_exchange_n (); // expect: CPPStdCodes
    __atomic_compare_exchange (); // expect: CPPStdCodes
    __atomic_add_fetch (); // expect: CPPStdCodes
    __atomic_sub_fetch (); // expect: CPPStdCodes
    __atomic_and_fetch (); // expect: CPPStdCodes
    __atomic_xor_fetch (); // expect: CPPStdCodes
    __atomic_or_fetch (); // expect: CPPStdCodes
    __atomic_nand_fetch (); // expect: CPPStdCodes
    __atomic_fetch_add (); // expect: CPPStdCodes
    __atomic_fetch_sub (); // expect: CPPStdCodes
    __atomic_fetch_and (); // expect: CPPStdCodes
    __atomic_fetch_xor (); // expect: CPPStdCodes
    __atomic_fetch_or (); // expect: CPPStdCodes
    __atomic_fetch_nand (); // expect: CPPStdCodes
    __atomic_test_and_set (); // expect: CPPStdCodes
    __atomic_clear (); // expect: CPPStdCodes
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
    __sync_fetch_and_add (); //expect: CPPStdCodes
    __sync_fetch_and_sub (); //expect: CPPStdCodes
    __sync_fetch_and_or (); //expect: CPPStdCodes
    __sync_fetch_and_and (); //expect: CPPStdCodes
    __sync_fetch_and_xor (); //expect: CPPStdCodes
    __sync_fetch_and_nand (); //expect: CPPStdCodes
    __sync_add_and_fetch (); //expect: CPPStdCodes
    __sync_sub_and_fetch (); //expect: CPPStdCodes
    __sync_or_and_fetch (); //expect: CPPStdCodes
    __sync_and_and_fetch (); //expect: CPPStdCodes
    __sync_xor_and_fetch (); //expect: CPPStdCodes
    __sync_nand_and_fetch (); //expect: CPPStdCodes
    __sync_bool_compare_and_swap (); //expect: CPPStdCodes
    __sync_val_compare_and_swap (); //expect: CPPStdCodes
}

// shall not generate issue in aarch64.
void aarch64_intrinsic_test()
{
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
}

// shall generate issue in aarch64.
void arm_intrinsic_test()
{
    __builtin_arm_getwcgr0(); //expect: IntrinsicIssue
    __builtin_arm_setwcgr0(); //expect: IntrinsicIssue
    __builtin_arm_getwcgr1(); //expect: IntrinsicIssue
    __builtin_arm_setwcgr1(); //expect: IntrinsicIssue
    __builtin_arm_getwcgr2(); //expect: IntrinsicIssue
    __builtin_arm_setwcgr2(); //expect: IntrinsicIssue
    __builtin_arm_getwcgr3(); //expect: IntrinsicIssue
    __builtin_arm_setwcgr3(); //expect: IntrinsicIssue
    __builtin_arm_textrmsb(); //expect: IntrinsicIssue
    __builtin_arm_textrmsh(); //expect: IntrinsicIssue
    __builtin_arm_textrmsw(); //expect: IntrinsicIssue
    __builtin_arm_textrmub(); //expect: IntrinsicIssue
    __builtin_arm_textrmuh(); //expect: IntrinsicIssue
    __builtin_arm_textrmuw(); //expect: IntrinsicIssue
    __builtin_arm_tinsrb(); //expect: IntrinsicIssue
    __builtin_arm_tinsrh(); //expect: IntrinsicIssue
    __builtin_arm_tinsrw(); //expect: IntrinsicIssue
    __builtin_arm_tmia(); //expect: IntrinsicIssue
    __builtin_arm_tmiabb(); //expect: IntrinsicIssue
    __builtin_arm_tmiabt(); //expect: IntrinsicIssue
    __builtin_arm_tmiaph(); //expect: IntrinsicIssue
    __builtin_arm_tmiatb(); //expect: IntrinsicIssue
    __builtin_arm_tmiatt(); //expect: IntrinsicIssue
    __builtin_arm_tmovmskb(); //expect: IntrinsicIssue
    __builtin_arm_tmovmskh(); //expect: IntrinsicIssue
    __builtin_arm_tmovmskw(); //expect: IntrinsicIssue
    __builtin_arm_waccb(); //expect: IntrinsicIssue
    __builtin_arm_wacch(); //expect: IntrinsicIssue
    __builtin_arm_waccw(); //expect: IntrinsicIssue
    __builtin_arm_waddb(); //expect: IntrinsicIssue
    __builtin_arm_waddbss(); //expect: IntrinsicIssue
    __builtin_arm_waddbus(); //expect: IntrinsicIssue
    __builtin_arm_waddh(); //expect: IntrinsicIssue
    __builtin_arm_waddhss(); //expect: IntrinsicIssue
    __builtin_arm_waddhus(); //expect: IntrinsicIssue
    __builtin_arm_waddw(); //expect: IntrinsicIssue
    __builtin_arm_waddwss(); //expect: IntrinsicIssue
    __builtin_arm_waddwus(); //expect: IntrinsicIssue
    __builtin_arm_walign(); //expect: IntrinsicIssue
    __builtin_arm_wand(); //expect: IntrinsicIssue
    __builtin_arm_wandn(); //expect: IntrinsicIssue
    __builtin_arm_wavg2b(); //expect: IntrinsicIssue
    __builtin_arm_wavg2br(); //expect: IntrinsicIssue
    __builtin_arm_wavg2h(); //expect: IntrinsicIssue
    __builtin_arm_wavg2hr(); //expect: IntrinsicIssue
    __builtin_arm_wcmpeqb(); //expect: IntrinsicIssue
    __builtin_arm_wcmpeqh(); //expect: IntrinsicIssue
    __builtin_arm_wcmpeqw(); //expect: IntrinsicIssue
    __builtin_arm_wcmpgtsb(); //expect: IntrinsicIssue
    __builtin_arm_wcmpgtsh(); //expect: IntrinsicIssue
    __builtin_arm_wcmpgtsw(); //expect: IntrinsicIssue
    __builtin_arm_wcmpgtub(); //expect: IntrinsicIssue
    __builtin_arm_wcmpgtuh(); //expect: IntrinsicIssue
    __builtin_arm_wcmpgtuw(); //expect: IntrinsicIssue
    __builtin_arm_wmacs(); //expect: IntrinsicIssue
    __builtin_arm_wmacsz(); //expect: IntrinsicIssue
    __builtin_arm_wmacu(); //expect: IntrinsicIssue
    __builtin_arm_wmacuz(); //expect: IntrinsicIssue
    __builtin_arm_wmadds(); //expect: IntrinsicIssue
    __builtin_arm_wmaddu(); //expect: IntrinsicIssue
    __builtin_arm_wmaxsb(); //expect: IntrinsicIssue
    __builtin_arm_wmaxsh(); //expect: IntrinsicIssue
    __builtin_arm_wmaxsw(); //expect: IntrinsicIssue
    __builtin_arm_wmaxub(); //expect: IntrinsicIssue
    __builtin_arm_wmaxuh(); //expect: IntrinsicIssue
    __builtin_arm_wmaxuw(); //expect: IntrinsicIssue
    __builtin_arm_wminsb(); //expect: IntrinsicIssue
    __builtin_arm_wminsh(); //expect: IntrinsicIssue
    __builtin_arm_wminsw(); //expect: IntrinsicIssue
    __builtin_arm_wminub(); //expect: IntrinsicIssue
    __builtin_arm_wminuh(); //expect: IntrinsicIssue
    __builtin_arm_wminuw(); //expect: IntrinsicIssue
    __builtin_arm_wmulsm(); //expect: IntrinsicIssue
    __builtin_arm_wmulul(); //expect: IntrinsicIssue
    __builtin_arm_wmulum(); //expect: IntrinsicIssue
    __builtin_arm_wor(); //expect: IntrinsicIssue
    __builtin_arm_wpackdss(); //expect: IntrinsicIssue
    __builtin_arm_wpackdus(); //expect: IntrinsicIssue
    __builtin_arm_wpackhss(); //expect: IntrinsicIssue
    __builtin_arm_wpackhus(); //expect: IntrinsicIssue
    __builtin_arm_wpackwss(); //expect: IntrinsicIssue
    __builtin_arm_wpackwus(); //expect: IntrinsicIssue
    __builtin_arm_wrord(); //expect: IntrinsicIssue
    __builtin_arm_wrordi(); //expect: IntrinsicIssue
    __builtin_arm_wrorh(); //expect: IntrinsicIssue
    __builtin_arm_wrorhi(); //expect: IntrinsicIssue
    __builtin_arm_wrorw(); //expect: IntrinsicIssue
    __builtin_arm_wrorwi(); //expect: IntrinsicIssue
    __builtin_arm_wsadb(); //expect: IntrinsicIssue
    __builtin_arm_wsadbz(); //expect: IntrinsicIssue
    __builtin_arm_wsadh(); //expect: IntrinsicIssue
    __builtin_arm_wsadhz(); //expect: IntrinsicIssue
    __builtin_arm_wshufh(); //expect: IntrinsicIssue
    __builtin_arm_wslld(); //expect: IntrinsicIssue
    __builtin_arm_wslldi(); //expect: IntrinsicIssue
    __builtin_arm_wsllh(); //expect: IntrinsicIssue
    __builtin_arm_wsllhi(); //expect: IntrinsicIssue
    __builtin_arm_wsllw(); //expect: IntrinsicIssue
    __builtin_arm_wsllwi(); //expect: IntrinsicIssue
    __builtin_arm_wsrad(); //expect: IntrinsicIssue
    __builtin_arm_wsradi(); //expect: IntrinsicIssue
    __builtin_arm_wsrah(); //expect: IntrinsicIssue
    __builtin_arm_wsrahi(); //expect: IntrinsicIssue
    __builtin_arm_wsraw(); //expect: IntrinsicIssue
    __builtin_arm_wsrawi(); //expect: IntrinsicIssue
    __builtin_arm_wsrld(); //expect: IntrinsicIssue
    __builtin_arm_wsrldi(); //expect: IntrinsicIssue
    __builtin_arm_wsrlh(); //expect: IntrinsicIssue
    __builtin_arm_wsrlhi(); //expect: IntrinsicIssue
    __builtin_arm_wsrlw(); //expect: IntrinsicIssue
    __builtin_arm_wsrlwi(); //expect: IntrinsicIssue
    __builtin_arm_wsubb(); //expect: IntrinsicIssue
    __builtin_arm_wsubbss(); //expect: IntrinsicIssue
    __builtin_arm_wsubbus(); //expect: IntrinsicIssue
    __builtin_arm_wsubh(); //expect: IntrinsicIssue
    __builtin_arm_wsubhss(); //expect: IntrinsicIssue
    __builtin_arm_wsubhus(); //expect: IntrinsicIssue
    __builtin_arm_wsubw(); //expect: IntrinsicIssue
    __builtin_arm_wsubwss(); //expect: IntrinsicIssue
    __builtin_arm_wsubwus(); //expect: IntrinsicIssue
    __builtin_arm_wunpckehsb(); //expect: IntrinsicIssue
    __builtin_arm_wunpckehsh(); //expect: IntrinsicIssue
    __builtin_arm_wunpckehsw(); //expect: IntrinsicIssue
    __builtin_arm_wunpckehub(); //expect: IntrinsicIssue
    __builtin_arm_wunpckehuh(); //expect: IntrinsicIssue
    __builtin_arm_wunpckehuw(); //expect: IntrinsicIssue
    __builtin_arm_wunpckelsb(); //expect: IntrinsicIssue
    __builtin_arm_wunpckelsh(); //expect: IntrinsicIssue
    __builtin_arm_wunpckelsw(); //expect: IntrinsicIssue
    __builtin_arm_wunpckelub(); //expect: IntrinsicIssue
    __builtin_arm_wunpckeluh(); //expect: IntrinsicIssue
    __builtin_arm_wunpckeluw(); //expect: IntrinsicIssue
    __builtin_arm_wunpckihb(); //expect: IntrinsicIssue
    __builtin_arm_wunpckihh(); //expect: IntrinsicIssue
    __builtin_arm_wunpckihw(); //expect: IntrinsicIssue
    __builtin_arm_wunpckilb(); //expect: IntrinsicIssue
    __builtin_arm_wunpckilh(); //expect: IntrinsicIssue
    __builtin_arm_wunpckilw(); //expect: IntrinsicIssue
    __builtin_arm_wxor(); //expect: IntrinsicIssue
    __builtin_arm_wzero(); //expect: IntrinsicIssue
    _arm_smlal(); //expect: IntrinsicIssue
    _arm_umlal(); //expect: IntrinsicIssue
    _arm_clz(); //expect: IntrinsicIssue
    _arm_qadd(); //expect: IntrinsicIssue
    _arm_qdadd(); //expect: IntrinsicIssue
    _arm_qdsub(); //expect: IntrinsicIssue
    _arm_qsub(); //expect: IntrinsicIssue
    _arm_smlabb(); //expect: IntrinsicIssue
    _arm_smlabt(); //expect: IntrinsicIssue
    _arm_smlatb(); //expect: IntrinsicIssue
    _arm_smlatt(); //expect: IntrinsicIssue
    _arm_smlalbb(); //expect: IntrinsicIssue
    _arm_smlalbt(); //expect: IntrinsicIssue
    _arm_smlaltb(); //expect: IntrinsicIssue
    _arm_smlaltt(); //expect: IntrinsicIssue
    _arm_smlawb(); //expect: IntrinsicIssue
    _arm_smlawt(); //expect: IntrinsicIssue
    _arm_smulbb(); //expect: IntrinsicIssue
    _arm_smulbt(); //expect: IntrinsicIssue
    _arm_smultb(); //expect: IntrinsicIssue
    _arm_smultt(); //expect: IntrinsicIssue
    _arm_smulwb(); //expect: IntrinsicIssue
    _arm_smulwt(); //expect: IntrinsicIssue
    _arm_sadd16(); //expect: IntrinsicIssue
    _arm_sadd8(); //expect: IntrinsicIssue
    _arm_sasx(); //expect: IntrinsicIssue
    _arm_ssax(); //expect: IntrinsicIssue
    _arm_ssub16(); //expect: IntrinsicIssue
    _arm_ssub8(); //expect: IntrinsicIssue
    _arm_shadd16(); //expect: IntrinsicIssue
    _arm_shadd8(); //expect: IntrinsicIssue
    _arm_shasx(); //expect: IntrinsicIssue
    _arm_shsax(); //expect: IntrinsicIssue
    _arm_shsub16(); //expect: IntrinsicIssue
    _arm_shsub8(); //expect: IntrinsicIssue
    _arm_qadd16(); //expect: IntrinsicIssue
    _arm_qadd8(); //expect: IntrinsicIssue
    _arm_qasx(); //expect: IntrinsicIssue
    _arm_qsax(); //expect: IntrinsicIssue
    _arm_qsub16(); //expect: IntrinsicIssue
    _arm_qsub8(); //expect: IntrinsicIssue
    _arm_uadd16(); //expect: IntrinsicIssue
    _arm_uadd8(); //expect: IntrinsicIssue
    _arm_uasx(); //expect: IntrinsicIssue
    _arm_usax(); //expect: IntrinsicIssue
    _arm_usub16(); //expect: IntrinsicIssue
    _arm_usub8(); //expect: IntrinsicIssue
    _arm_uhadd16(); //expect: IntrinsicIssue
    _arm_uhadd8(); //expect: IntrinsicIssue
    _arm_uhasx(); //expect: IntrinsicIssue
    _arm_uhsax(); //expect: IntrinsicIssue
    _arm_uhsub16(); //expect: IntrinsicIssue
    _arm_uhsub8(); //expect: IntrinsicIssue
    _arm_uqadd16(); //expect: IntrinsicIssue
    _arm_uqadd8(); //expect: IntrinsicIssue
    _arm_uqasx(); //expect: IntrinsicIssue
    _arm_uqsax(); //expect: IntrinsicIssue
    _arm_uqsub16(); //expect: IntrinsicIssue
    _arm_uqsub8(); //expect: IntrinsicIssue
    _arm_sxtab(); //expect: IntrinsicIssue
    _arm_sxtab16(); //expect: IntrinsicIssue
    _arm_sxtah(); //expect: IntrinsicIssue
    _arm_uxtab(); //expect: IntrinsicIssue
    _arm_uxtab16(); //expect: IntrinsicIssue
    _arm_uxtah(); //expect: IntrinsicIssue
    _arm_sxtb(); //expect: IntrinsicIssue
    _arm_sxtb16(); //expect: IntrinsicIssue
    _arm_sxth(); //expect: IntrinsicIssue
    _arm_uxtb(); //expect: IntrinsicIssue
    _arm_uxtb16(); //expect: IntrinsicIssue
    _arm_uxth(); //expect: IntrinsicIssue
    _arm_pkhbt(); //expect: IntrinsicIssue
    _arm_pkhtb(); //expect: IntrinsicIssue
    _arm_usad8(); //expect: IntrinsicIssue
    _arm_usada8(); //expect: IntrinsicIssue
    _arm_ssat(); //expect: IntrinsicIssue
    _arm_usat(); //expect: IntrinsicIssue
    _arm_ssat16(); //expect: IntrinsicIssue
    _arm_usat16(); //expect: IntrinsicIssue
    _arm_rev(); //expect: IntrinsicIssue
    _arm_rev16(); //expect: IntrinsicIssue
    _arm_revsh(); //expect: IntrinsicIssue
    _arm_smlad(); //expect: IntrinsicIssue
    _arm_smladx(); //expect: IntrinsicIssue
    _arm_smlsd(); //expect: IntrinsicIssue
    _arm_smlsdx(); //expect: IntrinsicIssue
    _arm_smmla(); //expect: IntrinsicIssue
    _arm_smmlar(); //expect: IntrinsicIssue
    _arm_smmls(); //expect: IntrinsicIssue
    _arm_smmlsr(); //expect: IntrinsicIssue
    _arm_smmul(); //expect: IntrinsicIssue
    _arm_smmulr(); //expect: IntrinsicIssue
    _arm_smlald(); //expect: IntrinsicIssue
    _arm_smlaldx(); //expect: IntrinsicIssue
    _arm_smlsld(); //expect: IntrinsicIssue
    _arm_smlsldx(); //expect: IntrinsicIssue
    _arm_smuad(); //expect: IntrinsicIssue
    _arm_smuadx(); //expect: IntrinsicIssue
    _arm_smusd(); //expect: IntrinsicIssue
    _arm_smusdx(); //expect: IntrinsicIssue
    _arm_smull(); //expect: IntrinsicIssue
    _arm_umaal(); //expect: IntrinsicIssue
    _arm_bfc(); //expect: IntrinsicIssue
    _arm_bfi(); //expect: IntrinsicIssue
    _arm_rbit(); //expect: IntrinsicIssue
    _arm_sbfx(); //expect: IntrinsicIssue
    _arm_ubfx(); //expect: IntrinsicIssue
    _arm_sdiv(); //expect: IntrinsicIssue
    _arm_udiv(); //expect: IntrinsicIssue
    __cps(); //expect: IntrinsicIssue
    __dmb(); //expect: IntrinsicIssue
    __dsb(); //expect: IntrinsicIssue
    __isb(); //expect: IntrinsicIssue
    __emit(); //expect: IntrinsicIssue
    __hvc(); //expect: IntrinsicIssue
    __iso_volatile_load16(); //expect: IntrinsicIssue
    __iso_volatile_load32(); //expect: IntrinsicIssue
    __iso_volatile_load64(); //expect: IntrinsicIssue
    __iso_volatile_load8(); //expect: IntrinsicIssue
    __iso_volatile_store16(); //expect: IntrinsicIssue
    __iso_volatile_store32(); //expect: IntrinsicIssue
    __iso_volatile_store64(); //expect: IntrinsicIssue
    __iso_volatile_store8(); //expect: IntrinsicIssue
    __ldrexd(); //expect: IntrinsicIssue
    __prefetch(); //expect: IntrinsicIssue
    __rdpmccntr64(); //expect: IntrinsicIssue
    __sev(); //expect: IntrinsicIssue
    __static_assert(); //expect: IntrinsicIssue
    __swi(); //expect: IntrinsicIssue
    __trap(); //expect: IntrinsicIssue
    __wfe(); //expect: IntrinsicIssue
    __wfi(); //expect: IntrinsicIssue
    _AddSatInt(); //expect: IntrinsicIssue
    _CopyDoubleFromInt64(); //expect: IntrinsicIssue
    _CopyFloatFromInt32(); //expect: IntrinsicIssue
    _CopyInt32FromFloat(); //expect: IntrinsicIssue
    _CopyInt64FromDouble(); //expect: IntrinsicIssue
    _CountLeadingOnes(); //expect: IntrinsicIssue
    _CountLeadingOnes64(); //expect: IntrinsicIssue
    _CountLeadingSigns(); //expect: IntrinsicIssue
    _CountLeadingSigns64(); //expect: IntrinsicIssue
    _CountLeadingZeros(); //expect: IntrinsicIssue
    _CountLeadingZeros64(); //expect: IntrinsicIssue
    _CountOneBits(); //expect: IntrinsicIssue
    _CountOneBits64(); //expect: IntrinsicIssue
    _DAddSatInt(); //expect: IntrinsicIssue
    _DSubSatInt(); //expect: IntrinsicIssue
    _isunordered(); //expect: IntrinsicIssue
    _isunorderedf(); //expect: IntrinsicIssue
    _MoveFromCoprocessor(); //expect: IntrinsicIssue
    _MoveFromCoprocessor2(); //expect: IntrinsicIssue
    _MoveFromCoprocessor64(); //expect: IntrinsicIssue
    _MoveToCoprocessor(); //expect: IntrinsicIssue
    _MoveToCoprocessor2(); //expect: IntrinsicIssue
    _MoveToCoprocessor64(); //expect: IntrinsicIssue
    _MulHigh(); //expect: IntrinsicIssue
    _MulUnsignedHigh(); //expect: IntrinsicIssue
    _ReadBankedReg(); //expect: IntrinsicIssue
    _ReadStatusReg(); //expect: IntrinsicIssue
    _SubSatInt(); //expect: IntrinsicIssue
    _WriteBankedReg(); //expect: IntrinsicIssue
    _WriteStatusReg(); //expect: IntrinsicIssue

    __assume(); //expect: IntrinsicIssue
    __code_seg(); //expect: IntrinsicIssue
    __debugbreak(); //expect: IntrinsicIssue
    __fastfail(); //expect: IntrinsicIssue
    __nop(); //expect: IntrinsicIssue
    __yield(); //expect: IntrinsicIssue
    _AddressOfReturnAddress(); //expect: IntrinsicIssue
    _BitScanForward(); //expect: IntrinsicIssue
    _BitScanForward64(); //expect: IntrinsicIssue
    _BitScanReverse(); //expect: IntrinsicIssue
    _BitScanReverse64(); //expect: IntrinsicIssue
    _bittest(); //expect: IntrinsicIssue
    _bittest64(); //expect: IntrinsicIssue
    _bittestandcomplement(); //expect: IntrinsicIssue
    _bittestandreset(); //expect: IntrinsicIssue
    _bittestandset(); //expect: IntrinsicIssue
    _byteswap_uint64(); //expect: IntrinsicIssue
    _byteswap_ulong(); //expect: IntrinsicIssue
    _byteswap_ushort(); //expect: IntrinsicIssue
    _disable(); //expect: IntrinsicIssue
    _enable(); //expect: IntrinsicIssue
    _lrotl(); //expect: IntrinsicIssue
    _lrotr(); //expect: IntrinsicIssue
    _ReadBarrier(); //expect: IntrinsicIssue
    _ReadWriteBarrier(); //expect: IntrinsicIssue
    _ReturnAddress(); //expect: IntrinsicIssue
    _rotl(); //expect: IntrinsicIssue
    _rotl16(); //expect: IntrinsicIssue
    _rotl64(); //expect: IntrinsicIssue
    _rotl8(); //expect: IntrinsicIssue
    _rotr(); //expect: IntrinsicIssue
    _rotr16(); //expect: IntrinsicIssue
    _rotr64(); //expect: IntrinsicIssue
    _rotr8(); //expect: IntrinsicIssue
    _setjmpex(); //expect: IntrinsicIssue
    _WriteBarrier(); //expect: IntrinsicIssue

    _InterlockedAdd(); //expect: IntrinsicIssue
    _InterlockedAdd64(); //expect: IntrinsicIssue
    _InterlockedAdd64_acq(); //expect: IntrinsicIssue
    _InterlockedAdd64_nf(); //expect: IntrinsicIssue
    _InterlockedAdd64_rel(); //expect: IntrinsicIssue
    _InterlockedAdd_acq(); //expect: IntrinsicIssue
    _InterlockedAdd_nf(); //expect: IntrinsicIssue
    _InterlockedAdd_rel(); //expect: IntrinsicIssue
    _InterlockedAnd(); //expect: IntrinsicIssue
    _InterlockedAnd16(); //expect: IntrinsicIssue
    _InterlockedAnd16_acq(); //expect: IntrinsicIssue
    _InterlockedAnd16_nf(); //expect: IntrinsicIssue
    _InterlockedAnd16_rel(); //expect: IntrinsicIssue
    _InterlockedAnd64(); //expect: IntrinsicIssue
    _InterlockedAnd64_acq(); //expect: IntrinsicIssue
    _InterlockedAnd64_nf(); //expect: IntrinsicIssue
    _InterlockedAnd64_rel(); //expect: IntrinsicIssue
    _InterlockedAnd8(); //expect: IntrinsicIssue
    _InterlockedAnd8_acq(); //expect: IntrinsicIssue
    _InterlockedAnd8_nf(); //expect: IntrinsicIssue
    _InterlockedAnd8_rel(); //expect: IntrinsicIssue
    _InterlockedAnd_acq(); //expect: IntrinsicIssue
    _InterlockedAnd_nf(); //expect: IntrinsicIssue
    _InterlockedAnd_rel(); //expect: IntrinsicIssue
    _InterlockedCompareExchange(); //expect: IntrinsicIssue
    _InterlockedCompareExchange16(); //expect: IntrinsicIssue
    _InterlockedCompareExchange16_acq(); //expect: IntrinsicIssue
    _InterlockedCompareExchange16_nf(); //expect: IntrinsicIssue
    _InterlockedCompareExchange16_rel(); //expect: IntrinsicIssue
    _InterlockedCompareExchange64(); //expect: IntrinsicIssue
    _InterlockedCompareExchange64_acq(); //expect: IntrinsicIssue
    _InterlockedCompareExchange64_nf(); //expect: IntrinsicIssue
    _InterlockedCompareExchange64_rel(); //expect: IntrinsicIssue
    _InterlockedCompareExchange8(); //expect: IntrinsicIssue
    _InterlockedCompareExchange8_acq(); //expect: IntrinsicIssue
    _InterlockedCompareExchange8_nf(); //expect: IntrinsicIssue
    _InterlockedCompareExchange8_rel(); //expect: IntrinsicIssue
    _InterlockedCompareExchangePointer(); //expect: IntrinsicIssue
    _InterlockedCompareExchangePointer_acq(); //expect: IntrinsicIssue
    _InterlockedCompareExchangePointer_nf(); //expect: IntrinsicIssue
    _InterlockedCompareExchangePointer_rel(); //expect: IntrinsicIssue
    _InterlockedCompareExchange_acq(); //expect: IntrinsicIssue
    _InterlockedCompareExchange_nf(); //expect: IntrinsicIssue
    _InterlockedCompareExchange_rel(); //expect: IntrinsicIssue
    _InterlockedDecrement(); //expect: IntrinsicIssue
    _InterlockedDecrement16(); //expect: IntrinsicIssue
    _InterlockedDecrement16_acq(); //expect: IntrinsicIssue
    _InterlockedDecrement16_nf(); //expect: IntrinsicIssue
    _InterlockedDecrement16_rel(); //expect: IntrinsicIssue
    _InterlockedDecrement64(); //expect: IntrinsicIssue
    _InterlockedDecrement64_acq(); //expect: IntrinsicIssue
    _InterlockedDecrement64_nf(); //expect: IntrinsicIssue
    _InterlockedDecrement64_rel(); //expect: IntrinsicIssue
    _InterlockedDecrement_acq(); //expect: IntrinsicIssue
    _InterlockedDecrement_nf(); //expect: IntrinsicIssue
    _InterlockedDecrement_rel(); //expect: IntrinsicIssue
    _InterlockedExchange(); //expect: IntrinsicIssue
    _InterlockedExchange16(); //expect: IntrinsicIssue
    _InterlockedExchange16_acq(); //expect: IntrinsicIssue
    _InterlockedExchange16_nf(); //expect: IntrinsicIssue
    _InterlockedExchange64(); //expect: IntrinsicIssue
    _InterlockedExchange64_acq(); //expect: IntrinsicIssue
    _InterlockedExchange64_nf(); //expect: IntrinsicIssue
    _InterlockedExchange8(); //expect: IntrinsicIssue
    _InterlockedExchange8_acq(); //expect: IntrinsicIssue
    _InterlockedExchange8_nf(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd16(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd16_acq(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd16_nf(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd16_rel(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd64(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd64_acq(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd64_nf(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd64_rel(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd8(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd8_acq(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd8_nf(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd8_rel(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd_acq(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd_nf(); //expect: IntrinsicIssue
    _InterlockedExchangeAdd_rel(); //expect: IntrinsicIssue
    _InterlockedExchangePointer(); //expect: IntrinsicIssue
    _InterlockedExchangePointer_acq(); //expect: IntrinsicIssue
    _InterlockedExchangePointer_nf(); //expect: IntrinsicIssue
    _InterlockedExchange_acq(); //expect: IntrinsicIssue
    _InterlockedExchange_nf(); //expect: IntrinsicIssue
    _InterlockedIncrement(); //expect: IntrinsicIssue
    _InterlockedIncrement16(); //expect: IntrinsicIssue
    _InterlockedIncrement16_acq(); //expect: IntrinsicIssue
    _InterlockedIncrement16_nf(); //expect: IntrinsicIssue
    _InterlockedIncrement16_rel(); //expect: IntrinsicIssue
    _InterlockedIncrement64(); //expect: IntrinsicIssue
    _InterlockedIncrement64_acq(); //expect: IntrinsicIssue
    _InterlockedIncrement64_nf(); //expect: IntrinsicIssue
    _InterlockedIncrement64_rel(); //expect: IntrinsicIssue
    _InterlockedIncrement_acq(); //expect: IntrinsicIssue
    _InterlockedIncrement_nf(); //expect: IntrinsicIssue
    _InterlockedIncrement_rel(); //expect: IntrinsicIssue
    _InterlockedOr(); //expect: IntrinsicIssue
    _InterlockedOr16(); //expect: IntrinsicIssue
    _InterlockedOr16_acq(); //expect: IntrinsicIssue
    _InterlockedOr16_nf(); //expect: IntrinsicIssue
    _InterlockedOr16_rel(); //expect: IntrinsicIssue
    _InterlockedOr64(); //expect: IntrinsicIssue
    _InterlockedOr64_acq(); //expect: IntrinsicIssue
    _InterlockedOr64_nf(); //expect: IntrinsicIssue
    _InterlockedOr64_rel(); //expect: IntrinsicIssue
    _InterlockedOr8(); //expect: IntrinsicIssue
    _InterlockedOr8_acq(); //expect: IntrinsicIssue
    _InterlockedOr8_nf(); //expect: IntrinsicIssue
    _InterlockedOr8_rel(); //expect: IntrinsicIssue
    _InterlockedOr_acq(); //expect: IntrinsicIssue
    _InterlockedOr_nf(); //expect: IntrinsicIssue
    _InterlockedOr_rel(); //expect: IntrinsicIssue
    _InterlockedXor(); //expect: IntrinsicIssue
    _InterlockedXor16(); //expect: IntrinsicIssue
    _InterlockedXor16_acq(); //expect: IntrinsicIssue
    _InterlockedXor16_nf(); //expect: IntrinsicIssue
    _InterlockedXor16_rel(); //expect: IntrinsicIssue
    _InterlockedXor64(); //expect: IntrinsicIssue
    _InterlockedXor64_acq(); //expect: IntrinsicIssue
    _InterlockedXor64_nf(); //expect: IntrinsicIssue
    _InterlockedXor64_rel(); //expect: IntrinsicIssue
    _InterlockedXor8(); //expect: IntrinsicIssue
    _InterlockedXor8_acq(); //expect: IntrinsicIssue
    _InterlockedXor8_nf(); //expect: IntrinsicIssue
    _InterlockedXor8_rel(); //expect: IntrinsicIssue
    _InterlockedXor_acq(); //expect: IntrinsicIssue
    _InterlockedXor_nf(); //expect: IntrinsicIssue
    _InterlockedXor_rel(); //expect: IntrinsicIssue
    _interlockedbittestandreset(); //expect: IntrinsicIssue
    _interlockedbittestandreset_acq(); //expect: IntrinsicIssue
    _interlockedbittestandreset_nf(); //expect: IntrinsicIssue
    _interlockedbittestandreset_rel(); //expect: IntrinsicIssue
    _interlockedbittestandset(); //expect: IntrinsicIssue
    _interlockedbittestandset_acq(); //expect: IntrinsicIssue
    _interlockedbittestandset_nf(); //expect: IntrinsicIssue
    _interlockedbittestandset_rel(); //expect: IntrinsicIssue
}

// shall generate issue in aarch64.
void x86_intrinsic_test()
{
    _mm_srli_epi64(); //expect: IntrinsicIssue 
    _mm_shuffle_epi8(); //expect: IntrinsicIssue 
    _mm_extract_ps(); //expect: IntrinsicIssue 
    _mm_set1_epi64x(); //expect: IntrinsicIssue 
    _mm_mul_epu32(); //expect: IntrinsicIssue 
    _mm_add_epi64(); //expect: IntrinsicIssue 

    _InterlockedAnd8_np(); //expect: IntrinsicIssue 
    _InterlockedOr8_np(); //expect: IntrinsicIssue 
    _InterlockedXor8_np(); //expect: IntrinsicIssue 

    __builtin_ia32_pand(); //expect: IntrinsicIssue 
    __builtin_ia32_pandn(); //expect: IntrinsicIssue 
    __builtin_ia32_por(); //expect: IntrinsicIssue 
    __builtin_ia32_pxor(); //expect: IntrinsicIssue 

    _mm_cvtsd_f64(); //expect: IntrinsicIssue 
    __builtin_copysignq(); //expect: IntrinsicIssue 
    __builtin_huge_valq(); //expect: IntrinsicIssue 
    __builtin_infq(); //expect: IntrinsicIssue 
    __builtin_fabsq(); //expect: IntrinsicIssue 
    __builtin_ia32_vec_ext_v4sf(); //expect: IntrinsicIssue 
    _mm_cvtss_f32(); //expect: IntrinsicIssue 
    _m_to_float(); //expect: IntrinsicIssue 
    _div128(); //expect: IntrinsicIssue 
    _InterlockedAnd64_HLEAcquire(); //expect: IntrinsicIssue   
    _InterlockedAnd64_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedAnd64_np(); //expect: IntrinsicIssue 
    _InterlockedCompareExchange64_HLEAcquire(); //expect: IntrinsicIssue 
    _InterlockedCompareExchange64_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedCompareExchange64_np(); //expect: IntrinsicIssue 
    _InterlockedExchange64_HLEAcquire(); //expect: IntrinsicIssue 
    _InterlockedExchange64_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedExchangeAdd64_HLEAcquire(); //expect: IntrinsicIssue 
    _InterlockedExchangeAdd64_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedOr64_HLEAcquire(); //expect: IntrinsicIssue 
    _InterlockedOr64_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedOr64_np(); //expect: IntrinsicIssue 
    _InterlockedXor64_HLEAcquire(); //expect: IntrinsicIssue 
    _InterlockedXor64_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedXor64_np(); //expect: IntrinsicIssue 
    _loadbe_i64(); //expect: IntrinsicIssue 
    _mm_cvtsd_si64(); //expect: IntrinsicIssue 
    _mm_cvtsd_si64x(); //expect: IntrinsicIssue 
    _mm_cvtsi128_si64(); //expect: IntrinsicIssue 
    _mm_cvtsi128_si64x(); //expect: IntrinsicIssue 
    _mm_cvtss_si64(); //expect: IntrinsicIssue 
    _mm_cvtss_si64x(); //expect: IntrinsicIssue 
    _mm_cvttsd_si64(); //expect: IntrinsicIssue 
    _mm_cvttsd_si64x(); //expect: IntrinsicIssue 
    _mm_cvttss_si64(); //expect: IntrinsicIssue 
    _mm_cvttss_si64x(); //expect: IntrinsicIssue 
    _mm_extract_epi64(); //expect: IntrinsicIssue 
    _mm_popcnt_u64(); //expect: IntrinsicIssue 
    _mul128(); //expect: IntrinsicIssue 
    __mulh(); //expect: IntrinsicIssue 
    __emul(); //expect: IntrinsicIssue 
    __ll_rshift(); //expect: IntrinsicIssue 
    _sarx_i64(); //expect: IntrinsicIssue 
    __builtin_cpu_is(); //expect: IntrinsicIssue 
    __builtin_cpu_supports(); //expect: IntrinsicIssue  
    __builtin_ia32_comieq(); //expect: IntrinsicIssue 
    __builtin_ia32_comige(); //expect: IntrinsicIssue 
    __builtin_ia32_comigt(); //expect: IntrinsicIssue 
    __builtin_ia32_comile(); //expect: IntrinsicIssue 
    __builtin_ia32_comilt(); //expect: IntrinsicIssue 
    __builtin_ia32_comineq(); //expect: IntrinsicIssue 
    __builtin_ia32_comisdeq(); //expect: IntrinsicIssue 
    __builtin_ia32_comisdge(); //expect: IntrinsicIssue 
    __builtin_ia32_comisdgt(); //expect: IntrinsicIssue 
    __builtin_ia32_comisdle(); //expect: IntrinsicIssue 
    __builtin_ia32_comisdlt(); //expect: IntrinsicIssue 
    __builtin_ia32_comisdneq(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtsd2si(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtss2si(); //expect: IntrinsicIssue 
    __builtin_ia32_cvttsd2si(); //expect: IntrinsicIssue 
    __builtin_ia32_cvttss2si(); //expect: IntrinsicIssue 
    __builtin_ia32_movmskpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_movmskpd(); //expect: IntrinsicIssue 
    __builtin_ia32_movmskps256(); //expect: IntrinsicIssue 
    __builtin_ia32_movmskps(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpestri128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpestria128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpestric128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpestrio128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpestris128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpestriz128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpistri128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpistria128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpistric128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpistrio128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpistris128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpistriz128(); //expect: IntrinsicIssue 
    __builtin_ia32_pextrw(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovmskb128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovmskb256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovmskb(); //expect: IntrinsicIssue 
    __builtin_ia32_ptestc128(); //expect: IntrinsicIssue 
    __builtin_ia32_ptestc256(); //expect: IntrinsicIssue 
    __builtin_ia32_ptestnzc128(); //expect: IntrinsicIssue 
    __builtin_ia32_ptestnzc256(); //expect: IntrinsicIssue 
    __builtin_ia32_ptestz128(); //expect: IntrinsicIssue 
    __builtin_ia32_ptestz256(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomieq(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomige(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomigt(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomile(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomilt(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomineq(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomisdeq(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomisdge(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomisdgt(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomisdle(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomisdlt(); //expect: IntrinsicIssue 
    __builtin_ia32_ucomisdneq(); //expect: IntrinsicIssue 
    __builtin_ia32_vec_ext_v16qi(); //expect: IntrinsicIssue 
    __builtin_ia32_vec_ext_v4si(); //expect: IntrinsicIssue  
    __builtin_ia32_vtestcpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vtestcpd(); //expect: IntrinsicIssue 
    __builtin_ia32_vtestcps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vtestcps(); //expect: IntrinsicIssue 
    __builtin_ia32_vtestnzcpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vtestnzcpd(); //expect: IntrinsicIssue  
    __builtin_ia32_vtestnzcps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vtestnzcps(); //expect: IntrinsicIssue 
    __builtin_ia32_vtestzpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vtestzpd(); //expect: IntrinsicIssue  
    __builtin_ia32_vtestzps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vtestzps(); //expect: IntrinsicIssue 
    __builtin_ia32_xbegin(); //expect: IntrinsicIssue 
    __builtin_ia32_xtest(); //expect: IntrinsicIssue 
    _div64(); //expect: IntrinsicIssue 
    _loadbe_i32(); //expect: IntrinsicIssue  
    _mm256_movemask_epi8(); //expect: IntrinsicIssue 
    _mm256_movemask_pd(); //expect: IntrinsicIssue 
    _mm256_movemask_ps(); //expect: IntrinsicIssue 
    _mm256_testc_pd(); //expect: IntrinsicIssue 
    _mm256_testc_ps(); //expect: IntrinsicIssue 
    _mm256_testc_si256(); //expect: IntrinsicIssue 
    _mm256_testnzc_pd(); //expect: IntrinsicIssue 
    _mm256_testnzc_ps(); //expect: IntrinsicIssue 
    _mm256_testnzc_si256(); //expect: IntrinsicIssue 
    _mm256_testz_pd(); //expect: IntrinsicIssue 
    _mm256_testz_ps(); //expect: IntrinsicIssue 
    _mm256_testz_si256(); //expect: IntrinsicIssue 
    _mm_cmpestra(); //expect: IntrinsicIssue 
    _mm_cmpestrc(); //expect: IntrinsicIssue 
    _mm_cmpestri(); //expect: IntrinsicIssue 
    _mm_cmpestro(); //expect: IntrinsicIssue 
    _mm_cmpestrs(); //expect: IntrinsicIssue 
    _mm_cmpestrz(); //expect: IntrinsicIssue 
    _mm_cmpistra(); //expect: IntrinsicIssue 
    _mm_cmpistrc(); //expect: IntrinsicIssue 
    _mm_cmpistri(); //expect: IntrinsicIssue 
    _mm_cmpistro(); //expect: IntrinsicIssue 
    _mm_cmpistrs(); //expect: IntrinsicIssue 
    _mm_cmpistrz(); //expect: IntrinsicIssue 
    _mm_comieq_sd(); //expect: IntrinsicIssue 
    _mm_comieq_ss(); //expect: IntrinsicIssue 
    _mm_comige_sd(); //expect: IntrinsicIssue 
    _mm_comige_ss(); //expect: IntrinsicIssue 
    _mm_comigt_sd(); //expect: IntrinsicIssue 
    _mm_comigt_ss(); //expect: IntrinsicIssue 
    _mm_comile_sd(); //expect: IntrinsicIssue 
    _mm_comile_ss(); //expect: IntrinsicIssue 
    _mm_comilt_sd(); //expect: IntrinsicIssue 
    _mm_comilt_ss(); //expect: IntrinsicIssue 
    _mm_comineq_sd(); //expect: IntrinsicIssue 
    _mm_comineq_ss(); //expect: IntrinsicIssue 
    _mm_cvtsd_si32(); //expect: IntrinsicIssue 
    _mm_cvtsi128_si32(); //expect: IntrinsicIssue 
    _mm_cvt_ss2si(); //expect: IntrinsicIssue 
    _mm_cvttsd_si32(); //expect: IntrinsicIssue 
    _mm_cvtt_ss2si(); //expect: IntrinsicIssue 
    _mm_extract_epi16(); //expect: IntrinsicIssue 
    _mm_extract_epi32(); //expect: IntrinsicIssue 
    _mm_extract_epi8(); //expect: IntrinsicIssue 
    _mm_extract_ps(); //expect: IntrinsicIssue 
    _mm_movemask_epi8(); //expect: IntrinsicIssue 
    _mm_movemask_pd(); //expect: IntrinsicIssue 
    _mm_movemask_ps(); //expect: IntrinsicIssue 
    _mm_popcnt_u32(); //expect: IntrinsicIssue
    _mm_testc_pd(); //expect: IntrinsicIssue 
    _mm_testc_ps(); //expect: IntrinsicIssue 
    _mm_testc_si128(); //expect: IntrinsicIssue 
    _mm_testnzc_pd(); //expect: IntrinsicIssue 
    _mm_testnzc_ps(); //expect: IntrinsicIssue  
    _mm_testnzc_si128(); //expect: IntrinsicIssue 
    _mm_testz_pd(); //expect: IntrinsicIssue 
    _mm_testz_ps(); //expect: IntrinsicIssue 
    _mm_testz_si128(); //expect: IntrinsicIssue 
    _mm_ucomieq_sd(); //expect: IntrinsicIssue 
    _mm_ucomieq_ss(); //expect: IntrinsicIssue 
    _mm_ucomige_sd(); //expect: IntrinsicIssue 
    _mm_ucomige_ss(); //expect: IntrinsicIssue 
    _mm_ucomigt_sd(); //expect: IntrinsicIssue 
    _mm_ucomigt_ss(); //expect: IntrinsicIssue 
    _mm_ucomile_sd(); //expect: IntrinsicIssue 
    _mm_ucomile_ss(); //expect: IntrinsicIssue 
    _mm_ucomilt_sd(); //expect: IntrinsicIssue 
    _mm_ucomilt_ss(); //expect: IntrinsicIssue 
    _mm_ucomineq_sd(); //expect: IntrinsicIssue 
    _mm_ucomineq_ss(); //expect: IntrinsicIssue 
    _m_pextrw(); //expect: IntrinsicIssue 
    _m_pmovmskb(); //expect: IntrinsicIssue 
    _m_to_int(); //expect: IntrinsicIssue 
    _rdrand16_step(); //expect: IntrinsicIssue 
    _rdrand32_step(); //expect: IntrinsicIssue 
    _rdrand64_step(); //expect: IntrinsicIssue 
    _rdseed16_step(); //expect: IntrinsicIssue 
    _rdseed32_step(); //expect: IntrinsicIssue 
    _rdseed64_step(); //expect: IntrinsicIssue 
    _sarx_i32(); //expect: IntrinsicIssue
    _InterlockedAddLargeStatistic(); //expect: IntrinsicIssue 
    _InterlockedAnd_HLEAcquire(); //expect: IntrinsicIssue 
    _InterlockedAnd_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedAnd_np(); //expect: IntrinsicIssue 
    _InterlockedCompareExchange_HLEAcquire(); //expect: IntrinsicIssue 
    _InterlockedCompareExchange_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedCompareExchange_np(); //expect: IntrinsicIssue 
    _InterlockedExchangeAdd_HLEAcquire(); //expect: IntrinsicIssue 
    _InterlockedExchangeAdd_HLERelease(); //expect: IntrinsicIssue  
    _InterlockedExchange_HLEAcquire(); //expect: IntrinsicIssue 
    _InterlockedExchange_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedOr_HLEAcquire(); //expect: IntrinsicIssue
    _InterlockedOr_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedOr_np(); //expect: IntrinsicIssue 
    _InterlockedXor_HLEAcquire(); //expect: IntrinsicIssue  
    _InterlockedXor_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedXor_np(); //expect: IntrinsicIssue  
    __builtin_ia32_cvtsd2si64(); //expect: IntrinsicIssue 
    __builtin_ia32_cvttsd2si64(); //expect: IntrinsicIssue 
    __builtin_ia32_vec_ext_v2di(); //expect: IntrinsicIssue 
    _mm256_castpd256_pd128(); //expect: IntrinsicIssue 
    _mm256_extractf128_pd(); //expect: IntrinsicIssue 
    _mm_add_pd(); //expect: IntrinsicIssue 
    _mm_add_sd(); //expect: IntrinsicIssue 
    _mm_addsub_pd(); //expect: IntrinsicIssue 
    _mm_andnot_pd(); //expect: IntrinsicIssue 
    _mm_and_pd(); //expect: IntrinsicIssue 
    _mm_blend_pd(); //expect: IntrinsicIssue 
    _mm_blendv_pd(); //expect: IntrinsicIssue 
    _mm_broadcastsd_pd(); //expect: IntrinsicIssue 
    _mm_castps_pd(); //expect: IntrinsicIssue 
    _mm_castsi128_pd(); //expect: IntrinsicIssue 
    _mm_cmpeq_pd(); //expect: IntrinsicIssue 
    _mm_cmpeq_sd(); //expect: IntrinsicIssue 
    _mm_cmpge_pd(); //expect: IntrinsicIssue 
    _mm_cmpge_sd(); //expect: IntrinsicIssue 
    _mm_cmpgt_pd(); //expect: IntrinsicIssue 
    _mm_cmpgt_sd(); //expect: IntrinsicIssue 
    _mm_cmple_pd(); //expect: IntrinsicIssue 
    _mm_cmple_sd(); //expect: IntrinsicIssue 
    _mm_cmplt_pd(); //expect: IntrinsicIssue 
    _mm_cmplt_sd(); //expect: IntrinsicIssue 
    _mm_cmpneq_pd(); //expect: IntrinsicIssue  
    _mm_cmpneq_sd(); //expect: IntrinsicIssue 
    _mm_cmpnge_pd(); //expect: IntrinsicIssue 
    _mm_cmpnge_sd(); //expect: IntrinsicIssue 
    _mm_cmpngt_pd(); //expect: IntrinsicIssue 
    _mm_cmpngt_sd(); //expect: IntrinsicIssue 
    _mm_cmpnle_pd(); //expect: IntrinsicIssue 
    _mm_cmpnle_sd(); //expect: IntrinsicIssue 
    _mm_cmpnlt_pd(); //expect: IntrinsicIssue 
    _mm_cmpnlt_sd(); //expect: IntrinsicIssue 
    _mm_cmpord_pd(); //expect: IntrinsicIssue 
    _mm_cmpord_sd(); //expect: IntrinsicIssue 
    _mm_cmp_pd(); //expect: IntrinsicIssue 
    _mm_cmp_sd(); //expect: IntrinsicIssue 
    _mm_cmpunord_pd(); //expect: IntrinsicIssue 
    _mm_cmpunord_sd(); //expect: IntrinsicIssue 
    _mm_cvtepi32_pd(); //expect: IntrinsicIssue 
    _mm_cvtpi32_pd(); //expect: IntrinsicIssue 
    _mm_cvtps_pd(); //expect: IntrinsicIssue 
    _mm_cvtsi32_sd(); //expect: IntrinsicIssue 
    _mm_cvtsi64_sd(); //expect: IntrinsicIssue 
    _mm_cvtsi64x_sd(); //expect: IntrinsicIssue 
    _mm_cvtss_sd(); //expect: IntrinsicIssue 
    _mm_div_pd(); //expect: IntrinsicIssue 
    _mm_div_sd(); //expect: IntrinsicIssue 
    _mm_dp_pd(); //expect: IntrinsicIssue 
    _mm_fmadd_pd(); //expect: IntrinsicIssue 
    _mm_fmadd_sd(); //expect: IntrinsicIssue 
    _mm_fmaddsub_pd(); //expect: IntrinsicIssue 
    _mm_fmsubadd_pd(); //expect: IntrinsicIssue 
    _mm_fmsub_pd(); //expect: IntrinsicIssue 
    _mm_fmsub_sd(); //expect: IntrinsicIssue 
    _mm_fnmadd_pd(); //expect: IntrinsicIssue 
    _mm_fnmadd_sd(); //expect: IntrinsicIssue 
    _mm_fnmsub_pd(); //expect: IntrinsicIssue 
    _mm_fnmsub_sd(); //expect: IntrinsicIssue 
    _mm_frcz_pd(); //expect: IntrinsicIssue  
    _mm_frcz_sd(); //expect: IntrinsicIssue 
    _mm_hadd_pd(); //expect: IntrinsicIssue  
    _mm_hsub_pd(); //expect: IntrinsicIssue 
    _mm_i32gather_pd(); //expect: IntrinsicIssue 
    _mm_i64gather_pd(); //expect: IntrinsicIssue 
    _mm_load1_pd(); //expect: IntrinsicIssue 
    _mm_loaddup_pd(); //expect: IntrinsicIssue 
    _mm_loadh_pd(); //expect: IntrinsicIssue 
    _mm_loadl_pd(); //expect: IntrinsicIssue 
    _mm_load_pd(); //expect: IntrinsicIssue 
    _mm_loadr_pd(); //expect: IntrinsicIssue 
    _mm_load_sd(); //expect: IntrinsicIssue  
    _mm_loadu_pd(); //expect: IntrinsicIssue  
    _mm_macc_pd(); //expect: IntrinsicIssue  
    _mm_macc_sd(); //expect: IntrinsicIssue  
    _mm_macc_sd(); //expect: IntrinsicIssue  
    _mm_maddsub_pd(); //expect: IntrinsicIssue  
    _mm_mask_i32gather_pd(); //expect: IntrinsicIssue  
    _mm_mask_i64gather_pd(); //expect: IntrinsicIssue  
    _mm_maskload_pd(); //expect: IntrinsicIssue  
    _mm_max_pd(); //expect: IntrinsicIssue  
    _mm_max_sd(); //expect: IntrinsicIssue   
    _mm_min_pd(); //expect: IntrinsicIssue  
    _mm_min_sd(); //expect: IntrinsicIssue  
    _mm_movedup_pd(); //expect: IntrinsicIssue  
    _mm_move_sd(); //expect: IntrinsicIssue  
    _mm_msubadd_pd(); //expect: IntrinsicIssue  
    _mm_msub_pd(); //expect: IntrinsicIssue  
    _mm_msub_sd(); //expect: IntrinsicIssue  
    _mm_mul_pd(); //expect: IntrinsicIssue  
    _mm_mul_sd(); //expect: IntrinsicIssue  
    _mm_nmacc_pd(); //expect: IntrinsicIssue 
    _mm_nmacc_sd(); //expect: IntrinsicIssue  
    _mm_nmsub_pd(); //expect: IntrinsicIssue  
    _mm_nmsub_sd(); //expect: IntrinsicIssue 
    _mm_or_pd(); //expect: IntrinsicIssue  
    _mm_permute2_pd(); //expect: IntrinsicIssue  
    _mm_permute_pd(); //expect: IntrinsicIssue  
    _mm_permutevar_pd(); //expect: IntrinsicIssue  
    _mm_round_pd(); //expect: IntrinsicIssue  
    _mm_round_sd(); //expect: IntrinsicIssue  
    _mm_set1_pd(); //expect: IntrinsicIssue  
    _mm_set_pd(); //expect: IntrinsicIssue  
    _mm_setr_pd(); //expect: IntrinsicIssue  
    _mm_set_sd(); //expect: IntrinsicIssue  
    _mm_setzero_pd(); //expect: IntrinsicIssue  
    _mm_shuffle_pd(); //expect: IntrinsicIssue  
    _mm_sqrt_pd(); //expect: IntrinsicIssue  
    _mm_sqrt_sd(); //expect: IntrinsicIssue  
    _mm_sub_pd(); //expect: IntrinsicIssue  
    _mm_sub_sd(); //expect: IntrinsicIssue  
    _mm_unpackhi_pd(); //expect: IntrinsicIssue  
    _mm_unpacklo_pd(); //expect: IntrinsicIssue  
    _mm_xor_pd(); //expect: IntrinsicIssue  
    _mm256_castsi256_si128(); //expect: IntrinsicIssue  
    _mm256_cvtpd_epi32(); //expect: IntrinsicIssue  
    _mm256_cvtps_ph(); //expect: IntrinsicIssue  
    _mm256_cvttpd_epi32(); //expect: IntrinsicIssue  
    _mm256_extractf128_si256(); //expect: IntrinsicIssue  
    _mm256_extracti128_si256(); //expect: IntrinsicIssue  
    _mm256_mask_i64gather_epi32(); //expect: IntrinsicIssue  
     _mm_abs_epi16(); //expect: IntrinsicIssue  
    _mm_abs_epi32(); //expect: IntrinsicIssue  
    _mm_abs_epi8(); //expect: IntrinsicIssue  
    _mm_add_epi16(); //expect: IntrinsicIssue  
    _mm_add_epi32(); //expect: IntrinsicIssue  
    _mm_add_epi64(); //expect: IntrinsicIssue   
    _mm_add_epi8(); //expect: IntrinsicIssue  
    _mm_adds_epi16(); //expect: IntrinsicIssue  
    _mm_adds_epi8(); //expect: IntrinsicIssue  
    _mm_adds_epu16(); //expect: IntrinsicIssue  
    _mm_adds_epu8(); //expect: IntrinsicIssue  
    _mm_aesdeclast_si128(); //expect: IntrinsicIssue  
    _mm_aesdec_si128(); //expect: IntrinsicIssue  
    _mm_aesenclast_si128(); //expect: IntrinsicIssue  
    _mm_aesenc_si128(); //expect: IntrinsicIssue  
    _mm_aesimc_si128(); //expect: IntrinsicIssue  
    _mm_aeskeygenassist_si128(); //expect: IntrinsicIssue  
    _mm_alignr_epi8(); //expect: IntrinsicIssue  
    _mm_andnot_si128(); //expect: IntrinsicIssue  
    _mm_andnot_si128(); //expect: IntrinsicIssue  
    _mm_and_si128(); //expect: IntrinsicIssue  
    _mm_avg_epu16(); //expect: IntrinsicIssue  
    _mm_avg_epu8(); //expect: IntrinsicIssue  
    _mm_blend_epi16(); //expect: IntrinsicIssue   
    _mm_blend_epi32(); //expect: IntrinsicIssue  
    _mm_blendv_epi8(); //expect: IntrinsicIssue  
    _mm_broadcastb_epi8(); //expect: IntrinsicIssue  
    _mm_broadcastd_epi32(); //expect: IntrinsicIssue  
    _mm_broadcastq_epi64(); //expect: IntrinsicIssue  
    _mm_broadcastw_epi16(); //expect: IntrinsicIssue  
    _mm_castpd_si128(); //expect: IntrinsicIssue  
    _mm_castps_si128(); //expect: IntrinsicIssue  
    _mm_clmulepi64_si128(); //expect: IntrinsicIssue  
    _mm_cmov_si128(); //expect: IntrinsicIssue  
    _mm_cmpeq_epi16(); //expect: IntrinsicIssue  
    _mm_cmpeq_epi32(); //expect: IntrinsicIssue  
    _mm_cmpeq_epi64(); //expect: IntrinsicIssue   
    _mm_cmpeq_epi8(); //expect: IntrinsicIssue  
    _mm_cmpestrm(); //expect: IntrinsicIssue   
    _mm_cmpgt_epi16(); //expect: IntrinsicIssue  
    _mm_cmpgt_epi32(); //expect: IntrinsicIssue  
    _mm_cmpgt_epi64(); //expect: IntrinsicIssue  
    _mm_cmpgt_epi8(); //expect: IntrinsicIssue  
    _mm_cmpistrm(); //expect: IntrinsicIssue  
    _mm_cmplt_epi16(); //expect: IntrinsicIssue  
    _mm_cmplt_epi32(); //expect: IntrinsicIssue  
    _mm_cmplt_epi8(); //expect: IntrinsicIssue  
    _mm_com_epi16(); //expect: IntrinsicIssue  
    _mm_com_epi32(); //expect: IntrinsicIssue 
    _mm_com_epi64(); //expect: IntrinsicIssue  
    _mm_com_epi8(); //expect: IntrinsicIssue  
    _mm_com_epu16(); //expect: IntrinsicIssue  
    _mm_com_epu32(); //expect: IntrinsicIssue  
    _mm_com_epu64(); //expect: IntrinsicIssue  
    _mm_com_epu8(); //expect: IntrinsicIssue 
    _mm_cvtepi16_epi32(); //expect: IntrinsicIssue  
    _mm_cvtepi16_epi64(); //expect: IntrinsicIssue  
    _mm_cvtepi32_epi64(); //expect: IntrinsicIssue  
    _mm_cvtepi8_epi16(); //expect: IntrinsicIssue  
    _mm_cvtepi8_epi32(); //expect: IntrinsicIssue 
    _mm_cvtepi8_epi64(); //expect: IntrinsicIssue  
    _mm_cvtepu16_epi32(); //expect: IntrinsicIssue  
    _mm_cvtepu16_epi64(); //expect: IntrinsicIssue  
    _mm_cvtepu32_epi64(); //expect: IntrinsicIssue  
    _mm_cvtepu8_epi16(); //expect: IntrinsicIssue  
    _mm_cvtepu8_epi32(); //expect: IntrinsicIssue  
    _mm_cvtepu8_epi64(); //expect: IntrinsicIssue  
    _mm_cvtpd_epi32(); //expect: IntrinsicIssue  
    _mm_cvtps_epi32(); //expect: IntrinsicIssue  
    _mm_cvtps_ph(); //expect: IntrinsicIssue  
    _mm_cvtsi32_si128(); //expect: IntrinsicIssue  
    _mm_cvtsi64_si128(); //expect: IntrinsicIssue  
    _mm_cvtsi64x_si128(); //expect: IntrinsicIssue   
    _mm_cvttpd_epi32(); //expect: IntrinsicIssue   
    _mm_cvttps_epi32(); //expect: IntrinsicIssue  
    _mm_extracti_si64(); //expect: IntrinsicIssue   
    _mm_extract_si64(); //expect: IntrinsicIssue  
    _mm_haddd_epi16(); //expect: IntrinsicIssue  
    _mm_haddd_epi8(); //expect: IntrinsicIssue  
    _mm_haddd_epu16(); //expect: IntrinsicIssue  
    _mm_haddd_epu8(); //expect: IntrinsicIssue  
    _mm_hadd_epi16(); //expect: IntrinsicIssue  
    _mm_hadd_epi32(); //expect: IntrinsicIssue  
    _mm_haddq_epi16(); //expect: IntrinsicIssue  
    _mm_haddq_epi32(); //expect: IntrinsicIssue  
    _mm_haddq_epi8(); //expect: IntrinsicIssue  
    _mm_haddq_epu16(); //expect: IntrinsicIssue  
    _mm_haddq_epu32(); //expect: IntrinsicIssue  
    _mm_haddq_epu8(); //expect: IntrinsicIssue  
    _mm_hadds_epi16(); //expect: IntrinsicIssue  
    _mm_haddw_epi8(); //expect: IntrinsicIssue  
    _mm_haddw_epu8(); //expect: IntrinsicIssue  
    _mm_hsubd_epi16(); //expect: IntrinsicIssue  
    _mm_hsub_epi16(); //expect: IntrinsicIssue  
    _mm_hsub_epi32(); //expect: IntrinsicIssue  
    _mm_hsubq_epi32(); //expect: IntrinsicIssue  
    _mm_hsubs_epi16(); //expect: IntrinsicIssue  
    _mm_hsubw_epi8(); //expect: IntrinsicIssue  
    _mm_i32gather_epi32(); //expect: IntrinsicIssue  
    _mm_i32gather_epi64(); //expect: IntrinsicIssue  
    _mm_i64gather_epi32(); //expect: IntrinsicIssue  
    _mm_i64gather_epi64(); //expect: IntrinsicIssue  
    _mm_insert_epi16(); //expect: IntrinsicIssue  
    _mm_insert_epi32(); //expect: IntrinsicIssue  
    _mm_insert_epi64(); //expect: IntrinsicIssue 
    _mm_insert_epi8(); //expect: IntrinsicIssue   
    _mm_inserti_si64(); //expect: IntrinsicIssue  
    _mm_insert_si64(); //expect: IntrinsicIssue  
    _mm_lddqu_si128(); //expect: IntrinsicIssue  
    _mm_loadl_epi64(); //expect: IntrinsicIssue  
    _mm_load_si128(); //expect: IntrinsicIssue  
    _mm_loadu_si128(); //expect: IntrinsicIssue  
    _mm_maccd_epi16(); //expect: IntrinsicIssue  
    _mm_macc_epi16(); //expect: IntrinsicIssue  
    _mm_macc_epi32(); //expect: IntrinsicIssue  
    _mm_macchi_epi32(); //expect: IntrinsicIssue  
    _mm_macclo_epi32(); //expect: IntrinsicIssue  
    _mm_maccsd_epi16(); //expect: IntrinsicIssue  
    _mm_maccs_epi16(); //expect: IntrinsicIssue  
    _mm_maccs_epi32(); //expect: IntrinsicIssue  
    _mm_maccshi_epi32(); //expect: IntrinsicIssue  
    _mm_maccslo_epi32(); //expect: IntrinsicIssue  
    _mm_maddd_epi16(); //expect: IntrinsicIssue  
    _mm_madd_epi16(); //expect: IntrinsicIssue  
    _mm_maddsd_epi16(); //expect: IntrinsicIssue  
    _mm_maddubs_epi16(); //expect: IntrinsicIssue  
    _mm_mask_i32gather_epi32(); //expect: IntrinsicIssue  
    _mm_mask_i32gather_epi64(); //expect: IntrinsicIssue  
    _mm_mask_i64gather_epi32(); //expect: IntrinsicIssue   
    _mm_mask_i64gather_epi64(); //expect: IntrinsicIssue  
    _mm_maskload_epi32(); //expect: IntrinsicIssue  
    _mm_maskload_epi64(); //expect: IntrinsicIssue  
    _mm_max_epi16(); //expect: IntrinsicIssue  
    _mm_max_epi32(); //expect: IntrinsicIssue  
    _mm_max_epi8 (); //expect: IntrinsicIssue  
    _mm_max_epu16(); //expect: IntrinsicIssue  
    _mm_max_epu32(); //expect: IntrinsicIssue  
    _mm_max_epu8(); //expect: IntrinsicIssue  
    _mm_min_epi16(); //expect: IntrinsicIssue 
    _mm_min_epi32(); //expect: IntrinsicIssue  
    _mm_min_epi8(); //expect: IntrinsicIssue   
    _mm_min_epu16(); //expect: IntrinsicIssue  
    _mm_min_epu32(); //expect: IntrinsicIssue  
    _mm_min_epu8(); //expect: IntrinsicIssue  
    _mm_minpos_epu16(); //expect: IntrinsicIssue  
    _mm_move_epi64(); //expect: IntrinsicIssue  
    _mm_movpi64_epi64(); //expect: IntrinsicIssue  
    _mm_mpsadbw_epu8(); //expect: IntrinsicIssue  
    _mm_mul_epi32(); //expect: IntrinsicIssue  
    _mm_mul_epu32(); //expect: IntrinsicIssue  
    _mm_mulhi_epi16(); //expect: IntrinsicIssue  
    _mm_mulhi_epu16(); //expect: IntrinsicIssue  
    _mm_mulhrs_epi16(); //expect: IntrinsicIssue  
    _mm_mullo_epi16(); //expect: IntrinsicIssue  
    _mm_mullo_epi32(); //expect: IntrinsicIssue  
    _mm_or_si128(); //expect: IntrinsicIssue  
    _mm_packs_epi16(); //expect: IntrinsicIssue  
    _mm_packs_epi32(); //expect: IntrinsicIssue  
    _mm_packus_epi16(); //expect: IntrinsicIssue  
    _mm_packus_epi32(); //expect: IntrinsicIssue  
    _mm_perm_epi8(); //expect: IntrinsicIssue  
    _mm_rot_epi16(); //expect: IntrinsicIssue  
    _mm_rot_epi16(); //expect: IntrinsicIssue  
    _mm_rot_epi32(); //expect: IntrinsicIssue  
    _mm_rot_epi32(); //expect: IntrinsicIssue  
    _mm_rot_epi64(); //expect: IntrinsicIssue  
    _mm_rot_epi64(); //expect: IntrinsicIssue  
    _mm_rot_epi8(); //expect: IntrinsicIssue  
    _mm_rot_epi8(); //expect: IntrinsicIssue  
    _mm_roti_epi16(); //expect: IntrinsicIssue  
    _mm_roti_epi32(); //expect: IntrinsicIssue  
    _mm_roti_epi64(); //expect: IntrinsicIssue  
    _mm_roti_epi8(); //expect: IntrinsicIssue  
    _mm_sad_epu8(); //expect: IntrinsicIssue  
    _mm_set1_epi16(); //expect: IntrinsicIssue  
    _mm_set1_epi32(); //expect: IntrinsicIssue  
    _mm_set1_epi64(); //expect: IntrinsicIssue  
    _mm_set1_epi64x(); //expect: IntrinsicIssue  
    _mm_set1_epi8(); //expect: IntrinsicIssue  
    _mm_set_epi16(); //expect: IntrinsicIssue  
    _mm_set_epi32(); //expect: IntrinsicIssue  
    _mm_set_epi64(); //expect: IntrinsicIssue  
    _mm_set_epi64x(); //expect: IntrinsicIssue  
    _mm_set_epi8(); //expect: IntrinsicIssue  
    _mm_setl_epi64(); //expect: IntrinsicIssue 
    _mm_setr_epi16(); //expect: IntrinsicIssue 
    _mm_setr_epi32(); //expect: IntrinsicIssue 
    _mm_setr_epi64(); //expect: IntrinsicIssue 
    _mm_setr_epi8(); //expect: IntrinsicIssue 
    _mm_setzero_si128(); //expect: IntrinsicIssue 
    _mm_sha_epi16(); //expect: IntrinsicIssue 
    _mm_sha_epi32(); //expect: IntrinsicIssue 
    _mm_sha_epi64(); //expect: IntrinsicIssue 
    _mm_sha_epi8(); //expect: IntrinsicIssue 
    _mm_shl_epi16(); //expect: IntrinsicIssue 
    _mm_shl_epi32(); //expect: IntrinsicIssue 
    _mm_shl_epi64(); //expect: IntrinsicIssue
    _mm_shl_epi8(); //expect: IntrinsicIssue 
    _mm_shuffle_epi32(); //expect: IntrinsicIssue  
    _mm_shuffle_epi8(); //expect: IntrinsicIssue 
    _mm_shufflehi_epi16(); //expect: IntrinsicIssue 
    _mm_shufflelo_epi16(); //expect: IntrinsicIssue 
    _mm_sign_epi16(); //expect: IntrinsicIssue 
    _mm_sign_epi32(); //expect: IntrinsicIssue 
    _mm_sign_epi8(); //expect: IntrinsicIssue 
    _mm_sll_epi16(); //expect: IntrinsicIssue 
    _mm_sll_epi32(); //expect: IntrinsicIssue 
    _mm_sll_epi64(); //expect: IntrinsicIssue 
    _mm_slli_epi16(); //expect: IntrinsicIssue 
    _mm_slli_epi32(); //expect: IntrinsicIssue 
    _mm_slli_epi64(); //expect: IntrinsicIssue 
    _mm_slli_si128(); //expect: IntrinsicIssue 
    _mm_sllv_epi32(); //expect: IntrinsicIssue 
    _mm_sllv_epi64(); //expect: IntrinsicIssue 
    _mm_sra_epi16(); //expect: IntrinsicIssue 
    _mm_sra_epi32(); //expect: IntrinsicIssue 
    _mm_srai_epi16(); //expect: IntrinsicIssue 
    _mm_srai_epi32(); //expect: IntrinsicIssue 
    _mm_srav_epi32(); //expect: IntrinsicIssue 
    _mm_srl_epi16(); //expect: IntrinsicIssue  
    _mm_srl_epi32(); //expect: IntrinsicIssue  
    _mm_srl_epi64(); //expect: IntrinsicIssue  
    _mm_srli_epi16(); //expect: IntrinsicIssue 
    _mm_srli_epi32(); //expect: IntrinsicIssue 
    _mm_srli_epi64(); //expect: IntrinsicIssue 
    _mm_srli_si128(); //expect: IntrinsicIssue 
    _mm_srlv_epi32(); //expect: IntrinsicIssue 
    _mm_srlv_epi64(); //expect: IntrinsicIssue 
    _mm_stream_load_si128(); //expect: IntrinsicIssue 
    _mm_sub_epi16(); //expect: IntrinsicIssue 
    _mm_sub_epi32(); //expect: IntrinsicIssue 
    _mm_sub_epi64(); //expect: IntrinsicIssue 
    _mm_sub_epi8(); //expect: IntrinsicIssue 
    _mm_subs_epi16(); //expect: IntrinsicIssue 
    _mm_subs_epi8(); //expect: IntrinsicIssue 
    _mm_subs_epu16(); //expect: IntrinsicIssue 
    _mm_subs_epu8(); //expect: IntrinsicIssue 
    _mm_unpackhi_epi16(); //expect: IntrinsicIssue 
    _mm_unpackhi_epi32(); //expect: IntrinsicIssue 
    _mm_unpackhi_epi64(); //expect: IntrinsicIssue 
    _mm_unpackhi_epi8(); //expect: IntrinsicIssue
    _mm_unpacklo_epi16(); //expect: IntrinsicIssue 
    _mm_unpacklo_epi32(); //expect: IntrinsicIssue  
    _mm_unpacklo_epi64(); //expect: IntrinsicIssue 
    _mm_unpacklo_epi8(); //expect: IntrinsicIssue
    _mm_xor_si128(); //expect: IntrinsicIssue 
    _mm256_castps256_ps128(); //expect: IntrinsicIssue  
    _mm256_cvtpd_ps(); //expect: IntrinsicIssue 
    _mm256_extractf128_ps(); //expect: IntrinsicIssue 
    _mm256_i64gather_ps(); //expect: IntrinsicIssue 
    _mm256_mask_i64gather_ps(); //expect: IntrinsicIssue 
    _mm_add_ps(); //expect: IntrinsicIssue 
    _mm_add_ss(); //expect: IntrinsicIssue 
    _mm_addsub_ps(); //expect: IntrinsicIssue 
    _mm_andnot_ps(); //expect: IntrinsicIssue 
    _mm_and_ps(); //expect: IntrinsicIssue
    _mm_blend_ps(); //expect: IntrinsicIssue  
    _mm_blendv_ps(); //expect: IntrinsicIssue 
    _mm_broadcast_ss(); //expect: IntrinsicIssue  
    _mm_broadcastss_ps(); //expect: IntrinsicIssue
    _mm_castpd_ps(); //expect: IntrinsicIssue
    _mm_castsi128_ps(); //expect: IntrinsicIssue
    _mm_cmpeq_ps(); //expect: IntrinsicIssue 
    _mm_cmpeq_ss(); //expect: IntrinsicIssue 
    _mm_cmpge_ps(); //expect: IntrinsicIssue 
    _mm_cmpge_ss(); //expect: IntrinsicIssue 
    _mm_cmpgt_ps(); //expect: IntrinsicIssue 
    _mm_cmpgt_ss(); //expect: IntrinsicIssue 
    _mm_cmple_ps(); //expect: IntrinsicIssue 
    _mm_cmple_ss(); //expect: IntrinsicIssue 
    _mm_cmplt_ps(); //expect: IntrinsicIssue 
    _mm_cmplt_ss(); //expect: IntrinsicIssue 
    _mm_cmpneq_ps(); //expect: IntrinsicIssue 
    _mm_cmpneq_ss(); //expect: IntrinsicIssue 
    _mm_cmpnge_ps(); //expect: IntrinsicIssue 
    _mm_cmpnge_ss(); //expect: IntrinsicIssue 
    _mm_cmpngt_ps(); //expect: IntrinsicIssue 
    _mm_cmpngt_ss(); //expect: IntrinsicIssue
    _mm_cmpnle_ps(); //expect: IntrinsicIssue 
    _mm_cmpnle_ss(); //expect: IntrinsicIssue 
    _mm_cmpnlt_ps(); //expect: IntrinsicIssue  
    _mm_cmpnlt_ss(); //expect: IntrinsicIssue 
    _mm_cmpord_ps(); //expect: IntrinsicIssue 
    _mm_cmpord_ss(); //expect: IntrinsicIssue 
    _mm_cmp_ps(); //expect: IntrinsicIssue 
    _mm_cmp_ss(); //expect: IntrinsicIssue 
    _mm_cmpunord_ps(); //expect: IntrinsicIssue 
    _mm_cmpunord_ss(); //expect: IntrinsicIssue 
    _mm_cvtepi32_ps(); //expect: IntrinsicIssue 
    _mm_cvtpd_ps(); //expect: IntrinsicIssue 
    _mm_cvtph_ps(); //expect: IntrinsicIssue 
    _mm_cvt_pi2ps(); //expect: IntrinsicIssue 
    _mm_cvtsd_ss(); //expect: IntrinsicIssue
    _mm_cvt_si2ss(); //expect: IntrinsicIssue 
    _mm_cvtsi64_ss(); //expect: IntrinsicIssue 
    _mm_cvtsi64x_ss(); //expect: IntrinsicIssue 
    _mm_div_ps(); //expect: IntrinsicIssue 
    _mm_div_ss(); //expect: IntrinsicIssue  
    _mm_dp_ps(); //expect: IntrinsicIssue 
    _mm_fmadd_ps(); //expect: IntrinsicIssue 
    _mm_fmadd_ss(); //expect: IntrinsicIssue 
    _mm_fmaddsub_ps(); //expect: IntrinsicIssue 
    _mm_fmsubadd_ps(); //expect: IntrinsicIssue 
    _mm_fmsub_ps(); //expect: IntrinsicIssue 
    _mm_fmsub_ss(); //expect: IntrinsicIssue 
    _mm_fnmadd_ps(); //expect: IntrinsicIssue 
    _mm_fnmadd_ss(); //expect: IntrinsicIssue 
    _mm_fnmsub_ps(); //expect: IntrinsicIssue 
    _mm_fnmsub_ss(); //expect: IntrinsicIssue 
    _mm_frcz_ps(); //expect: IntrinsicIssue 
    _mm_frcz_ss(); //expect: IntrinsicIssue 
    _mm_hadd_ps(); //expect: IntrinsicIssue 
    _mm_hsub_ps(); //expect: IntrinsicIssue 
    _mm_i32gather_ps(); //expect: IntrinsicIssue 
    _mm_i64gather_ps(); //expect: IntrinsicIssue 
    _mm_insert_ps(); //expect: IntrinsicIssue 
    _mm_loadh_pi(); //expect: IntrinsicIssue 
    _mm_loadl_pi(); //expect: IntrinsicIssue 
    _mm_load_ps1(); //expect: IntrinsicIssue 
    _mm_load_ps(); //expect: IntrinsicIssue
    _mm_loadr_ps(); //expect: IntrinsicIssue 
    _mm_load_ss(); //expect: IntrinsicIssue 
    _mm_loadu_ps(); //expect: IntrinsicIssue 
    _mm_macc_ps(); //expect: IntrinsicIssue 
    _mm_macc_ss(); //expect: IntrinsicIssue 
    _mm_maddsub_ps(); //expect: IntrinsicIssue 
    _mm_mask_i32gather_ps(); //expect: IntrinsicIssue 
    _mm_mask_i64gather_ps(); //expect: IntrinsicIssue 
    _mm_maskload_ps(); //expect: IntrinsicIssue 
    _mm_max_ps(); //expect: IntrinsicIssue 
    _mm_max_ss(); //expect: IntrinsicIssue 
    _mm_min_ps(); //expect: IntrinsicIssue 
    _mm_min_ss(); //expect: IntrinsicIssue 
    _mm_movehdup_ps(); //expect: IntrinsicIssue 
    _mm_movehl_ps(); //expect: IntrinsicIssue 
    _mm_moveldup_ps(); //expect: IntrinsicIssue 
    _mm_movelh_ps(); //expect: IntrinsicIssue 
    _mm_move_ss(); //expect: IntrinsicIssue 
    _mm_msubadd_ps(); //expect: IntrinsicIssue 
    _mm_msub_ps(); //expect: IntrinsicIssue 
    _mm_msub_ss(); //expect: IntrinsicIssue 
    _mm_mul_ps(); //expect: IntrinsicIssue 
    _mm_mul_ss(); //expect: IntrinsicIssue 
    _mm_nmacc_ps(); //expect: IntrinsicIssue 
    _mm_nmacc_ss(); //expect: IntrinsicIssue 
    _mm_nmsub_ps(); //expect: IntrinsicIssue 
    _mm_nmsub_ss(); //expect: IntrinsicIssue 
    _mm_or_ps(); //expect: IntrinsicIssue 
    _mm_permute2_ps(); //expect: IntrinsicIssue 
    _mm_permute_ps(); //expect: IntrinsicIssue 
    _mm_permutevar_ps(); //expect: IntrinsicIssue 
    _mm_rcp_ps(); //expect: IntrinsicIssue 
    _mm_rcp_ss(); //expect: IntrinsicIssue 
    _mm_round_ps(); //expect: IntrinsicIssue 
    _mm_round_ss(); //expect: IntrinsicIssue 
    _mm_rsqrt_ps(); //expect: IntrinsicIssue 
    _mm_rsqrt_ss(); //expect: IntrinsicIssue 
    _mm_set_ps1(); //expect: IntrinsicIssue 
    _mm_set_ps(); //expect: IntrinsicIssue 
    _mm_setr_ps(); //expect: IntrinsicIssue 
    _mm_set_ss(); //expect: IntrinsicIssue 
    _mm_setzero_ps(); //expect: IntrinsicIssue 
    _mm_shuffle_ps(); //expect: IntrinsicIssue 
    _mm_sqrt_ps(); //expect: IntrinsicIssue 
    _mm_sqrt_ss(); //expect: IntrinsicIssue 
    _mm_sub_ps(); //expect: IntrinsicIssue 
    _mm_sub_ss(); //expect: IntrinsicIssue 
    _mm_unpackhi_ps(); //expect: IntrinsicIssue 
    _mm_unpacklo_ps(); //expect: IntrinsicIssue 
    _mm_xor_ps(); //expect: IntrinsicIssue 
    _mm256_add_pd(); //expect: IntrinsicIssue 
    _mm256_addsub_pd(); //expect: IntrinsicIssue 
    _mm256_andnot_pd(); //expect: IntrinsicIssue 
    _mm256_and_pd(); //expect: IntrinsicIssue  
    _mm256_blend_pd(); //expect: IntrinsicIssue
    _mm256_blendv_pd(); //expect: IntrinsicIssue 
    _mm256_broadcast_pd(); //expect: IntrinsicIssue 
    _mm256_broadcast_sd(); //expect: IntrinsicIssue 
    _mm256_broadcastsd_pd(); //expect: IntrinsicIssue 
    _mm256_castpd128_pd256(); //expect: IntrinsicIssue 
    _mm256_castps_pd(); //expect: IntrinsicIssue 
    _mm256_castsi256_pd(); //expect: IntrinsicIssue  
    _mm256_cmp_pd(); //expect: IntrinsicIssue 
    _mm256_cvtepi32_pd(); //expect: IntrinsicIssue 
    _mm256_cvtps_pd(); //expect: IntrinsicIssue 
    _mm256_div_pd(); //expect: IntrinsicIssue 
    _mm256_fmadd_pd(); //expect: IntrinsicIssue  
    _mm256_fmaddsub_pd(); //expect: IntrinsicIssue 
    _mm256_fmsubadd_pd(); //expect: IntrinsicIssue 
    _mm256_fmsub_pd(); //expect: IntrinsicIssue 
    _mm256_fnmadd_pd(); //expect: IntrinsicIssue 
    _mm256_fnmsub_pd(); //expect: IntrinsicIssue 
    _mm256_frcz_pd(); //expect: IntrinsicIssue 
    _mm256_hadd_pd(); //expect: IntrinsicIssue 
    _mm256_hsub_pd(); //expect: IntrinsicIssue 
    _mm256_i32gather_pd(); //expect: IntrinsicIssue 
    _mm256_i64gather_pd(); //expect: IntrinsicIssue 
    _mm256_insertf128_pd(); //expect: IntrinsicIssue 
    _mm256_load_pd(); //expect: IntrinsicIssue 
    _mm256_loadu_pd(); //expect: IntrinsicIssue 
     _mm256_macc_pd(); //expect: IntrinsicIssue 
    _mm256_maddsub_pd(); //expect: IntrinsicIssue 
    _mm256_mask_i32gather_pd(); //expect: IntrinsicIssue 
    _mm256_mask_i64gather_pd(); //expect: IntrinsicIssue 
    _mm256_maskload_pd(); //expect: IntrinsicIssue 
    _mm256_max_pd(); //expect: IntrinsicIssue 
    _mm256_min_pd(); //expect: IntrinsicIssue 
    _mm256_movedup_pd(); //expect: IntrinsicIssue 
    _mm256_msubadd_pd(); //expect: IntrinsicIssue 
    _mm256_msub_pd(); //expect: IntrinsicIssue 
    _mm256_mul_pd(); //expect: IntrinsicIssue 
    _mm256_nmacc_pd(); //expect: IntrinsicIssue   
    _mm256_nmsub_pd(); //expect: IntrinsicIssue 
    _mm256_or_pd(); //expect: IntrinsicIssue 
    _mm256_permute2f128_pd(); //expect: IntrinsicIssue 
    _mm256_permute2_pd(); //expect: IntrinsicIssue 
    _mm256_permute4x64_pd(); //expect: IntrinsicIssue 
    _mm256_permute_pd(); //expect: IntrinsicIssue 
    _mm256_permutevar_pd(); //expect: IntrinsicIssue 
    _mm256_round_pd(); //expect: IntrinsicIssue  
    _mm256_set1_pd(); //expect: IntrinsicIssue
    _mm256_set_pd(); //expect: IntrinsicIssue  
    _mm256_setr_pd(); //expect: IntrinsicIssue 
    _mm256_setzero_pd(); //expect: IntrinsicIssue 
    _mm256_shuffle_pd(); //expect: IntrinsicIssue 
    _mm256_sqrt_pd(); //expect: IntrinsicIssue 
    _mm256_sub_pd(); //expect: IntrinsicIssue 
    _mm256_unpackhi_pd(); //expect: IntrinsicIssue 
    _mm256_unpacklo_pd(); //expect: IntrinsicIssue 
    _mm256_xor_pd(); //expect: IntrinsicIssue 
    _mm_macc_pd(); //expect: IntrinsicIssue 
    _mm_maddsub_pd(); //expect: IntrinsicIssue 
    _mm_msubadd_pd(); //expect: IntrinsicIssue 
    _mm_msub_pd(); //expect: IntrinsicIssue 
    _mm_nmacc_pd(); //expect: IntrinsicIssue 
    _mm_nmsub_pd(); //expect: IntrinsicIssue 
    _mm256_abs_epi16(); //expect: IntrinsicIssue 
    _mm256_abs_epi32(); //expect: IntrinsicIssue 
    _mm256_abs_epi8(); //expect: IntrinsicIssue 
    _mm256_add_epi16(); //expect: IntrinsicIssue 
    _mm256_add_epi32(); //expect: IntrinsicIssue 
    _mm256_add_epi64(); //expect: IntrinsicIssue 
    _mm256_add_epi8(); //expect: IntrinsicIssue 
    _mm256_adds_epi16(); //expect: IntrinsicIssue 
    _mm256_adds_epi8(); //expect: IntrinsicIssue 
    _mm256_adds_epu16(); //expect: IntrinsicIssue 
    _mm256_adds_epu8(); //expect: IntrinsicIssue  
    _mm256_alignr_epi8(); //expect: IntrinsicIssue 
    _mm256_andnot_si256(); //expect: IntrinsicIssue 
    _mm256_and_si256(); //expect: IntrinsicIssue 
    _mm256_avg_epu16(); //expect: IntrinsicIssue 
    _mm256_avg_epu8(); //expect: IntrinsicIssue 
    _mm256_avg_epu8(); //expect: IntrinsicIssue 
    _mm256_blend_epi16(); //expect: IntrinsicIssue 
    _mm256_blend_epi32(); //expect: IntrinsicIssue  
    _mm256_blendv_epi8(); //expect: IntrinsicIssue 
    _mm256_broadcastb_epi8(); //expect: IntrinsicIssue 
    _mm256_broadcastd_epi32(); //expect: IntrinsicIssue 
    _mm256_broadcastq_epi64(); //expect: IntrinsicIssue 
    _mm256_broadcastsi128_si256(); //expect: IntrinsicIssue 
    _mm256_broadcastw_epi16(); //expect: IntrinsicIssue 
    _mm256_castpd_si256(); //expect: IntrinsicIssue 
    _mm256_castps_si256(); //expect: IntrinsicIssue 
    _mm256_castsi128_si256(); //expect: IntrinsicIssue 
    _mm256_cmov_si256(); //expect: IntrinsicIssue 
    _mm256_cmpeq_epi16(); //expect: IntrinsicIssue 
    _mm256_cmpeq_epi32(); //expect: IntrinsicIssue 
    _mm256_cmpeq_epi64(); //expect: IntrinsicIssue 
    _mm256_cmpeq_epi8(); //expect: IntrinsicIssue 
    _mm256_cmpgt_epi16(); //expect: IntrinsicIssue 
    _mm256_cmpgt_epi32(); //expect: IntrinsicIssue 
    _mm256_cmpgt_epi64(); //expect: IntrinsicIssue 
    _mm256_cmpgt_epi8(); //expect: IntrinsicIssue 
    _mm256_cvtepi16_epi32(); //expect: IntrinsicIssue 
    _mm256_cvtepi16_epi64(); //expect: IntrinsicIssue 
    _mm256_cvtepi32_epi64(); //expect: IntrinsicIssue 
    _mm256_cvtepi8_epi16(); //expect: IntrinsicIssue  
    _mm256_cvtepi8_epi32(); //expect: IntrinsicIssue 
    _mm256_cvtepi8_epi64(); //expect: IntrinsicIssue
    _mm256_cvtepu16_epi32(); //expect: IntrinsicIssue 
    _mm256_cvtepu16_epi64(); //expect: IntrinsicIssue 
    _mm256_cvtepu32_epi64(); //expect: IntrinsicIssue  
    _mm256_cvtepu8_epi16(); //expect: IntrinsicIssue 
    _mm256_cvtepu8_epi32(); //expect: IntrinsicIssue 
    _mm256_cvtepu8_epi64(); //expect: IntrinsicIssue 
    _mm256_cvtps_epi32(); //expect: IntrinsicIssue 
    _mm256_cvttps_epi32(); //expect: IntrinsicIssue 
    _mm256_hadd_epi16(); //expect: IntrinsicIssue 
    _mm256_hadd_epi32(); //expect: IntrinsicIssue 
    _mm256_hadds_epi16(); //expect: IntrinsicIssue 
    _mm256_hsub_epi16(); //expect: IntrinsicIssue 
    _mm256_hsub_epi32(); //expect: IntrinsicIssue  
    _mm256_hsubs_epi16(); //expect: IntrinsicIssue 
    _mm256_i32gather_epi32(); //expect: IntrinsicIssue 
    _mm256_i32gather_epi64(); //expect: IntrinsicIssue 
    _mm256_i64gather_epi32(); //expect: IntrinsicIssue 
    _mm256_i64gather_epi64(); //expect: IntrinsicIssue 
    _mm256_insertf128_si256(); //expect: IntrinsicIssue 
    _mm256_inserti128_si256(); //expect: IntrinsicIssue 
    _mm256_lddqu_si256(); //expect: IntrinsicIssue 
    _mm256_load_si256(); //expect: IntrinsicIssue  
    _mm256_loadu_si256(); //expect: IntrinsicIssue 
    _mm256_madd_epi16(); //expect: IntrinsicIssue  
    _mm256_maddubs_epi16(); //expect: IntrinsicIssue 
    _mm256_mask_i32gather_epi32(); //expect: IntrinsicIssue 
    _mm256_mask_i32gather_epi64(); //expect: IntrinsicIssue 
    _mm256_mask_i64gather_epi64(); //expect: IntrinsicIssue 
    _mm256_maskload_epi32(); //expect: IntrinsicIssue 
    _mm256_maskload_epi64(); //expect: IntrinsicIssue 
    _mm256_max_epi16(); //expect: IntrinsicIssue 
    _mm256_max_epi32(); //expect: IntrinsicIssue 
    _mm256_max_epi8(); //expect: IntrinsicIssue 
    _mm256_max_epu16(); //expect: IntrinsicIssue 
    _mm256_max_epu32(); //expect: IntrinsicIssue 
    _mm256_max_epu8(); //expect: IntrinsicIssue 
    _mm256_min_epi16(); //expect: IntrinsicIssue 
    _mm256_min_epi32(); //expect: IntrinsicIssue 
    _mm256_min_epi8(); //expect: IntrinsicIssue 
    _mm256_min_epu16(); //expect: IntrinsicIssue 
    _mm256_min_epu32(); //expect: IntrinsicIssue 
    _mm256_min_epu8(); //expect: IntrinsicIssue  
    _mm256_mpsadbw_epu8(); //expect: IntrinsicIssue
    _mm256_mul_epi32(); //expect: IntrinsicIssue  
    _mm256_mul_epu32(); //expect: IntrinsicIssue 
    _mm256_mulhi_epi16(); //expect: IntrinsicIssue 
    _mm256_mulhi_epu16(); //expect: IntrinsicIssue 
    _mm256_mulhrs_epi16(); //expect: IntrinsicIssue 
    _mm256_mullo_epi16(); //expect: IntrinsicIssue 
    _mm256_mullo_epi32(); //expect: IntrinsicIssue 
    _mm256_or_si256(); //expect: IntrinsicIssue 
    _mm256_packs_epi16(); //expect: IntrinsicIssue 
    _mm256_packs_epi32(); //expect: IntrinsicIssue 
    _mm256_packus_epi16(); //expect: IntrinsicIssue 
    _mm256_packus_epi32(); //expect: IntrinsicIssue 
    _mm256_permute2f128_si256(); //expect: IntrinsicIssue 
    _mm256_permute2x128_si256(); //expect: IntrinsicIssue  
    _mm256_permute4x64_epi64(); //expect: IntrinsicIssue 
    _mm256_permutevar8x32_epi32(); //expect: IntrinsicIssue 
    _mm256_sad_epu8(); //expect: IntrinsicIssue  
    _mm256_set1_epi16(); //expect: IntrinsicIssue 
    _mm256_set1_epi32(); //expect: IntrinsicIssue 
    _mm256_set1_epi64x(); //expect: IntrinsicIssue 
    _mm256_set1_epi8(); //expect: IntrinsicIssue 
    _mm256_set_epi16(); //expect: IntrinsicIssue 
    _mm256_set_epi32(); //expect: IntrinsicIssue 
    _mm256_set_epi64x(); //expect: IntrinsicIssue 
    _mm256_set_epi8(); //expect: IntrinsicIssue 
    _mm256_setr_epi16(); //expect: IntrinsicIssue 
    _mm256_setr_epi32(); //expect: IntrinsicIssue 
    _mm256_setr_epi64x(); //expect: IntrinsicIssue 
    _mm256_setr_epi8(); //expect: IntrinsicIssue 
    _mm256_setzero_si256(); //expect: IntrinsicIssue 
    _mm256_shuffle_epi32(); //expect: IntrinsicIssue 
    _mm256_shuffle_epi8(); //expect: IntrinsicIssue  
    _mm256_shufflehi_epi16(); //expect: IntrinsicIssue 
    _mm256_shufflelo_epi16(); //expect: IntrinsicIssue 
    _mm256_sign_epi16(); //expect: IntrinsicIssue 
    _mm256_sign_epi32(); //expect: IntrinsicIssue 
    _mm256_sign_epi8(); //expect: IntrinsicIssue 
    _mm256_sll_epi16(); //expect: IntrinsicIssue 
    _mm256_sll_epi32(); //expect: IntrinsicIssue 
    _mm256_sll_epi64(); //expect: IntrinsicIssue 
    _mm256_slli_epi16(); //expect: IntrinsicIssue 
    _mm256_slli_epi32(); //expect: IntrinsicIssue 
    _mm256_slli_epi64(); //expect: IntrinsicIssue 
    _mm256_slli_si256(); //expect: IntrinsicIssue 
    _mm256_sllv_epi32(); //expect: IntrinsicIssue 
    _mm256_sllv_epi64(); //expect: IntrinsicIssue 
    _mm256_sra_epi16(); //expect: IntrinsicIssue 
    _mm256_sra_epi32(); //expect: IntrinsicIssue  
    _mm256_srai_epi16(); //expect: IntrinsicIssue 
    _mm256_srai_epi32(); //expect: IntrinsicIssue 
    _mm256_srav_epi32(); //expect: IntrinsicIssue  
    _mm256_srl_epi16(); //expect: IntrinsicIssue 
    _mm256_srl_epi32(); //expect: IntrinsicIssue 
    _mm256_srl_epi64(); //expect: IntrinsicIssue 
    _mm256_srli_epi16(); //expect: IntrinsicIssue  
    _mm256_srli_epi32(); //expect: IntrinsicIssue 
    _mm256_srli_epi64(); //expect: IntrinsicIssue 
    _mm256_srli_si256(); //expect: IntrinsicIssue 
    _mm256_srlv_epi32(); //expect: IntrinsicIssue 
    _mm256_srlv_epi64(); //expect: IntrinsicIssue 
    _mm256_stream_load_si256(); //expect: IntrinsicIssue 
    _mm256_sub_epi16(); //expect: IntrinsicIssue 
    _mm256_sub_epi32(); //expect: IntrinsicIssue 
    _mm256_sub_epi64(); //expect: IntrinsicIssue 
    _mm256_sub_epi8(); //expect: IntrinsicIssue 
    _mm256_subs_epi16(); //expect: IntrinsicIssue 
    _mm256_subs_epi8(); //expect: IntrinsicIssue 
    _mm256_subs_epu16(); //expect: IntrinsicIssue 
    _mm256_subs_epu8(); //expect: IntrinsicIssue 
    _mm256_unpackhi_epi16(); //expect: IntrinsicIssue 
    _mm256_unpackhi_epi32(); //expect: IntrinsicIssue 
    _mm256_unpackhi_epi64(); //expect: IntrinsicIssue 
    _mm256_unpackhi_epi8(); //expect: IntrinsicIssue 
    _mm256_unpacklo_epi16(); //expect: IntrinsicIssue 
    _mm256_unpacklo_epi32(); //expect: IntrinsicIssue 
    _mm256_unpacklo_epi64(); //expect: IntrinsicIssue 
    _mm256_unpacklo_epi8(); //expect: IntrinsicIssue 
    _mm256_xor_si256(); //expect: IntrinsicIssue 
    _mm256_add_ps(); //expect: IntrinsicIssue 
    _mm256_addsub_ps(); //expect: IntrinsicIssue 
    _mm256_andnot_ps(); //expect: IntrinsicIssue 
    _mm256_and_ps(); //expect: IntrinsicIssue 
    _mm256_blend_ps(); //expect: IntrinsicIssue 
    _mm256_blendv_ps(); //expect: IntrinsicIssue 
    _mm256_broadcast_ps(); //expect: IntrinsicIssue 
    _mm256_broadcast_ss(); //expect: IntrinsicIssue 
    _mm256_broadcastss_ps(); //expect: IntrinsicIssue 
    _mm256_castpd_ps(); //expect: IntrinsicIssue 
    _mm256_castps128_ps256(); //expect: IntrinsicIssue 
    _mm256_castsi256_ps(); //expect: IntrinsicIssue 
    _mm256_cmp_ps(); //expect: IntrinsicIssue 
    _mm256_cvtepi32_ps(); //expect: IntrinsicIssue 
    _mm256_cvtph_ps(); //expect: IntrinsicIssue 
    _mm256_div_ps(); //expect: IntrinsicIssue 
    _mm256_dp_ps(); //expect: IntrinsicIssue 
    _mm256_fmadd_ps(); //expect: IntrinsicIssue 
    _mm256_fmaddsub_ps(); //expect: IntrinsicIssue 
    _mm256_fmsubadd_ps(); //expect: IntrinsicIssue 
    _mm256_fmsub_ps(); //expect: IntrinsicIssue 
    _mm256_fnmadd_ps(); //expect: IntrinsicIssue 
    _mm256_fnmsub_ps(); //expect: IntrinsicIssue 
    _mm256_frcz_ps(); //expect: IntrinsicIssue 
    _mm256_hadd_ps(); //expect: IntrinsicIssue 
    _mm256_hsub_ps(); //expect: IntrinsicIssue 
    _mm256_i32gather_ps(); //expect: IntrinsicIssue 
    _mm256_insertf128_ps(); //expect: IntrinsicIssue 
    _mm256_load_ps(); //expect: IntrinsicIssue 
    _mm256_loadu_ps(); //expect: IntrinsicIssue 
    _mm256_macc_ps(); //expect: IntrinsicIssue 
    _mm256_maddsub_ps(); //expect: IntrinsicIssue 
    _mm256_mask_i32gather_ps(); //expect: IntrinsicIssue 
    _mm256_maskload_ps(); //expect: IntrinsicIssue 
    _mm256_max_ps(); //expect: IntrinsicIssue 
    _mm256_min_ps(); //expect: IntrinsicIssue 
    _mm256_movehdup_ps(); //expect: IntrinsicIssue 
    _mm256_moveldup_ps(); //expect: IntrinsicIssue 
    _mm256_msubadd_ps(); //expect: IntrinsicIssue 
    _mm256_msub_ps(); //expect: IntrinsicIssue 
    _mm256_mul_ps(); //expect: IntrinsicIssue 
    _mm256_nmacc_ps(); //expect: IntrinsicIssue 
    _mm256_nmsub_ps(); //expect: IntrinsicIssue 
    _mm256_or_ps(); //expect: IntrinsicIssue 
    _mm256_permute2f128_ps(); //expect: IntrinsicIssue 
    _mm256_permute2_ps(); //expect: IntrinsicIssue 
    _mm256_permute_ps(); //expect: IntrinsicIssue 
    _mm256_permutevar8x32_ps(); //expect: IntrinsicIssue 
    _mm256_permutevar_ps(); //expect: IntrinsicIssue 
    _mm256_rcp_ps(); //expect: IntrinsicIssue 
    _mm256_round_ps(); //expect: IntrinsicIssue 
    _mm256_rsqrt_ps(); //expect: IntrinsicIssue 
    _mm256_set1_ps(); //expect: IntrinsicIssue 
    _mm256_set_ps(); //expect: IntrinsicIssue 
    _mm256_setr_ps(); //expect: IntrinsicIssue 
    _mm256_setzero_ps(); //expect: IntrinsicIssue 
    _mm256_shuffle_ps(); //expect: IntrinsicIssue 
    _mm256_sqrt_ps(); //expect: IntrinsicIssue  
    _mm256_sub_ps(); //expect: IntrinsicIssue 
    _mm256_unpackhi_ps(); //expect: IntrinsicIssue 
    _mm256_unpacklo_ps(); //expect: IntrinsicIssue 
    _mm256_xor_ps(); //expect: IntrinsicIssue 
    _mm_macc_ps(); //expect: IntrinsicIssue 
    _mm_maddsub_ps(); //expect: IntrinsicIssue 
    _mm_msubadd_ps(); //expect: IntrinsicIssue  
    _mm_msub_ps(); //expect: IntrinsicIssue 
    _mm_nmacc_ps(); //expect: IntrinsicIssue 
    _mm_nmsub_ps(); //expect: IntrinsicIssue 
    _m_from_float(); //expect: IntrinsicIssue 
    _m_from_int(); //expect: IntrinsicIssue 
    _mm_abs_pi16(); //expect: IntrinsicIssue 
    _mm_abs_pi32(); //expect: IntrinsicIssue 
    _mm_abs_pi8(); //expect: IntrinsicIssue 
    _mm_add_si64(); //expect: IntrinsicIssue 
    _mm_alignr_pi8(); //expect: IntrinsicIssue 
    _mm_cvtpd_pi32(); //expect: IntrinsicIssue 
    _mm_cvt_ps2pi(); //expect: IntrinsicIssue 
    _mm_cvttpd_pi32(); //expect: IntrinsicIssue 
    _mm_cvtt_ps2pi(); //expect: IntrinsicIssue 
    _mm_hadd_pi16(); //expect: IntrinsicIssue 
    _mm_hadd_pi32(); //expect: IntrinsicIssue 
    _mm_hadds_pi16(); //expect: IntrinsicIssue 
    _mm_hsub_pi16(); //expect: IntrinsicIssue 
    _mm_hsub_pi32(); //expect: IntrinsicIssue 
    _mm_hsubs_pi16(); //expect: IntrinsicIssue 
    _mm_maddubs_pi16(); //expect: IntrinsicIssue 
    _mm_movepi64_pi64(); //expect: IntrinsicIssue 
    _mm_mulhrs_pi16(); //expect: IntrinsicIssue 
    _mm_mul_su32(); //expect: IntrinsicIssue 
    _mm_set1_pi16(); //expect: IntrinsicIssue 
    _mm_set1_pi32(); //expect: IntrinsicIssue 
    _mm_set1_pi8(); //expect: IntrinsicIssue 
    _mm_set_pi16(); //expect: IntrinsicIssue 
    _mm_set_pi32(); //expect: IntrinsicIssue 
    _mm_set_pi8(); //expect: IntrinsicIssue 
    _mm_setr_pi16(); //expect: IntrinsicIssue 
    _mm_setr_pi32(); //expect: IntrinsicIssue 
    _mm_setr_pi8(); //expect: IntrinsicIssue 
    _mm_setzero_si64(); //expect: IntrinsicIssue 
    _mm_shuffle_pi8(); //expect: IntrinsicIssue 
    _mm_sign_pi16(); //expect: IntrinsicIssue 
    _mm_sign_pi32(); //expect: IntrinsicIssue 
    _mm_sign_pi8(); //expect: IntrinsicIssue 
    _mm_sub_si64(); //expect: IntrinsicIssue 
    _m_packssdw(); //expect: IntrinsicIssue 
    _m_packsswb(); //expect: IntrinsicIssue 
    _m_packuswb(); //expect: IntrinsicIssue 
    _m_paddb(); //expect: IntrinsicIssue 
    _m_paddd(); //expect: IntrinsicIssue 
    _m_paddsb(); //expect: IntrinsicIssue 
    _m_paddsw(); //expect: IntrinsicIssue 
    _m_paddusb(); //expect: IntrinsicIssue 
    _m_paddusw(); //expect: IntrinsicIssue 
    _m_paddw(); //expect: IntrinsicIssue 
    _m_pand(); //expect: IntrinsicIssue 
    _m_pandn(); //expect: IntrinsicIssue 
    _m_pavgb(); //expect: IntrinsicIssue 
    _m_pavgusb(); //expect: IntrinsicIssue 
    _m_pavgw(); //expect: IntrinsicIssue 
    _m_pcmpeqb(); //expect: IntrinsicIssue 
    _m_pcmpeqd(); //expect: IntrinsicIssue 
    _m_pcmpeqw(); //expect: IntrinsicIssue 
    _m_pcmpgtb(); //expect: IntrinsicIssue 
    _m_pcmpgtd(); //expect: IntrinsicIssue 
    _m_pcmpgtw(); //expect: IntrinsicIssue 
    _m_pf2id(); //expect: IntrinsicIssue 
    _m_pf2iw(); //expect: IntrinsicIssue 
    _m_pfacc(); //expect: IntrinsicIssue 
    _m_pfadd(); //expect: IntrinsicIssue 
    _m_pfcmpeq(); //expect: IntrinsicIssue 
    _m_pfcmpge(); //expect: IntrinsicIssue 
    _m_pfcmpgt(); //expect: IntrinsicIssue 
    _m_pfmax(); //expect: IntrinsicIssue 
    _m_pfmin(); //expect: IntrinsicIssue 
    _m_pfmul(); //expect: IntrinsicIssue 
    _m_pfnacc(); //expect: IntrinsicIssue 
    _m_pfpnacc(); //expect: IntrinsicIssue 
    _m_pfrcpit1(); //expect: IntrinsicIssue 
    _m_pfrcpit2(); //expect: IntrinsicIssue
    _m_pfrcp(); //expect: IntrinsicIssue
    _m_pfrsqit1(); //expect: IntrinsicIssue 
    _m_pfrsqrt(); //expect: IntrinsicIssue 
    _m_pfsub(); //expect: IntrinsicIssue 
    _m_pfsubr(); //expect: IntrinsicIssue 
    _m_pi2fd(); //expect: IntrinsicIssue 
    _m_pi2fw(); //expect: IntrinsicIssue
    _m_pinsrw(); //expect: IntrinsicIssue 
    _m_pmaddwd(); //expect: IntrinsicIssue
    _m_pmaxsw(); //expect: IntrinsicIssue 
    _m_pmaxub(); //expect: IntrinsicIssue
    _m_pminsw(); //expect: IntrinsicIssue 
    _m_pminub(); //expect: IntrinsicIssue 
    _m_pmulhrw(); //expect: IntrinsicIssue 
    _m_pmulhuw(); //expect: IntrinsicIssue 
    _m_pmulhw(); //expect: IntrinsicIssue 
    _m_pmullw(); //expect: IntrinsicIssue 
    _m_por(); //expect: IntrinsicIssue  
    _m_psadbw(); //expect: IntrinsicIssue 
    _m_pshufw(); //expect: IntrinsicIssue 
    _m_pslldi(); //expect: IntrinsicIssue 
    _m_pslld(); //expect: IntrinsicIssue 
    _m_psllqi(); //expect: IntrinsicIssue
    _m_psllq(); //expect: IntrinsicIssue
    _m_psllwi(); //expect: IntrinsicIssue 
    _m_psllw(); //expect: IntrinsicIssue
    _m_psradi(); //expect: IntrinsicIssue 
    _m_psrad(); //expect: IntrinsicIssue 
    _m_psrawi(); //expect: IntrinsicIssue 
    _m_psraw(); //expect: IntrinsicIssue
    _m_psrldi(); //expect: IntrinsicIssue
    _m_psrld(); //expect: IntrinsicIssue 
    _m_psrlqi(); //expect: IntrinsicIssue
    _m_psrlq(); //expect: IntrinsicIssue 
    _m_psrlwi(); //expect: IntrinsicIssue 
    _m_psrlw(); //expect: IntrinsicIssue 
    _m_psubb(); //expect: IntrinsicIssue 
    _m_psubd(); //expect: IntrinsicIssue
    _m_psubsb(); //expect: IntrinsicIssue 
    _m_psubsw(); //expect: IntrinsicIssue 
    _m_psubusb(); //expect: IntrinsicIssue 
    _m_psubusw(); //expect: IntrinsicIssue
    _m_psubw(); //expect: IntrinsicIssue  
    _m_pswapd(); //expect: IntrinsicIssue 
    _m_punpckhbw(); //expect: IntrinsicIssue 
    _m_punpckhdq(); //expect: IntrinsicIssue 
    _m_punpckhwd(); //expect: IntrinsicIssue 
    _m_punpcklbw(); //expect: IntrinsicIssue 
    _m_punpckldq(); //expect: IntrinsicIssue 
    _m_punpcklwd(); //expect: IntrinsicIssue 
    _m_pxor(); //expect: IntrinsicIssue 
    _InterlockedAnd16_np(); //expect: IntrinsicIssue 
    _InterlockedCompareExchange16_np(); //expect: IntrinsicIssue 
    _InterlockedOr16_np(); //expect: IntrinsicIssue 
    _InterlockedXor16_np(); //expect: IntrinsicIssue 
    _loadbe_i16(); //expect: IntrinsicIssue 
    _addcarry_u16(); //expect: IntrinsicIssue 
    _addcarry_u32(); //expect: IntrinsicIssue 
    _addcarry_u64(); //expect: IntrinsicIssue 
    _addcarry_u8(); //expect: IntrinsicIssue 
    _addcarryx_u32(); //expect: IntrinsicIssue 
    _addcarryx_u64(); //expect: IntrinsicIssue 
    _bittestandcomplement64(); //expect: IntrinsicIssue 
    _bittestandreset64(); //expect: IntrinsicIssue 
    _bittestandset64(); //expect: IntrinsicIssue 
    __builtin_ia32_lwpins16(); //expect: IntrinsicIssue 
    __builtin_ia32_lwpins32(); //expect: IntrinsicIssue 
    __builtin_ia32_lwpins64(); //expect: IntrinsicIssue 
    __inbyte(); //expect: IntrinsicIssue 
    _interlockedbittestandreset64_HLEAcquire(); //expect: IntrinsicIssue 
    _interlockedbittestandreset64_HLERelease(); //expect: IntrinsicIssue 
    _interlockedbittestandreset64(); //expect: IntrinsicIssue 
    _interlockedbittestandreset_HLEAcquire(); //expect: IntrinsicIssue 
    _interlockedbittestandreset_HLERelease(); //expect: IntrinsicIssue 
    _interlockedbittestandset64_HLEAcquire(); //expect: IntrinsicIssue
    _interlockedbittestandset64_HLERelease(); //expect: IntrinsicIssue 
    _interlockedbittestandset64(); //expect: IntrinsicIssue 
    _interlockedbittestandset_HLEAcquire(); //expect: IntrinsicIssue 
    _interlockedbittestandset_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedCompareExchange128(); //expect: IntrinsicIssue 
    __lwpins32(); //expect: IntrinsicIssue 
    __lwpins64(); //expect: IntrinsicIssue 
    __readfsbyte(); //expect: IntrinsicIssue 
    __readgsbyte(); //expect: IntrinsicIssue 
    _subborrow_u16(); //expect: IntrinsicIssue 
    _subborrow_u32(); //expect: IntrinsicIssue 
    _subborrow_u64(); //expect: IntrinsicIssue 
    _subborrow_u8(); //expect: IntrinsicIssue  
    __vmx_on(); //expect: IntrinsicIssue 
    __vmx_vmclear(); //expect: IntrinsicIssue 
    __vmx_vmlaunch(); //expect: IntrinsicIssue 
    __vmx_vmptrld(); //expect: IntrinsicIssue 
    __vmx_vmread(); //expect: IntrinsicIssue 
    __vmx_vmresume(); //expect: IntrinsicIssue 
    __vmx_vmwrite(); //expect: IntrinsicIssue 
    _andn_u64(); //expect: IntrinsicIssue 
    _bextri_u64(); //expect: IntrinsicIssue 
    _bextr_u64(); //expect: IntrinsicIssue 
    _blcfill_u64(); //expect: IntrinsicIssue 
    _blcic_u64(); //expect: IntrinsicIssue 
    _blci_u64(); //expect: IntrinsicIssue 
    _blcmsk_u64(); //expect: IntrinsicIssue 
    _blcs_u64(); //expect: IntrinsicIssue 
    _blsfill_u64(); //expect: IntrinsicIssue 
    _blsic_u64(); //expect: IntrinsicIssue 
    _blsi_u64(); //expect: IntrinsicIssue 
    _blsmsk_u64(); //expect: IntrinsicIssue 
    _blsr_u64(); //expect: IntrinsicIssue 
    _bzhi_u64(); //expect: IntrinsicIssue 
    _load_be_u64(); //expect: IntrinsicIssue 
    __lzcnt64(); //expect: IntrinsicIssue 
    _lzcnt_u64(); //expect: IntrinsicIssue 
    _mm_crc32_u64(); //expect: IntrinsicIssue 
    _mulx_u64(); //expect: IntrinsicIssue 
    __emulu(); //expect: IntrinsicIssue  
    __ll_lshift(); //expect: IntrinsicIssue 
    __ull_rshift(); //expect: IntrinsicIssue 
    _pdep_u64(); //expect: IntrinsicIssue 
    _pext_u64(); //expect: IntrinsicIssue 
    __popcnt64(); //expect: IntrinsicIssue 
    __rdtscp(); //expect: IntrinsicIssue 
    __rdtsc(); //expect: IntrinsicIssue 
    __readcr0(); //expect: IntrinsicIssue 
    __readcr2(); //expect: IntrinsicIssue 
    __readcr3(); //expect: IntrinsicIssue 
    __readcr4(); //expect: IntrinsicIssue 
    __readcr8(); //expect: IntrinsicIssue 
    __readdr(); //expect: IntrinsicIssue 
    __readeflags(); //expect: IntrinsicIssue 
    _readfsbase_u64(); //expect: IntrinsicIssue 
    _readgsbase_u64(); //expect: IntrinsicIssue 
    __readgsqword(); //expect: IntrinsicIssue  
    __readmsr(); //expect: IntrinsicIssue 
    __readpmc(); //expect: IntrinsicIssue 
    _rorx_u64(); //expect: IntrinsicIssue 
    __shiftleft128(); //expect: IntrinsicIssue 
    __shiftright128(); //expect: IntrinsicIssue 
    _shlx_u64(); //expect: IntrinsicIssue 
    _shrx_u64(); //expect: IntrinsicIssue 
    _t1mskc_u64(); //expect: IntrinsicIssue 
    _tzcnt_u64(); //expect: IntrinsicIssue 
    _tzmsk_u64(); //expect: IntrinsicIssue 
    _udiv128(); //expect: IntrinsicIssue 
    _umul128(); //expect: IntrinsicIssue 
    __umulh(); //expect: IntrinsicIssue 
    _xgetbv(); //expect: IntrinsicIssue 
    _andn_u32(); //expect: IntrinsicIssue 
    _bextri_u32(); //expect: IntrinsicIssue 
    _bextr_u32(); //expect: IntrinsicIssue 
    _blcfill_u32(); //expect: IntrinsicIssue 
    _blcic_u32(); //expect: IntrinsicIssue 
    _blci_u32(); //expect: IntrinsicIssue 
    _blcmsk_u32(); //expect: IntrinsicIssue 
    _blcs_u32(); //expect: IntrinsicIssue 
    _blsfill_u32(); //expect: IntrinsicIssue 
    _blsic_u32(); //expect: IntrinsicIssue 
    _blsi_u32(); //expect: IntrinsicIssue 
    _blsmsk_u32(); //expect: IntrinsicIssue 
    _blsr_u32(); //expect: IntrinsicIssue 
    __builtin_ia32_bextri_u32(); //expect: IntrinsicIssue 
    __builtin_ia32_bextr_u32(); //expect: IntrinsicIssue 
    __builtin_ia32_crc32hi(); //expect: IntrinsicIssue 
    __builtin_ia32_crc32qi(); //expect: IntrinsicIssue 
    __builtin_ia32_crc32si(); //expect: IntrinsicIssue 
    __builtin_ia32_lzcnt_u32(); //expect: IntrinsicIssue 
    __builtin_ia32_rdfsbase32(); //expect: IntrinsicIssue 
    __builtin_ia32_rdgsbase32(); //expect: IntrinsicIssue 
    __builtin_ia32_rdrand16_step(); //expect: IntrinsicIssue 
    __builtin_ia32_rdrand32_step(); //expect: IntrinsicIssue 
    __builtin_ia32_rdrand64_step(); //expect: IntrinsicIssue  
    _bzhi_u32(); //expect: IntrinsicIssue
    __getcallerseflags(); //expect: IntrinsicIssue 
    _load_be_u32(); //expect: IntrinsicIssue 
    _lzcnt_u32(); //expect: IntrinsicIssue 
    __lzcnt(); //expect: IntrinsicIssue 
    _mm_crc32_u16(); //expect: IntrinsicIssue 
    _mm_crc32_u32(); //expect: IntrinsicIssue 
    _mm_crc32_u8(); //expect: IntrinsicIssue 
    _mm_getcsr(); //expect: IntrinsicIssue 
    _mulx_u32(); //expect: IntrinsicIssue 
    _pdep_u32(); //expect: IntrinsicIssue 
    _pext_u32(); //expect: IntrinsicIssue 
    __popcnt(); //expect: IntrinsicIssue 
    _readfsbase_u32(); //expect: IntrinsicIssue 
    _readgsbase_u32(); //expect: IntrinsicIssue 
    _rorx_u32(); //expect: IntrinsicIssue 
    _shlx_u32(); //expect: IntrinsicIssue 
    _shrx_u32(); //expect: IntrinsicIssue 
    _t1mskc_u32(); //expect: IntrinsicIssue 
    _tzcnt_u32(); //expect: IntrinsicIssue 
    _tzmsk_u32(); //expect: IntrinsicIssue 
    _udiv64(); //expect: IntrinsicIssue 
    __indword(); //expect: IntrinsicIssue 
    __builtin_ia32_bextri_u64(); //expect: IntrinsicIssue 
    __builtin_ia32_bextr_u64(); //expect: IntrinsicIssue 
    __builtin_ia32_crc32di(); //expect: IntrinsicIssue 
    __builtin_ia32_lzcnt_u64(); //expect: IntrinsicIssue 
    __builtin_ia32_rdfsbase64(); //expect: IntrinsicIssue 
    __builtin_ia32_rdgsbase64(); //expect: IntrinsicIssue 
    _bzhi_u64(); //expect: IntrinsicIssue 
    _pdep_u64(); //expect: IntrinsicIssue 
    _pext_u64(); //expect: IntrinsicIssue 
    __readcr0(); //expect: IntrinsicIssue 
    __readcr2(); //expect: IntrinsicIssue 
    __readcr3(); //expect: IntrinsicIssue 
    __readcr4(); //expect: IntrinsicIssue 
    __readcr8(); //expect: IntrinsicIssue 
    __readfsdword(); //expect: IntrinsicIssue 
    __readgsdword(); //expect: IntrinsicIssue 
    __segmentlimit(); //expect: IntrinsicIssue 
    __readdr(); //expect: IntrinsicIssue 
    __readeflags(); //expect: IntrinsicIssue 
    __builtin_ia32_lzcnt_16(); //expect: IntrinsicIssue 
    __inword(); //expect: IntrinsicIssue 
    _load_be_u16(); //expect: IntrinsicIssue 
    __lzcnt16(); //expect: IntrinsicIssue 
    __popcnt16(); //expect: IntrinsicIssue 
    __readfsword(); //expect: IntrinsicIssue 
    __readgsword(); //expect: IntrinsicIssue 
    __builtin_ia32_pabsw256(); //expect: IntrinsicIssue 
    __builtin_ia32_packssdw256(); //expect: IntrinsicIssue 
    __builtin_ia32_packusdw256(); //expect: IntrinsicIssue 
    __builtin_ia32_paddsw256(); //expect: IntrinsicIssue 
    __builtin_ia32_paddusw256(); //expect: IntrinsicIssue 
    __builtin_ia32_paddw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pavgw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pblendw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pbroadcastw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpeqw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpgtw256(); //expect: IntrinsicIssue 
    __builtin_ia32_phaddsw256(); //expect: IntrinsicIssue 
    __builtin_ia32_phaddw256(); //expect: IntrinsicIssue 
    __builtin_ia32_phsubsw256(); //expect: IntrinsicIssue 
    __builtin_ia32_phsubw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaddwd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaxsw256(); //expect: IntrinsicIssue
    __builtin_ia32_pmaxuw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pminsw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pminuw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovsxbw256 (); //expect: IntrinsicIssue 
    __builtin_ia32_pmovzxbw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmulhrsw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmulhuw256(); //expect: IntrinsicIssue
    __builtin_ia32_pmulhw256(); //expect: IntrinsicIssue  
    __builtin_ia32_pmullw256(); //expect: IntrinsicIssue 
    __builtin_ia32_psadbw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pshufhw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pshuflw256(); //expect: IntrinsicIssue 
    __builtin_ia32_psignw256(); //expect: IntrinsicIssue 
    __builtin_ia32_psllw256(); //expect: IntrinsicIssue 
    __builtin_ia32_psllwi256(); //expect: IntrinsicIssue 
    __builtin_ia32_psraw256(); //expect: IntrinsicIssue 
    __builtin_ia32_psrawi256(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlw256(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlwi256(); //expect: IntrinsicIssue 
    __builtin_ia32_psubsw256(); //expect: IntrinsicIssue 
    __builtin_ia32_psubusw256(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckhwd256(); //expect: IntrinsicIssue 
    __builtin_ia32_punpcklwd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcmov_v16hi256(); //expect: IntrinsicIssue 
    __builtin_ia32_lddqu(); //expect: IntrinsicIssue 
    __builtin_ia32_loaddqu(); //expect: IntrinsicIssue 
    __builtin_ia32_mpsadbw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pabsb128(); //expect: IntrinsicIssue 
    __builtin_ia32_packsswb128(); //expect: IntrinsicIssue 
    __builtin_ia32_packuswb128(); //expect: IntrinsicIssue
    __builtin_ia32_paddb128(); //expect: IntrinsicIssue
    __builtin_ia32_pavgb128(); //expect: IntrinsicIssue
    __builtin_ia32_pblendvb128(); //expect: IntrinsicIssue
    __builtin_ia32_pbroadcastb128(); //expect: IntrinsicIssue
    __builtin_ia32_pcmpeqb128(); //expect: IntrinsicIssue
    __builtin_ia32_pcmpestrm128(); //expect: IntrinsicIssue
    __builtin_ia32_pcmpgtb128(); //expect: IntrinsicIssue
    __builtin_ia32_pcmpistrm128(); //expect: IntrinsicIssue
    __builtin_ia32_pmaxsb128(); //expect: IntrinsicIssue
    __builtin_ia32_pmaxub128(); //expect: IntrinsicIssue
    __builtin_ia32_pminsb128(); //expect: IntrinsicIssue
    __builtin_ia32_pminub128(); //expect: IntrinsicIssue 
    __builtin_ia32_pshufb128(); //expect: IntrinsicIssue
    __builtin_ia32_psignb128(); //expect: IntrinsicIssue 
    __builtin_ia32_psubb128(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckhbw128(); //expect: IntrinsicIssue 
    __builtin_ia32_punpcklbw128(); //expect: IntrinsicIssue 
    __builtin_ia32_vec_set_v16qi(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcmov_v16qi(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomeqb(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomequb(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomfalseb(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomfalseub(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgeb(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgeub(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgtb(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgtub(); //expect: IntrinsicIssue  
    __builtin_ia32_vpcomleb(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomleub(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomltb(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomltub(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomneb(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomneub(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomtrueb(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomtrueub(); //expect: IntrinsicIssue 
    __builtin_ia32_vpperm(); //expect: IntrinsicIssue 
    __builtin_ia32_vprotb(); //expect: IntrinsicIssue 
    __builtin_ia32_vpshab(); //expect: IntrinsicIssue 
    __builtin_ia32_vpshlb(); //expect: IntrinsicIssue 
    __builtin_ia32_palignr(); //expect: IntrinsicIssue 
    __builtin_ia32_pmuludq(); //expect: IntrinsicIssue 
    __builtin_ia32_psadbw(); //expect: IntrinsicIssue 
    __builtin_ia32_psllqi(); //expect: IntrinsicIssue 
    __builtin_ia32_psllq(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlqi(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlq(); //expect: IntrinsicIssue 
    __builtin_ia32_addpd(); //expect: IntrinsicIssue 
    __builtin_ia32_addsd(); //expect: IntrinsicIssue 
    __builtin_ia32_addsubpd(); //expect: IntrinsicIssue 
    __builtin_ia32_andnpd(); //expect: IntrinsicIssue 
    __builtin_ia32_andpd(); //expect: IntrinsicIssue 
    __builtin_ia32_blendpd(); //expect: IntrinsicIssue 
    __builtin_ia32_blendvpd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpeqpd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpeqsd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpgepd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpgtpd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmplepd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmplesd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpltpd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpltsd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpneqpd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpneqsd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpngepd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpngtpd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpnlepd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpnlesd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpnltpd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpnltsd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpordpd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpordsd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmppd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpsd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpunordpd(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpunordsd(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtdq2pd(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtpi2pd(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtps2pd(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtsi2sd(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtsi642sd(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtss2sd(); //expect: IntrinsicIssue 
    __builtin_ia32_divpd(); //expect: IntrinsicIssue 
    __builtin_ia32_divsd(); //expect: IntrinsicIssue 
    __builtin_ia32_dppd(); //expect: IntrinsicIssue 
    __builtin_ia32_fmaddpd(); //expect: IntrinsicIssue 
    __builtin_ia32_fmaddsd(); //expect: IntrinsicIssue 
    __builtin_ia32_fmaddsubpd(); //expect: IntrinsicIssue 
    __builtin_ia32_fmsubaddpd(); //expect: IntrinsicIssue 
    __builtin_ia32_fmsubpd(); //expect: IntrinsicIssue 
    __builtin_ia32_fmsubsd(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmaddpd(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmaddsd(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmsubpd(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmsubsd(); //expect: IntrinsicIssue 
    __builtin_ia32_gatherdiv2df(); //expect: IntrinsicIssue 
    __builtin_ia32_gathersiv2df(); //expect: IntrinsicIssue 
    __builtin_ia32_haddpd(); //expect: IntrinsicIssue 
    __builtin_ia32_hsubpd(); //expect: IntrinsicIssue 
    __builtin_ia32_loadddup(); //expect: IntrinsicIssue 
    __builtin_ia32_loadhpd(); //expect: IntrinsicIssue 
    __builtin_ia32_loadlpd(); //expect: IntrinsicIssue 
    __builtin_ia32_loadupd(); //expect: IntrinsicIssue 
    __builtin_ia32_maskloadpd(); //expect: IntrinsicIssue 
    __builtin_ia32_maxpd(); //expect: IntrinsicIssue 
    __builtin_ia32_maxsd(); //expect: IntrinsicIssue 
    __builtin_ia32_minpd(); //expect: IntrinsicIssue 
    __builtin_ia32_minsd(); //expect: IntrinsicIssue 
    __builtin_ia32_movddup(); //expect: IntrinsicIssue 
    __builtin_ia32_movsd(); //expect: IntrinsicIssue  
    __builtin_ia32_mulpd(); //expect: IntrinsicIssue 
    __builtin_ia32_mulsd(); //expect: IntrinsicIssue 
    __builtin_ia32_orpd(); //expect: IntrinsicIssue 
    __builtin_ia32_pd_pd256(); //expect: IntrinsicIssue 
    __builtin_ia32_roundpd(); //expect: IntrinsicIssue 
    __builtin_ia32_roundsd(); //expect: IntrinsicIssue 
    __builtin_ia32_shufpd(); //expect: IntrinsicIssue 
    __builtin_ia32_sqrtpd(); //expect: IntrinsicIssue 
    __builtin_ia32_sqrtsd(); //expect: IntrinsicIssue 
    __builtin_ia32_subpd(); //expect: IntrinsicIssue 
    __builtin_ia32_subsd(); //expect: IntrinsicIssue 
    __builtin_ia32_unpckhpd(); //expect: IntrinsicIssue 
    __builtin_ia32_unpcklpd(); //expect: IntrinsicIssue 
    __builtin_ia32_vextractf128_pd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vfrczpd(); //expect: IntrinsicIssue 
    __builtin_ia32_vfrczsd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcmov_v2df(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermil2pd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermilpd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermilvarpd(); //expect: IntrinsicIssue 
    __builtin_ia32_xorpd(); //expect: IntrinsicIssue 
    __builtin_ia32_aesdec128(); //expect: IntrinsicIssue 
    __builtin_ia32_aesdeclast128(); //expect: IntrinsicIssue 
    __builtin_ia32_aesenc128(); //expect: IntrinsicIssue
    __builtin_ia32_aesenclast128(); //expect: IntrinsicIssue 
    __builtin_ia32_aesimc128(); //expect: IntrinsicIssue 
    __builtin_ia32_aeskeygenassist128(); //expect: IntrinsicIssue 
    __builtin_ia32_extrqi(); //expect: IntrinsicIssue 
    __builtin_ia32_extrq(); //expect: IntrinsicIssue 
    __builtin_ia32_gatherdiv2di(); //expect: IntrinsicIssue 
    __builtin_ia32_gathersiv2di(); //expect: IntrinsicIssue
    __builtin_ia32_insertqi(); //expect: IntrinsicIssue  
    __builtin_ia32_insertq(); //expect: IntrinsicIssue 
    __builtin_ia32_maskloadq(); //expect: IntrinsicIssue 
    __builtin_ia32_movntdqa(); //expect: IntrinsicIssue 
    __builtin_ia32_movq128(); //expect: IntrinsicIssue 
    __builtin_ia32_paddq128(); //expect: IntrinsicIssue 
    __builtin_ia32_paddq(); //expect: IntrinsicIssue 
    __builtin_ia32_palignr128(); //expect: IntrinsicIssue 
    __builtin_ia32_pand128(); //expect: IntrinsicIssue 
    __builtin_ia32_pandn128(); //expect: IntrinsicIssue 
    __builtin_ia32_pbroadcastq128(); //expect: IntrinsicIssue 
    __builtin_ia32_pclmulqdq128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpeqq(); //expect: IntrinsicIssue  
    __builtin_ia32_pcmpgtq(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovsxbq128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovsxdq128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovsxwq128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovzxbq128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovzxdq128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovzxwq128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmuldq128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmuludq128(); //expect: IntrinsicIssue 
    __builtin_ia32_por128(); //expect: IntrinsicIssue 
    __builtin_ia32_psadbw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pslldqi128(); //expect: IntrinsicIssue 
    __builtin_ia32_psllq128(); //expect: IntrinsicIssue 
    __builtin_ia32_psllqi128(); //expect: IntrinsicIssue 
    __builtin_ia32_psllv2di(); //expect: IntrinsicIssue 
    __builtin_ia32_psrldqi128(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlq128(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlqi128(); //expect: IntrinsicIssue  
    __builtin_ia32_psrlv2di(); //expect: IntrinsicIssue 
    __builtin_ia32_psubq128(); //expect: IntrinsicIssue 
    __builtin_ia32_psubq(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckhqdq128(); //expect: IntrinsicIssue
    __builtin_ia32_punpcklqdq128(); //expect: IntrinsicIssue 
    __builtin_ia32_pxor128(); //expect: IntrinsicIssue
    __builtin_ia32_vec_set_v2di(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcmov(); //expect: IntrinsicIssue
    __builtin_ia32_vpcmov_v2di(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomeqq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomequq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomfalseq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomfalseuq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgeq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgeuq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgtq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgtuq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomleq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomleuq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomltq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomltuq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomneq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomneuq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomtrueq(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomtrueuq(); //expect: IntrinsicIssue  
    __builtin_ia32_vphaddbq(); //expect: IntrinsicIssue 
    __builtin_ia32_vphadddq(); //expect: IntrinsicIssue 
    __builtin_ia32_vphaddubq(); //expect: IntrinsicIssue 
    __builtin_ia32_vphaddudq(); //expect: IntrinsicIssue 
    __builtin_ia32_vphadduwq(); //expect: IntrinsicIssue 
    __builtin_ia32_vphaddwq(); //expect: IntrinsicIssue
    __builtin_ia32_vphsubdq(); //expect: IntrinsicIssue
    __builtin_ia32_vpmacsdqh(); //expect: IntrinsicIssue
    __builtin_ia32_vpmacsdql(); //expect: IntrinsicIssue
    __builtin_ia32_vpmacssdqh(); //expect: IntrinsicIssue
    __builtin_ia32_vpmacssdql(); //expect: IntrinsicIssue
    __builtin_ia32_vprotq(); //expect: IntrinsicIssue
    __builtin_ia32_vpshaq(); //expect: IntrinsicIssue
    __builtin_ia32_vpshlq(); //expect: IntrinsicIssue
    __builtin_ia32_pfacc(); //expect: IntrinsicIssue
    __builtin_ia32_pfadd(); //expect: IntrinsicIssue
    __builtin_ia32_pfmax(); //expect: IntrinsicIssue 
    __builtin_ia32_pfmin(); //expect: IntrinsicIssue 
    __builtin_ia32_pfmul(); //expect: IntrinsicIssue 
    __builtin_ia32_pfnacc(); //expect: IntrinsicIssue 
    __builtin_ia32_pfpnacc(); //expect: IntrinsicIssue 
    __builtin_ia32_pfrcpit1(); //expect: IntrinsicIssue 
    __builtin_ia32_pfrcpit2(); //expect: IntrinsicIssue
    __builtin_ia32_pfrcp(); //expect: IntrinsicIssue
    __builtin_ia32_pfrsqrtit1 (); //expect: IntrinsicIssue
    __builtin_ia32_pfrsqrt(); //expect: IntrinsicIssue
    __builtin_ia32_pfsubr(); //expect: IntrinsicIssue
    __builtin_ia32_pfsub(); //expect: IntrinsicIssue
    __builtin_ia32_pi2fd(); //expect: IntrinsicIssue
    __builtin_ia32_pi2fw(); //expect: IntrinsicIssue
    __builtin_ia32_pswapdsf(); //expect: IntrinsicIssue
    __builtin_ia32_cvtpd2pi(); //expect: IntrinsicIssue
    __builtin_ia32_cvtps2pi(); //expect: IntrinsicIssue
    __builtin_ia32_cvttpd2pi(); //expect: IntrinsicIssue
    __builtin_ia32_cvttps2pi(); //expect: IntrinsicIssue
    __builtin_ia32_pabsd(); //expect: IntrinsicIssue
    __builtin_ia32_paddd(); //expect: IntrinsicIssue
    __builtin_ia32_pcmpeqd(); //expect: IntrinsicIssue
    __builtin_ia32_pcmpgtd(); //expect: IntrinsicIssue
    __builtin_ia32_pf2id(); //expect: IntrinsicIssue
    __builtin_ia32_pf2iw(); //expect: IntrinsicIssue
    __builtin_ia32_pfcmpeq(); //expect: IntrinsicIssue
    __builtin_ia32_pfcmpge(); //expect: IntrinsicIssue
    __builtin_ia32_pfcmpgt(); //expect: IntrinsicIssue
    __builtin_ia32_phaddd(); //expect: IntrinsicIssue
    __builtin_ia32_phsubd(); //expect: IntrinsicIssue
    __builtin_ia32_psignd(); //expect: IntrinsicIssue
    __builtin_ia32_pslldi(); //expect: IntrinsicIssue 
    __builtin_ia32_pslld(); //expect: IntrinsicIssue 
    __builtin_ia32_psradi(); //expect: IntrinsicIssue 
    __builtin_ia32_psrad(); //expect: IntrinsicIssue 
    __builtin_ia32_psrldi(); //expect: IntrinsicIssue 
    __builtin_ia32_psrld(); //expect: IntrinsicIssue 
    __builtin_ia32_psubd(); //expect: IntrinsicIssue 
    __builtin_ia32_pswapdsi(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckhdq(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckldq(); //expect: IntrinsicIssue 
    __builtin_ia32_psubw256(); //expect: IntrinsicIssue 
    __builtin_ia32_lddqu256(); //expect: IntrinsicIssue 
    __builtin_ia32_loaddqu256(); //expect: IntrinsicIssue 
    __builtin_ia32_mpsadbw256(); //expect: IntrinsicIssue 
    __builtin_ia32_pabsb256(); //expect: IntrinsicIssue 
    __builtin_ia32_packsswb256(); //expect: IntrinsicIssue 
    __builtin_ia32_packuswb256(); //expect: IntrinsicIssue 
    __builtin_ia32_paddb256(); //expect: IntrinsicIssue 
    __builtin_ia32_paddsb256(); //expect: IntrinsicIssue 
    __builtin_ia32_paddusb256(); //expect: IntrinsicIssue 
    __builtin_ia32_pavgb256(); //expect: IntrinsicIssue
    __builtin_ia32_pblendvb256(); //expect: IntrinsicIssue
    __builtin_ia32_pbroadcastb256(); //expect: IntrinsicIssue
    __builtin_ia32_pcmpeqb256(); //expect: IntrinsicIssue
    __builtin_ia32_pcmpgtb256(); //expect: IntrinsicIssue
    __builtin_ia32_pmaddubsw256(); //expect: IntrinsicIssue
    __builtin_ia32_pmaxsb256(); //expect: IntrinsicIssue
    __builtin_ia32_pmaxub256(); //expect: IntrinsicIssue
    __builtin_ia32_pminsb256(); //expect: IntrinsicIssue 
    __builtin_ia32_pminub256(); //expect: IntrinsicIssue
    __builtin_ia32_pshufb256(); //expect: IntrinsicIssue
    __builtin_ia32_psignb256(); //expect: IntrinsicIssue
    __builtin_ia32_psubb256(); //expect: IntrinsicIssue
    __builtin_ia32_psubsb256(); //expect: IntrinsicIssue
    __builtin_ia32_psubusb256(); //expect: IntrinsicIssue
    __builtin_ia32_punpckhbw256(); //expect: IntrinsicIssue
    __builtin_ia32_punpcklbw256(); //expect: IntrinsicIssue
    __builtin_ia32_vpcmov_v32qi256(); //expect: IntrinsicIssue
    __builtin_ia32_addpd256(); //expect: IntrinsicIssue
    __builtin_ia32_addsubpd256(); //expect: IntrinsicIssue
    __builtin_ia32_andnpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_andpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_blendpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_blendvpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_cmppd256(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtdq2pd256(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtps2pd256(); //expect: IntrinsicIssue 
    __builtin_ia32_divpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_fmaddpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_fmaddsubpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_fmsubaddpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_fmsubpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmaddpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmsubpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_gatherdiv4df(); //expect: IntrinsicIssue 
    __builtin_ia32_gathersiv4df(); //expect: IntrinsicIssue 
    __builtin_ia32_haddpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_hsubpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_loadupd256(); //expect: IntrinsicIssue
    __builtin_ia32_maskloadpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_maxpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_minpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_movddup256(); //expect: IntrinsicIssue 
    __builtin_ia32_mulpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_orpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pd256_pd(); //expect: IntrinsicIssue 
    __builtin_ia32_permdf256(); //expect: IntrinsicIssue 
    __builtin_ia32_roundpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_shufpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_sqrtpd256(); //expect: IntrinsicIssue
    __builtin_ia32_subpd256(); //expect: IntrinsicIssue
    __builtin_ia32_unpckhpd256(); //expect: IntrinsicIssue
    __builtin_ia32_unpcklpd256(); //expect: IntrinsicIssue
    __builtin_ia32_vbroadcastf128_pd256(); //expect: IntrinsicIssue  
    __builtin_ia32_vbroadcastsd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vbroadcastsd_pd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vfrczpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vinsertf128_pd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcmov_v4df256(); //expect: IntrinsicIssue 
    __builtin_ia32_vperm2f128_pd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermil2pd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermilpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermilvarpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_xorpd256(); //expect: IntrinsicIssue 
    __builtin_ia32_andnotsi256(); //expect: IntrinsicIssue 
    __builtin_ia32_andsi256(); //expect: IntrinsicIssue 
    __builtin_ia32_extract128i256(); //expect: IntrinsicIssue 
    __builtin_ia32_gatherdiv4di(); //expect: IntrinsicIssue 
    __builtin_ia32_gathersiv4di(); //expect: IntrinsicIssue 
    __builtin_ia32_insert128i256(); //expect: IntrinsicIssue 
    __builtin_ia32_maskloadq256(); //expect: IntrinsicIssue 
    __builtin_ia32_movntdqa256(); //expect: IntrinsicIssue 
    __builtin_ia32_paddq256(); //expect: IntrinsicIssue 
    __builtin_ia32_palignr256(); //expect: IntrinsicIssue 
    __builtin_ia32_pbroadcastq256(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpeqq256(); //expect: IntrinsicIssue
    __builtin_ia32_pcmpgtq256(); //expect: IntrinsicIssue
    __builtin_ia32_permdi256(); //expect: IntrinsicIssue
    __builtin_ia32_permti256(); //expect: IntrinsicIssue
    __builtin_ia32_pmovsxbq256(); //expect: IntrinsicIssue
    __builtin_ia32_pmovsxdq256(); //expect: IntrinsicIssue
    __builtin_ia32_pmovsxwq256(); //expect: IntrinsicIssue
    __builtin_ia32_pmovzxbq256(); //expect: IntrinsicIssue
    __builtin_ia32_pmovzxdq256(); //expect: IntrinsicIssue
    __builtin_ia32_pmovzxwq256(); //expect: IntrinsicIssue
    __builtin_ia32_pmuldq256(); //expect: IntrinsicIssue
    __builtin_ia32_pmuludq256(); //expect: IntrinsicIssue
    __builtin_ia32_por256(); //expect: IntrinsicIssue
    __builtin_ia32_pslldqi256(); //expect: IntrinsicIssue
    __builtin_ia32_psllq256(); //expect: IntrinsicIssue
    __builtin_ia32_psllqi256(); //expect: IntrinsicIssue
    __builtin_ia32_psllv4di(); //expect: IntrinsicIssue
    __builtin_ia32_psrldqi256(); //expect: IntrinsicIssue
    __builtin_ia32_psrlq256(); //expect: IntrinsicIssue
    __builtin_ia32_psrlqi256(); //expect: IntrinsicIssue
    __builtin_ia32_psrlv4di(); //expect: IntrinsicIssue 
    __builtin_ia32_psubq256(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckhqdq256(); //expect: IntrinsicIssue 
    __builtin_ia32_punpcklqdq256(); //expect: IntrinsicIssue  
    __builtin_ia32_pxor256(); //expect: IntrinsicIssue 
    __builtin_ia32_vbroadcastsi256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcmov_v4di256(); //expect: IntrinsicIssue 
    __builtin_ia32_pabsw(); //expect: IntrinsicIssue 
    __builtin_ia32_packssdw(); //expect: IntrinsicIssue 
    __builtin_ia32_paddsw(); //expect: IntrinsicIssue 
    __builtin_ia32_paddusw(); //expect: IntrinsicIssue 
    __builtin_ia32_paddw(); //expect: IntrinsicIssue 
    __builtin_ia32_pavgw(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpeqw(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpgtw(); //expect: IntrinsicIssue 
    __builtin_ia32_phaddsw(); //expect: IntrinsicIssue 
    __builtin_ia32_phaddw(); //expect: IntrinsicIssue 
    __builtin_ia32_phsubsw(); //expect: IntrinsicIssue 
    __builtin_ia32_phsubw(); //expect: IntrinsicIssue 
    __builtin_ia32_pinsrw(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaddubsw(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaxsw(); //expect: IntrinsicIssue 
    __builtin_ia32_pminsw(); //expect: IntrinsicIssue 
    __builtin_ia32_pmulhrsw(); //expect: IntrinsicIssue 
    __builtin_ia32_pmulhrw(); //expect: IntrinsicIssue 
    __builtin_ia32_pmulhuw(); //expect: IntrinsicIssue 
    __builtin_ia32_pmulhw(); //expect: IntrinsicIssue 
    __builtin_ia32_pmullw(); //expect: IntrinsicIssue 
    __builtin_ia32_psignw(); //expect: IntrinsicIssue 
    __builtin_ia32_psllwi(); //expect: IntrinsicIssue 
    __builtin_ia32_psllw(); //expect: IntrinsicIssue 
    __builtin_ia32_psrawi(); //expect: IntrinsicIssue 
    __builtin_ia32_psraw(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlwi(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlw(); //expect: IntrinsicIssue 
    __builtin_ia32_psubsw(); //expect: IntrinsicIssue 
    __builtin_ia32_psubusw(); //expect: IntrinsicIssue 
    __builtin_ia32_psubw(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckhwd(); //expect: IntrinsicIssue 
    __builtin_ia32_punpcklwd(); //expect: IntrinsicIssue 
    __builtin_ia32_addps(); //expect: IntrinsicIssue 
    __builtin_ia32_addss(); //expect: IntrinsicIssue 
    __builtin_ia32_addsubps(); //expect: IntrinsicIssue 
    __builtin_ia32_andnps(); //expect: IntrinsicIssue 
    __builtin_ia32_andps(); //expect: IntrinsicIssue 
    __builtin_ia32_blendps(); //expect: IntrinsicIssue 
    __builtin_ia32_blendvps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpss(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtdq2ps(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtpd2ps256(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtpd2ps(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtpi2ps(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtsd2ss(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtsi2ss(); //expect: IntrinsicIssue 
    __builtin_ia32_divps(); //expect: IntrinsicIssue 
    __builtin_ia32_divss(); //expect: IntrinsicIssue 
    __builtin_ia32_dpps(); //expect: IntrinsicIssue 
    __builtin_ia32_fmaddps(); //expect: IntrinsicIssue 
    __builtin_ia32_fmaddss(); //expect: IntrinsicIssue 
    __builtin_ia32_fmaddsubps(); //expect: IntrinsicIssue 
    __builtin_ia32_fmsubaddps(); //expect: IntrinsicIssue 
    __builtin_ia32_fmsubps(); //expect: IntrinsicIssue 
    __builtin_ia32_fmsubss(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmaddps(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmaddss(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmsubps(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmsubss(); //expect: IntrinsicIssue 
    __builtin_ia32_gatherdiv4sf256(); //expect: IntrinsicIssue 
    __builtin_ia32_gatherdiv4sf(); //expect: IntrinsicIssue 
    __builtin_ia32_gathersiv4sf(); //expect: IntrinsicIssue 
    __builtin_ia32_haddps(); //expect: IntrinsicIssue 
    __builtin_ia32_hsubps(); //expect: IntrinsicIssue 
    __builtin_ia32_insertps128(); //expect: IntrinsicIssue 
    __builtin_ia32_loadaps(); //expect: IntrinsicIssue 
    __builtin_ia32_loadhps(); //expect: IntrinsicIssue 
    __builtin_ia32_loadlps(); //expect: IntrinsicIssue 
    __builtin_ia32_loadsss(); //expect: IntrinsicIssue 
    __builtin_ia32_loadups(); //expect: IntrinsicIssue 
    __builtin_ia32_maskloadps(); //expect: IntrinsicIssue 
    __builtin_ia32_maxps(); //expect: IntrinsicIssue 
    __builtin_ia32_maxss(); //expect: IntrinsicIssue 
    __builtin_ia32_minps(); //expect: IntrinsicIssue 
    __builtin_ia32_minss(); //expect: IntrinsicIssue 
    __builtin_ia32_movhlps(); //expect: IntrinsicIssue 
    __builtin_ia32_movlhps(); //expect: IntrinsicIssue 
    __builtin_ia32_movshdup(); //expect: IntrinsicIssue 
    __builtin_ia32_movsldup(); //expect: IntrinsicIssue 
    __builtin_ia32_movss(); //expect: IntrinsicIssue 
    __builtin_ia32_mulps(); //expect: IntrinsicIssue 
    __builtin_ia32_mulss(); //expect: IntrinsicIssue 
    __builtin_ia32_orps(); //expect: IntrinsicIssue 
    __builtin_ia32_ps_ps256(); //expect: IntrinsicIssue 
    __builtin_ia32_rcpps(); //expect: IntrinsicIssue 
    __builtin_ia32_rcpss(); //expect: IntrinsicIssue 
    __builtin_ia32_roundps(); //expect: IntrinsicIssue 
    __builtin_ia32_roundss(); //expect: IntrinsicIssue 
    __builtin_ia32_rsqrtps(); //expect: IntrinsicIssue 
    __builtin_ia32_rsqrtss(); //expect: IntrinsicIssue 
    __builtin_ia32_shufps(); //expect: IntrinsicIssue 
    __builtin_ia32_sqrtps(); //expect: IntrinsicIssue 
    __builtin_ia32_sqrtss(); //expect: IntrinsicIssue 
    __builtin_ia32_subps(); //expect: IntrinsicIssue 
    __builtin_ia32_subss(); //expect: IntrinsicIssue 
    __builtin_ia32_unpckhps(); //expect: IntrinsicIssue 
    __builtin_ia32_unpcklps(); //expect: IntrinsicIssue 
    __builtin_ia32_vbroadcastss(); //expect: IntrinsicIssue 
    __builtin_ia32_vbroadcastss_ps(); //expect: IntrinsicIssue 
    __builtin_ia32_vec_set_v4sf(); //expect: IntrinsicIssue 
    __builtin_ia32_vextractf128_ps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vfrczps(); //expect: IntrinsicIssue 
    __builtin_ia32_vfrczss(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcmov_v4sf(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermil2ps(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermilps(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermilvarps(); //expect: IntrinsicIssue 
    __builtin_ia32_xorps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpeqps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpeqss(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpgeps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpgtps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpleps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpless(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpltps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpltss(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpneqps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpneqss(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpngeps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpngtps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpnleps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpnless(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpnltps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpnlts(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpordps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpordss(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpunordps(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpunordss(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtpd2dq256(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtpd2dq(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtps2dq(); //expect: IntrinsicIssue 
    __builtin_ia32_cvttpd2dq256(); //expect: IntrinsicIssue 
    __builtin_ia32_cvttpd2dq(); //expect: IntrinsicIssue 
    __builtin_ia32_cvttps2dq(); //expect: IntrinsicIssue 
    __builtin_ia32_gatherdiv4si256(); //expect: IntrinsicIssue 
    __builtin_ia32_gatherdiv4si(); //expect: IntrinsicIssue 
    __builtin_ia32_gathersiv4si(); //expect: IntrinsicIssue 
    __builtin_ia32_maskloadd(); //expect: IntrinsicIssue 
    __builtin_ia32_pabsd128(); //expect: IntrinsicIssue 
    __builtin_ia32_paddd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pblendd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pbroadcastd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpeqd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpgtd128(); //expect: IntrinsicIssue 
    __builtin_ia32_phaddd128(); //expect: IntrinsicIssue 
    __builtin_ia32_phsubd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaddwd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaxsd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaxud128(); //expect: IntrinsicIssue 
    __builtin_ia32_pminsd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pminud128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovsxbd128(); //expect: IntrinsicIssue
    __builtin_ia32_pmovsxwd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovzxbd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovzxwd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmulld128(); //expect: IntrinsicIssue 
    __builtin_ia32_pshufd(); //expect: IntrinsicIssue 
    __builtin_ia32_psignd128(); //expect: IntrinsicIssue 
    __builtin_ia32_pslld128(); //expect: IntrinsicIssue 
    __builtin_ia32_pslldi128(); //expect: IntrinsicIssue 
    __builtin_ia32_psllv4si(); //expect: IntrinsicIssue 
    __builtin_ia32_psrad128(); //expect: IntrinsicIssue 
    __builtin_ia32_psradi128(); //expect: IntrinsicIssue 
    __builtin_ia32_psrav4si(); //expect: IntrinsicIssue 
    __builtin_ia32_psrld128(); //expect: IntrinsicIssue 
    __builtin_ia32_psrldi128(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlv4si(); //expect: IntrinsicIssue 
    __builtin_ia32_psubd128(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckhdq128(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckldq128(); //expect: IntrinsicIssue 
    __builtin_ia32_si_si256(); //expect: IntrinsicIssue 
    __builtin_ia32_vec_set_v4si(); //expect: IntrinsicIssue 
    __builtin_ia32_vextractf128_si256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcmov_v4si(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomeqd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomequd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomfalsed(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomfalseud(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomged(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgeud(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgtd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgtud(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomled(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomleud(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomltd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomltud(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomned(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomneud(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomtrued(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomtrueud(); //expect: IntrinsicIssue 
    __builtin_ia32_vphaddbd(); //expect: IntrinsicIssue 
    __builtin_ia32_vphaddubd(); //expect: IntrinsicIssue 
    __builtin_ia32_vphadduwd(); //expect: IntrinsicIssue 
    __builtin_ia32_vphaddwd(); //expect: IntrinsicIssue 
    __builtin_ia32_vphsubwd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpmacsdd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpmacssdd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpmacsswd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpmacswd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpmadcsswd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpmadcswd(); //expect: IntrinsicIssue 
    __builtin_ia32_vprotd(); //expect: IntrinsicIssue 
    __builtin_ia32_vpshad(); //expect: IntrinsicIssue 
    __builtin_ia32_vpshld(); //expect: IntrinsicIssue 
    __builtin_ia32_pabsw128(); //expect: IntrinsicIssue 
    __builtin_ia32_packssdw128(); //expect: IntrinsicIssue 
    __builtin_ia32_packusdw128(); //expect: IntrinsicIssue 
    __builtin_ia32_paddw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pavgw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pblendw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pbroadcastw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpeqw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpgtw128(); //expect: IntrinsicIssue 
    __builtin_ia32_phaddsw128(); //expect: IntrinsicIssue 
    __builtin_ia32_phaddw128(); //expect: IntrinsicIssue 
    __builtin_ia32_phminposuw128(); //expect: IntrinsicIssue 
    __builtin_ia32_phsubsw128(); //expect: IntrinsicIssue 
    __builtin_ia32_phsubw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaddubsw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaxsw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaxuw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pminsw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pminuw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovsxbw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovzxbw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmulhrsw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmulhuw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmulhw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pmullw128(); //expect: IntrinsicIssue 
    __builtin_ia32_pshufhw(); //expect: IntrinsicIssue 
    __builtin_ia32_pshuflw(); //expect: IntrinsicIssue 
    __builtin_ia32_psignw128(); //expect: IntrinsicIssue 
    __builtin_ia32_psllw128(); //expect: IntrinsicIssue 
    __builtin_ia32_psllwi128(); //expect: IntrinsicIssue 
    __builtin_ia32_psraw128(); //expect: IntrinsicIssue 
    __builtin_ia32_psrawi128(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlw128(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlwi128(); //expect: IntrinsicIssue 
    __builtin_ia32_psubw128(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckhwd128(); //expect: IntrinsicIssue 
    __builtin_ia32_punpcklwd128(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcmov_v8hi(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomequw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomeqw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomfalseuw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomfalsew(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgeuw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgew(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgtuw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomgtw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomleuw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomlew(); //expect: IntrinsicIssue  
    __builtin_ia32_vpcomltuw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomltw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomneuw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomnew(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomtrueuw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcomtruew(); //expect: IntrinsicIssue 
    __builtin_ia32_vphaddbw(); //expect: IntrinsicIssue 
    __builtin_ia32_vphaddubw(); //expect: IntrinsicIssue 
    __builtin_ia32_vphsubbw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpmacssww(); //expect: IntrinsicIssue 
    __builtin_ia32_vpmacsww(); //expect: IntrinsicIssue 
    __builtin_ia32_vprotw(); //expect: IntrinsicIssue
    __builtin_ia32_vpshaw(); //expect: IntrinsicIssue 
    __builtin_ia32_vpshlw(); //expect: IntrinsicIssue 
    __builtin_ia32_pabsb(); //expect: IntrinsicIssue 
    __builtin_ia32_packsswb(); //expect: IntrinsicIssue 
    __builtin_ia32_packuswb(); //expect: IntrinsicIssue 
    __builtin_ia32_paddb(); //expect: IntrinsicIssue 
    __builtin_ia32_paddsb(); //expect: IntrinsicIssue 
    __builtin_ia32_paddusb(); //expect: IntrinsicIssue 
    __builtin_ia32_pavgb(); //expect: IntrinsicIssue 
    __builtin_ia32_pavgusb(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpeqb(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpgtb(); //expect: IntrinsicIssue
    __builtin_ia32_pmaxub(); //expect: IntrinsicIssue 
    __builtin_ia32_pminub(); //expect: IntrinsicIssue 
    __builtin_ia32_pshufb(); //expect: IntrinsicIssue 
    __builtin_ia32_psignb(); //expect: IntrinsicIssue  
    __builtin_ia32_psubb(); //expect: IntrinsicIssue 
    __builtin_ia32_psubsb(); //expect: IntrinsicIssue 
    __builtin_ia32_psubusb(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckhbw(); //expect: IntrinsicIssue 
    __builtin_ia32_punpcklbw(); //expect: IntrinsicIssue 
    __builtin_ia32_addps256(); //expect: IntrinsicIssue 
    __builtin_ia32_addsubps256(); //expect: IntrinsicIssue 
    __builtin_ia32_andnps256(); //expect: IntrinsicIssue 
    __builtin_ia32_andps256(); //expect: IntrinsicIssue 
    __builtin_ia32_blendps256(); //expect: IntrinsicIssue 
    __builtin_ia32_blendvps256(); //expect: IntrinsicIssue 
    __builtin_ia32_cmpps256(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtdq2ps256(); //expect: IntrinsicIssue 
    __builtin_ia32_divps256(); //expect: IntrinsicIssue 
    __builtin_ia32_dpps256(); //expect: IntrinsicIssue 
    __builtin_ia32_fmaddps256(); //expect: IntrinsicIssue 
    __builtin_ia32_fmaddsubps256(); //expect: IntrinsicIssue 
    __builtin_ia32_fmsubaddps256(); //expect: IntrinsicIssue 
    __builtin_ia32_fmsubps256(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmaddps256(); //expect: IntrinsicIssue 
    __builtin_ia32_fnmsubps256(); //expect: IntrinsicIssue 
    __builtin_ia32_gathersiv8sf(); //expect: IntrinsicIssue 
    __builtin_ia32_haddps256(); //expect: IntrinsicIssue 
    __builtin_ia32_hsubps256(); //expect: IntrinsicIssue 
    __builtin_ia32_loadups256(); //expect: IntrinsicIssue 
    __builtin_ia32_maskloadps256(); //expect: IntrinsicIssue 
    __builtin_ia32_maxps256(); //expect: IntrinsicIssue 
    __builtin_ia32_minps256(); //expect: IntrinsicIssue 
    __builtin_ia32_movshdup256(); //expect: IntrinsicIssue 
    __builtin_ia32_movsldup256(); //expect: IntrinsicIssue 
    __builtin_ia32_mulps256(); //expect: IntrinsicIssue 
    __builtin_ia32_orps256(); //expect: IntrinsicIssue 
    __builtin_ia32_permvarsf256(); //expect: IntrinsicIssue 
    __builtin_ia32_ps256_ps(); //expect: IntrinsicIssue
    __builtin_ia32_rcpps256(); //expect: IntrinsicIssue 
    __builtin_ia32_roundps256(); //expect: IntrinsicIssue 
    __builtin_ia32_rsqrtps256(); //expect: IntrinsicIssue 
    __builtin_ia32_rsqrtps_nr256(); //expect: IntrinsicIssue 
    __builtin_ia32_shufps256(); //expect: IntrinsicIssue 
    __builtin_ia32_sqrtps256(); //expect: IntrinsicIssue 
    __builtin_ia32_sqrtps_nr256(); //expect: IntrinsicIssue 
    __builtin_ia32_subps256(); //expect: IntrinsicIssue 
    __builtin_ia32_unpckhps256(); //expect: IntrinsicIssue 
    __builtin_ia32_unpcklps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vbroadcastf128_ps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vbroadcastss256(); //expect: IntrinsicIssue 
    __builtin_ia32_vbroadcastss_ps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vfrczps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vinsertf128_ps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcmov_v8sf256(); //expect: IntrinsicIssue 
    __builtin_ia32_vperm2f128_ps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermil2ps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermilps256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpermilvarps256(); //expect: IntrinsicIssue 
    __builtin_ia32_xorps256(); //expect: IntrinsicIssue 
    __builtin_ia32_cvtps2dq256(); //expect: IntrinsicIssue 
    __builtin_ia32_cvttps2dq256(); //expect: IntrinsicIssue 
    __builtin_ia32_gathersiv8si(); //expect: IntrinsicIssue 
    __builtin_ia32_maskloadd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pabsd256(); //expect: IntrinsicIssue 
    __builtin_ia32_paddd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pblendd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pbroadcastd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpeqd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pcmpgtd256(); //expect: IntrinsicIssue 
    __builtin_ia32_permvarsi256(); //expect: IntrinsicIssue 
    __builtin_ia32_phaddd256(); //expect: IntrinsicIssue 
    __builtin_ia32_phsubd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaxsd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmaxud256(); //expect: IntrinsicIssue 
    __builtin_ia32_pminsd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pminud256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovsxbd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovsxwd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovzxbd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmovzxwd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pmulld256(); //expect: IntrinsicIssue 
    __builtin_ia32_pshufd256(); //expect: IntrinsicIssue 
    __builtin_ia32_psignd256(); //expect: IntrinsicIssue 
    __builtin_ia32_pslld256(); //expect: IntrinsicIssue 
    __builtin_ia32_pslldi256(); //expect: IntrinsicIssue 
    __builtin_ia32_psllv8si(); //expect: IntrinsicIssue 
    __builtin_ia32_psrad256(); //expect: IntrinsicIssue 
    __builtin_ia32_psradi256(); //expect: IntrinsicIssue 
    __builtin_ia32_psrav8si(); //expect: IntrinsicIssue 
    __builtin_ia32_psrld256(); //expect: IntrinsicIssue 
    __builtin_ia32_psrldi256(); //expect: IntrinsicIssue 
    __builtin_ia32_psrlv8si(); //expect: IntrinsicIssue 
    __builtin_ia32_psubd256(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckhdq256(); //expect: IntrinsicIssue 
    __builtin_ia32_punpckldq256(); //expect: IntrinsicIssue 
    __builtin_ia32_si256_si(); //expect: IntrinsicIssue
    __builtin_ia32_vinsertf128_si256(); //expect: IntrinsicIssue 
    __builtin_ia32_vpcmov_v8si256(); //expect: IntrinsicIssue 
    __builtin_ia32_vperm2f128_si256(); //expect: IntrinsicIssue 
    __addfsbyte(); //expect: IntrinsicIssue 
    __addfsdword(); //expect: IntrinsicIssue 
    __addfsword(); //expect: IntrinsicIssue 
    __addgsbyte(); //expect: IntrinsicIssue 
    __addgsdword(); //expect: IntrinsicIssue 
    __addgsqword(); //expect: IntrinsicIssue 
    __addgsword(); //expect: IntrinsicIssue 
    __builtin_cpu_init(); //expect: IntrinsicIssue 
    __builtin_ia32_clflush(); //expect: IntrinsicIssue 
    __builtin_ia32_femms(); //expect: IntrinsicIssue 
    __builtin_ia32_lfence(); //expect: IntrinsicIssue 
    __builtin_ia32_llwpcb16(); //expect: IntrinsicIssue
    __builtin_ia32_llwpcb16(); //expect: IntrinsicIssue
    __builtin_ia32_llwpcb32(); //expect: IntrinsicIssue
    __builtin_ia32_llwpcb32(); //expect: IntrinsicIssue
    __builtin_ia32_llwpcb64(); //expect: IntrinsicIssue
    __builtin_ia32_llwpcb64(); //expect: IntrinsicIssue
    __builtin_ia32_lwpval16(); //expect: IntrinsicIssue 
    __builtin_ia32_lwpval32(); //expect: IntrinsicIssue 
    __builtin_ia32_lwpval64(); //expect: IntrinsicIssue 
    __builtin_ia32_maskmovdqu(); //expect: IntrinsicIssue 
    __builtin_ia32_maskmovq(); //expect: IntrinsicIssue 
    __builtin_ia32_maskstored256(); //expect: IntrinsicIssue  
    __builtin_ia32_maskstored(); //expect: IntrinsicIssue 
    __builtin_ia32_maskstorepd256(); //expect: IntrinsicIssue 
    __builtin_ia32_maskstorepd(); //expect: IntrinsicIssue 
    __builtin_ia32_maskstoreps256(); //expect: IntrinsicIssue 
    __builtin_ia32_maskstoreps(); //expect: IntrinsicIssue 
    __builtin_ia32_maskstoreq256(); //expect: IntrinsicIssue 
    __builtin_ia32_maskstoreq(); //expect: IntrinsicIssue 
    __builtin_ia32_mfence(); //expect: IntrinsicIssue 
    __builtin_ia32_monitor(); //expect: IntrinsicIssue 
    __builtin_ia32_movntdq(); //expect: IntrinsicIssue 
    __builtin_ia32_movnti64(); //expect: IntrinsicIssue 
    __builtin_ia32_movnti(); //expect: IntrinsicIssue 
    __builtin_ia32_movntpd(); //expect: IntrinsicIssue 
    __builtin_ia32_movntps(); //expect: IntrinsicIssue 
    __builtin_ia32_movntq(); //expect: IntrinsicIssue 
    __builtin_ia32_movntsd(); //expect: IntrinsicIssue 
    __builtin_ia32_movntss(); //expect: IntrinsicIssue 
    __builtin_ia32_mwait(); //expect: IntrinsicIssue 
    __builtin_ia32_pause(); //expect: IntrinsicIssue 
    __builtin_ia32_sfence(); //expect: IntrinsicIssue 
    __builtin_ia32_storeaps(); //expect: IntrinsicIssue 
    __builtin_ia32_storedqu256(); //expect: IntrinsicIssue 
    __builtin_ia32_storedqu(); //expect: IntrinsicIssue 
    __builtin_ia32_storehps(); //expect: IntrinsicIssue 
    __builtin_ia32_storelps(); //expect: IntrinsicIssue 
    __builtin_ia32_storess(); //expect: IntrinsicIssue 
    __builtin_ia32_storeupd256(); //expect: IntrinsicIssue 
    __builtin_ia32_storeupd(); //expect: IntrinsicIssue 
    __builtin_ia32_storeups256(); //expect: IntrinsicIssue 
    __builtin_ia32_storeups(); //expect: IntrinsicIssue 
    __builtin_ia32_vzeroall(); //expect: IntrinsicIssue 
    __builtin_ia32_vzeroupper(); //expect: IntrinsicIssue 
    __builtin_ia32_xabort(); //expect: IntrinsicIssue 
    __builtin_ia32_xend(); //expect: IntrinsicIssue 
    _clac(); //expect: IntrinsicIssue 
    __cpuidex(); //expect: IntrinsicIssue 
    __cpuid(); //expect: IntrinsicIssue  
    __faststorefence(); //expect: IntrinsicIssue 
    _fxrstor64(); //expect: IntrinsicIssue 
    _fxrstor(); //expect: IntrinsicIssue 
    _fxsave64(); //expect: IntrinsicIssue 
    _fxsave(); //expect: IntrinsicIssue 
    __halt(); //expect: IntrinsicIssue 
    __inbytestring(); //expect: IntrinsicIssue 
    __incfsbyte(); //expect: IntrinsicIssue 
    __incfsdword(); //expect: IntrinsicIssue 
    __incfsword(); //expect: IntrinsicIssue 
    __incgsbyte(); //expect: IntrinsicIssue 
    __incgsdword(); //expect: IntrinsicIssue 
    __incgsqword(); //expect: IntrinsicIssue 
    __incgsword(); //expect: IntrinsicIssue 
    __indwordstring(); //expect: IntrinsicIssue 
    __int2c(); //expect: IntrinsicIssue 
    _InterlockedCompareExchangePointer_HLEAcquire(); //expect: IntrinsicIssue 
    _InterlockedCompareExchangePointer_HLERelease(); //expect: IntrinsicIssue 
    _InterlockedCompareExchangePointer_np(); //expect: IntrinsicIssue 
    _InterlockedExchangePointer_HLEAcquire(); //expect: IntrinsicIssue 
    _InterlockedExchangePointer_HLERelease(); //expect: IntrinsicIssue 
    __invlpg(); //expect: IntrinsicIssue 
    _invpcid(); //expect: IntrinsicIssue 
    __inwordstring(); //expect: IntrinsicIssue 
    _lgdt(); //expect: IntrinsicIssue 
    __lidt(); //expect: IntrinsicIssue 
    __llwpcb(); //expect: IntrinsicIssue 
    __lwpval32(); //expect: IntrinsicIssue 
    __lwpval64(); //expect: IntrinsicIssue 
    _m_empty(); //expect: IntrinsicIssue 
    _m_femms(); //expect: IntrinsicIssue 
    _mm256_maskstore_epi32(); //expect: IntrinsicIssue 
    _mm256_maskstore_epi64(); //expect: IntrinsicIssue 
    _mm256_maskstore_pd(); //expect: IntrinsicIssue 
    _mm256_maskstore_ps(); //expect: IntrinsicIssue 
    _mm256_store_pd(); //expect: IntrinsicIssue 
    _mm256_store_ps(); //expect: IntrinsicIssue 
    _mm256_store_si256(); //expect: IntrinsicIssue 
    _mm256_storeu_pd(); //expect: IntrinsicIssue 
    _mm256_storeu_ps(); //expect: IntrinsicIssue 
    _mm256_storeu_si256(); //expect: IntrinsicIssue 
    __mm256_stream_pd(); //expect: IntrinsicIssue 
    _mm256_stream_ps(); //expect: IntrinsicIssue 
    __mm256_stream_si256(); //expect: IntrinsicIssue 
    _mm256_zeroall(); //expect: IntrinsicIssue 
    _mm256_zeroupper(); //expect: IntrinsicIssue 
    _m_maskmovq(); //expect: IntrinsicIssue 
    _mm_clflush(); //expect: IntrinsicIssue 
    _mm_lfence(); //expect: IntrinsicIssue 
    _mm_maskmoveu_si128(); //expect: IntrinsicIssue 
    _mm_maskstore_epi32(); //expect: IntrinsicIssue 
    _mm_maskstore_epi64(); //expect: IntrinsicIssue 
    _mm_maskstore_pd(); //expect: IntrinsicIssue 
    _mm_maskstore_ps(); //expect: IntrinsicIssue 
    _mm_mfence(); //expect: IntrinsicIssue 
    _mm_monitor(); //expect: IntrinsicIssue 
    _mm_mwait(); //expect: IntrinsicIssue 
    _mm_pause(); //expect: IntrinsicIssue 
    _mm_prefetch(); //expect: IntrinsicIssue 
    _mm_setcsr(); //expect: IntrinsicIssue 
    _mm_sfence(); //expect: IntrinsicIssue  
    _mm_store1_pd(); //expect: IntrinsicIssue 
    _mm_storeh_pd(); //expect: IntrinsicIssue 
    _mm_storeh_pi(); //expect: IntrinsicIssue 
    _mm_storel_epi64(); //expect: IntrinsicIssue 
    _mm_storel_pd(); //expect: IntrinsicIssue 
    _mm_storel_pi(); //expect: IntrinsicIssue 
    _mm_store_pd(); //expect: IntrinsicIssue 
    _mm_store_ps1(); //expect: IntrinsicIssue 
    _mm_store_ps(); //expect: IntrinsicIssue 
    _mm_storer_pd(); //expect: IntrinsicIssue 
    _mm_storer_ps(); //expect: IntrinsicIssue 
    _mm_store_sd(); //expect: IntrinsicIssue 
    _mm_store_si128(); //expect: IntrinsicIssue 
    _mm_store_ss(); //expect: IntrinsicIssue 
    _mm_storeu_pd(); //expect: IntrinsicIssue 
    _mm_storeu_ps(); //expect: IntrinsicIssue 
    _mm_storeu_si128(); //expect: IntrinsicIssue 
    _mm_stream_pd(); //expect: IntrinsicIssue 
    _mm_stream_pd(); //expect: IntrinsicIssue 
    _mm_stream_pi(); //expect: IntrinsicIssue 
    _mm_stream_ps(); //expect: IntrinsicIssue 
    _mm_stream_sd(); //expect: IntrinsicIssue 
    _mm_stream_si128(); //expect: IntrinsicIssue 
    _mm_stream_si32(); //expect: IntrinsicIssue 
    _mm_stream_si64x(); //expect: IntrinsicIssue 
    _mm_stream_ss(); //expect: IntrinsicIssue 
    __movsb(); //expect: IntrinsicIssue 
    __movsd(); //expect: IntrinsicIssue 
    __movsq(); //expect: IntrinsicIssue 
    __movsw(); //expect: IntrinsicIssue 
    _m_prefetch(); //expect: IntrinsicIssue 
    _m_prefetchw(); //expect: IntrinsicIssue 
    __nvreg_restore_fence(); //expect: IntrinsicIssue 
    __nvreg_save_fence(); //expect: IntrinsicIssue 
    __outbytestring(); //expect: IntrinsicIssue 
    __outbyte(); //expect: IntrinsicIssue 
    __outdwordstring(); //expect: IntrinsicIssue 
    __outdword(); //expect: IntrinsicIssue 
    __outwordstring(); //expect: IntrinsicIssue 
    __outword(); //expect: IntrinsicIssue 
    _rsm(); //expect: IntrinsicIssue 
    _sgdt(); //expect: IntrinsicIssue 
    _sgdt(); //expect: IntrinsicIssue 
    __sidt(); //expect: IntrinsicIssue 
    * __slwpcb(); //expect: IntrinsicIssue 
    _stac(); //expect: IntrinsicIssue 
    _Store64_HLERelease(); //expect: IntrinsicIssue 
    _storebe_i16(); //expect: IntrinsicIssue 
    _storebe_i32(); //expect: IntrinsicIssue 
    _storebe_i64(); //expect: IntrinsicIssue 
    _store_be_u16(); //expect: IntrinsicIssue 
    _store_be_u32(); //expect: IntrinsicIssue 
    _store_be_u64(); //expect: IntrinsicIssue 
    _Store_HLERelease(); //expect: IntrinsicIssue 
    _StorePointer_HLERelease(); //expect: IntrinsicIssue 
    __stosb(); //expect: IntrinsicIssue 
    __stosd(); //expect: IntrinsicIssue 
    __stosq(); //expect: IntrinsicIssue 
    __stosw(); //expect: IntrinsicIssue 
    __svm_clgi(); //expect: IntrinsicIssue 
    __svm_invlpga(); //expect: IntrinsicIssue 
    __svm_skinit(); //expect: IntrinsicIssue 
    __svm_stgi(); //expect: IntrinsicIssue 
    __svm_vmload(); //expect: IntrinsicIssue 
    __svm_vmrun(); //expect: IntrinsicIssue 
    __svm_vmsave(); //expect: IntrinsicIssue 
    __ud2(); //expect: IntrinsicIssue 
    __vmx_off(); //expect: IntrinsicIssue  
    __vmx_vmptrst(); //expect: IntrinsicIssue 
    __wbinvd(); //expect: IntrinsicIssue 
    __writecr0(); //expect: IntrinsicIssue 
    __writecr0(); //expect: IntrinsicIssue 
    __writecr3(); //expect: IntrinsicIssue 
    __writecr3(); //expect: IntrinsicIssue 
    __writecr4(); //expect: IntrinsicIssue 
    __writecr4(); //expect: IntrinsicIssue 
    __writecr8(); //expect: IntrinsicIssue 
    __writecr8(); //expect: IntrinsicIssue 
    __writedr(); //expect: IntrinsicIssue 
    __writedr(); //expect: IntrinsicIssue 
    __writeeflags(); //expect: IntrinsicIssue 
    __writeeflags(); //expect: IntrinsicIssue 
    _writefsbase_u32(); //expect: IntrinsicIssue 
    _writefsbase_u64(); //expect: IntrinsicIssue 
    _writefsbase_u64(); //expect: IntrinsicIssue 
    __writefsbyte(); //expect: IntrinsicIssue 
    __writefsdword(); //expect: IntrinsicIssue 
    __writefsword(); //expect: IntrinsicIssue 
    _writegsbase_u32(); //expect: IntrinsicIssue 
    _writegsbase_u64(); //expect: IntrinsicIssue 
    _writegsbase_u64(); //expect: IntrinsicIssue 
    __writegsbyte(); //expect: IntrinsicIssue 
    __writegsdword(); //expect: IntrinsicIssue 
    __writegsqword(); //expect: IntrinsicIssue 
    __writegsword(); //expect: IntrinsicIssue 
    __writemsr(); //expect: IntrinsicIssue 
    _xrstor64(); //expect: IntrinsicIssue 
    _xrstor(); //expect: IntrinsicIssue 
    _xsave64(); //expect: IntrinsicIssue 
    _xsaveopt64(); //expect: IntrinsicIssue 
    _xsaveopt(); //expect: IntrinsicIssue 
    _xsave(); //expect: IntrinsicIssue 
    _xsetbv(); //expect: IntrinsicIssue 
}

// shall generate issue in aarch64.
void OTHER_ARCH_INTRINSICS()
{
    _addcary(); //expect: IntrinsicIssue 
    _allow_cpu_features(); //expect: IntrinsicIssue 
    _bit_scan_(); //expect: IntrinsicIssue 
    _bnd_(); //expect: IntrinsicIssue 
    _rdpip_(); //expect: IntrinsicIssue 
    _rotwa(); //expect: IntrinsicIssue 
    vec_v(); //expect: IntrinsicIssue 
    _otherarch_intrinsic_(); //expect: IntrinsicIssue 
}

// shall generate issue in aarch64.
void INCOMPATIBLE_UCRT_INTRINSICS()
{
    _abs64(); //expect: IntrinsicIssue
    _alloca(); //expect: IntrinsicIssue
    _byteswap_uint64(); //expect: IntrinsicIssue
    _byteswap_ulong(); //expect: IntrinsicIssue
    _byteswap_ushort(); //expect: IntrinsicIssue
    _lrotl(); //expect: IntrinsicIssue
    _lrotr(); //expect: IntrinsicIssue
    _rotl(); //expect: IntrinsicIssue
    _rotl64(); //expect: IntrinsicIssue
    _rotr(); //expect: IntrinsicIssue
    _rotr64(); //expect: IntrinsicIssue
    _strset(); //expect: IntrinsicIssue
    _wcsset(); //expect: IntrinsicIssue
    wcscat();
    strset(); //expect: IntrinsicIssue
    wcscmp();
    wcslen();
}