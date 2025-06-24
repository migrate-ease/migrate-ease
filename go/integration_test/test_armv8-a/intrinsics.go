package main

/*
#include <stdio.h>

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
    __atomic_load_n (); //expect: GolangCPPStdCodes
    __atomic_load (); //expect: GolangCPPStdCodes
    __atomic_store_n (); //expect: GolangCPPStdCodes
    __atomic_store ();  // expect: GolangCPPStdCodes
    __atomic_exchange_n (); // expect: GolangCPPStdCodes
    __atomic_exchange (); // expect: GolangCPPStdCodes
    __atomic_compare_exchange_n (); // expect: GolangCPPStdCodes
    __atomic_compare_exchange (); // expect: GolangCPPStdCodes
    __atomic_add_fetch (); // expect: GolangCPPStdCodes
    __atomic_sub_fetch (); // expect: GolangCPPStdCodes
    __atomic_and_fetch (); // expect: GolangCPPStdCodes
    __atomic_xor_fetch (); // expect: GolangCPPStdCodes
    __atomic_or_fetch (); // expect: GolangCPPStdCodes
    __atomic_nand_fetch (); // expect: GolangCPPStdCodes
    __atomic_fetch_add (); // expect: GolangCPPStdCodes
    __atomic_fetch_sub (); // expect: GolangCPPStdCodes
    __atomic_fetch_and (); // expect: GolangCPPStdCodes
    __atomic_fetch_xor (); // expect: GolangCPPStdCodes
    __atomic_fetch_or (); // expect: GolangCPPStdCodes
    __atomic_fetch_nand (); // expect: GolangCPPStdCodes
    __atomic_test_and_set (); // expect: GolangCPPStdCodes
    __atomic_clear (); // expect: GolangCPPStdCodes
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
    __sync_fetch_and_add (); //expect: GolangCPPStdCodes
    __sync_fetch_and_sub (); //expect: GolangCPPStdCodes
    __sync_fetch_and_or (); //expect: GolangCPPStdCodes
    __sync_fetch_and_and (); //expect: GolangCPPStdCodes
    __sync_fetch_and_xor (); //expect: GolangCPPStdCodes
    __sync_fetch_and_nand (); //expect: GolangCPPStdCodes
    __sync_add_and_fetch (); //expect: GolangCPPStdCodes
    __sync_sub_and_fetch (); //expect: GolangCPPStdCodes
    __sync_or_and_fetch (); //expect: GolangCPPStdCodes
    __sync_and_and_fetch (); //expect: GolangCPPStdCodes
    __sync_xor_and_fetch (); //expect: GolangCPPStdCodes
    __sync_nand_and_fetch (); //expect: GolangCPPStdCodes
    __sync_bool_compare_and_swap (); //expect: GolangCPPStdCodes
    __sync_val_compare_and_swap (); //expect: GolangCPPStdCodes
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
    __builtin_arm_getwcgr0(); //expect: GolangIntrinsicIssue
    __builtin_arm_setwcgr0(); //expect: GolangIntrinsicIssue
    __builtin_arm_getwcgr1(); //expect: GolangIntrinsicIssue
    __builtin_arm_setwcgr1(); //expect: GolangIntrinsicIssue
    __builtin_arm_getwcgr2(); //expect: GolangIntrinsicIssue
    __builtin_arm_setwcgr2(); //expect: GolangIntrinsicIssue
    __builtin_arm_getwcgr3(); //expect: GolangIntrinsicIssue
    __builtin_arm_setwcgr3(); //expect: GolangIntrinsicIssue
    __builtin_arm_textrmsb(); //expect: GolangIntrinsicIssue
    __builtin_arm_textrmsh(); //expect: GolangIntrinsicIssue
    __builtin_arm_textrmsw(); //expect: GolangIntrinsicIssue
    __builtin_arm_textrmub(); //expect: GolangIntrinsicIssue
    __builtin_arm_textrmuh(); //expect: GolangIntrinsicIssue
    __builtin_arm_textrmuw(); //expect: GolangIntrinsicIssue
    __builtin_arm_tinsrb(); //expect: GolangIntrinsicIssue
    __builtin_arm_tinsrh(); //expect: GolangIntrinsicIssue
    __builtin_arm_tinsrw(); //expect: GolangIntrinsicIssue
    __builtin_arm_tmia(); //expect: GolangIntrinsicIssue
    __builtin_arm_tmiabb(); //expect: GolangIntrinsicIssue
    __builtin_arm_tmiabt(); //expect: GolangIntrinsicIssue
    __builtin_arm_tmiaph(); //expect: GolangIntrinsicIssue
    __builtin_arm_tmiatb(); //expect: GolangIntrinsicIssue
    __builtin_arm_tmiatt(); //expect: GolangIntrinsicIssue
    __builtin_arm_tmovmskb(); //expect: GolangIntrinsicIssue
    __builtin_arm_tmovmskh(); //expect: GolangIntrinsicIssue
    __builtin_arm_tmovmskw(); //expect: GolangIntrinsicIssue
    __builtin_arm_waccb(); //expect: GolangIntrinsicIssue
    __builtin_arm_wacch(); //expect: GolangIntrinsicIssue
    __builtin_arm_waccw(); //expect: GolangIntrinsicIssue
    __builtin_arm_waddb(); //expect: GolangIntrinsicIssue
    __builtin_arm_waddbss(); //expect: GolangIntrinsicIssue
    __builtin_arm_waddbus(); //expect: GolangIntrinsicIssue
    __builtin_arm_waddh(); //expect: GolangIntrinsicIssue
    __builtin_arm_waddhss(); //expect: GolangIntrinsicIssue
    __builtin_arm_waddhus(); //expect: GolangIntrinsicIssue
    __builtin_arm_waddw(); //expect: GolangIntrinsicIssue
    __builtin_arm_waddwss(); //expect: GolangIntrinsicIssue
    __builtin_arm_waddwus(); //expect: GolangIntrinsicIssue
    __builtin_arm_walign(); //expect: GolangIntrinsicIssue
    __builtin_arm_wand(); //expect: GolangIntrinsicIssue
    __builtin_arm_wandn(); //expect: GolangIntrinsicIssue
    __builtin_arm_wavg2b(); //expect: GolangIntrinsicIssue
    __builtin_arm_wavg2br(); //expect: GolangIntrinsicIssue
    __builtin_arm_wavg2h(); //expect: GolangIntrinsicIssue
    __builtin_arm_wavg2hr(); //expect: GolangIntrinsicIssue
    __builtin_arm_wcmpeqb(); //expect: GolangIntrinsicIssue
    __builtin_arm_wcmpeqh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wcmpeqw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wcmpgtsb(); //expect: GolangIntrinsicIssue
    __builtin_arm_wcmpgtsh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wcmpgtsw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wcmpgtub(); //expect: GolangIntrinsicIssue
    __builtin_arm_wcmpgtuh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wcmpgtuw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmacs(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmacsz(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmacu(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmacuz(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmadds(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmaddu(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmaxsb(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmaxsh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmaxsw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmaxub(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmaxuh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmaxuw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wminsb(); //expect: GolangIntrinsicIssue
    __builtin_arm_wminsh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wminsw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wminub(); //expect: GolangIntrinsicIssue
    __builtin_arm_wminuh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wminuw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmulsm(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmulul(); //expect: GolangIntrinsicIssue
    __builtin_arm_wmulum(); //expect: GolangIntrinsicIssue
    __builtin_arm_wor(); //expect: GolangIntrinsicIssue
    __builtin_arm_wpackdss(); //expect: GolangIntrinsicIssue
    __builtin_arm_wpackdus(); //expect: GolangIntrinsicIssue
    __builtin_arm_wpackhss(); //expect: GolangIntrinsicIssue
    __builtin_arm_wpackhus(); //expect: GolangIntrinsicIssue
    __builtin_arm_wpackwss(); //expect: GolangIntrinsicIssue
    __builtin_arm_wpackwus(); //expect: GolangIntrinsicIssue
    __builtin_arm_wrord(); //expect: GolangIntrinsicIssue
    __builtin_arm_wrordi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wrorh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wrorhi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wrorw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wrorwi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsadb(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsadbz(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsadh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsadhz(); //expect: GolangIntrinsicIssue
    __builtin_arm_wshufh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wslld(); //expect: GolangIntrinsicIssue
    __builtin_arm_wslldi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsllh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsllhi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsllw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsllwi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsrad(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsradi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsrah(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsrahi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsraw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsrawi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsrld(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsrldi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsrlh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsrlhi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsrlw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsrlwi(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsubb(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsubbss(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsubbus(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsubh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsubhss(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsubhus(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsubw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsubwss(); //expect: GolangIntrinsicIssue
    __builtin_arm_wsubwus(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckehsb(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckehsh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckehsw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckehub(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckehuh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckehuw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckelsb(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckelsh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckelsw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckelub(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckeluh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckeluw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckihb(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckihh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckihw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckilb(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckilh(); //expect: GolangIntrinsicIssue
    __builtin_arm_wunpckilw(); //expect: GolangIntrinsicIssue
    __builtin_arm_wxor(); //expect: GolangIntrinsicIssue
    __builtin_arm_wzero(); //expect: GolangIntrinsicIssue
    _arm_smlal(); //expect: GolangIntrinsicIssue
    _arm_umlal(); //expect: GolangIntrinsicIssue
    _arm_clz(); //expect: GolangIntrinsicIssue
    _arm_qadd(); //expect: GolangIntrinsicIssue
    _arm_qdadd(); //expect: GolangIntrinsicIssue
    _arm_qdsub(); //expect: GolangIntrinsicIssue
    _arm_qsub(); //expect: GolangIntrinsicIssue
    _arm_smlabb(); //expect: GolangIntrinsicIssue
    _arm_smlabt(); //expect: GolangIntrinsicIssue
    _arm_smlatb(); //expect: GolangIntrinsicIssue
    _arm_smlatt(); //expect: GolangIntrinsicIssue
    _arm_smlalbb(); //expect: GolangIntrinsicIssue
    _arm_smlalbt(); //expect: GolangIntrinsicIssue
    _arm_smlaltb(); //expect: GolangIntrinsicIssue
    _arm_smlaltt(); //expect: GolangIntrinsicIssue
    _arm_smlawb(); //expect: GolangIntrinsicIssue
    _arm_smlawt(); //expect: GolangIntrinsicIssue
    _arm_smulbb(); //expect: GolangIntrinsicIssue
    _arm_smulbt(); //expect: GolangIntrinsicIssue
    _arm_smultb(); //expect: GolangIntrinsicIssue
    _arm_smultt(); //expect: GolangIntrinsicIssue
    _arm_smulwb(); //expect: GolangIntrinsicIssue
    _arm_smulwt(); //expect: GolangIntrinsicIssue
    _arm_sadd16(); //expect: GolangIntrinsicIssue
    _arm_sadd8(); //expect: GolangIntrinsicIssue
    _arm_sasx(); //expect: GolangIntrinsicIssue
    _arm_ssax(); //expect: GolangIntrinsicIssue
    _arm_ssub16(); //expect: GolangIntrinsicIssue
    _arm_ssub8(); //expect: GolangIntrinsicIssue
    _arm_shadd16(); //expect: GolangIntrinsicIssue
    _arm_shadd8(); //expect: GolangIntrinsicIssue
    _arm_shasx(); //expect: GolangIntrinsicIssue
    _arm_shsax(); //expect: GolangIntrinsicIssue
    _arm_shsub16(); //expect: GolangIntrinsicIssue
    _arm_shsub8(); //expect: GolangIntrinsicIssue
    _arm_qadd16(); //expect: GolangIntrinsicIssue
    _arm_qadd8(); //expect: GolangIntrinsicIssue
    _arm_qasx(); //expect: GolangIntrinsicIssue
    _arm_qsax(); //expect: GolangIntrinsicIssue
    _arm_qsub16(); //expect: GolangIntrinsicIssue
    _arm_qsub8(); //expect: GolangIntrinsicIssue
    _arm_uadd16(); //expect: GolangIntrinsicIssue
    _arm_uadd8(); //expect: GolangIntrinsicIssue
    _arm_uasx(); //expect: GolangIntrinsicIssue
    _arm_usax(); //expect: GolangIntrinsicIssue
    _arm_usub16(); //expect: GolangIntrinsicIssue
    _arm_usub8(); //expect: GolangIntrinsicIssue
    _arm_uhadd16(); //expect: GolangIntrinsicIssue
    _arm_uhadd8(); //expect: GolangIntrinsicIssue
    _arm_uhasx(); //expect: GolangIntrinsicIssue
    _arm_uhsax(); //expect: GolangIntrinsicIssue
    _arm_uhsub16(); //expect: GolangIntrinsicIssue
    _arm_uhsub8(); //expect: GolangIntrinsicIssue
    _arm_uqadd16(); //expect: GolangIntrinsicIssue
    _arm_uqadd8(); //expect: GolangIntrinsicIssue
    _arm_uqasx(); //expect: GolangIntrinsicIssue
    _arm_uqsax(); //expect: GolangIntrinsicIssue
    _arm_uqsub16(); //expect: GolangIntrinsicIssue
    _arm_uqsub8(); //expect: GolangIntrinsicIssue
    _arm_sxtab(); //expect: GolangIntrinsicIssue
    _arm_sxtab16(); //expect: GolangIntrinsicIssue
    _arm_sxtah(); //expect: GolangIntrinsicIssue
    _arm_uxtab(); //expect: GolangIntrinsicIssue
    _arm_uxtab16(); //expect: GolangIntrinsicIssue
    _arm_uxtah(); //expect: GolangIntrinsicIssue
    _arm_sxtb(); //expect: GolangIntrinsicIssue
    _arm_sxtb16(); //expect: GolangIntrinsicIssue
    _arm_sxth(); //expect: GolangIntrinsicIssue
    _arm_uxtb(); //expect: GolangIntrinsicIssue
    _arm_uxtb16(); //expect: GolangIntrinsicIssue
    _arm_uxth(); //expect: GolangIntrinsicIssue
    _arm_pkhbt(); //expect: GolangIntrinsicIssue
    _arm_pkhtb(); //expect: GolangIntrinsicIssue
    _arm_usad8(); //expect: GolangIntrinsicIssue
    _arm_usada8(); //expect: GolangIntrinsicIssue
    _arm_ssat(); //expect: GolangIntrinsicIssue
    _arm_usat(); //expect: GolangIntrinsicIssue
    _arm_ssat16(); //expect: GolangIntrinsicIssue
    _arm_usat16(); //expect: GolangIntrinsicIssue
    _arm_rev(); //expect: GolangIntrinsicIssue
    _arm_rev16(); //expect: GolangIntrinsicIssue
    _arm_revsh(); //expect: GolangIntrinsicIssue
    _arm_smlad(); //expect: GolangIntrinsicIssue
    _arm_smladx(); //expect: GolangIntrinsicIssue
    _arm_smlsd(); //expect: GolangIntrinsicIssue
    _arm_smlsdx(); //expect: GolangIntrinsicIssue
    _arm_smmla(); //expect: GolangIntrinsicIssue
    _arm_smmlar(); //expect: GolangIntrinsicIssue
    _arm_smmls(); //expect: GolangIntrinsicIssue
    _arm_smmlsr(); //expect: GolangIntrinsicIssue
    _arm_smmul(); //expect: GolangIntrinsicIssue
    _arm_smmulr(); //expect: GolangIntrinsicIssue
    _arm_smlald(); //expect: GolangIntrinsicIssue
    _arm_smlaldx(); //expect: GolangIntrinsicIssue
    _arm_smlsld(); //expect: GolangIntrinsicIssue
    _arm_smlsldx(); //expect: GolangIntrinsicIssue
    _arm_smuad(); //expect: GolangIntrinsicIssue
    _arm_smuadx(); //expect: GolangIntrinsicIssue
    _arm_smusd(); //expect: GolangIntrinsicIssue
    _arm_smusdx(); //expect: GolangIntrinsicIssue
    _arm_smull(); //expect: GolangIntrinsicIssue
    _arm_umaal(); //expect: GolangIntrinsicIssue
    _arm_bfc(); //expect: GolangIntrinsicIssue
    _arm_bfi(); //expect: GolangIntrinsicIssue
    _arm_rbit(); //expect: GolangIntrinsicIssue
    _arm_sbfx(); //expect: GolangIntrinsicIssue
    _arm_ubfx(); //expect: GolangIntrinsicIssue
    _arm_sdiv(); //expect: GolangIntrinsicIssue
    _arm_udiv(); //expect: GolangIntrinsicIssue
    __cps(); //expect: GolangIntrinsicIssue
    __dmb(); //expect: GolangIntrinsicIssue
    __dsb(); //expect: GolangIntrinsicIssue
    __isb(); //expect: GolangIntrinsicIssue
    __emit(); //expect: GolangIntrinsicIssue
    __hvc(); //expect: GolangIntrinsicIssue
    __iso_volatile_load16(); //expect: GolangIntrinsicIssue
    __iso_volatile_load32(); //expect: GolangIntrinsicIssue
    __iso_volatile_load64(); //expect: GolangIntrinsicIssue
    __iso_volatile_load8(); //expect: GolangIntrinsicIssue
    __iso_volatile_store16(); //expect: GolangIntrinsicIssue
    __iso_volatile_store32(); //expect: GolangIntrinsicIssue
    __iso_volatile_store64(); //expect: GolangIntrinsicIssue
    __iso_volatile_store8(); //expect: GolangIntrinsicIssue
    __ldrexd(); //expect: GolangIntrinsicIssue
    __prefetch(); //expect: GolangIntrinsicIssue
    __rdpmccntr64(); //expect: GolangIntrinsicIssue
    __sev(); //expect: GolangIntrinsicIssue
    __static_assert(); //expect: GolangIntrinsicIssue
    __swi(); //expect: GolangIntrinsicIssue
    __trap(); //expect: GolangIntrinsicIssue
    __wfe(); //expect: GolangIntrinsicIssue
    __wfi(); //expect: GolangIntrinsicIssue
    _AddSatInt(); //expect: GolangIntrinsicIssue
    _CopyDoubleFromInt64(); //expect: GolangIntrinsicIssue
    _CopyFloatFromInt32(); //expect: GolangIntrinsicIssue
    _CopyInt32FromFloat(); //expect: GolangIntrinsicIssue
    _CopyInt64FromDouble(); //expect: GolangIntrinsicIssue
    _CountLeadingOnes(); //expect: GolangIntrinsicIssue
    _CountLeadingOnes64(); //expect: GolangIntrinsicIssue
    _CountLeadingSigns(); //expect: GolangIntrinsicIssue
    _CountLeadingSigns64(); //expect: GolangIntrinsicIssue
    _CountLeadingZeros(); //expect: GolangIntrinsicIssue
    _CountLeadingZeros64(); //expect: GolangIntrinsicIssue
    _CountOneBits(); //expect: GolangIntrinsicIssue
    _CountOneBits64(); //expect: GolangIntrinsicIssue
    _DAddSatInt(); //expect: GolangIntrinsicIssue
    _DSubSatInt(); //expect: GolangIntrinsicIssue
    _isunordered(); //expect: GolangIntrinsicIssue
    _isunorderedf(); //expect: GolangIntrinsicIssue
    _MoveFromCoprocessor(); //expect: GolangIntrinsicIssue
    _MoveFromCoprocessor2(); //expect: GolangIntrinsicIssue
    _MoveFromCoprocessor64(); //expect: GolangIntrinsicIssue
    _MoveToCoprocessor(); //expect: GolangIntrinsicIssue
    _MoveToCoprocessor2(); //expect: GolangIntrinsicIssue
    _MoveToCoprocessor64(); //expect: GolangIntrinsicIssue
    _MulHigh(); //expect: GolangIntrinsicIssue
    _MulUnsignedHigh(); //expect: GolangIntrinsicIssue
    _ReadBankedReg(); //expect: GolangIntrinsicIssue
    _ReadStatusReg(); //expect: GolangIntrinsicIssue
    _SubSatInt(); //expect: GolangIntrinsicIssue
    _WriteBankedReg(); //expect: GolangIntrinsicIssue
    _WriteStatusReg(); //expect: GolangIntrinsicIssue

    __assume(); //expect: GolangIntrinsicIssue
    __code_seg(); //expect: GolangIntrinsicIssue
    __debugbreak(); //expect: GolangIntrinsicIssue
    __fastfail(); //expect: GolangIntrinsicIssue
    __nop(); //expect: GolangIntrinsicIssue
    __yield(); //expect: GolangIntrinsicIssue
    _AddressOfReturnAddress(); //expect: GolangIntrinsicIssue
    _BitScanForward(); //expect: GolangIntrinsicIssue
    _BitScanForward64(); //expect: GolangIntrinsicIssue
    _BitScanReverse(); //expect: GolangIntrinsicIssue
    _BitScanReverse64(); //expect: GolangIntrinsicIssue
    _bittest(); //expect: GolangIntrinsicIssue
    _bittest64(); //expect: GolangIntrinsicIssue
    _bittestandcomplement(); //expect: GolangIntrinsicIssue
    _bittestandreset(); //expect: GolangIntrinsicIssue
    _bittestandset(); //expect: GolangIntrinsicIssue
    _byteswap_uint64(); //expect: GolangIntrinsicIssue
    _byteswap_ulong(); //expect: GolangIntrinsicIssue
    _byteswap_ushort(); //expect: GolangIntrinsicIssue
    _disable(); //expect: GolangIntrinsicIssue
    _enable(); //expect: GolangIntrinsicIssue
    _lrotl(); //expect: GolangIntrinsicIssue
    _lrotr(); //expect: GolangIntrinsicIssue
    _ReadBarrier(); //expect: GolangIntrinsicIssue
    _ReadWriteBarrier(); //expect: GolangIntrinsicIssue
    _ReturnAddress(); //expect: GolangIntrinsicIssue
    _rotl(); //expect: GolangIntrinsicIssue
    _rotl16(); //expect: GolangIntrinsicIssue
    _rotl64(); //expect: GolangIntrinsicIssue
    _rotl8(); //expect: GolangIntrinsicIssue
    _rotr(); //expect: GolangIntrinsicIssue
    _rotr16(); //expect: GolangIntrinsicIssue
    _rotr64(); //expect: GolangIntrinsicIssue
    _rotr8(); //expect: GolangIntrinsicIssue
    _setjmpex(); //expect: GolangIntrinsicIssue
    _WriteBarrier(); //expect: GolangIntrinsicIssue

    _InterlockedAdd(); //expect: GolangIntrinsicIssue
    _InterlockedAdd64(); //expect: GolangIntrinsicIssue
    _InterlockedAdd64_acq(); //expect: GolangIntrinsicIssue
    _InterlockedAdd64_nf(); //expect: GolangIntrinsicIssue
    _InterlockedAdd64_rel(); //expect: GolangIntrinsicIssue
    _InterlockedAdd_acq(); //expect: GolangIntrinsicIssue
    _InterlockedAdd_nf(); //expect: GolangIntrinsicIssue
    _InterlockedAdd_rel(); //expect: GolangIntrinsicIssue
    _InterlockedAnd(); //expect: GolangIntrinsicIssue
    _InterlockedAnd16(); //expect: GolangIntrinsicIssue
    _InterlockedAnd16_acq(); //expect: GolangIntrinsicIssue
    _InterlockedAnd16_nf(); //expect: GolangIntrinsicIssue
    _InterlockedAnd16_rel(); //expect: GolangIntrinsicIssue
    _InterlockedAnd64(); //expect: GolangIntrinsicIssue
    _InterlockedAnd64_acq(); //expect: GolangIntrinsicIssue
    _InterlockedAnd64_nf(); //expect: GolangIntrinsicIssue
    _InterlockedAnd64_rel(); //expect: GolangIntrinsicIssue
    _InterlockedAnd8(); //expect: GolangIntrinsicIssue
    _InterlockedAnd8_acq(); //expect: GolangIntrinsicIssue
    _InterlockedAnd8_nf(); //expect: GolangIntrinsicIssue
    _InterlockedAnd8_rel(); //expect: GolangIntrinsicIssue
    _InterlockedAnd_acq(); //expect: GolangIntrinsicIssue
    _InterlockedAnd_nf(); //expect: GolangIntrinsicIssue
    _InterlockedAnd_rel(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange16(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange16_acq(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange16_nf(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange16_rel(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange64(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange64_acq(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange64_nf(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange64_rel(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange8(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange8_acq(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange8_nf(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange8_rel(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchangePointer(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchangePointer_acq(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchangePointer_nf(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchangePointer_rel(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange_acq(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange_nf(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange_rel(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement16(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement16_acq(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement16_nf(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement16_rel(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement64(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement64_acq(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement64_nf(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement64_rel(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement_acq(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement_nf(); //expect: GolangIntrinsicIssue
    _InterlockedDecrement_rel(); //expect: GolangIntrinsicIssue
    _InterlockedExchange(); //expect: GolangIntrinsicIssue
    _InterlockedExchange16(); //expect: GolangIntrinsicIssue
    _InterlockedExchange16_acq(); //expect: GolangIntrinsicIssue
    _InterlockedExchange16_nf(); //expect: GolangIntrinsicIssue
    _InterlockedExchange64(); //expect: GolangIntrinsicIssue
    _InterlockedExchange64_acq(); //expect: GolangIntrinsicIssue
    _InterlockedExchange64_nf(); //expect: GolangIntrinsicIssue
    _InterlockedExchange8(); //expect: GolangIntrinsicIssue
    _InterlockedExchange8_acq(); //expect: GolangIntrinsicIssue
    _InterlockedExchange8_nf(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd16(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd16_acq(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd16_nf(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd16_rel(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd64(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd64_acq(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd64_nf(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd64_rel(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd8(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd8_acq(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd8_nf(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd8_rel(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd_acq(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd_nf(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd_rel(); //expect: GolangIntrinsicIssue
    _InterlockedExchangePointer(); //expect: GolangIntrinsicIssue
    _InterlockedExchangePointer_acq(); //expect: GolangIntrinsicIssue
    _InterlockedExchangePointer_nf(); //expect: GolangIntrinsicIssue
    _InterlockedExchange_acq(); //expect: GolangIntrinsicIssue
    _InterlockedExchange_nf(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement16(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement16_acq(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement16_nf(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement16_rel(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement64(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement64_acq(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement64_nf(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement64_rel(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement_acq(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement_nf(); //expect: GolangIntrinsicIssue
    _InterlockedIncrement_rel(); //expect: GolangIntrinsicIssue
    _InterlockedOr(); //expect: GolangIntrinsicIssue
    _InterlockedOr16(); //expect: GolangIntrinsicIssue
    _InterlockedOr16_acq(); //expect: GolangIntrinsicIssue
    _InterlockedOr16_nf(); //expect: GolangIntrinsicIssue
    _InterlockedOr16_rel(); //expect: GolangIntrinsicIssue
    _InterlockedOr64(); //expect: GolangIntrinsicIssue
    _InterlockedOr64_acq(); //expect: GolangIntrinsicIssue
    _InterlockedOr64_nf(); //expect: GolangIntrinsicIssue
    _InterlockedOr64_rel(); //expect: GolangIntrinsicIssue
    _InterlockedOr8(); //expect: GolangIntrinsicIssue
    _InterlockedOr8_acq(); //expect: GolangIntrinsicIssue
    _InterlockedOr8_nf(); //expect: GolangIntrinsicIssue
    _InterlockedOr8_rel(); //expect: GolangIntrinsicIssue
    _InterlockedOr_acq(); //expect: GolangIntrinsicIssue
    _InterlockedOr_nf(); //expect: GolangIntrinsicIssue
    _InterlockedOr_rel(); //expect: GolangIntrinsicIssue
    _InterlockedXor(); //expect: GolangIntrinsicIssue
    _InterlockedXor16(); //expect: GolangIntrinsicIssue
    _InterlockedXor16_acq(); //expect: GolangIntrinsicIssue
    _InterlockedXor16_nf(); //expect: GolangIntrinsicIssue
    _InterlockedXor16_rel(); //expect: GolangIntrinsicIssue
    _InterlockedXor64(); //expect: GolangIntrinsicIssue
    _InterlockedXor64_acq(); //expect: GolangIntrinsicIssue
    _InterlockedXor64_nf(); //expect: GolangIntrinsicIssue
    _InterlockedXor64_rel(); //expect: GolangIntrinsicIssue
    _InterlockedXor8(); //expect: GolangIntrinsicIssue
    _InterlockedXor8_acq(); //expect: GolangIntrinsicIssue
    _InterlockedXor8_nf(); //expect: GolangIntrinsicIssue
    _InterlockedXor8_rel(); //expect: GolangIntrinsicIssue
    _InterlockedXor_acq(); //expect: GolangIntrinsicIssue
    _InterlockedXor_nf(); //expect: GolangIntrinsicIssue
    _InterlockedXor_rel(); //expect: GolangIntrinsicIssue
    _interlockedbittestandreset(); //expect: GolangIntrinsicIssue
    _interlockedbittestandreset_acq(); //expect: GolangIntrinsicIssue
    _interlockedbittestandreset_nf(); //expect: GolangIntrinsicIssue
    _interlockedbittestandreset_rel(); //expect: GolangIntrinsicIssue
    _interlockedbittestandset(); //expect: GolangIntrinsicIssue
    _interlockedbittestandset_acq(); //expect: GolangIntrinsicIssue
    _interlockedbittestandset_nf(); //expect: GolangIntrinsicIssue
    _interlockedbittestandset_rel(); //expect: GolangIntrinsicIssue
}

// shall generate issue in aarch64.
void x86_intrinsic_test()
{
    _mm_srli_epi64(); //expect: GolangIntrinsicIssue
    _mm_shuffle_epi8(); //expect: GolangIntrinsicIssue
    _mm_extract_ps(); //expect: GolangIntrinsicIssue
    _mm_set1_epi64x(); //expect: GolangIntrinsicIssue
    _mm_mul_epu32(); //expect: GolangIntrinsicIssue
    _mm_add_epi64(); //expect: GolangIntrinsicIssue

    _InterlockedAnd8_np(); //expect: GolangIntrinsicIssue
    _InterlockedOr8_np(); //expect: GolangIntrinsicIssue
    _InterlockedXor8_np(); //expect: GolangIntrinsicIssue

    __builtin_ia32_pand(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pandn(); //expect: GolangIntrinsicIssue
    __builtin_ia32_por(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pxor(); //expect: GolangIntrinsicIssue

    _mm_cvtsd_f64(); //expect: GolangIntrinsicIssue
    __builtin_copysignq(); //expect: GolangIntrinsicIssue
    __builtin_huge_valq(); //expect: GolangIntrinsicIssue
    __builtin_infq(); //expect: GolangIntrinsicIssue
    __builtin_fabsq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vec_ext_v4sf(); //expect: GolangIntrinsicIssue
    _mm_cvtss_f32(); //expect: GolangIntrinsicIssue
    _m_to_float(); //expect: GolangIntrinsicIssue
    _div128(); //expect: GolangIntrinsicIssue
    _InterlockedAnd64_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedAnd64_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedAnd64_np(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange64_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange64_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange64_np(); //expect: GolangIntrinsicIssue
    _InterlockedExchange64_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedExchange64_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd64_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd64_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedOr64_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedOr64_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedOr64_np(); //expect: GolangIntrinsicIssue
    _InterlockedXor64_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedXor64_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedXor64_np(); //expect: GolangIntrinsicIssue
    _loadbe_i64(); //expect: GolangIntrinsicIssue
    _mm_cvtsd_si64(); //expect: GolangIntrinsicIssue
    _mm_cvtsd_si64x(); //expect: GolangIntrinsicIssue
    _mm_cvtsi128_si64(); //expect: GolangIntrinsicIssue
    _mm_cvtsi128_si64x(); //expect: GolangIntrinsicIssue
    _mm_cvtss_si64(); //expect: GolangIntrinsicIssue
    _mm_cvtss_si64x(); //expect: GolangIntrinsicIssue
    _mm_cvttsd_si64(); //expect: GolangIntrinsicIssue
    _mm_cvttsd_si64x(); //expect: GolangIntrinsicIssue
    _mm_cvttss_si64(); //expect: GolangIntrinsicIssue
    _mm_cvttss_si64x(); //expect: GolangIntrinsicIssue
    _mm_extract_epi64(); //expect: GolangIntrinsicIssue
    _mm_popcnt_u64(); //expect: GolangIntrinsicIssue
    _mul128(); //expect: GolangIntrinsicIssue
    __mulh(); //expect: GolangIntrinsicIssue
    __emul(); //expect: GolangIntrinsicIssue
    __ll_rshift(); //expect: GolangIntrinsicIssue
    _sarx_i64(); //expect: GolangIntrinsicIssue
    __builtin_cpu_is(); //expect: GolangIntrinsicIssue
    __builtin_cpu_supports(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comieq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comige(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comigt(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comile(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comilt(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comineq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comisdeq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comisdge(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comisdgt(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comisdle(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comisdlt(); //expect: GolangIntrinsicIssue
    __builtin_ia32_comisdneq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtsd2si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtss2si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvttsd2si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvttss2si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movmskpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movmskpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movmskps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movmskps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpestri128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpestria128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpestric128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpestrio128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpestris128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpestriz128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpistri128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpistria128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpistric128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpistrio128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpistris128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpistriz128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pextrw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovmskb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovmskb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovmskb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ptestc128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ptestc256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ptestnzc128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ptestnzc256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ptestz128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ptestz256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomieq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomige(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomigt(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomile(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomilt(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomineq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomisdeq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomisdge(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomisdgt(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomisdle(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomisdlt(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ucomisdneq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vec_ext_v16qi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vec_ext_v4si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestcpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestcpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestcps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestcps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestnzcpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestnzcpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestnzcps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestnzcps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestzpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestzpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestzps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vtestzps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_xbegin(); //expect: GolangIntrinsicIssue
    __builtin_ia32_xtest(); //expect: GolangIntrinsicIssue
    _div64(); //expect: GolangIntrinsicIssue
    _loadbe_i32(); //expect: GolangIntrinsicIssue
    _mm256_movemask_epi8(); //expect: GolangIntrinsicIssue
    _mm256_movemask_pd(); //expect: GolangIntrinsicIssue
    _mm256_movemask_ps(); //expect: GolangIntrinsicIssue
    _mm256_testc_pd(); //expect: GolangIntrinsicIssue
    _mm256_testc_ps(); //expect: GolangIntrinsicIssue
    _mm256_testc_si256(); //expect: GolangIntrinsicIssue
    _mm256_testnzc_pd(); //expect: GolangIntrinsicIssue
    _mm256_testnzc_ps(); //expect: GolangIntrinsicIssue
    _mm256_testnzc_si256(); //expect: GolangIntrinsicIssue
    _mm256_testz_pd(); //expect: GolangIntrinsicIssue
    _mm256_testz_ps(); //expect: GolangIntrinsicIssue
    _mm256_testz_si256(); //expect: GolangIntrinsicIssue
    _mm_cmpestra(); //expect: GolangIntrinsicIssue
    _mm_cmpestrc(); //expect: GolangIntrinsicIssue
    _mm_cmpestri(); //expect: GolangIntrinsicIssue
    _mm_cmpestro(); //expect: GolangIntrinsicIssue
    _mm_cmpestrs(); //expect: GolangIntrinsicIssue
    _mm_cmpestrz(); //expect: GolangIntrinsicIssue
    _mm_cmpistra(); //expect: GolangIntrinsicIssue
    _mm_cmpistrc(); //expect: GolangIntrinsicIssue
    _mm_cmpistri(); //expect: GolangIntrinsicIssue
    _mm_cmpistro(); //expect: GolangIntrinsicIssue
    _mm_cmpistrs(); //expect: GolangIntrinsicIssue
    _mm_cmpistrz(); //expect: GolangIntrinsicIssue
    _mm_comieq_sd(); //expect: GolangIntrinsicIssue
    _mm_comieq_ss(); //expect: GolangIntrinsicIssue
    _mm_comige_sd(); //expect: GolangIntrinsicIssue
    _mm_comige_ss(); //expect: GolangIntrinsicIssue
    _mm_comigt_sd(); //expect: GolangIntrinsicIssue
    _mm_comigt_ss(); //expect: GolangIntrinsicIssue
    _mm_comile_sd(); //expect: GolangIntrinsicIssue
    _mm_comile_ss(); //expect: GolangIntrinsicIssue
    _mm_comilt_sd(); //expect: GolangIntrinsicIssue
    _mm_comilt_ss(); //expect: GolangIntrinsicIssue
    _mm_comineq_sd(); //expect: GolangIntrinsicIssue
    _mm_comineq_ss(); //expect: GolangIntrinsicIssue
    _mm_cvtsd_si32(); //expect: GolangIntrinsicIssue
    _mm_cvtsi128_si32(); //expect: GolangIntrinsicIssue
    _mm_cvt_ss2si(); //expect: GolangIntrinsicIssue
    _mm_cvttsd_si32(); //expect: GolangIntrinsicIssue
    _mm_cvtt_ss2si(); //expect: GolangIntrinsicIssue
    _mm_extract_epi16(); //expect: GolangIntrinsicIssue
    _mm_extract_epi32(); //expect: GolangIntrinsicIssue
    _mm_extract_epi8(); //expect: GolangIntrinsicIssue
    _mm_extract_ps(); //expect: GolangIntrinsicIssue
    _mm_movemask_epi8(); //expect: GolangIntrinsicIssue
    _mm_movemask_pd(); //expect: GolangIntrinsicIssue
    _mm_movemask_ps(); //expect: GolangIntrinsicIssue
    _mm_popcnt_u32(); //expect: GolangIntrinsicIssue
    _mm_testc_pd(); //expect: GolangIntrinsicIssue
    _mm_testc_ps(); //expect: GolangIntrinsicIssue
    _mm_testc_si128(); //expect: GolangIntrinsicIssue
    _mm_testnzc_pd(); //expect: GolangIntrinsicIssue
    _mm_testnzc_ps(); //expect: GolangIntrinsicIssue
    _mm_testnzc_si128(); //expect: GolangIntrinsicIssue
    _mm_testz_pd(); //expect: GolangIntrinsicIssue
    _mm_testz_ps(); //expect: GolangIntrinsicIssue
    _mm_testz_si128(); //expect: GolangIntrinsicIssue
    _mm_ucomieq_sd(); //expect: GolangIntrinsicIssue
    _mm_ucomieq_ss(); //expect: GolangIntrinsicIssue
    _mm_ucomige_sd(); //expect: GolangIntrinsicIssue
    _mm_ucomige_ss(); //expect: GolangIntrinsicIssue
    _mm_ucomigt_sd(); //expect: GolangIntrinsicIssue
    _mm_ucomigt_ss(); //expect: GolangIntrinsicIssue
    _mm_ucomile_sd(); //expect: GolangIntrinsicIssue
    _mm_ucomile_ss(); //expect: GolangIntrinsicIssue
    _mm_ucomilt_sd(); //expect: GolangIntrinsicIssue
    _mm_ucomilt_ss(); //expect: GolangIntrinsicIssue
    _mm_ucomineq_sd(); //expect: GolangIntrinsicIssue
    _mm_ucomineq_ss(); //expect: GolangIntrinsicIssue
    _m_pextrw(); //expect: GolangIntrinsicIssue
    _m_pmovmskb(); //expect: GolangIntrinsicIssue
    _m_to_int(); //expect: GolangIntrinsicIssue
    _rdrand16_step(); //expect: GolangIntrinsicIssue
    _rdrand32_step(); //expect: GolangIntrinsicIssue
    _rdrand64_step(); //expect: GolangIntrinsicIssue
    _rdseed16_step(); //expect: GolangIntrinsicIssue
    _rdseed32_step(); //expect: GolangIntrinsicIssue
    _rdseed64_step(); //expect: GolangIntrinsicIssue
    _sarx_i32(); //expect: GolangIntrinsicIssue
    _InterlockedAddLargeStatistic(); //expect: GolangIntrinsicIssue
    _InterlockedAnd_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedAnd_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedAnd_np(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange_np(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedExchangeAdd_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedExchange_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedExchange_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedOr_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedOr_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedOr_np(); //expect: GolangIntrinsicIssue
    _InterlockedXor_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedXor_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedXor_np(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtsd2si64(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvttsd2si64(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vec_ext_v2di(); //expect: GolangIntrinsicIssue
    _mm256_castpd256_pd128(); //expect: GolangIntrinsicIssue
    _mm256_extractf128_pd(); //expect: GolangIntrinsicIssue
    _mm_add_pd(); //expect: GolangIntrinsicIssue
    _mm_add_sd(); //expect: GolangIntrinsicIssue
    _mm_addsub_pd(); //expect: GolangIntrinsicIssue
    _mm_andnot_pd(); //expect: GolangIntrinsicIssue
    _mm_and_pd(); //expect: GolangIntrinsicIssue
    _mm_blend_pd(); //expect: GolangIntrinsicIssue
    _mm_blendv_pd(); //expect: GolangIntrinsicIssue
    _mm_broadcastsd_pd(); //expect: GolangIntrinsicIssue
    _mm_castps_pd(); //expect: GolangIntrinsicIssue
    _mm_castsi128_pd(); //expect: GolangIntrinsicIssue
    _mm_cmpeq_pd(); //expect: GolangIntrinsicIssue
    _mm_cmpeq_sd(); //expect: GolangIntrinsicIssue
    _mm_cmpge_pd(); //expect: GolangIntrinsicIssue
    _mm_cmpge_sd(); //expect: GolangIntrinsicIssue
    _mm_cmpgt_pd(); //expect: GolangIntrinsicIssue
    _mm_cmpgt_sd(); //expect: GolangIntrinsicIssue
    _mm_cmple_pd(); //expect: GolangIntrinsicIssue
    _mm_cmple_sd(); //expect: GolangIntrinsicIssue
    _mm_cmplt_pd(); //expect: GolangIntrinsicIssue
    _mm_cmplt_sd(); //expect: GolangIntrinsicIssue
    _mm_cmpneq_pd(); //expect: GolangIntrinsicIssue
    _mm_cmpneq_sd(); //expect: GolangIntrinsicIssue
    _mm_cmpnge_pd(); //expect: GolangIntrinsicIssue
    _mm_cmpnge_sd(); //expect: GolangIntrinsicIssue
    _mm_cmpngt_pd(); //expect: GolangIntrinsicIssue
    _mm_cmpngt_sd(); //expect: GolangIntrinsicIssue
    _mm_cmpnle_pd(); //expect: GolangIntrinsicIssue
    _mm_cmpnle_sd(); //expect: GolangIntrinsicIssue
    _mm_cmpnlt_pd(); //expect: GolangIntrinsicIssue
    _mm_cmpnlt_sd(); //expect: GolangIntrinsicIssue
    _mm_cmpord_pd(); //expect: GolangIntrinsicIssue
    _mm_cmpord_sd(); //expect: GolangIntrinsicIssue
    _mm_cmp_pd(); //expect: GolangIntrinsicIssue
    _mm_cmp_sd(); //expect: GolangIntrinsicIssue
    _mm_cmpunord_pd(); //expect: GolangIntrinsicIssue
    _mm_cmpunord_sd(); //expect: GolangIntrinsicIssue
    _mm_cvtepi32_pd(); //expect: GolangIntrinsicIssue
    _mm_cvtpi32_pd(); //expect: GolangIntrinsicIssue
    _mm_cvtps_pd(); //expect: GolangIntrinsicIssue
    _mm_cvtsi32_sd(); //expect: GolangIntrinsicIssue
    _mm_cvtsi64_sd(); //expect: GolangIntrinsicIssue
    _mm_cvtsi64x_sd(); //expect: GolangIntrinsicIssue
    _mm_cvtss_sd(); //expect: GolangIntrinsicIssue
    _mm_div_pd(); //expect: GolangIntrinsicIssue
    _mm_div_sd(); //expect: GolangIntrinsicIssue
    _mm_dp_pd(); //expect: GolangIntrinsicIssue
    _mm_fmadd_pd(); //expect: GolangIntrinsicIssue
    _mm_fmadd_sd(); //expect: GolangIntrinsicIssue
    _mm_fmaddsub_pd(); //expect: GolangIntrinsicIssue
    _mm_fmsubadd_pd(); //expect: GolangIntrinsicIssue
    _mm_fmsub_pd(); //expect: GolangIntrinsicIssue
    _mm_fmsub_sd(); //expect: GolangIntrinsicIssue
    _mm_fnmadd_pd(); //expect: GolangIntrinsicIssue
    _mm_fnmadd_sd(); //expect: GolangIntrinsicIssue
    _mm_fnmsub_pd(); //expect: GolangIntrinsicIssue
    _mm_fnmsub_sd(); //expect: GolangIntrinsicIssue
    _mm_frcz_pd(); //expect: GolangIntrinsicIssue
    _mm_frcz_sd(); //expect: GolangIntrinsicIssue
    _mm_hadd_pd(); //expect: GolangIntrinsicIssue
    _mm_hsub_pd(); //expect: GolangIntrinsicIssue
    _mm_i32gather_pd(); //expect: GolangIntrinsicIssue
    _mm_i64gather_pd(); //expect: GolangIntrinsicIssue
    _mm_load1_pd(); //expect: GolangIntrinsicIssue
    _mm_loaddup_pd(); //expect: GolangIntrinsicIssue
    _mm_loadh_pd(); //expect: GolangIntrinsicIssue
    _mm_loadl_pd(); //expect: GolangIntrinsicIssue
    _mm_load_pd(); //expect: GolangIntrinsicIssue
    _mm_loadr_pd(); //expect: GolangIntrinsicIssue
    _mm_load_sd(); //expect: GolangIntrinsicIssue
    _mm_loadu_pd(); //expect: GolangIntrinsicIssue
    _mm_macc_pd(); //expect: GolangIntrinsicIssue
    _mm_macc_sd(); //expect: GolangIntrinsicIssue
    _mm_macc_sd(); //expect: GolangIntrinsicIssue
    _mm_maddsub_pd(); //expect: GolangIntrinsicIssue
    _mm_mask_i32gather_pd(); //expect: GolangIntrinsicIssue
    _mm_mask_i64gather_pd(); //expect: GolangIntrinsicIssue
    _mm_maskload_pd(); //expect: GolangIntrinsicIssue
    _mm_max_pd(); //expect: GolangIntrinsicIssue
    _mm_max_sd(); //expect: GolangIntrinsicIssue
    _mm_min_pd(); //expect: GolangIntrinsicIssue
    _mm_min_sd(); //expect: GolangIntrinsicIssue
    _mm_movedup_pd(); //expect: GolangIntrinsicIssue
    _mm_move_sd(); //expect: GolangIntrinsicIssue
    _mm_msubadd_pd(); //expect: GolangIntrinsicIssue
    _mm_msub_pd(); //expect: GolangIntrinsicIssue
    _mm_msub_sd(); //expect: GolangIntrinsicIssue
    _mm_mul_pd(); //expect: GolangIntrinsicIssue
    _mm_mul_sd(); //expect: GolangIntrinsicIssue
    _mm_nmacc_pd(); //expect: GolangIntrinsicIssue
    _mm_nmacc_sd(); //expect: GolangIntrinsicIssue
    _mm_nmsub_pd(); //expect: GolangIntrinsicIssue
    _mm_nmsub_sd(); //expect: GolangIntrinsicIssue
    _mm_or_pd(); //expect: GolangIntrinsicIssue
    _mm_permute2_pd(); //expect: GolangIntrinsicIssue
    _mm_permute_pd(); //expect: GolangIntrinsicIssue
    _mm_permutevar_pd(); //expect: GolangIntrinsicIssue
    _mm_round_pd(); //expect: GolangIntrinsicIssue
    _mm_round_sd(); //expect: GolangIntrinsicIssue
    _mm_set1_pd(); //expect: GolangIntrinsicIssue
    _mm_set_pd(); //expect: GolangIntrinsicIssue
    _mm_setr_pd(); //expect: GolangIntrinsicIssue
    _mm_set_sd(); //expect: GolangIntrinsicIssue
    _mm_setzero_pd(); //expect: GolangIntrinsicIssue
    _mm_shuffle_pd(); //expect: GolangIntrinsicIssue
    _mm_sqrt_pd(); //expect: GolangIntrinsicIssue
    _mm_sqrt_sd(); //expect: GolangIntrinsicIssue
    _mm_sub_pd(); //expect: GolangIntrinsicIssue
    _mm_sub_sd(); //expect: GolangIntrinsicIssue
    _mm_unpackhi_pd(); //expect: GolangIntrinsicIssue
    _mm_unpacklo_pd(); //expect: GolangIntrinsicIssue
    _mm_xor_pd(); //expect: GolangIntrinsicIssue
    _mm256_castsi256_si128(); //expect: GolangIntrinsicIssue
    _mm256_cvtpd_epi32(); //expect: GolangIntrinsicIssue
    _mm256_cvtps_ph(); //expect: GolangIntrinsicIssue
    _mm256_cvttpd_epi32(); //expect: GolangIntrinsicIssue
    _mm256_extractf128_si256(); //expect: GolangIntrinsicIssue
    _mm256_extracti128_si256(); //expect: GolangIntrinsicIssue
    _mm256_mask_i64gather_epi32(); //expect: GolangIntrinsicIssue
     _mm_abs_epi16(); //expect: GolangIntrinsicIssue
    _mm_abs_epi32(); //expect: GolangIntrinsicIssue
    _mm_abs_epi8(); //expect: GolangIntrinsicIssue
    _mm_add_epi16(); //expect: GolangIntrinsicIssue
    _mm_add_epi32(); //expect: GolangIntrinsicIssue
    _mm_add_epi64(); //expect: GolangIntrinsicIssue
    _mm_add_epi8(); //expect: GolangIntrinsicIssue
    _mm_adds_epi16(); //expect: GolangIntrinsicIssue
    _mm_adds_epi8(); //expect: GolangIntrinsicIssue
    _mm_adds_epu16(); //expect: GolangIntrinsicIssue
    _mm_adds_epu8(); //expect: GolangIntrinsicIssue
    _mm_aesdeclast_si128(); //expect: GolangIntrinsicIssue
    _mm_aesdec_si128(); //expect: GolangIntrinsicIssue
    _mm_aesenclast_si128(); //expect: GolangIntrinsicIssue
    _mm_aesenc_si128(); //expect: GolangIntrinsicIssue
    _mm_aesimc_si128(); //expect: GolangIntrinsicIssue
    _mm_aeskeygenassist_si128(); //expect: GolangIntrinsicIssue
    _mm_alignr_epi8(); //expect: GolangIntrinsicIssue
    _mm_andnot_si128(); //expect: GolangIntrinsicIssue
    _mm_andnot_si128(); //expect: GolangIntrinsicIssue
    _mm_and_si128(); //expect: GolangIntrinsicIssue
    _mm_avg_epu16(); //expect: GolangIntrinsicIssue
    _mm_avg_epu8(); //expect: GolangIntrinsicIssue
    _mm_blend_epi16(); //expect: GolangIntrinsicIssue
    _mm_blend_epi32(); //expect: GolangIntrinsicIssue
    _mm_blendv_epi8(); //expect: GolangIntrinsicIssue
    _mm_broadcastb_epi8(); //expect: GolangIntrinsicIssue
    _mm_broadcastd_epi32(); //expect: GolangIntrinsicIssue
    _mm_broadcastq_epi64(); //expect: GolangIntrinsicIssue
    _mm_broadcastw_epi16(); //expect: GolangIntrinsicIssue
    _mm_castpd_si128(); //expect: GolangIntrinsicIssue
    _mm_castps_si128(); //expect: GolangIntrinsicIssue
    _mm_clmulepi64_si128(); //expect: GolangIntrinsicIssue
    _mm_cmov_si128(); //expect: GolangIntrinsicIssue
    _mm_cmpeq_epi16(); //expect: GolangIntrinsicIssue
    _mm_cmpeq_epi32(); //expect: GolangIntrinsicIssue
    _mm_cmpeq_epi64(); //expect: GolangIntrinsicIssue
    _mm_cmpeq_epi8(); //expect: GolangIntrinsicIssue
    _mm_cmpestrm(); //expect: GolangIntrinsicIssue
    _mm_cmpgt_epi16(); //expect: GolangIntrinsicIssue
    _mm_cmpgt_epi32(); //expect: GolangIntrinsicIssue
    _mm_cmpgt_epi64(); //expect: GolangIntrinsicIssue
    _mm_cmpgt_epi8(); //expect: GolangIntrinsicIssue
    _mm_cmpistrm(); //expect: GolangIntrinsicIssue
    _mm_cmplt_epi16(); //expect: GolangIntrinsicIssue
    _mm_cmplt_epi32(); //expect: GolangIntrinsicIssue
    _mm_cmplt_epi8(); //expect: GolangIntrinsicIssue
    _mm_com_epi16(); //expect: GolangIntrinsicIssue
    _mm_com_epi32(); //expect: GolangIntrinsicIssue
    _mm_com_epi64(); //expect: GolangIntrinsicIssue
    _mm_com_epi8(); //expect: GolangIntrinsicIssue
    _mm_com_epu16(); //expect: GolangIntrinsicIssue
    _mm_com_epu32(); //expect: GolangIntrinsicIssue
    _mm_com_epu64(); //expect: GolangIntrinsicIssue
    _mm_com_epu8(); //expect: GolangIntrinsicIssue
    _mm_cvtepi16_epi32(); //expect: GolangIntrinsicIssue
    _mm_cvtepi16_epi64(); //expect: GolangIntrinsicIssue
    _mm_cvtepi32_epi64(); //expect: GolangIntrinsicIssue
    _mm_cvtepi8_epi16(); //expect: GolangIntrinsicIssue
    _mm_cvtepi8_epi32(); //expect: GolangIntrinsicIssue
    _mm_cvtepi8_epi64(); //expect: GolangIntrinsicIssue
    _mm_cvtepu16_epi32(); //expect: GolangIntrinsicIssue
    _mm_cvtepu16_epi64(); //expect: GolangIntrinsicIssue
    _mm_cvtepu32_epi64(); //expect: GolangIntrinsicIssue
    _mm_cvtepu8_epi16(); //expect: GolangIntrinsicIssue
    _mm_cvtepu8_epi32(); //expect: GolangIntrinsicIssue
    _mm_cvtepu8_epi64(); //expect: GolangIntrinsicIssue
    _mm_cvtpd_epi32(); //expect: GolangIntrinsicIssue
    _mm_cvtps_epi32(); //expect: GolangIntrinsicIssue
    _mm_cvtps_ph(); //expect: GolangIntrinsicIssue
    _mm_cvtsi32_si128(); //expect: GolangIntrinsicIssue
    _mm_cvtsi64_si128(); //expect: GolangIntrinsicIssue
    _mm_cvtsi64x_si128(); //expect: GolangIntrinsicIssue
    _mm_cvttpd_epi32(); //expect: GolangIntrinsicIssue
    _mm_cvttps_epi32(); //expect: GolangIntrinsicIssue
    _mm_extracti_si64(); //expect: GolangIntrinsicIssue
    _mm_extract_si64(); //expect: GolangIntrinsicIssue
    _mm_haddd_epi16(); //expect: GolangIntrinsicIssue
    _mm_haddd_epi8(); //expect: GolangIntrinsicIssue
    _mm_haddd_epu16(); //expect: GolangIntrinsicIssue
    _mm_haddd_epu8(); //expect: GolangIntrinsicIssue
    _mm_hadd_epi16(); //expect: GolangIntrinsicIssue
    _mm_hadd_epi32(); //expect: GolangIntrinsicIssue
    _mm_haddq_epi16(); //expect: GolangIntrinsicIssue
    _mm_haddq_epi32(); //expect: GolangIntrinsicIssue
    _mm_haddq_epi8(); //expect: GolangIntrinsicIssue
    _mm_haddq_epu16(); //expect: GolangIntrinsicIssue
    _mm_haddq_epu32(); //expect: GolangIntrinsicIssue
    _mm_haddq_epu8(); //expect: GolangIntrinsicIssue
    _mm_hadds_epi16(); //expect: GolangIntrinsicIssue
    _mm_haddw_epi8(); //expect: GolangIntrinsicIssue
    _mm_haddw_epu8(); //expect: GolangIntrinsicIssue
    _mm_hsubd_epi16(); //expect: GolangIntrinsicIssue
    _mm_hsub_epi16(); //expect: GolangIntrinsicIssue
    _mm_hsub_epi32(); //expect: GolangIntrinsicIssue
    _mm_hsubq_epi32(); //expect: GolangIntrinsicIssue
    _mm_hsubs_epi16(); //expect: GolangIntrinsicIssue
    _mm_hsubw_epi8(); //expect: GolangIntrinsicIssue
    _mm_i32gather_epi32(); //expect: GolangIntrinsicIssue
    _mm_i32gather_epi64(); //expect: GolangIntrinsicIssue
    _mm_i64gather_epi32(); //expect: GolangIntrinsicIssue
    _mm_i64gather_epi64(); //expect: GolangIntrinsicIssue
    _mm_insert_epi16(); //expect: GolangIntrinsicIssue
    _mm_insert_epi32(); //expect: GolangIntrinsicIssue
    _mm_insert_epi64(); //expect: GolangIntrinsicIssue
    _mm_insert_epi8(); //expect: GolangIntrinsicIssue
    _mm_inserti_si64(); //expect: GolangIntrinsicIssue
    _mm_insert_si64(); //expect: GolangIntrinsicIssue
    _mm_lddqu_si128(); //expect: GolangIntrinsicIssue
    _mm_loadl_epi64(); //expect: GolangIntrinsicIssue
    _mm_load_si128(); //expect: GolangIntrinsicIssue
    _mm_loadu_si128(); //expect: GolangIntrinsicIssue
    _mm_maccd_epi16(); //expect: GolangIntrinsicIssue
    _mm_macc_epi16(); //expect: GolangIntrinsicIssue
    _mm_macc_epi32(); //expect: GolangIntrinsicIssue
    _mm_macchi_epi32(); //expect: GolangIntrinsicIssue
    _mm_macclo_epi32(); //expect: GolangIntrinsicIssue
    _mm_maccsd_epi16(); //expect: GolangIntrinsicIssue
    _mm_maccs_epi16(); //expect: GolangIntrinsicIssue
    _mm_maccs_epi32(); //expect: GolangIntrinsicIssue
    _mm_maccshi_epi32(); //expect: GolangIntrinsicIssue
    _mm_maccslo_epi32(); //expect: GolangIntrinsicIssue
    _mm_maddd_epi16(); //expect: GolangIntrinsicIssue
    _mm_madd_epi16(); //expect: GolangIntrinsicIssue
    _mm_maddsd_epi16(); //expect: GolangIntrinsicIssue
    _mm_maddubs_epi16(); //expect: GolangIntrinsicIssue
    _mm_mask_i32gather_epi32(); //expect: GolangIntrinsicIssue
    _mm_mask_i32gather_epi64(); //expect: GolangIntrinsicIssue
    _mm_mask_i64gather_epi32(); //expect: GolangIntrinsicIssue
    _mm_mask_i64gather_epi64(); //expect: GolangIntrinsicIssue
    _mm_maskload_epi32(); //expect: GolangIntrinsicIssue
    _mm_maskload_epi64(); //expect: GolangIntrinsicIssue
    _mm_max_epi16(); //expect: GolangIntrinsicIssue
    _mm_max_epi32(); //expect: GolangIntrinsicIssue
    _mm_max_epi8 (); //expect: GolangIntrinsicIssue
    _mm_max_epu16(); //expect: GolangIntrinsicIssue
    _mm_max_epu32(); //expect: GolangIntrinsicIssue
    _mm_max_epu8(); //expect: GolangIntrinsicIssue
    _mm_min_epi16(); //expect: GolangIntrinsicIssue
    _mm_min_epi32(); //expect: GolangIntrinsicIssue
    _mm_min_epi8(); //expect: GolangIntrinsicIssue
    _mm_min_epu16(); //expect: GolangIntrinsicIssue
    _mm_min_epu32(); //expect: GolangIntrinsicIssue
    _mm_min_epu8(); //expect: GolangIntrinsicIssue
    _mm_minpos_epu16(); //expect: GolangIntrinsicIssue
    _mm_move_epi64(); //expect: GolangIntrinsicIssue
    _mm_movpi64_epi64(); //expect: GolangIntrinsicIssue
    _mm_mpsadbw_epu8(); //expect: GolangIntrinsicIssue
    _mm_mul_epi32(); //expect: GolangIntrinsicIssue
    _mm_mul_epu32(); //expect: GolangIntrinsicIssue
    _mm_mulhi_epi16(); //expect: GolangIntrinsicIssue
    _mm_mulhi_epu16(); //expect: GolangIntrinsicIssue
    _mm_mulhrs_epi16(); //expect: GolangIntrinsicIssue
    _mm_mullo_epi16(); //expect: GolangIntrinsicIssue
    _mm_mullo_epi32(); //expect: GolangIntrinsicIssue
    _mm_or_si128(); //expect: GolangIntrinsicIssue
    _mm_packs_epi16(); //expect: GolangIntrinsicIssue
    _mm_packs_epi32(); //expect: GolangIntrinsicIssue
    _mm_packus_epi16(); //expect: GolangIntrinsicIssue
    _mm_packus_epi32(); //expect: GolangIntrinsicIssue
    _mm_perm_epi8(); //expect: GolangIntrinsicIssue
    _mm_rot_epi16(); //expect: GolangIntrinsicIssue
    _mm_rot_epi16(); //expect: GolangIntrinsicIssue
    _mm_rot_epi32(); //expect: GolangIntrinsicIssue
    _mm_rot_epi32(); //expect: GolangIntrinsicIssue
    _mm_rot_epi64(); //expect: GolangIntrinsicIssue
    _mm_rot_epi64(); //expect: GolangIntrinsicIssue
    _mm_rot_epi8(); //expect: GolangIntrinsicIssue
    _mm_rot_epi8(); //expect: GolangIntrinsicIssue
    _mm_roti_epi16(); //expect: GolangIntrinsicIssue
    _mm_roti_epi32(); //expect: GolangIntrinsicIssue
    _mm_roti_epi64(); //expect: GolangIntrinsicIssue
    _mm_roti_epi8(); //expect: GolangIntrinsicIssue
    _mm_sad_epu8(); //expect: GolangIntrinsicIssue
    _mm_set1_epi16(); //expect: GolangIntrinsicIssue
    _mm_set1_epi32(); //expect: GolangIntrinsicIssue
    _mm_set1_epi64(); //expect: GolangIntrinsicIssue
    _mm_set1_epi64x(); //expect: GolangIntrinsicIssue
    _mm_set1_epi8(); //expect: GolangIntrinsicIssue
    _mm_set_epi16(); //expect: GolangIntrinsicIssue
    _mm_set_epi32(); //expect: GolangIntrinsicIssue
    _mm_set_epi64(); //expect: GolangIntrinsicIssue
    _mm_set_epi64x(); //expect: GolangIntrinsicIssue
    _mm_set_epi8(); //expect: GolangIntrinsicIssue
    _mm_setl_epi64(); //expect: GolangIntrinsicIssue
    _mm_setr_epi16(); //expect: GolangIntrinsicIssue
    _mm_setr_epi32(); //expect: GolangIntrinsicIssue
    _mm_setr_epi64(); //expect: GolangIntrinsicIssue
    _mm_setr_epi8(); //expect: GolangIntrinsicIssue
    _mm_setzero_si128(); //expect: GolangIntrinsicIssue
    _mm_sha_epi16(); //expect: GolangIntrinsicIssue
    _mm_sha_epi32(); //expect: GolangIntrinsicIssue
    _mm_sha_epi64(); //expect: GolangIntrinsicIssue
    _mm_sha_epi8(); //expect: GolangIntrinsicIssue
    _mm_shl_epi16(); //expect: GolangIntrinsicIssue
    _mm_shl_epi32(); //expect: GolangIntrinsicIssue
    _mm_shl_epi64(); //expect: GolangIntrinsicIssue
    _mm_shl_epi8(); //expect: GolangIntrinsicIssue
    _mm_shuffle_epi32(); //expect: GolangIntrinsicIssue
    _mm_shuffle_epi8(); //expect: GolangIntrinsicIssue
    _mm_shufflehi_epi16(); //expect: GolangIntrinsicIssue
    _mm_shufflelo_epi16(); //expect: GolangIntrinsicIssue
    _mm_sign_epi16(); //expect: GolangIntrinsicIssue
    _mm_sign_epi32(); //expect: GolangIntrinsicIssue
    _mm_sign_epi8(); //expect: GolangIntrinsicIssue
    _mm_sll_epi16(); //expect: GolangIntrinsicIssue
    _mm_sll_epi32(); //expect: GolangIntrinsicIssue
    _mm_sll_epi64(); //expect: GolangIntrinsicIssue
    _mm_slli_epi16(); //expect: GolangIntrinsicIssue
    _mm_slli_epi32(); //expect: GolangIntrinsicIssue
    _mm_slli_epi64(); //expect: GolangIntrinsicIssue
    _mm_slli_si128(); //expect: GolangIntrinsicIssue
    _mm_sllv_epi32(); //expect: GolangIntrinsicIssue
    _mm_sllv_epi64(); //expect: GolangIntrinsicIssue
    _mm_sra_epi16(); //expect: GolangIntrinsicIssue
    _mm_sra_epi32(); //expect: GolangIntrinsicIssue
    _mm_srai_epi16(); //expect: GolangIntrinsicIssue
    _mm_srai_epi32(); //expect: GolangIntrinsicIssue
    _mm_srav_epi32(); //expect: GolangIntrinsicIssue
    _mm_srl_epi16(); //expect: GolangIntrinsicIssue
    _mm_srl_epi32(); //expect: GolangIntrinsicIssue
    _mm_srl_epi64(); //expect: GolangIntrinsicIssue
    _mm_srli_epi16(); //expect: GolangIntrinsicIssue
    _mm_srli_epi32(); //expect: GolangIntrinsicIssue
    _mm_srli_epi64(); //expect: GolangIntrinsicIssue
    _mm_srli_si128(); //expect: GolangIntrinsicIssue
    _mm_srlv_epi32(); //expect: GolangIntrinsicIssue
    _mm_srlv_epi64(); //expect: GolangIntrinsicIssue
    _mm_stream_load_si128(); //expect: GolangIntrinsicIssue
    _mm_sub_epi16(); //expect: GolangIntrinsicIssue
    _mm_sub_epi32(); //expect: GolangIntrinsicIssue
    _mm_sub_epi64(); //expect: GolangIntrinsicIssue
    _mm_sub_epi8(); //expect: GolangIntrinsicIssue
    _mm_subs_epi16(); //expect: GolangIntrinsicIssue
    _mm_subs_epi8(); //expect: GolangIntrinsicIssue
    _mm_subs_epu16(); //expect: GolangIntrinsicIssue
    _mm_subs_epu8(); //expect: GolangIntrinsicIssue
    _mm_unpackhi_epi16(); //expect: GolangIntrinsicIssue
    _mm_unpackhi_epi32(); //expect: GolangIntrinsicIssue
    _mm_unpackhi_epi64(); //expect: GolangIntrinsicIssue
    _mm_unpackhi_epi8(); //expect: GolangIntrinsicIssue
    _mm_unpacklo_epi16(); //expect: GolangIntrinsicIssue
    _mm_unpacklo_epi32(); //expect: GolangIntrinsicIssue
    _mm_unpacklo_epi64(); //expect: GolangIntrinsicIssue
    _mm_unpacklo_epi8(); //expect: GolangIntrinsicIssue
    _mm_xor_si128(); //expect: GolangIntrinsicIssue
    _mm256_castps256_ps128(); //expect: GolangIntrinsicIssue
    _mm256_cvtpd_ps(); //expect: GolangIntrinsicIssue
    _mm256_extractf128_ps(); //expect: GolangIntrinsicIssue
    _mm256_i64gather_ps(); //expect: GolangIntrinsicIssue
    _mm256_mask_i64gather_ps(); //expect: GolangIntrinsicIssue
    _mm_add_ps(); //expect: GolangIntrinsicIssue
    _mm_add_ss(); //expect: GolangIntrinsicIssue
    _mm_addsub_ps(); //expect: GolangIntrinsicIssue
    _mm_andnot_ps(); //expect: GolangIntrinsicIssue
    _mm_and_ps(); //expect: GolangIntrinsicIssue
    _mm_blend_ps(); //expect: GolangIntrinsicIssue
    _mm_blendv_ps(); //expect: GolangIntrinsicIssue
    _mm_broadcast_ss(); //expect: GolangIntrinsicIssue
    _mm_broadcastss_ps(); //expect: GolangIntrinsicIssue
    _mm_castpd_ps(); //expect: GolangIntrinsicIssue
    _mm_castsi128_ps(); //expect: GolangIntrinsicIssue
    _mm_cmpeq_ps(); //expect: GolangIntrinsicIssue
    _mm_cmpeq_ss(); //expect: GolangIntrinsicIssue
    _mm_cmpge_ps(); //expect: GolangIntrinsicIssue
    _mm_cmpge_ss(); //expect: GolangIntrinsicIssue
    _mm_cmpgt_ps(); //expect: GolangIntrinsicIssue
    _mm_cmpgt_ss(); //expect: GolangIntrinsicIssue
    _mm_cmple_ps(); //expect: GolangIntrinsicIssue
    _mm_cmple_ss(); //expect: GolangIntrinsicIssue
    _mm_cmplt_ps(); //expect: GolangIntrinsicIssue
    _mm_cmplt_ss(); //expect: GolangIntrinsicIssue
    _mm_cmpneq_ps(); //expect: GolangIntrinsicIssue
    _mm_cmpneq_ss(); //expect: GolangIntrinsicIssue
    _mm_cmpnge_ps(); //expect: GolangIntrinsicIssue
    _mm_cmpnge_ss(); //expect: GolangIntrinsicIssue
    _mm_cmpngt_ps(); //expect: GolangIntrinsicIssue
    _mm_cmpngt_ss(); //expect: GolangIntrinsicIssue
    _mm_cmpnle_ps(); //expect: GolangIntrinsicIssue
    _mm_cmpnle_ss(); //expect: GolangIntrinsicIssue
    _mm_cmpnlt_ps(); //expect: GolangIntrinsicIssue
    _mm_cmpnlt_ss(); //expect: GolangIntrinsicIssue
    _mm_cmpord_ps(); //expect: GolangIntrinsicIssue
    _mm_cmpord_ss(); //expect: GolangIntrinsicIssue
    _mm_cmp_ps(); //expect: GolangIntrinsicIssue
    _mm_cmp_ss(); //expect: GolangIntrinsicIssue
    _mm_cmpunord_ps(); //expect: GolangIntrinsicIssue
    _mm_cmpunord_ss(); //expect: GolangIntrinsicIssue
    _mm_cvtepi32_ps(); //expect: GolangIntrinsicIssue
    _mm_cvtpd_ps(); //expect: GolangIntrinsicIssue
    _mm_cvtph_ps(); //expect: GolangIntrinsicIssue
    _mm_cvt_pi2ps(); //expect: GolangIntrinsicIssue
    _mm_cvtsd_ss(); //expect: GolangIntrinsicIssue
    _mm_cvt_si2ss(); //expect: GolangIntrinsicIssue
    _mm_cvtsi64_ss(); //expect: GolangIntrinsicIssue
    _mm_cvtsi64x_ss(); //expect: GolangIntrinsicIssue
    _mm_div_ps(); //expect: GolangIntrinsicIssue
    _mm_div_ss(); //expect: GolangIntrinsicIssue
    _mm_dp_ps(); //expect: GolangIntrinsicIssue
    _mm_fmadd_ps(); //expect: GolangIntrinsicIssue
    _mm_fmadd_ss(); //expect: GolangIntrinsicIssue
    _mm_fmaddsub_ps(); //expect: GolangIntrinsicIssue
    _mm_fmsubadd_ps(); //expect: GolangIntrinsicIssue
    _mm_fmsub_ps(); //expect: GolangIntrinsicIssue
    _mm_fmsub_ss(); //expect: GolangIntrinsicIssue
    _mm_fnmadd_ps(); //expect: GolangIntrinsicIssue
    _mm_fnmadd_ss(); //expect: GolangIntrinsicIssue
    _mm_fnmsub_ps(); //expect: GolangIntrinsicIssue
    _mm_fnmsub_ss(); //expect: GolangIntrinsicIssue
    _mm_frcz_ps(); //expect: GolangIntrinsicIssue
    _mm_frcz_ss(); //expect: GolangIntrinsicIssue
    _mm_hadd_ps(); //expect: GolangIntrinsicIssue
    _mm_hsub_ps(); //expect: GolangIntrinsicIssue
    _mm_i32gather_ps(); //expect: GolangIntrinsicIssue
    _mm_i64gather_ps(); //expect: GolangIntrinsicIssue
    _mm_insert_ps(); //expect: GolangIntrinsicIssue
    _mm_loadh_pi(); //expect: GolangIntrinsicIssue
    _mm_loadl_pi(); //expect: GolangIntrinsicIssue
    _mm_load_ps1(); //expect: GolangIntrinsicIssue
    _mm_load_ps(); //expect: GolangIntrinsicIssue
    _mm_loadr_ps(); //expect: GolangIntrinsicIssue
    _mm_load_ss(); //expect: GolangIntrinsicIssue
    _mm_loadu_ps(); //expect: GolangIntrinsicIssue
    _mm_macc_ps(); //expect: GolangIntrinsicIssue
    _mm_macc_ss(); //expect: GolangIntrinsicIssue
    _mm_maddsub_ps(); //expect: GolangIntrinsicIssue
    _mm_mask_i32gather_ps(); //expect: GolangIntrinsicIssue
    _mm_mask_i64gather_ps(); //expect: GolangIntrinsicIssue
    _mm_maskload_ps(); //expect: GolangIntrinsicIssue
    _mm_max_ps(); //expect: GolangIntrinsicIssue
    _mm_max_ss(); //expect: GolangIntrinsicIssue
    _mm_min_ps(); //expect: GolangIntrinsicIssue
    _mm_min_ss(); //expect: GolangIntrinsicIssue
    _mm_movehdup_ps(); //expect: GolangIntrinsicIssue
    _mm_movehl_ps(); //expect: GolangIntrinsicIssue
    _mm_moveldup_ps(); //expect: GolangIntrinsicIssue
    _mm_movelh_ps(); //expect: GolangIntrinsicIssue
    _mm_move_ss(); //expect: GolangIntrinsicIssue
    _mm_msubadd_ps(); //expect: GolangIntrinsicIssue
    _mm_msub_ps(); //expect: GolangIntrinsicIssue
    _mm_msub_ss(); //expect: GolangIntrinsicIssue
    _mm_mul_ps(); //expect: GolangIntrinsicIssue
    _mm_mul_ss(); //expect: GolangIntrinsicIssue
    _mm_nmacc_ps(); //expect: GolangIntrinsicIssue
    _mm_nmacc_ss(); //expect: GolangIntrinsicIssue
    _mm_nmsub_ps(); //expect: GolangIntrinsicIssue
    _mm_nmsub_ss(); //expect: GolangIntrinsicIssue
    _mm_or_ps(); //expect: GolangIntrinsicIssue
    _mm_permute2_ps(); //expect: GolangIntrinsicIssue
    _mm_permute_ps(); //expect: GolangIntrinsicIssue
    _mm_permutevar_ps(); //expect: GolangIntrinsicIssue
    _mm_rcp_ps(); //expect: GolangIntrinsicIssue
    _mm_rcp_ss(); //expect: GolangIntrinsicIssue
    _mm_round_ps(); //expect: GolangIntrinsicIssue
    _mm_round_ss(); //expect: GolangIntrinsicIssue
    _mm_rsqrt_ps(); //expect: GolangIntrinsicIssue
    _mm_rsqrt_ss(); //expect: GolangIntrinsicIssue
    _mm_set_ps1(); //expect: GolangIntrinsicIssue
    _mm_set_ps(); //expect: GolangIntrinsicIssue
    _mm_setr_ps(); //expect: GolangIntrinsicIssue
    _mm_set_ss(); //expect: GolangIntrinsicIssue
    _mm_setzero_ps(); //expect: GolangIntrinsicIssue
    _mm_shuffle_ps(); //expect: GolangIntrinsicIssue
    _mm_sqrt_ps(); //expect: GolangIntrinsicIssue
    _mm_sqrt_ss(); //expect: GolangIntrinsicIssue
    _mm_sub_ps(); //expect: GolangIntrinsicIssue
    _mm_sub_ss(); //expect: GolangIntrinsicIssue
    _mm_unpackhi_ps(); //expect: GolangIntrinsicIssue
    _mm_unpacklo_ps(); //expect: GolangIntrinsicIssue
    _mm_xor_ps(); //expect: GolangIntrinsicIssue
    _mm256_add_pd(); //expect: GolangIntrinsicIssue
    _mm256_addsub_pd(); //expect: GolangIntrinsicIssue
    _mm256_andnot_pd(); //expect: GolangIntrinsicIssue
    _mm256_and_pd(); //expect: GolangIntrinsicIssue
    _mm256_blend_pd(); //expect: GolangIntrinsicIssue
    _mm256_blendv_pd(); //expect: GolangIntrinsicIssue
    _mm256_broadcast_pd(); //expect: GolangIntrinsicIssue
    _mm256_broadcast_sd(); //expect: GolangIntrinsicIssue
    _mm256_broadcastsd_pd(); //expect: GolangIntrinsicIssue
    _mm256_castpd128_pd256(); //expect: GolangIntrinsicIssue
    _mm256_castps_pd(); //expect: GolangIntrinsicIssue
    _mm256_castsi256_pd(); //expect: GolangIntrinsicIssue
    _mm256_cmp_pd(); //expect: GolangIntrinsicIssue
    _mm256_cvtepi32_pd(); //expect: GolangIntrinsicIssue
    _mm256_cvtps_pd(); //expect: GolangIntrinsicIssue
    _mm256_div_pd(); //expect: GolangIntrinsicIssue
    _mm256_fmadd_pd(); //expect: GolangIntrinsicIssue
    _mm256_fmaddsub_pd(); //expect: GolangIntrinsicIssue
    _mm256_fmsubadd_pd(); //expect: GolangIntrinsicIssue
    _mm256_fmsub_pd(); //expect: GolangIntrinsicIssue
    _mm256_fnmadd_pd(); //expect: GolangIntrinsicIssue
    _mm256_fnmsub_pd(); //expect: GolangIntrinsicIssue
    _mm256_frcz_pd(); //expect: GolangIntrinsicIssue
    _mm256_hadd_pd(); //expect: GolangIntrinsicIssue
    _mm256_hsub_pd(); //expect: GolangIntrinsicIssue
    _mm256_i32gather_pd(); //expect: GolangIntrinsicIssue
    _mm256_i64gather_pd(); //expect: GolangIntrinsicIssue
    _mm256_insertf128_pd(); //expect: GolangIntrinsicIssue
    _mm256_load_pd(); //expect: GolangIntrinsicIssue
    _mm256_loadu_pd(); //expect: GolangIntrinsicIssue
     _mm256_macc_pd(); //expect: GolangIntrinsicIssue
    _mm256_maddsub_pd(); //expect: GolangIntrinsicIssue
    _mm256_mask_i32gather_pd(); //expect: GolangIntrinsicIssue
    _mm256_mask_i64gather_pd(); //expect: GolangIntrinsicIssue
    _mm256_maskload_pd(); //expect: GolangIntrinsicIssue
    _mm256_max_pd(); //expect: GolangIntrinsicIssue
    _mm256_min_pd(); //expect: GolangIntrinsicIssue
    _mm256_movedup_pd(); //expect: GolangIntrinsicIssue
    _mm256_msubadd_pd(); //expect: GolangIntrinsicIssue
    _mm256_msub_pd(); //expect: GolangIntrinsicIssue
    _mm256_mul_pd(); //expect: GolangIntrinsicIssue
    _mm256_nmacc_pd(); //expect: GolangIntrinsicIssue
    _mm256_nmsub_pd(); //expect: GolangIntrinsicIssue
    _mm256_or_pd(); //expect: GolangIntrinsicIssue
    _mm256_permute2f128_pd(); //expect: GolangIntrinsicIssue
    _mm256_permute2_pd(); //expect: GolangIntrinsicIssue
    _mm256_permute4x64_pd(); //expect: GolangIntrinsicIssue
    _mm256_permute_pd(); //expect: GolangIntrinsicIssue
    _mm256_permutevar_pd(); //expect: GolangIntrinsicIssue
    _mm256_round_pd(); //expect: GolangIntrinsicIssue
    _mm256_set1_pd(); //expect: GolangIntrinsicIssue
    _mm256_set_pd(); //expect: GolangIntrinsicIssue
    _mm256_setr_pd(); //expect: GolangIntrinsicIssue
    _mm256_setzero_pd(); //expect: GolangIntrinsicIssue
    _mm256_shuffle_pd(); //expect: GolangIntrinsicIssue
    _mm256_sqrt_pd(); //expect: GolangIntrinsicIssue
    _mm256_sub_pd(); //expect: GolangIntrinsicIssue
    _mm256_unpackhi_pd(); //expect: GolangIntrinsicIssue
    _mm256_unpacklo_pd(); //expect: GolangIntrinsicIssue
    _mm256_xor_pd(); //expect: GolangIntrinsicIssue
    _mm_macc_pd(); //expect: GolangIntrinsicIssue
    _mm_maddsub_pd(); //expect: GolangIntrinsicIssue
    _mm_msubadd_pd(); //expect: GolangIntrinsicIssue
    _mm_msub_pd(); //expect: GolangIntrinsicIssue
    _mm_nmacc_pd(); //expect: GolangIntrinsicIssue
    _mm_nmsub_pd(); //expect: GolangIntrinsicIssue
    _mm256_abs_epi16(); //expect: GolangIntrinsicIssue
    _mm256_abs_epi32(); //expect: GolangIntrinsicIssue
    _mm256_abs_epi8(); //expect: GolangIntrinsicIssue
    _mm256_add_epi16(); //expect: GolangIntrinsicIssue
    _mm256_add_epi32(); //expect: GolangIntrinsicIssue
    _mm256_add_epi64(); //expect: GolangIntrinsicIssue
    _mm256_add_epi8(); //expect: GolangIntrinsicIssue
    _mm256_adds_epi16(); //expect: GolangIntrinsicIssue
    _mm256_adds_epi8(); //expect: GolangIntrinsicIssue
    _mm256_adds_epu16(); //expect: GolangIntrinsicIssue
    _mm256_adds_epu8(); //expect: GolangIntrinsicIssue
    _mm256_alignr_epi8(); //expect: GolangIntrinsicIssue
    _mm256_andnot_si256(); //expect: GolangIntrinsicIssue
    _mm256_and_si256(); //expect: GolangIntrinsicIssue
    _mm256_avg_epu16(); //expect: GolangIntrinsicIssue
    _mm256_avg_epu8(); //expect: GolangIntrinsicIssue
    _mm256_avg_epu8(); //expect: GolangIntrinsicIssue
    _mm256_blend_epi16(); //expect: GolangIntrinsicIssue
    _mm256_blend_epi32(); //expect: GolangIntrinsicIssue
    _mm256_blendv_epi8(); //expect: GolangIntrinsicIssue
    _mm256_broadcastb_epi8(); //expect: GolangIntrinsicIssue
    _mm256_broadcastd_epi32(); //expect: GolangIntrinsicIssue
    _mm256_broadcastq_epi64(); //expect: GolangIntrinsicIssue
    _mm256_broadcastsi128_si256(); //expect: GolangIntrinsicIssue
    _mm256_broadcastw_epi16(); //expect: GolangIntrinsicIssue
    _mm256_castpd_si256(); //expect: GolangIntrinsicIssue
    _mm256_castps_si256(); //expect: GolangIntrinsicIssue
    _mm256_castsi128_si256(); //expect: GolangIntrinsicIssue
    _mm256_cmov_si256(); //expect: GolangIntrinsicIssue
    _mm256_cmpeq_epi16(); //expect: GolangIntrinsicIssue
    _mm256_cmpeq_epi32(); //expect: GolangIntrinsicIssue
    _mm256_cmpeq_epi64(); //expect: GolangIntrinsicIssue
    _mm256_cmpeq_epi8(); //expect: GolangIntrinsicIssue
    _mm256_cmpgt_epi16(); //expect: GolangIntrinsicIssue
    _mm256_cmpgt_epi32(); //expect: GolangIntrinsicIssue
    _mm256_cmpgt_epi64(); //expect: GolangIntrinsicIssue
    _mm256_cmpgt_epi8(); //expect: GolangIntrinsicIssue
    _mm256_cvtepi16_epi32(); //expect: GolangIntrinsicIssue
    _mm256_cvtepi16_epi64(); //expect: GolangIntrinsicIssue
    _mm256_cvtepi32_epi64(); //expect: GolangIntrinsicIssue
    _mm256_cvtepi8_epi16(); //expect: GolangIntrinsicIssue
    _mm256_cvtepi8_epi32(); //expect: GolangIntrinsicIssue
    _mm256_cvtepi8_epi64(); //expect: GolangIntrinsicIssue
    _mm256_cvtepu16_epi32(); //expect: GolangIntrinsicIssue
    _mm256_cvtepu16_epi64(); //expect: GolangIntrinsicIssue
    _mm256_cvtepu32_epi64(); //expect: GolangIntrinsicIssue
    _mm256_cvtepu8_epi16(); //expect: GolangIntrinsicIssue
    _mm256_cvtepu8_epi32(); //expect: GolangIntrinsicIssue
    _mm256_cvtepu8_epi64(); //expect: GolangIntrinsicIssue
    _mm256_cvtps_epi32(); //expect: GolangIntrinsicIssue
    _mm256_cvttps_epi32(); //expect: GolangIntrinsicIssue
    _mm256_hadd_epi16(); //expect: GolangIntrinsicIssue
    _mm256_hadd_epi32(); //expect: GolangIntrinsicIssue
    _mm256_hadds_epi16(); //expect: GolangIntrinsicIssue
    _mm256_hsub_epi16(); //expect: GolangIntrinsicIssue
    _mm256_hsub_epi32(); //expect: GolangIntrinsicIssue
    _mm256_hsubs_epi16(); //expect: GolangIntrinsicIssue
    _mm256_i32gather_epi32(); //expect: GolangIntrinsicIssue
    _mm256_i32gather_epi64(); //expect: GolangIntrinsicIssue
    _mm256_i64gather_epi32(); //expect: GolangIntrinsicIssue
    _mm256_i64gather_epi64(); //expect: GolangIntrinsicIssue
    _mm256_insertf128_si256(); //expect: GolangIntrinsicIssue
    _mm256_inserti128_si256(); //expect: GolangIntrinsicIssue
    _mm256_lddqu_si256(); //expect: GolangIntrinsicIssue
    _mm256_load_si256(); //expect: GolangIntrinsicIssue
    _mm256_loadu_si256(); //expect: GolangIntrinsicIssue
    _mm256_madd_epi16(); //expect: GolangIntrinsicIssue
    _mm256_maddubs_epi16(); //expect: GolangIntrinsicIssue
    _mm256_mask_i32gather_epi32(); //expect: GolangIntrinsicIssue
    _mm256_mask_i32gather_epi64(); //expect: GolangIntrinsicIssue
    _mm256_mask_i64gather_epi64(); //expect: GolangIntrinsicIssue
    _mm256_maskload_epi32(); //expect: GolangIntrinsicIssue
    _mm256_maskload_epi64(); //expect: GolangIntrinsicIssue
    _mm256_max_epi16(); //expect: GolangIntrinsicIssue
    _mm256_max_epi32(); //expect: GolangIntrinsicIssue
    _mm256_max_epi8(); //expect: GolangIntrinsicIssue
    _mm256_max_epu16(); //expect: GolangIntrinsicIssue
    _mm256_max_epu32(); //expect: GolangIntrinsicIssue
    _mm256_max_epu8(); //expect: GolangIntrinsicIssue
    _mm256_min_epi16(); //expect: GolangIntrinsicIssue
    _mm256_min_epi32(); //expect: GolangIntrinsicIssue
    _mm256_min_epi8(); //expect: GolangIntrinsicIssue
    _mm256_min_epu16(); //expect: GolangIntrinsicIssue
    _mm256_min_epu32(); //expect: GolangIntrinsicIssue
    _mm256_min_epu8(); //expect: GolangIntrinsicIssue
    _mm256_mpsadbw_epu8(); //expect: GolangIntrinsicIssue
    _mm256_mul_epi32(); //expect: GolangIntrinsicIssue
    _mm256_mul_epu32(); //expect: GolangIntrinsicIssue
    _mm256_mulhi_epi16(); //expect: GolangIntrinsicIssue
    _mm256_mulhi_epu16(); //expect: GolangIntrinsicIssue
    _mm256_mulhrs_epi16(); //expect: GolangIntrinsicIssue
    _mm256_mullo_epi16(); //expect: GolangIntrinsicIssue
    _mm256_mullo_epi32(); //expect: GolangIntrinsicIssue
    _mm256_or_si256(); //expect: GolangIntrinsicIssue
    _mm256_packs_epi16(); //expect: GolangIntrinsicIssue
    _mm256_packs_epi32(); //expect: GolangIntrinsicIssue
    _mm256_packus_epi16(); //expect: GolangIntrinsicIssue
    _mm256_packus_epi32(); //expect: GolangIntrinsicIssue
    _mm256_permute2f128_si256(); //expect: GolangIntrinsicIssue
    _mm256_permute2x128_si256(); //expect: GolangIntrinsicIssue
    _mm256_permute4x64_epi64(); //expect: GolangIntrinsicIssue
    _mm256_permutevar8x32_epi32(); //expect: GolangIntrinsicIssue
    _mm256_sad_epu8(); //expect: GolangIntrinsicIssue
    _mm256_set1_epi16(); //expect: GolangIntrinsicIssue
    _mm256_set1_epi32(); //expect: GolangIntrinsicIssue
    _mm256_set1_epi64x(); //expect: GolangIntrinsicIssue
    _mm256_set1_epi8(); //expect: GolangIntrinsicIssue
    _mm256_set_epi16(); //expect: GolangIntrinsicIssue
    _mm256_set_epi32(); //expect: GolangIntrinsicIssue
    _mm256_set_epi64x(); //expect: GolangIntrinsicIssue
    _mm256_set_epi8(); //expect: GolangIntrinsicIssue
    _mm256_setr_epi16(); //expect: GolangIntrinsicIssue
    _mm256_setr_epi32(); //expect: GolangIntrinsicIssue
    _mm256_setr_epi64x(); //expect: GolangIntrinsicIssue
    _mm256_setr_epi8(); //expect: GolangIntrinsicIssue
    _mm256_setzero_si256(); //expect: GolangIntrinsicIssue
    _mm256_shuffle_epi32(); //expect: GolangIntrinsicIssue
    _mm256_shuffle_epi8(); //expect: GolangIntrinsicIssue
    _mm256_shufflehi_epi16(); //expect: GolangIntrinsicIssue
    _mm256_shufflelo_epi16(); //expect: GolangIntrinsicIssue
    _mm256_sign_epi16(); //expect: GolangIntrinsicIssue
    _mm256_sign_epi32(); //expect: GolangIntrinsicIssue
    _mm256_sign_epi8(); //expect: GolangIntrinsicIssue
    _mm256_sll_epi16(); //expect: GolangIntrinsicIssue
    _mm256_sll_epi32(); //expect: GolangIntrinsicIssue
    _mm256_sll_epi64(); //expect: GolangIntrinsicIssue
    _mm256_slli_epi16(); //expect: GolangIntrinsicIssue
    _mm256_slli_epi32(); //expect: GolangIntrinsicIssue
    _mm256_slli_epi64(); //expect: GolangIntrinsicIssue
    _mm256_slli_si256(); //expect: GolangIntrinsicIssue
    _mm256_sllv_epi32(); //expect: GolangIntrinsicIssue
    _mm256_sllv_epi64(); //expect: GolangIntrinsicIssue
    _mm256_sra_epi16(); //expect: GolangIntrinsicIssue
    _mm256_sra_epi32(); //expect: GolangIntrinsicIssue
    _mm256_srai_epi16(); //expect: GolangIntrinsicIssue
    _mm256_srai_epi32(); //expect: GolangIntrinsicIssue
    _mm256_srav_epi32(); //expect: GolangIntrinsicIssue
    _mm256_srl_epi16(); //expect: GolangIntrinsicIssue
    _mm256_srl_epi32(); //expect: GolangIntrinsicIssue
    _mm256_srl_epi64(); //expect: GolangIntrinsicIssue
    _mm256_srli_epi16(); //expect: GolangIntrinsicIssue
    _mm256_srli_epi32(); //expect: GolangIntrinsicIssue
    _mm256_srli_epi64(); //expect: GolangIntrinsicIssue
    _mm256_srli_si256(); //expect: GolangIntrinsicIssue
    _mm256_srlv_epi32(); //expect: GolangIntrinsicIssue
    _mm256_srlv_epi64(); //expect: GolangIntrinsicIssue
    _mm256_stream_load_si256(); //expect: GolangIntrinsicIssue
    _mm256_sub_epi16(); //expect: GolangIntrinsicIssue
    _mm256_sub_epi32(); //expect: GolangIntrinsicIssue
    _mm256_sub_epi64(); //expect: GolangIntrinsicIssue
    _mm256_sub_epi8(); //expect: GolangIntrinsicIssue
    _mm256_subs_epi16(); //expect: GolangIntrinsicIssue
    _mm256_subs_epi8(); //expect: GolangIntrinsicIssue
    _mm256_subs_epu16(); //expect: GolangIntrinsicIssue
    _mm256_subs_epu8(); //expect: GolangIntrinsicIssue
    _mm256_unpackhi_epi16(); //expect: GolangIntrinsicIssue
    _mm256_unpackhi_epi32(); //expect: GolangIntrinsicIssue
    _mm256_unpackhi_epi64(); //expect: GolangIntrinsicIssue
    _mm256_unpackhi_epi8(); //expect: GolangIntrinsicIssue
    _mm256_unpacklo_epi16(); //expect: GolangIntrinsicIssue
    _mm256_unpacklo_epi32(); //expect: GolangIntrinsicIssue
    _mm256_unpacklo_epi64(); //expect: GolangIntrinsicIssue
    _mm256_unpacklo_epi8(); //expect: GolangIntrinsicIssue
    _mm256_xor_si256(); //expect: GolangIntrinsicIssue
    _mm256_add_ps(); //expect: GolangIntrinsicIssue
    _mm256_addsub_ps(); //expect: GolangIntrinsicIssue
    _mm256_andnot_ps(); //expect: GolangIntrinsicIssue
    _mm256_and_ps(); //expect: GolangIntrinsicIssue
    _mm256_blend_ps(); //expect: GolangIntrinsicIssue
    _mm256_blendv_ps(); //expect: GolangIntrinsicIssue
    _mm256_broadcast_ps(); //expect: GolangIntrinsicIssue
    _mm256_broadcast_ss(); //expect: GolangIntrinsicIssue
    _mm256_broadcastss_ps(); //expect: GolangIntrinsicIssue
    _mm256_castpd_ps(); //expect: GolangIntrinsicIssue
    _mm256_castps128_ps256(); //expect: GolangIntrinsicIssue
    _mm256_castsi256_ps(); //expect: GolangIntrinsicIssue
    _mm256_cmp_ps(); //expect: GolangIntrinsicIssue
    _mm256_cvtepi32_ps(); //expect: GolangIntrinsicIssue
    _mm256_cvtph_ps(); //expect: GolangIntrinsicIssue
    _mm256_div_ps(); //expect: GolangIntrinsicIssue
    _mm256_dp_ps(); //expect: GolangIntrinsicIssue
    _mm256_fmadd_ps(); //expect: GolangIntrinsicIssue
    _mm256_fmaddsub_ps(); //expect: GolangIntrinsicIssue
    _mm256_fmsubadd_ps(); //expect: GolangIntrinsicIssue
    _mm256_fmsub_ps(); //expect: GolangIntrinsicIssue
    _mm256_fnmadd_ps(); //expect: GolangIntrinsicIssue
    _mm256_fnmsub_ps(); //expect: GolangIntrinsicIssue
    _mm256_frcz_ps(); //expect: GolangIntrinsicIssue
    _mm256_hadd_ps(); //expect: GolangIntrinsicIssue
    _mm256_hsub_ps(); //expect: GolangIntrinsicIssue
    _mm256_i32gather_ps(); //expect: GolangIntrinsicIssue
    _mm256_insertf128_ps(); //expect: GolangIntrinsicIssue
    _mm256_load_ps(); //expect: GolangIntrinsicIssue
    _mm256_loadu_ps(); //expect: GolangIntrinsicIssue
    _mm256_macc_ps(); //expect: GolangIntrinsicIssue
    _mm256_maddsub_ps(); //expect: GolangIntrinsicIssue
    _mm256_mask_i32gather_ps(); //expect: GolangIntrinsicIssue
    _mm256_maskload_ps(); //expect: GolangIntrinsicIssue
    _mm256_max_ps(); //expect: GolangIntrinsicIssue
    _mm256_min_ps(); //expect: GolangIntrinsicIssue
    _mm256_movehdup_ps(); //expect: GolangIntrinsicIssue
    _mm256_moveldup_ps(); //expect: GolangIntrinsicIssue
    _mm256_msubadd_ps(); //expect: GolangIntrinsicIssue
    _mm256_msub_ps(); //expect: GolangIntrinsicIssue
    _mm256_mul_ps(); //expect: GolangIntrinsicIssue
    _mm256_nmacc_ps(); //expect: GolangIntrinsicIssue
    _mm256_nmsub_ps(); //expect: GolangIntrinsicIssue
    _mm256_or_ps(); //expect: GolangIntrinsicIssue
    _mm256_permute2f128_ps(); //expect: GolangIntrinsicIssue
    _mm256_permute2_ps(); //expect: GolangIntrinsicIssue
    _mm256_permute_ps(); //expect: GolangIntrinsicIssue
    _mm256_permutevar8x32_ps(); //expect: GolangIntrinsicIssue
    _mm256_permutevar_ps(); //expect: GolangIntrinsicIssue
    _mm256_rcp_ps(); //expect: GolangIntrinsicIssue
    _mm256_round_ps(); //expect: GolangIntrinsicIssue
    _mm256_rsqrt_ps(); //expect: GolangIntrinsicIssue
    _mm256_set1_ps(); //expect: GolangIntrinsicIssue
    _mm256_set_ps(); //expect: GolangIntrinsicIssue
    _mm256_setr_ps(); //expect: GolangIntrinsicIssue
    _mm256_setzero_ps(); //expect: GolangIntrinsicIssue
    _mm256_shuffle_ps(); //expect: GolangIntrinsicIssue
    _mm256_sqrt_ps(); //expect: GolangIntrinsicIssue
    _mm256_sub_ps(); //expect: GolangIntrinsicIssue
    _mm256_unpackhi_ps(); //expect: GolangIntrinsicIssue
    _mm256_unpacklo_ps(); //expect: GolangIntrinsicIssue
    _mm256_xor_ps(); //expect: GolangIntrinsicIssue
    _mm_macc_ps(); //expect: GolangIntrinsicIssue
    _mm_maddsub_ps(); //expect: GolangIntrinsicIssue
    _mm_msubadd_ps(); //expect: GolangIntrinsicIssue
    _mm_msub_ps(); //expect: GolangIntrinsicIssue
    _mm_nmacc_ps(); //expect: GolangIntrinsicIssue
    _mm_nmsub_ps(); //expect: GolangIntrinsicIssue
    _m_from_float(); //expect: GolangIntrinsicIssue
    _m_from_int(); //expect: GolangIntrinsicIssue
    _mm_abs_pi16(); //expect: GolangIntrinsicIssue
    _mm_abs_pi32(); //expect: GolangIntrinsicIssue
    _mm_abs_pi8(); //expect: GolangIntrinsicIssue
    _mm_add_si64(); //expect: GolangIntrinsicIssue
    _mm_alignr_pi8(); //expect: GolangIntrinsicIssue
    _mm_cvtpd_pi32(); //expect: GolangIntrinsicIssue
    _mm_cvt_ps2pi(); //expect: GolangIntrinsicIssue
    _mm_cvttpd_pi32(); //expect: GolangIntrinsicIssue
    _mm_cvtt_ps2pi(); //expect: GolangIntrinsicIssue
    _mm_hadd_pi16(); //expect: GolangIntrinsicIssue
    _mm_hadd_pi32(); //expect: GolangIntrinsicIssue
    _mm_hadds_pi16(); //expect: GolangIntrinsicIssue
    _mm_hsub_pi16(); //expect: GolangIntrinsicIssue
    _mm_hsub_pi32(); //expect: GolangIntrinsicIssue
    _mm_hsubs_pi16(); //expect: GolangIntrinsicIssue
    _mm_maddubs_pi16(); //expect: GolangIntrinsicIssue
    _mm_movepi64_pi64(); //expect: GolangIntrinsicIssue
    _mm_mulhrs_pi16(); //expect: GolangIntrinsicIssue
    _mm_mul_su32(); //expect: GolangIntrinsicIssue
    _mm_set1_pi16(); //expect: GolangIntrinsicIssue
    _mm_set1_pi32(); //expect: GolangIntrinsicIssue
    _mm_set1_pi8(); //expect: GolangIntrinsicIssue
    _mm_set_pi16(); //expect: GolangIntrinsicIssue
    _mm_set_pi32(); //expect: GolangIntrinsicIssue
    _mm_set_pi8(); //expect: GolangIntrinsicIssue
    _mm_setr_pi16(); //expect: GolangIntrinsicIssue
    _mm_setr_pi32(); //expect: GolangIntrinsicIssue
    _mm_setr_pi8(); //expect: GolangIntrinsicIssue
    _mm_setzero_si64(); //expect: GolangIntrinsicIssue
    _mm_shuffle_pi8(); //expect: GolangIntrinsicIssue
    _mm_sign_pi16(); //expect: GolangIntrinsicIssue
    _mm_sign_pi32(); //expect: GolangIntrinsicIssue
    _mm_sign_pi8(); //expect: GolangIntrinsicIssue
    _mm_sub_si64(); //expect: GolangIntrinsicIssue
    _m_packssdw(); //expect: GolangIntrinsicIssue
    _m_packsswb(); //expect: GolangIntrinsicIssue
    _m_packuswb(); //expect: GolangIntrinsicIssue
    _m_paddb(); //expect: GolangIntrinsicIssue
    _m_paddd(); //expect: GolangIntrinsicIssue
    _m_paddsb(); //expect: GolangIntrinsicIssue
    _m_paddsw(); //expect: GolangIntrinsicIssue
    _m_paddusb(); //expect: GolangIntrinsicIssue
    _m_paddusw(); //expect: GolangIntrinsicIssue
    _m_paddw(); //expect: GolangIntrinsicIssue
    _m_pand(); //expect: GolangIntrinsicIssue
    _m_pandn(); //expect: GolangIntrinsicIssue
    _m_pavgb(); //expect: GolangIntrinsicIssue
    _m_pavgusb(); //expect: GolangIntrinsicIssue
    _m_pavgw(); //expect: GolangIntrinsicIssue
    _m_pcmpeqb(); //expect: GolangIntrinsicIssue
    _m_pcmpeqd(); //expect: GolangIntrinsicIssue
    _m_pcmpeqw(); //expect: GolangIntrinsicIssue
    _m_pcmpgtb(); //expect: GolangIntrinsicIssue
    _m_pcmpgtd(); //expect: GolangIntrinsicIssue
    _m_pcmpgtw(); //expect: GolangIntrinsicIssue
    _m_pf2id(); //expect: GolangIntrinsicIssue
    _m_pf2iw(); //expect: GolangIntrinsicIssue
    _m_pfacc(); //expect: GolangIntrinsicIssue
    _m_pfadd(); //expect: GolangIntrinsicIssue
    _m_pfcmpeq(); //expect: GolangIntrinsicIssue
    _m_pfcmpge(); //expect: GolangIntrinsicIssue
    _m_pfcmpgt(); //expect: GolangIntrinsicIssue
    _m_pfmax(); //expect: GolangIntrinsicIssue
    _m_pfmin(); //expect: GolangIntrinsicIssue
    _m_pfmul(); //expect: GolangIntrinsicIssue
    _m_pfnacc(); //expect: GolangIntrinsicIssue
    _m_pfpnacc(); //expect: GolangIntrinsicIssue
    _m_pfrcpit1(); //expect: GolangIntrinsicIssue
    _m_pfrcpit2(); //expect: GolangIntrinsicIssue
    _m_pfrcp(); //expect: GolangIntrinsicIssue
    _m_pfrsqit1(); //expect: GolangIntrinsicIssue
    _m_pfrsqrt(); //expect: GolangIntrinsicIssue
    _m_pfsub(); //expect: GolangIntrinsicIssue
    _m_pfsubr(); //expect: GolangIntrinsicIssue
    _m_pi2fd(); //expect: GolangIntrinsicIssue
    _m_pi2fw(); //expect: GolangIntrinsicIssue
    _m_pinsrw(); //expect: GolangIntrinsicIssue
    _m_pmaddwd(); //expect: GolangIntrinsicIssue
    _m_pmaxsw(); //expect: GolangIntrinsicIssue
    _m_pmaxub(); //expect: GolangIntrinsicIssue
    _m_pminsw(); //expect: GolangIntrinsicIssue
    _m_pminub(); //expect: GolangIntrinsicIssue
    _m_pmulhrw(); //expect: GolangIntrinsicIssue
    _m_pmulhuw(); //expect: GolangIntrinsicIssue
    _m_pmulhw(); //expect: GolangIntrinsicIssue
    _m_pmullw(); //expect: GolangIntrinsicIssue
    _m_por(); //expect: GolangIntrinsicIssue
    _m_psadbw(); //expect: GolangIntrinsicIssue
    _m_pshufw(); //expect: GolangIntrinsicIssue
    _m_pslldi(); //expect: GolangIntrinsicIssue
    _m_pslld(); //expect: GolangIntrinsicIssue
    _m_psllqi(); //expect: GolangIntrinsicIssue
    _m_psllq(); //expect: GolangIntrinsicIssue
    _m_psllwi(); //expect: GolangIntrinsicIssue
    _m_psllw(); //expect: GolangIntrinsicIssue
    _m_psradi(); //expect: GolangIntrinsicIssue
    _m_psrad(); //expect: GolangIntrinsicIssue
    _m_psrawi(); //expect: GolangIntrinsicIssue
    _m_psraw(); //expect: GolangIntrinsicIssue
    _m_psrldi(); //expect: GolangIntrinsicIssue
    _m_psrld(); //expect: GolangIntrinsicIssue
    _m_psrlqi(); //expect: GolangIntrinsicIssue
    _m_psrlq(); //expect: GolangIntrinsicIssue
    _m_psrlwi(); //expect: GolangIntrinsicIssue
    _m_psrlw(); //expect: GolangIntrinsicIssue
    _m_psubb(); //expect: GolangIntrinsicIssue
    _m_psubd(); //expect: GolangIntrinsicIssue
    _m_psubsb(); //expect: GolangIntrinsicIssue
    _m_psubsw(); //expect: GolangIntrinsicIssue
    _m_psubusb(); //expect: GolangIntrinsicIssue
    _m_psubusw(); //expect: GolangIntrinsicIssue
    _m_psubw(); //expect: GolangIntrinsicIssue
    _m_pswapd(); //expect: GolangIntrinsicIssue
    _m_punpckhbw(); //expect: GolangIntrinsicIssue
    _m_punpckhdq(); //expect: GolangIntrinsicIssue
    _m_punpckhwd(); //expect: GolangIntrinsicIssue
    _m_punpcklbw(); //expect: GolangIntrinsicIssue
    _m_punpckldq(); //expect: GolangIntrinsicIssue
    _m_punpcklwd(); //expect: GolangIntrinsicIssue
    _m_pxor(); //expect: GolangIntrinsicIssue
    _InterlockedAnd16_np(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange16_np(); //expect: GolangIntrinsicIssue
    _InterlockedOr16_np(); //expect: GolangIntrinsicIssue
    _InterlockedXor16_np(); //expect: GolangIntrinsicIssue
    _loadbe_i16(); //expect: GolangIntrinsicIssue
    _addcarry_u16(); //expect: GolangIntrinsicIssue
    _addcarry_u32(); //expect: GolangIntrinsicIssue
    _addcarry_u64(); //expect: GolangIntrinsicIssue
    _addcarry_u8(); //expect: GolangIntrinsicIssue
    _addcarryx_u32(); //expect: GolangIntrinsicIssue
    _addcarryx_u64(); //expect: GolangIntrinsicIssue
    _bittestandcomplement64(); //expect: GolangIntrinsicIssue
    _bittestandreset64(); //expect: GolangIntrinsicIssue
    _bittestandset64(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lwpins16(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lwpins32(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lwpins64(); //expect: GolangIntrinsicIssue
    __inbyte(); //expect: GolangIntrinsicIssue
    _interlockedbittestandreset64_HLEAcquire(); //expect: GolangIntrinsicIssue
    _interlockedbittestandreset64_HLERelease(); //expect: GolangIntrinsicIssue
    _interlockedbittestandreset64(); //expect: GolangIntrinsicIssue
    _interlockedbittestandreset_HLEAcquire(); //expect: GolangIntrinsicIssue
    _interlockedbittestandreset_HLERelease(); //expect: GolangIntrinsicIssue
    _interlockedbittestandset64_HLEAcquire(); //expect: GolangIntrinsicIssue
    _interlockedbittestandset64_HLERelease(); //expect: GolangIntrinsicIssue
    _interlockedbittestandset64(); //expect: GolangIntrinsicIssue
    _interlockedbittestandset_HLEAcquire(); //expect: GolangIntrinsicIssue
    _interlockedbittestandset_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchange128(); //expect: GolangIntrinsicIssue
    __lwpins32(); //expect: GolangIntrinsicIssue
    __lwpins64(); //expect: GolangIntrinsicIssue
    __readfsbyte(); //expect: GolangIntrinsicIssue
    __readgsbyte(); //expect: GolangIntrinsicIssue
    _subborrow_u16(); //expect: GolangIntrinsicIssue
    _subborrow_u32(); //expect: GolangIntrinsicIssue
    _subborrow_u64(); //expect: GolangIntrinsicIssue
    _subborrow_u8(); //expect: GolangIntrinsicIssue
    __vmx_on(); //expect: GolangIntrinsicIssue
    __vmx_vmclear(); //expect: GolangIntrinsicIssue
    __vmx_vmlaunch(); //expect: GolangIntrinsicIssue
    __vmx_vmptrld(); //expect: GolangIntrinsicIssue
    __vmx_vmread(); //expect: GolangIntrinsicIssue
    __vmx_vmresume(); //expect: GolangIntrinsicIssue
    __vmx_vmwrite(); //expect: GolangIntrinsicIssue
    _andn_u64(); //expect: GolangIntrinsicIssue
    _bextri_u64(); //expect: GolangIntrinsicIssue
    _bextr_u64(); //expect: GolangIntrinsicIssue
    _blcfill_u64(); //expect: GolangIntrinsicIssue
    _blcic_u64(); //expect: GolangIntrinsicIssue
    _blci_u64(); //expect: GolangIntrinsicIssue
    _blcmsk_u64(); //expect: GolangIntrinsicIssue
    _blcs_u64(); //expect: GolangIntrinsicIssue
    _blsfill_u64(); //expect: GolangIntrinsicIssue
    _blsic_u64(); //expect: GolangIntrinsicIssue
    _blsi_u64(); //expect: GolangIntrinsicIssue
    _blsmsk_u64(); //expect: GolangIntrinsicIssue
    _blsr_u64(); //expect: GolangIntrinsicIssue
    _bzhi_u64(); //expect: GolangIntrinsicIssue
    _load_be_u64(); //expect: GolangIntrinsicIssue
    __lzcnt64(); //expect: GolangIntrinsicIssue
    _lzcnt_u64(); //expect: GolangIntrinsicIssue
    _mm_crc32_u64(); //expect: GolangIntrinsicIssue
    _mulx_u64(); //expect: GolangIntrinsicIssue
    __emulu(); //expect: GolangIntrinsicIssue
    __ll_lshift(); //expect: GolangIntrinsicIssue
    __ull_rshift(); //expect: GolangIntrinsicIssue
    _pdep_u64(); //expect: GolangIntrinsicIssue
    _pext_u64(); //expect: GolangIntrinsicIssue
    __popcnt64(); //expect: GolangIntrinsicIssue
    __rdtscp(); //expect: GolangIntrinsicIssue
    __rdtsc(); //expect: GolangIntrinsicIssue
    __readcr0(); //expect: GolangIntrinsicIssue
    __readcr2(); //expect: GolangIntrinsicIssue
    __readcr3(); //expect: GolangIntrinsicIssue
    __readcr4(); //expect: GolangIntrinsicIssue
    __readcr8(); //expect: GolangIntrinsicIssue
    __readdr(); //expect: GolangIntrinsicIssue
    __readeflags(); //expect: GolangIntrinsicIssue
    _readfsbase_u64(); //expect: GolangIntrinsicIssue
    _readgsbase_u64(); //expect: GolangIntrinsicIssue
    __readgsqword(); //expect: GolangIntrinsicIssue
    __readmsr(); //expect: GolangIntrinsicIssue
    __readpmc(); //expect: GolangIntrinsicIssue
    _rorx_u64(); //expect: GolangIntrinsicIssue
    __shiftleft128(); //expect: GolangIntrinsicIssue
    __shiftright128(); //expect: GolangIntrinsicIssue
    _shlx_u64(); //expect: GolangIntrinsicIssue
    _shrx_u64(); //expect: GolangIntrinsicIssue
    _t1mskc_u64(); //expect: GolangIntrinsicIssue
    _tzcnt_u64(); //expect: GolangIntrinsicIssue
    _tzmsk_u64(); //expect: GolangIntrinsicIssue
    _udiv128(); //expect: GolangIntrinsicIssue
    _umul128(); //expect: GolangIntrinsicIssue
    __umulh(); //expect: GolangIntrinsicIssue
    _xgetbv(); //expect: GolangIntrinsicIssue
    _andn_u32(); //expect: GolangIntrinsicIssue
    _bextri_u32(); //expect: GolangIntrinsicIssue
    _bextr_u32(); //expect: GolangIntrinsicIssue
    _blcfill_u32(); //expect: GolangIntrinsicIssue
    _blcic_u32(); //expect: GolangIntrinsicIssue
    _blci_u32(); //expect: GolangIntrinsicIssue
    _blcmsk_u32(); //expect: GolangIntrinsicIssue
    _blcs_u32(); //expect: GolangIntrinsicIssue
    _blsfill_u32(); //expect: GolangIntrinsicIssue
    _blsic_u32(); //expect: GolangIntrinsicIssue
    _blsi_u32(); //expect: GolangIntrinsicIssue
    _blsmsk_u32(); //expect: GolangIntrinsicIssue
    _blsr_u32(); //expect: GolangIntrinsicIssue
    __builtin_ia32_bextri_u32(); //expect: GolangIntrinsicIssue
    __builtin_ia32_bextr_u32(); //expect: GolangIntrinsicIssue
    __builtin_ia32_crc32hi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_crc32qi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_crc32si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lzcnt_u32(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rdfsbase32(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rdgsbase32(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rdrand16_step(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rdrand32_step(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rdrand64_step(); //expect: GolangIntrinsicIssue
    _bzhi_u32(); //expect: GolangIntrinsicIssue
    __getcallerseflags(); //expect: GolangIntrinsicIssue
    _load_be_u32(); //expect: GolangIntrinsicIssue
    _lzcnt_u32(); //expect: GolangIntrinsicIssue
    __lzcnt(); //expect: GolangIntrinsicIssue
    _mm_crc32_u16(); //expect: GolangIntrinsicIssue
    _mm_crc32_u32(); //expect: GolangIntrinsicIssue
    _mm_crc32_u8(); //expect: GolangIntrinsicIssue
    _mm_getcsr(); //expect: GolangIntrinsicIssue
    _mulx_u32(); //expect: GolangIntrinsicIssue
    _pdep_u32(); //expect: GolangIntrinsicIssue
    _pext_u32(); //expect: GolangIntrinsicIssue
    __popcnt(); //expect: GolangIntrinsicIssue
    _readfsbase_u32(); //expect: GolangIntrinsicIssue
    _readgsbase_u32(); //expect: GolangIntrinsicIssue
    _rorx_u32(); //expect: GolangIntrinsicIssue
    _shlx_u32(); //expect: GolangIntrinsicIssue
    _shrx_u32(); //expect: GolangIntrinsicIssue
    _t1mskc_u32(); //expect: GolangIntrinsicIssue
    _tzcnt_u32(); //expect: GolangIntrinsicIssue
    _tzmsk_u32(); //expect: GolangIntrinsicIssue
    _udiv64(); //expect: GolangIntrinsicIssue
    __indword(); //expect: GolangIntrinsicIssue
    __builtin_ia32_bextri_u64(); //expect: GolangIntrinsicIssue
    __builtin_ia32_bextr_u64(); //expect: GolangIntrinsicIssue
    __builtin_ia32_crc32di(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lzcnt_u64(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rdfsbase64(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rdgsbase64(); //expect: GolangIntrinsicIssue
    _bzhi_u64(); //expect: GolangIntrinsicIssue
    _pdep_u64(); //expect: GolangIntrinsicIssue
    _pext_u64(); //expect: GolangIntrinsicIssue
    __readcr0(); //expect: GolangIntrinsicIssue
    __readcr2(); //expect: GolangIntrinsicIssue
    __readcr3(); //expect: GolangIntrinsicIssue
    __readcr4(); //expect: GolangIntrinsicIssue
    __readcr8(); //expect: GolangIntrinsicIssue
    __readfsdword(); //expect: GolangIntrinsicIssue
    __readgsdword(); //expect: GolangIntrinsicIssue
    __segmentlimit(); //expect: GolangIntrinsicIssue
    __readdr(); //expect: GolangIntrinsicIssue
    __readeflags(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lzcnt_16(); //expect: GolangIntrinsicIssue
    __inword(); //expect: GolangIntrinsicIssue
    _load_be_u16(); //expect: GolangIntrinsicIssue
    __lzcnt16(); //expect: GolangIntrinsicIssue
    __popcnt16(); //expect: GolangIntrinsicIssue
    __readfsword(); //expect: GolangIntrinsicIssue
    __readgsword(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pabsw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_packssdw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_packusdw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddsw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddusw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pavgw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pblendw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pbroadcastw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpeqw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpgtw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phaddsw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phaddw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phsubsw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phsubw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaddwd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxsw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxuw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminsw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminuw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxbw256 (); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxbw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulhrsw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulhuw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulhw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmullw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psadbw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pshufhw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pshuflw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psignw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllwi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psraw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrawi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlwi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubsw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubusw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckhwd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpcklwd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v16hi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lddqu(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loaddqu(); //expect: GolangIntrinsicIssue
    __builtin_ia32_mpsadbw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pabsb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_packsswb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_packuswb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pavgb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pblendvb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pbroadcastb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpeqb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpestrm128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpgtb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpistrm128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxsb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxub128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminsb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminub128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pshufb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psignb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubb128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckhbw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpcklbw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vec_set_v16qi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v16qi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomeqb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomequb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomfalseb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomfalseub(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgeb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgeub(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgtb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgtub(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomleb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomleub(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomltb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomltub(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomneb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomneub(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomtrueb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomtrueub(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpperm(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vprotb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpshab(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpshlb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_palignr(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmuludq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psadbw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllqi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlqi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_addpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_addsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_addsubpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_andnpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_andpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_blendpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_blendvpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpeqpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpeqsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpgepd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpgtpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmplepd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmplesd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpltpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpltsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpneqpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpneqsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpngepd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpngtpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpnlepd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpnlesd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpnltpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpnltsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpordpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpordsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmppd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpunordpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpunordsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtdq2pd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtpi2pd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtps2pd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtsi2sd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtsi642sd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtss2sd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_divpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_divsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_dppd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmaddpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmaddsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmaddsubpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmsubaddpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmsubpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmsubsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmaddpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmaddsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmsubpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmsubsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gatherdiv2df(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gathersiv2df(); //expect: GolangIntrinsicIssue
    __builtin_ia32_haddpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_hsubpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loadddup(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loadhpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loadlpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loadupd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskloadpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maxpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maxsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_minpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_minsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movddup(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_mulpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_mulsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_orpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pd_pd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_roundpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_roundsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_shufpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_sqrtpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_sqrtsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_subpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_subsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_unpckhpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_unpcklpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vextractf128_pd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vfrczpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vfrczsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v2df(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermil2pd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermilpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermilvarpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_xorpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_aesdec128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_aesdeclast128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_aesenc128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_aesenclast128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_aesimc128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_aeskeygenassist128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_extrqi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_extrq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gatherdiv2di(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gathersiv2di(); //expect: GolangIntrinsicIssue
    __builtin_ia32_insertqi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_insertq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskloadq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movntdqa(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_palignr128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pand128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pandn128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pbroadcastq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pclmulqdq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpeqq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpgtq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxbq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxdq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxwq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxbq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxdq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxwq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmuldq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmuludq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_por128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psadbw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pslldqi128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllqi128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllv2di(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrldqi128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlqi128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlv2di(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckhqdq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpcklqdq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pxor128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vec_set_v2di(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v2di(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomeqq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomequq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomfalseq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomfalseuq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgeq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgeuq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgtq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgtuq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomleq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomleuq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomltq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomltuq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomneq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomneuq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomtrueq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomtrueuq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphaddbq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphadddq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphaddubq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphaddudq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphadduwq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphaddwq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphsubdq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmacsdqh(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmacsdql(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmacssdqh(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmacssdql(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vprotq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpshaq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpshlq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfacc(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfadd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfmax(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfmin(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfmul(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfnacc(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfpnacc(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfrcpit1(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfrcpit2(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfrcp(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfrsqrtit1 (); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfrsqrt(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfsubr(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfsub(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pi2fd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pi2fw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pswapdsf(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtpd2pi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtps2pi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvttpd2pi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvttps2pi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pabsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpeqd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpgtd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pf2id(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pf2iw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfcmpeq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfcmpge(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pfcmpgt(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phaddd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phsubd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psignd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pslldi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pslld(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psradi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrad(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrldi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrld(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pswapdsi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckhdq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckldq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lddqu256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loaddqu256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_mpsadbw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pabsb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_packsswb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_packuswb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddsb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddusb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pavgb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pblendvb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pbroadcastb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpeqb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpgtb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaddubsw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxsb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxub256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminsb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminub256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pshufb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psignb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubsb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubusb256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckhbw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpcklbw256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v32qi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_addpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_addsubpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_andnpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_andpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_blendpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_blendvpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmppd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtdq2pd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtps2pd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_divpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmaddpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmaddsubpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmsubaddpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmsubpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmaddpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmsubpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gatherdiv4df(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gathersiv4df(); //expect: GolangIntrinsicIssue
    __builtin_ia32_haddpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_hsubpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loadupd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskloadpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maxpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_minpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movddup256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_mulpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_orpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pd256_pd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_permdf256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_roundpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_shufpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_sqrtpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_subpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_unpckhpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_unpcklpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vbroadcastf128_pd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vbroadcastsd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vbroadcastsd_pd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vfrczpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vinsertf128_pd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v4df256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vperm2f128_pd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermil2pd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermilpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermilvarpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_xorpd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_andnotsi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_andsi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_extract128i256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gatherdiv4di(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gathersiv4di(); //expect: GolangIntrinsicIssue
    __builtin_ia32_insert128i256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskloadq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movntdqa256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_palignr256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pbroadcastq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpeqq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpgtq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_permdi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_permti256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxbq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxdq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxwq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxbq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxdq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxwq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmuldq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmuludq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_por256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pslldqi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllqi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllv4di(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrldqi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlqi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlv4di(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckhqdq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpcklqdq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pxor256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vbroadcastsi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v4di256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pabsw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_packssdw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddsw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddusw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pavgw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpeqw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpgtw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phaddsw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phaddw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phsubsw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phsubw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pinsrw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaddubsw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxsw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminsw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulhrsw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulhrw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulhuw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulhw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmullw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psignw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllwi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrawi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psraw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlwi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubsw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubusw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckhwd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpcklwd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_addps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_addss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_addsubps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_andnps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_andps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_blendps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_blendvps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtdq2ps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtpd2ps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtpd2ps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtpi2ps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtsd2ss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtsi2ss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_divps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_divss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_dpps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmaddps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmaddss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmaddsubps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmsubaddps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmsubps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmsubss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmaddps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmaddss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmsubps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmsubss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gatherdiv4sf256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gatherdiv4sf(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gathersiv4sf(); //expect: GolangIntrinsicIssue
    __builtin_ia32_haddps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_hsubps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_insertps128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loadaps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loadhps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loadlps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loadsss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loadups(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskloadps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maxps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maxss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_minps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_minss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movhlps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movlhps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movshdup(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movsldup(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_mulps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_mulss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_orps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ps_ps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rcpps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rcpss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_roundps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_roundss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rsqrtps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rsqrtss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_shufps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_sqrtps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_sqrtss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_subps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_subss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_unpckhps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_unpcklps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vbroadcastss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vbroadcastss_ps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vec_set_v4sf(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vextractf128_ps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vfrczps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vfrczss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v4sf(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermil2ps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermilps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermilvarps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_xorps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpeqps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpeqss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpgeps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpgtps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpleps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpless(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpltps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpltss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpneqps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpneqss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpngeps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpngtps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpnleps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpnless(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpnltps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpnlts(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpordps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpordss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpunordps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpunordss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtpd2dq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtpd2dq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtps2dq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvttpd2dq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvttpd2dq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvttps2dq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gatherdiv4si256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gatherdiv4si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gathersiv4si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskloadd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pabsd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pblendd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pbroadcastd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpeqd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpgtd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phaddd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phsubd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaddwd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxsd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxud128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminsd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminud128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxbd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxwd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxbd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxwd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulld128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pshufd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psignd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pslld128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pslldi128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllv4si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrad128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psradi128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrav4si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrld128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrldi128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlv4si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckhdq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckldq128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_si_si256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vec_set_v4si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vextractf128_si256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v4si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomeqd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomequd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomfalsed(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomfalseud(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomged(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgeud(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgtd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgtud(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomled(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomleud(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomltd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomltud(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomned(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomneud(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomtrued(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomtrueud(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphaddbd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphaddubd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphadduwd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphaddwd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphsubwd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmacsdd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmacssdd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmacsswd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmacswd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmadcsswd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmadcswd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vprotd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpshad(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpshld(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pabsw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_packssdw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_packusdw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pavgw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pblendw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pbroadcastw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpeqw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpgtw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phaddsw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phaddw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phminposuw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phsubsw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phsubw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaddubsw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxsw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxuw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminsw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminuw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxbw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxbw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulhrsw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulhuw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulhw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmullw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pshufhw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pshuflw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psignw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllwi128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psraw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrawi128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlwi128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubw128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckhwd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpcklwd128(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v8hi(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomequw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomeqw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomfalseuw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomfalsew(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgeuw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgew(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgtuw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomgtw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomleuw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomlew(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomltuw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomltw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomneuw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomnew(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomtrueuw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcomtruew(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphaddbw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphaddubw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vphsubbw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmacssww(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpmacsww(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vprotw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpshaw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpshlw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pabsb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_packsswb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_packuswb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddsb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddusb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pavgb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pavgusb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpeqb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpgtb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxub(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminub(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pshufb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psignb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubsb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubusb(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckhbw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpcklbw(); //expect: GolangIntrinsicIssue
    __builtin_ia32_addps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_addsubps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_andnps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_andps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_blendps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_blendvps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cmpps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtdq2ps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_divps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_dpps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmaddps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmaddsubps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmsubaddps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fmsubps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmaddps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_fnmsubps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gathersiv8sf(); //expect: GolangIntrinsicIssue
    __builtin_ia32_haddps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_hsubps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_loadups256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskloadps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maxps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_minps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movshdup256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movsldup256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_mulps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_orps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_permvarsf256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_ps256_ps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rcpps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_roundps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rsqrtps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_rsqrtps_nr256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_shufps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_sqrtps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_sqrtps_nr256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_subps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_unpckhps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_unpcklps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vbroadcastf128_ps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vbroadcastss256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vbroadcastss_ps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vfrczps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vinsertf128_ps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v8sf256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vperm2f128_ps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermil2ps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermilps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpermilvarps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_xorps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvtps2dq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_cvttps2dq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_gathersiv8si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskloadd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pabsd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_paddd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pblendd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pbroadcastd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpeqd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pcmpgtd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_permvarsi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phaddd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_phsubd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxsd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmaxud256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminsd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pminud256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxbd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovsxwd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxbd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmovzxwd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pmulld256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pshufd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psignd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pslld256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pslldi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psllv8si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrad256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psradi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrav8si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrld256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrldi256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psrlv8si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_psubd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckhdq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_punpckldq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_si256_si(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vinsertf128_si256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vpcmov_v8si256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vperm2f128_si256(); //expect: GolangIntrinsicIssue
    __addfsbyte(); //expect: GolangIntrinsicIssue
    __addfsdword(); //expect: GolangIntrinsicIssue
    __addfsword(); //expect: GolangIntrinsicIssue
    __addgsbyte(); //expect: GolangIntrinsicIssue
    __addgsdword(); //expect: GolangIntrinsicIssue
    __addgsqword(); //expect: GolangIntrinsicIssue
    __addgsword(); //expect: GolangIntrinsicIssue
    __builtin_cpu_init(); //expect: GolangIntrinsicIssue
    __builtin_ia32_clflush(); //expect: GolangIntrinsicIssue
    __builtin_ia32_femms(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lfence(); //expect: GolangIntrinsicIssue
    __builtin_ia32_llwpcb16(); //expect: GolangIntrinsicIssue
    __builtin_ia32_llwpcb16(); //expect: GolangIntrinsicIssue
    __builtin_ia32_llwpcb32(); //expect: GolangIntrinsicIssue
    __builtin_ia32_llwpcb32(); //expect: GolangIntrinsicIssue
    __builtin_ia32_llwpcb64(); //expect: GolangIntrinsicIssue
    __builtin_ia32_llwpcb64(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lwpval16(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lwpval32(); //expect: GolangIntrinsicIssue
    __builtin_ia32_lwpval64(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskmovdqu(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskmovq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskstored256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskstored(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskstorepd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskstorepd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskstoreps256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskstoreps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskstoreq256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_maskstoreq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_mfence(); //expect: GolangIntrinsicIssue
    __builtin_ia32_monitor(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movntdq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movnti64(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movnti(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movntpd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movntps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movntq(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movntsd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_movntss(); //expect: GolangIntrinsicIssue
    __builtin_ia32_mwait(); //expect: GolangIntrinsicIssue
    __builtin_ia32_pause(); //expect: GolangIntrinsicIssue
    __builtin_ia32_sfence(); //expect: GolangIntrinsicIssue
    __builtin_ia32_storeaps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_storedqu256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_storedqu(); //expect: GolangIntrinsicIssue
    __builtin_ia32_storehps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_storelps(); //expect: GolangIntrinsicIssue
    __builtin_ia32_storess(); //expect: GolangIntrinsicIssue
    __builtin_ia32_storeupd256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_storeupd(); //expect: GolangIntrinsicIssue
    __builtin_ia32_storeups256(); //expect: GolangIntrinsicIssue
    __builtin_ia32_storeups(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vzeroall(); //expect: GolangIntrinsicIssue
    __builtin_ia32_vzeroupper(); //expect: GolangIntrinsicIssue
    __builtin_ia32_xabort(); //expect: GolangIntrinsicIssue
    __builtin_ia32_xend(); //expect: GolangIntrinsicIssue
    _clac(); //expect: GolangIntrinsicIssue
    __cpuidex(); //expect: GolangIntrinsicIssue
    __cpuid(); //expect: GolangIntrinsicIssue
    __faststorefence(); //expect: GolangIntrinsicIssue
    _fxrstor64(); //expect: GolangIntrinsicIssue
    _fxrstor(); //expect: GolangIntrinsicIssue
    _fxsave64(); //expect: GolangIntrinsicIssue
    _fxsave(); //expect: GolangIntrinsicIssue
    __halt(); //expect: GolangIntrinsicIssue
    __inbytestring(); //expect: GolangIntrinsicIssue
    __incfsbyte(); //expect: GolangIntrinsicIssue
    __incfsdword(); //expect: GolangIntrinsicIssue
    __incfsword(); //expect: GolangIntrinsicIssue
    __incgsbyte(); //expect: GolangIntrinsicIssue
    __incgsdword(); //expect: GolangIntrinsicIssue
    __incgsqword(); //expect: GolangIntrinsicIssue
    __incgsword(); //expect: GolangIntrinsicIssue
    __indwordstring(); //expect: GolangIntrinsicIssue
    __int2c(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchangePointer_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchangePointer_HLERelease(); //expect: GolangIntrinsicIssue
    _InterlockedCompareExchangePointer_np(); //expect: GolangIntrinsicIssue
    _InterlockedExchangePointer_HLEAcquire(); //expect: GolangIntrinsicIssue
    _InterlockedExchangePointer_HLERelease(); //expect: GolangIntrinsicIssue
    __invlpg(); //expect: GolangIntrinsicIssue
    _invpcid(); //expect: GolangIntrinsicIssue
    __inwordstring(); //expect: GolangIntrinsicIssue
    _lgdt(); //expect: GolangIntrinsicIssue
    __lidt(); //expect: GolangIntrinsicIssue
    __llwpcb(); //expect: GolangIntrinsicIssue
    __lwpval32(); //expect: GolangIntrinsicIssue
    __lwpval64(); //expect: GolangIntrinsicIssue
    _m_empty(); //expect: GolangIntrinsicIssue
    _m_femms(); //expect: GolangIntrinsicIssue
    _mm256_maskstore_epi32(); //expect: GolangIntrinsicIssue
    _mm256_maskstore_epi64(); //expect: GolangIntrinsicIssue
    _mm256_maskstore_pd(); //expect: GolangIntrinsicIssue
    _mm256_maskstore_ps(); //expect: GolangIntrinsicIssue
    _mm256_store_pd(); //expect: GolangIntrinsicIssue
    _mm256_store_ps(); //expect: GolangIntrinsicIssue
    _mm256_store_si256(); //expect: GolangIntrinsicIssue
    _mm256_storeu_pd(); //expect: GolangIntrinsicIssue
    _mm256_storeu_ps(); //expect: GolangIntrinsicIssue
    _mm256_storeu_si256(); //expect: GolangIntrinsicIssue
    __mm256_stream_pd(); //expect: GolangIntrinsicIssue
    _mm256_stream_ps(); //expect: GolangIntrinsicIssue
    __mm256_stream_si256(); //expect: GolangIntrinsicIssue
    _mm256_zeroall(); //expect: GolangIntrinsicIssue
    _mm256_zeroupper(); //expect: GolangIntrinsicIssue
    _m_maskmovq(); //expect: GolangIntrinsicIssue
    _mm_clflush(); //expect: GolangIntrinsicIssue
    _mm_lfence(); //expect: GolangIntrinsicIssue
    _mm_maskmoveu_si128(); //expect: GolangIntrinsicIssue
    _mm_maskstore_epi32(); //expect: GolangIntrinsicIssue
    _mm_maskstore_epi64(); //expect: GolangIntrinsicIssue
    _mm_maskstore_pd(); //expect: GolangIntrinsicIssue
    _mm_maskstore_ps(); //expect: GolangIntrinsicIssue
    _mm_mfence(); //expect: GolangIntrinsicIssue
    _mm_monitor(); //expect: GolangIntrinsicIssue
    _mm_mwait(); //expect: GolangIntrinsicIssue
    _mm_pause(); //expect: GolangIntrinsicIssue
    _mm_prefetch(); //expect: GolangIntrinsicIssue
    _mm_setcsr(); //expect: GolangIntrinsicIssue
    _mm_sfence(); //expect: GolangIntrinsicIssue
    _mm_store1_pd(); //expect: GolangIntrinsicIssue
    _mm_storeh_pd(); //expect: GolangIntrinsicIssue
    _mm_storeh_pi(); //expect: GolangIntrinsicIssue
    _mm_storel_epi64(); //expect: GolangIntrinsicIssue
    _mm_storel_pd(); //expect: GolangIntrinsicIssue
    _mm_storel_pi(); //expect: GolangIntrinsicIssue
    _mm_store_pd(); //expect: GolangIntrinsicIssue
    _mm_store_ps1(); //expect: GolangIntrinsicIssue
    _mm_store_ps(); //expect: GolangIntrinsicIssue
    _mm_storer_pd(); //expect: GolangIntrinsicIssue
    _mm_storer_ps(); //expect: GolangIntrinsicIssue
    _mm_store_sd(); //expect: GolangIntrinsicIssue
    _mm_store_si128(); //expect: GolangIntrinsicIssue
    _mm_store_ss(); //expect: GolangIntrinsicIssue
    _mm_storeu_pd(); //expect: GolangIntrinsicIssue
    _mm_storeu_ps(); //expect: GolangIntrinsicIssue
    _mm_storeu_si128(); //expect: GolangIntrinsicIssue
    _mm_stream_pd(); //expect: GolangIntrinsicIssue
    _mm_stream_pd(); //expect: GolangIntrinsicIssue
    _mm_stream_pi(); //expect: GolangIntrinsicIssue
    _mm_stream_ps(); //expect: GolangIntrinsicIssue
    _mm_stream_sd(); //expect: GolangIntrinsicIssue
    _mm_stream_si128(); //expect: GolangIntrinsicIssue
    _mm_stream_si32(); //expect: GolangIntrinsicIssue
    _mm_stream_si64x(); //expect: GolangIntrinsicIssue
    _mm_stream_ss(); //expect: GolangIntrinsicIssue
    __movsb(); //expect: GolangIntrinsicIssue
    __movsd(); //expect: GolangIntrinsicIssue
    __movsq(); //expect: GolangIntrinsicIssue
    __movsw(); //expect: GolangIntrinsicIssue
    _m_prefetch(); //expect: GolangIntrinsicIssue
    _m_prefetchw(); //expect: GolangIntrinsicIssue
    __nvreg_restore_fence(); //expect: GolangIntrinsicIssue
    __nvreg_save_fence(); //expect: GolangIntrinsicIssue
    __outbytestring(); //expect: GolangIntrinsicIssue
    __outbyte(); //expect: GolangIntrinsicIssue
    __outdwordstring(); //expect: GolangIntrinsicIssue
    __outdword(); //expect: GolangIntrinsicIssue
    __outwordstring(); //expect: GolangIntrinsicIssue
    __outword(); //expect: GolangIntrinsicIssue
    _rsm(); //expect: GolangIntrinsicIssue
    _sgdt(); //expect: GolangIntrinsicIssue
    _sgdt(); //expect: GolangIntrinsicIssue
    __sidt(); //expect: GolangIntrinsicIssue
    * __slwpcb(); //expect: GolangIntrinsicIssue
    _stac(); //expect: GolangIntrinsicIssue
    _Store64_HLERelease(); //expect: GolangIntrinsicIssue
    _storebe_i16(); //expect: GolangIntrinsicIssue
    _storebe_i32(); //expect: GolangIntrinsicIssue
    _storebe_i64(); //expect: GolangIntrinsicIssue
    _store_be_u16(); //expect: GolangIntrinsicIssue
    _store_be_u32(); //expect: GolangIntrinsicIssue
    _store_be_u64(); //expect: GolangIntrinsicIssue
    _Store_HLERelease(); //expect: GolangIntrinsicIssue
    _StorePointer_HLERelease(); //expect: GolangIntrinsicIssue
    __stosb(); //expect: GolangIntrinsicIssue
    __stosd(); //expect: GolangIntrinsicIssue
    __stosq(); //expect: GolangIntrinsicIssue
    __stosw(); //expect: GolangIntrinsicIssue
    __svm_clgi(); //expect: GolangIntrinsicIssue
    __svm_invlpga(); //expect: GolangIntrinsicIssue
    __svm_skinit(); //expect: GolangIntrinsicIssue
    __svm_stgi(); //expect: GolangIntrinsicIssue
    __svm_vmload(); //expect: GolangIntrinsicIssue
    __svm_vmrun(); //expect: GolangIntrinsicIssue
    __svm_vmsave(); //expect: GolangIntrinsicIssue
    __ud2(); //expect: GolangIntrinsicIssue
    __vmx_off(); //expect: GolangIntrinsicIssue
    __vmx_vmptrst(); //expect: GolangIntrinsicIssue
    __wbinvd(); //expect: GolangIntrinsicIssue
    __writecr0(); //expect: GolangIntrinsicIssue
    __writecr0(); //expect: GolangIntrinsicIssue
    __writecr3(); //expect: GolangIntrinsicIssue
    __writecr3(); //expect: GolangIntrinsicIssue
    __writecr4(); //expect: GolangIntrinsicIssue
    __writecr4(); //expect: GolangIntrinsicIssue
    __writecr8(); //expect: GolangIntrinsicIssue
    __writecr8(); //expect: GolangIntrinsicIssue
    __writedr(); //expect: GolangIntrinsicIssue
    __writedr(); //expect: GolangIntrinsicIssue
    __writeeflags(); //expect: GolangIntrinsicIssue
    __writeeflags(); //expect: GolangIntrinsicIssue
    _writefsbase_u32(); //expect: GolangIntrinsicIssue
    _writefsbase_u64(); //expect: GolangIntrinsicIssue
    _writefsbase_u64(); //expect: GolangIntrinsicIssue
    __writefsbyte(); //expect: GolangIntrinsicIssue
    __writefsdword(); //expect: GolangIntrinsicIssue
    __writefsword(); //expect: GolangIntrinsicIssue
    _writegsbase_u32(); //expect: GolangIntrinsicIssue
    _writegsbase_u64(); //expect: GolangIntrinsicIssue
    _writegsbase_u64(); //expect: GolangIntrinsicIssue
    __writegsbyte(); //expect: GolangIntrinsicIssue
    __writegsdword(); //expect: GolangIntrinsicIssue
    __writegsqword(); //expect: GolangIntrinsicIssue
    __writegsword(); //expect: GolangIntrinsicIssue
    __writemsr(); //expect: GolangIntrinsicIssue
    _xrstor64(); //expect: GolangIntrinsicIssue
    _xrstor(); //expect: GolangIntrinsicIssue
    _xsave64(); //expect: GolangIntrinsicIssue
    _xsaveopt64(); //expect: GolangIntrinsicIssue
    _xsaveopt(); //expect: GolangIntrinsicIssue
    _xsave(); //expect: GolangIntrinsicIssue
    _xsetbv(); //expect: GolangIntrinsicIssue
}

// shall generate issue in aarch64.
void OTHER_ARCH_INTRINSICS()
{
    _addcary(); //expect: GolangIntrinsicIssue
    _allow_cpu_features(); //expect: GolangIntrinsicIssue
    _bit_scan_(); //expect: GolangIntrinsicIssue
    _bnd_(); //expect: GolangIntrinsicIssue
    _rdpip_(); //expect: GolangIntrinsicIssue
    _rotwa(); //expect: GolangIntrinsicIssue
    vec_v(); //expect: GolangIntrinsicIssue
    _otherarch_intrinsic_(); //expect: GolangIntrinsicIssue
}

// shall generate issue in aarch64.
void INCOMPATIBLE_UCRT_INTRINSICS()
{
    _abs64(); //expect: GolangIntrinsicIssue
    _alloca(); //expect: GolangIntrinsicIssue
    _byteswap_uint64(); //expect: GolangIntrinsicIssue
    _byteswap_ulong(); //expect: GolangIntrinsicIssue
    _byteswap_ushort(); //expect: GolangIntrinsicIssue
    _lrotl(); //expect: GolangIntrinsicIssue
    _lrotr(); //expect: GolangIntrinsicIssue
    _rotl(); //expect: GolangIntrinsicIssue
    _rotl64(); //expect: GolangIntrinsicIssue
    _rotr(); //expect: GolangIntrinsicIssue
    _rotr64(); //expect: GolangIntrinsicIssue
    _strset(); //expect: GolangIntrinsicIssue
    _wcsset(); //expect: GolangIntrinsicIssue
    wcscat();
    strset(); //expect: GolangIntrinsicIssue
    wcscmp();
    wcslen();
}

void printInt(int v) {
    printf("printint: %d\n", v);
}
*/
import "C"

func main() {
	v := 42
	C.printInt(C.int(v))
}
