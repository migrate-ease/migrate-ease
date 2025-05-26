#[cfg(all(any(target_arch = "aarch64"), target_feature = "neon"))]
fn add()
{
    use std::arch::aarch64::*;
    unsafe {
        __breakpoint();
        __crc32b();
        __crc32h();
        __crc32w();
        __crc32d();
        __crc32cb();
        __crc32ch();
        __crc32cw();
        __crc32cd();
        __dmb();
        __dsb();
        __isb();
        __nop();
        __rsr();
        __rsrp();
        __wsr();
        __wsrp();
        _cls_u32();
        _cls_u64();
        _clz_u64();
        _rbit_u64();
        _rev_u16();
        _rev_u32();
        _rev_u64();
        brk();
        vadd_f32();
        vadd_f64();
        vadd_s8();
        vadd_s16();
        vadd_s32();
        vadd_u8();
        vadd_u16();
        vadd_u32();
        vaddd_s64();
        vaddd_u64();
        vaddl_s8();
        vaddl_s16();
        vaddl_s32();
        vaddl_u8();
        vaddl_u16();
        vaddl_u32();
        vaddq_f32();
        vaddq_f64();
        vaddq_s8();
        vaddq_s16();
        vaddq_s32();
        vaddq_s64();
        vaddq_u8();
        vaddq_u16();
        vaddq_u32();
        vaddq_u64();
        vaesdq_u8();
        vaeseq_u8();
        vaesimcq_u8();
        vaesmcq_u8();
        vcombine_f32();
        vcombine_f64();
        vcombine_p8();
        vcombine_p16();
        vcombine_p64();
        vcombine_s8();
        vcombine_s16();
        vcombine_s32();
        vcombine_s64();
        vcombine_u8();
        vcombine_u16();
        vcombine_u32();
        vcombine_u64();
        vmaxv_f32();
        vmaxv_s8();
        vmaxv_s16();
        vmaxv_s32();
        vmaxv_u8();
        vmaxv_u16();
        vmaxv_u32();
        vmaxvq_f32();
        vmaxvq_f64();
        vmaxvq_s8();
        vmaxvq_s16();
        vmaxvq_s32();
        vmaxvq_u8();
        vmaxvq_u16();
        vmaxvq_u32();
        vminv_f32();
        vminv_s8();
        vminv_s16();
        vminv_s32();
        vminv_u8();
        vminv_u16();
        vminv_u32();
        vminvq_f32();
        vminvq_f64();
        vminvq_s8();
        vminvq_s16();
        vminvq_s32();
        vminvq_u8();
        vminvq_u16();
        vminvq_u32();
        vmovl_s8();
        vmovl_s16();
        vmovl_s32();
        vmovl_u8();
        vmovl_u16();
        vmovl_u32();
        vmovn_s16();
        vmovn_s32();
        vmovn_s64();
        vmovn_u16();
        vmovn_u32();
        vmovn_u64();
        vpmax_f32();
        vpmax_s8();
        vpmax_s16();
        vpmax_s32();
        vpmax_u8();
        vpmax_u16();
        vpmax_u32();
        vpmaxq_f32();
        vpmaxq_f64();
        vpmaxq_s8();
        vpmaxq_s16();
        vpmaxq_s32();
        vpmaxq_u8();
        vpmaxq_u16();
        vpmaxq_u32();
        vpmin_f32();
        vpmin_s8();
        vpmin_s16();
        vpmin_s32();
        vpmin_u8();
        vpmin_u16();
        vpmin_u32();
        vpminq_f32();
        vpminq_f64();
        vpminq_s8();
        vpminq_s16();
        vpminq_s32();
        vpminq_u8();
        vpminq_u16();
        vpminq_u32();
        vqtbl1_p8();
        vqtbl1_s8();
        vqtbl1_u8();
        vqtbl1q_p8();
        vqtbl1q_s8();
        vqtbl1q_u8();
        vqtbl2_p8();
        vqtbl2_s8();
        vqtbl2_u8();
        vqtbl2q_p8();
        vqtbl2q_s8();
        vqtbl2q_u8();
        vqtbl3_p8();
        vqtbl3_s8();
        vqtbl3_u8();
        vqtbl3q_p8();
        vqtbl3q_s8();
        vqtbl3q_u8();
        vqtbl4_p8();
        vqtbl4_s8();
        vqtbl4_u8();
        vqtbl4q_p8();
        vqtbl4q_s8();
        vqtbl4q_u8();
        vqtbx1_p8();
        vqtbx1_s8();
        vqtbx1_u8();
        vqtbx1q_p8();
        vqtbx1q_s8();
        vqtbx1q_u8();
        vqtbx2_p8();
        vqtbx2_s8();
        vqtbx2_u8();
        vqtbx2q_p8();
        vqtbx2q_s8();
        vqtbx2q_u8();
        vqtbx3_p8();
        vqtbx3_s8();
        vqtbx3_u8();
        vqtbx3q_p8();
        vqtbx3q_s8();
        vqtbx3q_u8();
        vqtbx4_p8();
        vqtbx4_s8();
        vqtbx4_u8();
        vqtbx4q_p8();
        vqtbx4q_s8();
        vqtbx4q_u8();
        vrsqrte_f32();
        vsha1cq_u32();
        vsha1h_u32();
        vsha1mq_u32();
        vsha1pq_u32();
        vsha1su0q_u32();
        vsha1su1q_u32();
        vsha256h2q_u32();
        vsha256hq_u32();
        vsha256su0q_u32();
        vsha256su1q_u32();
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
    }
}

#[cfg(all(any(target_arch = "x86", target_arch = "x86_64"), target_feature = "sse"))]
fn add()
{
    #[cfg(target_arch = "x86_64")]
    use std::arch::x86_64::*;
    unsafe {
        _MM_GET_EXCEPTION_MASK(); //expect: RustIntrinsicIssue
        _MM_GET_EXCEPTION_STATE(); //expect: RustIntrinsicIssue
        _MM_GET_FLUSH_ZERO_MODE(); //expect: RustIntrinsicIssue
        _MM_GET_ROUNDING_MODE(); //expect: RustIntrinsicIssue
        _MM_SET_EXCEPTION_MASK(); //expect: RustIntrinsicIssue
        _MM_SET_EXCEPTION_STATE(); //expect: RustIntrinsicIssue
        _MM_SET_FLUSH_ZERO_MODE(); //expect: RustIntrinsicIssue
        _MM_SET_ROUNDING_MODE(); //expect: RustIntrinsicIssue
        _MM_TRANSPOSE4_PS(); //expect: RustIntrinsicIssue
        __cpuid(); //expect: RustIntrinsicIssue
        __cpuid_count(); //expect: RustIntrinsicIssue
        __get_cpuid_max(); //expect: RustIntrinsicIssue
        __rdtscp(); //expect: RustIntrinsicIssue
        _addcarry_u32(); //expect: RustIntrinsicIssue
        _addcarry_u64(); //expect: RustIntrinsicIssue
        _addcarryx_u32(); //expect: RustIntrinsicIssue
        _addcarryx_u64(); //expect: RustIntrinsicIssue
        _andn_u32(); //expect: RustIntrinsicIssue
        _andn_u64(); //expect: RustIntrinsicIssue
        _bextr2_u32(); //expect: RustIntrinsicIssue
        _bextr2_u64(); //expect: RustIntrinsicIssue
        _bextr_u32(); //expect: RustIntrinsicIssue
        _bextr_u64(); //expect: RustIntrinsicIssue
        _blcfill_u32(); //expect: RustIntrinsicIssue
        _blcfill_u64(); //expect: RustIntrinsicIssue
        _blci_u32(); //expect: RustIntrinsicIssue
        _blci_u64(); //expect: RustIntrinsicIssue
        _blcic_u32(); //expect: RustIntrinsicIssue
        _blcic_u64(); //expect: RustIntrinsicIssue
        _blcmsk_u32(); //expect: RustIntrinsicIssue
        _blcmsk_u64(); //expect: RustIntrinsicIssue
        _blcs_u32(); //expect: RustIntrinsicIssue
        _blcs_u64(); //expect: RustIntrinsicIssue
        _blsfill_u32(); //expect: RustIntrinsicIssue
        _blsfill_u64(); //expect: RustIntrinsicIssue
        _blsi_u32(); //expect: RustIntrinsicIssue
        _blsi_u64(); //expect: RustIntrinsicIssue
        _blsic_u32(); //expect: RustIntrinsicIssue
        _blsic_u64(); //expect: RustIntrinsicIssue
        _blsmsk_u32(); //expect: RustIntrinsicIssue
        _blsmsk_u64(); //expect: RustIntrinsicIssue
        _blsr_u32(); //expect: RustIntrinsicIssue
        _blsr_u64(); //expect: RustIntrinsicIssue
        _bswap(); //expect: RustIntrinsicIssue
        _bswap64(); //expect: RustIntrinsicIssue
        _bzhi_u32(); //expect: RustIntrinsicIssue
        _bzhi_u64(); //expect: RustIntrinsicIssue
        _fxrstor(); //expect: RustIntrinsicIssue
        _fxrstor64(); //expect: RustIntrinsicIssue
        _fxsave(); //expect: RustIntrinsicIssue
        _fxsave64(); //expect: RustIntrinsicIssue
        _lzcnt_u32(); //expect: RustIntrinsicIssue
        _lzcnt_u64(); //expect: RustIntrinsicIssue
        _mm256_add_pd(); //expect: RustIntrinsicIssue
        _mm256_add_ps(); //expect: RustIntrinsicIssue
        _mm256_and_pd(); //expect: RustIntrinsicIssue
        _mm256_and_ps(); //expect: RustIntrinsicIssue
        _mm256_or_pd(); //expect: RustIntrinsicIssue
        _mm256_or_ps(); //expect: RustIntrinsicIssue
        _mm256_shuffle_pd(); //expect: RustIntrinsicIssue
        _mm256_shuffle_ps(); //expect: RustIntrinsicIssue
        _mm256_andnot_pd(); //expect: RustIntrinsicIssue
        _mm256_andnot_ps(); //expect: RustIntrinsicIssue
        _mm256_max_pd(); //expect: RustIntrinsicIssue
        _mm256_max_ps(); //expect: RustIntrinsicIssue
        _mm256_min_pd(); //expect: RustIntrinsicIssue
        _mm256_min_ps(); //expect: RustIntrinsicIssue
        _mm256_mul_pd(); //expect: RustIntrinsicIssue
        _mm256_mul_ps(); //expect: RustIntrinsicIssue
        _mm256_addsub_pd(); //expect: RustIntrinsicIssue
        _mm256_addsub_ps(); //expect: RustIntrinsicIssue
        _mm256_sub_pd(); //expect: RustIntrinsicIssue
        _mm256_sub_ps(); //expect: RustIntrinsicIssue
        _mm256_div_ps(); //expect: RustIntrinsicIssue
        _mm256_div_pd(); //expect: RustIntrinsicIssue
        _mm256_round_pd(); //expect: RustIntrinsicIssue
        _mm256_ceil_pd(); //expect: RustIntrinsicIssue
        _mm256_floor_pd(); //expect: RustIntrinsicIssue
        _mm256_round_ps(); //expect: RustIntrinsicIssue
        _mm256_ceil_ps(); //expect: RustIntrinsicIssue
        _mm256_floor_ps(); //expect: RustIntrinsicIssue
        _mm256_sqrt_ps(); //expect: RustIntrinsicIssue
        _mm256_sqrt_pd(); //expect: RustIntrinsicIssue
        _mm256_blend_pd(); //expect: RustIntrinsicIssue
        _mm256_blend_ps(); //expect: RustIntrinsicIssue
        _mm256_blendv_pd(); //expect: RustIntrinsicIssue
        _mm256_blendv_ps(); //expect: RustIntrinsicIssue
        _mm256_dp_ps(); //expect: RustIntrinsicIssue
        _mm256_hadd_pd(); //expect: RustIntrinsicIssue
        _mm256_hadd_ps(); //expect: RustIntrinsicIssue
        _mm256_hsub_pd(); //expect: RustIntrinsicIssue
        _mm256_hsub_ps(); //expect: RustIntrinsicIssue
        _mm256_xor_pd(); //expect: RustIntrinsicIssue
        _mm256_xor_ps(); //expect: RustIntrinsicIssue
        _mm256_cmp_pd(); //expect: RustIntrinsicIssue
        _mm256_cmp_ps(); //expect: RustIntrinsicIssue
        _mm256_cvtpd_ps(); //expect: RustIntrinsicIssue
        _mm256_cvtps_pd(); //expect: RustIntrinsicIssue
        _mm256_zeroall(); //expect: RustIntrinsicIssue
        _mm256_zeroupper(); //expect: RustIntrinsicIssue
        _mm256_permutevar_ps(); //expect: RustIntrinsicIssue
        _mm256_permute_ps(); //expect: RustIntrinsicIssue
        _mm256_permutevar_pd(); //expect: RustIntrinsicIssue
        _mm256_permute_pd(); //expect: RustIntrinsicIssue
        _mm256_broadcast_ss(); //expect: RustIntrinsicIssue
        _mm256_broadcast_sd(); //expect: RustIntrinsicIssue
        _mm256_broadcast_ps(); //expect: RustIntrinsicIssue
        _mm256_broadcast_pd(); //expect: RustIntrinsicIssue
        _mm256_load_pd(); //expect: RustIntrinsicIssue
        _mm256_store_pd(); //expect: RustIntrinsicIssue
        _mm256_load_ps(); //expect: RustIntrinsicIssue
        _mm256_store_ps(); //expect: RustIntrinsicIssue
        _mm256_loadu_pd(); //expect: RustIntrinsicIssue
        _mm256_storeu_pd(); //expect: RustIntrinsicIssue
        _mm256_loadu_ps(); //expect: RustIntrinsicIssue
        _mm256_storeu_ps(); //expect: RustIntrinsicIssue
        _mm256_maskload_pd(); //expect: RustIntrinsicIssue
        _mm256_maskstore_pd(); //expect: RustIntrinsicIssue
        _mm256_maskload_ps(); //expect: RustIntrinsicIssue
        _mm256_maskstore_ps(); //expect: RustIntrinsicIssue
        _mm256_movehdup_ps(); //expect: RustIntrinsicIssue
        _mm256_moveldup_ps(); //expect: RustIntrinsicIssue
        _mm256_movedup_pd(); //expect: RustIntrinsicIssue
        _mm256_stream_pd(); //expect: RustIntrinsicIssue
        _mm256_stream_ps(); //expect: RustIntrinsicIssue
        _mm256_rcp_ps(); //expect: RustIntrinsicIssue
        _mm256_rsqrt_ps(); //expect: RustIntrinsicIssue
        _mm256_unpackhi_pd(); //expect: RustIntrinsicIssue
        _mm256_unpackhi_ps(); //expect: RustIntrinsicIssue
        _mm256_unpacklo_pd(); //expect: RustIntrinsicIssue
        _mm256_unpacklo_ps(); //expect: RustIntrinsicIssue
        _mm256_testz_pd(); //expect: RustIntrinsicIssue
        _mm256_testc_pd(); //expect: RustIntrinsicIssue
        _mm256_testnzc_pd(); //expect: RustIntrinsicIssue
        _mm256_testz_ps(); //expect: RustIntrinsicIssue
        _mm256_testc_ps(); //expect: RustIntrinsicIssue
        _mm256_testnzc_ps(); //expect: RustIntrinsicIssue
        _mm256_movemask_pd(); //expect: RustIntrinsicIssue
        _mm256_movemask_ps(); //expect: RustIntrinsicIssue
        _mm256_setzero_pd(); //expect: RustIntrinsicIssue
        _mm256_setzero_ps(); //expect: RustIntrinsicIssue
        _mm256_set_pd(); //expect: RustIntrinsicIssue
        _mm256_set_ps(); //expect: RustIntrinsicIssue
        _mm256_setr_pd(); //expect: RustIntrinsicIssue
        _mm256_setr_ps(); //expect: RustIntrinsicIssue
        _mm256_castpd_ps(); //expect: RustIntrinsicIssue
        _mm256_castps_pd(); //expect: RustIntrinsicIssue
        _mm256_undefined_ps(); //expect: RustIntrinsicIssue
        _mm256_undefined_pd(); //expect: RustIntrinsicIssue
        _mm256_broadcastsd_pd(); //expect: RustIntrinsicIssue
        _mm256_broadcastss_ps(); //expect: RustIntrinsicIssue
        _mm256_fmadd_pd(); //expect: RustIntrinsicIssue
        _mm256_fmadd_ps(); //expect: RustIntrinsicIssue
        _mm256_fmaddsub_pd(); //expect: RustIntrinsicIssue
        _mm256_fmaddsub_ps(); //expect: RustIntrinsicIssue
        _mm256_fmsub_pd(); //expect: RustIntrinsicIssue
        _mm256_fmsub_ps(); //expect: RustIntrinsicIssue
        _mm256_fmsubadd_pd(); //expect: RustIntrinsicIssue
        _mm256_fmsubadd_ps(); //expect: RustIntrinsicIssue
        _mm256_fnmadd_pd(); //expect: RustIntrinsicIssue
        _mm256_fnmadd_ps(); //expect: RustIntrinsicIssue
        _mm256_fnmsub_pd(); //expect: RustIntrinsicIssue
        _mm256_fnmsub_ps(); //expect: RustIntrinsicIssue
        _mm256_abs_epi8(); //expect: RustIntrinsicIssue
        _mm256_abs_epi16(); //expect: RustIntrinsicIssue
        _mm256_abs_epi32(); //expect: RustIntrinsicIssue
        _mm256_add_epi8(); //expect: RustIntrinsicIssue
        _mm256_add_epi16(); //expect: RustIntrinsicIssue
        _mm256_add_epi32(); //expect: RustIntrinsicIssue
        _mm256_add_epi64(); //expect: RustIntrinsicIssue
        _mm256_adds_epi8(); //expect: RustIntrinsicIssue
        _mm256_adds_epi16(); //expect: RustIntrinsicIssue
        _mm256_adds_epu8(); //expect: RustIntrinsicIssue
        _mm256_adds_epu16(); //expect: RustIntrinsicIssue
        _mm256_alignr_epi8(); //expect: RustIntrinsicIssue
        _mm256_and_si256(); //expect: RustIntrinsicIssue
        _mm256_andnot_si256(); //expect: RustIntrinsicIssue
        _mm256_avg_epu8(); //expect: RustIntrinsicIssue
        _mm256_avg_epu16(); //expect: RustIntrinsicIssue
        _mm256_blend_epi16(); //expect: RustIntrinsicIssue
        _mm256_blend_epi32(); //expect: RustIntrinsicIssue
        _mm256_blendv_epi8(); //expect: RustIntrinsicIssue
        _mm256_broadcastb_epi8(); //expect: RustIntrinsicIssue
        _mm256_broadcastd_epi32(); //expect: RustIntrinsicIssue
        _mm256_broadcastq_epi64(); //expect: RustIntrinsicIssue
        _mm256_broadcastsi128_si256(); //expect: RustIntrinsicIssue
        _mm256_broadcastw_epi16(); //expect: RustIntrinsicIssue
        _mm256_bslli_epi128(); //expect: RustIntrinsicIssue
        _mm256_bsrli_epi128(); //expect: RustIntrinsicIssue
        _mm256_castpd128_pd256(); //expect: RustIntrinsicIssue
        _mm256_castpd256_pd128(); //expect: RustIntrinsicIssue
        _mm256_castpd_si256(); //expect: RustIntrinsicIssue
        _mm256_castps128_ps256(); //expect: RustIntrinsicIssue
        _mm256_castps256_ps128(); //expect: RustIntrinsicIssue
        _mm256_castps_si256(); //expect: RustIntrinsicIssue
        _mm256_castsi256_ps(); //expect: RustIntrinsicIssue
        _mm256_castsi256_pd(); //expect: RustIntrinsicIssue
        _mm256_castsi128_si256(); //expect: RustIntrinsicIssue
        _mm256_castsi256_si128(); //expect: RustIntrinsicIssue
        _mm256_cmpeq_epi8(); //expect: RustIntrinsicIssue
        _mm256_cmpeq_epi16(); //expect: RustIntrinsicIssue
        _mm256_cmpeq_epi32(); //expect: RustIntrinsicIssue
        _mm256_cmpeq_epi64(); //expect: RustIntrinsicIssue
        _mm256_cmpgt_epi8(); //expect: RustIntrinsicIssue
        _mm256_cmpgt_epi16(); //expect: RustIntrinsicIssue
        _mm256_cmpgt_epi32(); //expect: RustIntrinsicIssue
        _mm256_cmpgt_epi64(); //expect: RustIntrinsicIssue
        _mm256_cvtepi32_pd(); //expect: RustIntrinsicIssue
        _mm256_cvtepi32_ps(); //expect: RustIntrinsicIssue
        _mm256_cvtepi16_epi32(); //expect: RustIntrinsicIssue
        _mm256_cvtepi16_epi64(); //expect: RustIntrinsicIssue
        _mm256_cvtepi32_epi64(); //expect: RustIntrinsicIssue
        _mm256_cvtepi8_epi16(); //expect: RustIntrinsicIssue
        _mm256_cvtepi8_epi32(); //expect: RustIntrinsicIssue
        _mm256_cvtepi8_epi64(); //expect: RustIntrinsicIssue
        _mm256_cvtepu16_epi32(); //expect: RustIntrinsicIssue
        _mm256_cvtepu16_epi64(); //expect: RustIntrinsicIssue
        _mm256_cvtepu32_epi64(); //expect: RustIntrinsicIssue
        _mm256_cvtepu8_epi16(); //expect: RustIntrinsicIssue
        _mm256_cvtepu8_epi32(); //expect: RustIntrinsicIssue
        _mm256_cvtepu8_epi64(); //expect: RustIntrinsicIssue
        _mm256_cvtpd_epi32(); //expect: RustIntrinsicIssue
        _mm256_cvtps_epi32(); //expect: RustIntrinsicIssue
        _mm256_cvtsd_f64(); //expect: RustIntrinsicIssue
        _mm256_cvtsi256_si32(); //expect: RustIntrinsicIssue
        _mm256_cvtss_f32(); //expect: RustIntrinsicIssue
        _mm256_cvttpd_epi32(); //expect: RustIntrinsicIssue
        _mm256_cvttps_epi32(); //expect: RustIntrinsicIssue
        _mm256_extract_epi8(); //expect: RustIntrinsicIssue
        _mm256_extract_epi16(); //expect: RustIntrinsicIssue
        _mm256_extract_epi32(); //expect: RustIntrinsicIssue
        _mm256_extract_epi64(); //expect: RustIntrinsicIssue
        _mm256_extractf128_ps(); //expect: RustIntrinsicIssue
        _mm256_extractf128_pd(); //expect: RustIntrinsicIssue
        _mm256_extractf128_si256(); //expect: RustIntrinsicIssue
        _mm256_extracti128_si256(); //expect: RustIntrinsicIssue
        _mm256_hadd_epi16(); //expect: RustIntrinsicIssue
        _mm256_hadd_epi32(); //expect: RustIntrinsicIssue
        _mm256_hadds_epi16(); //expect: RustIntrinsicIssue
        _mm256_hsub_epi16(); //expect: RustIntrinsicIssue
        _mm256_hsub_epi32(); //expect: RustIntrinsicIssue
        _mm256_hsubs_epi16(); //expect: RustIntrinsicIssue
        _mm256_i32gather_ps(); //expect: RustIntrinsicIssue
        _mm256_i32gather_pd(); //expect: RustIntrinsicIssue
        _mm256_i64gather_ps(); //expect: RustIntrinsicIssue
        _mm256_i64gather_pd(); //expect: RustIntrinsicIssue
        _mm256_i32gather_epi32(); //expect: RustIntrinsicIssue
        _mm256_i32gather_epi64(); //expect: RustIntrinsicIssue
        _mm256_i64gather_epi32(); //expect: RustIntrinsicIssue
        _mm256_i64gather_epi64(); //expect: RustIntrinsicIssue
        _mm256_insert_epi8(); //expect: RustIntrinsicIssue
        _mm256_insert_epi16(); //expect: RustIntrinsicIssue
        _mm256_insert_epi32(); //expect: RustIntrinsicIssue
        _mm256_insert_epi64(); //expect: RustIntrinsicIssue
        _mm256_insertf128_ps(); //expect: RustIntrinsicIssue
        _mm256_insertf128_pd(); //expect: RustIntrinsicIssue
        _mm256_insertf128_si256(); //expect: RustIntrinsicIssue
        _mm256_inserti128_si256(); //expect: RustIntrinsicIssue
        _mm256_lddqu_si256(); //expect: RustIntrinsicIssue
        _mm256_load_si256(); //expect: RustIntrinsicIssue
        _mm256_loadu2_m128(); //expect: RustIntrinsicIssue
        _mm256_loadu2_m128d(); //expect: RustIntrinsicIssue
        _mm256_loadu2_m128i(); //expect: RustIntrinsicIssue
        _mm256_loadu_si256(); //expect: RustIntrinsicIssue
        _mm256_madd_epi16(); //expect: RustIntrinsicIssue
        _mm256_maddubs_epi16(); //expect: RustIntrinsicIssue
        _mm256_mask_i32gather_ps(); //expect: RustIntrinsicIssue
        _mm256_mask_i32gather_pd(); //expect: RustIntrinsicIssue
        _mm256_mask_i64gather_ps(); //expect: RustIntrinsicIssue
        _mm256_mask_i64gather_pd(); //expect: RustIntrinsicIssue
        _mm256_mask_i32gather_epi32(); //expect: RustIntrinsicIssue
        _mm256_mask_i32gather_epi64(); //expect: RustIntrinsicIssue
        _mm256_mask_i64gather_epi32(); //expect: RustIntrinsicIssue
        _mm256_mask_i64gather_epi64(); //expect: RustIntrinsicIssue
        _mm256_maskload_epi32(); //expect: RustIntrinsicIssue
        _mm256_maskload_epi64(); //expect: RustIntrinsicIssue
        _mm256_maskstore_epi32(); //expect: RustIntrinsicIssue
        _mm256_maskstore_epi64(); //expect: RustIntrinsicIssue
        _mm256_max_epi8(); //expect: RustIntrinsicIssue
        _mm256_max_epi16(); //expect: RustIntrinsicIssue
        _mm256_max_epi32(); //expect: RustIntrinsicIssue
        _mm256_max_epu8(); //expect: RustIntrinsicIssue
        _mm256_max_epu16(); //expect: RustIntrinsicIssue
        _mm256_max_epu32(); //expect: RustIntrinsicIssue
        _mm256_min_epi8(); //expect: RustIntrinsicIssue
        _mm256_min_epi16(); //expect: RustIntrinsicIssue
        _mm256_min_epi32(); //expect: RustIntrinsicIssue
        _mm256_min_epu8(); //expect: RustIntrinsicIssue
        _mm256_min_epu16(); //expect: RustIntrinsicIssue
        _mm256_min_epu32(); //expect: RustIntrinsicIssue
        _mm256_movemask_epi8(); //expect: RustIntrinsicIssue
        _mm256_mpsadbw_epu8(); //expect: RustIntrinsicIssue
        _mm256_mul_epi32(); //expect: RustIntrinsicIssue
        _mm256_mul_epu32(); //expect: RustIntrinsicIssue
        _mm256_mulhi_epi16(); //expect: RustIntrinsicIssue
        _mm256_mulhi_epu16(); //expect: RustIntrinsicIssue
        _mm256_mulhrs_epi16(); //expect: RustIntrinsicIssue
        _mm256_mullo_epi16(); //expect: RustIntrinsicIssue
        _mm256_mullo_epi32(); //expect: RustIntrinsicIssue
        _mm256_or_si256(); //expect: RustIntrinsicIssue
        _mm256_packs_epi16(); //expect: RustIntrinsicIssue
        _mm256_packs_epi32(); //expect: RustIntrinsicIssue
        _mm256_packus_epi16(); //expect: RustIntrinsicIssue
        _mm256_packus_epi32(); //expect: RustIntrinsicIssue
        _mm256_permute2f128_ps(); //expect: RustIntrinsicIssue
        _mm256_permute2f128_pd(); //expect: RustIntrinsicIssue
        _mm256_permute2f128_si256(); //expect: RustIntrinsicIssue
        _mm256_permute2x128_si256(); //expect: RustIntrinsicIssue
        _mm256_permute4x64_pd(); //expect: RustIntrinsicIssue
        _mm256_permute4x64_epi64(); //expect: RustIntrinsicIssue
        _mm256_permutevar8x32_ps(); //expect: RustIntrinsicIssue
        _mm256_permutevar8x32_epi32(); //expect: RustIntrinsicIssue
        _mm256_sad_epu8(); //expect: RustIntrinsicIssue
        _mm256_set1_pd(); //expect: RustIntrinsicIssue
        _mm256_set1_ps(); //expect: RustIntrinsicIssue
        _mm256_set1_epi8(); //expect: RustIntrinsicIssue
        _mm256_set1_epi16(); //expect: RustIntrinsicIssue
        _mm256_set1_epi32(); //expect: RustIntrinsicIssue
        _mm256_set1_epi64x(); //expect: RustIntrinsicIssue
        _mm256_set_epi8(); //expect: RustIntrinsicIssue
        _mm256_set_epi16(); //expect: RustIntrinsicIssue
        _mm256_set_epi32(); //expect: RustIntrinsicIssue
        _mm256_set_epi64x(); //expect: RustIntrinsicIssue
        _mm256_set_m128(); //expect: RustIntrinsicIssue
        _mm256_set_m128d(); //expect: RustIntrinsicIssue
        _mm256_set_m128i(); //expect: RustIntrinsicIssue
        _mm256_setr_epi8(); //expect: RustIntrinsicIssue
        _mm256_setr_epi16(); //expect: RustIntrinsicIssue
        _mm256_setr_epi32(); //expect: RustIntrinsicIssue
        _mm256_setr_epi64x(); //expect: RustIntrinsicIssue
        _mm256_setr_m128(); //expect: RustIntrinsicIssue
        _mm256_setr_m128d(); //expect: RustIntrinsicIssue
        _mm256_setr_m128i(); //expect: RustIntrinsicIssue
        _mm256_setzero_si256(); //expect: RustIntrinsicIssue
        _mm256_shuffle_epi8(); //expect: RustIntrinsicIssue
        _mm256_shuffle_epi32(); //expect: RustIntrinsicIssue
        _mm256_shufflehi_epi16(); //expect: RustIntrinsicIssue
        _mm256_shufflelo_epi16(); //expect: RustIntrinsicIssue
        _mm256_sign_epi8(); //expect: RustIntrinsicIssue
        _mm256_sign_epi16(); //expect: RustIntrinsicIssue
        _mm256_sign_epi32(); //expect: RustIntrinsicIssue
        _mm256_sll_epi16(); //expect: RustIntrinsicIssue
        _mm256_sll_epi32(); //expect: RustIntrinsicIssue
        _mm256_sll_epi64(); //expect: RustIntrinsicIssue
        _mm256_slli_epi16(); //expect: RustIntrinsicIssue
        _mm256_slli_epi32(); //expect: RustIntrinsicIssue
        _mm256_slli_epi64(); //expect: RustIntrinsicIssue
        _mm256_slli_si256(); //expect: RustIntrinsicIssue
        _mm256_sllv_epi32(); //expect: RustIntrinsicIssue
        _mm256_sllv_epi64(); //expect: RustIntrinsicIssue
        _mm256_sra_epi16(); //expect: RustIntrinsicIssue
        _mm256_sra_epi32(); //expect: RustIntrinsicIssue
        _mm256_srai_epi16(); //expect: RustIntrinsicIssue
        _mm256_srai_epi32(); //expect: RustIntrinsicIssue
        _mm256_srav_epi32(); //expect: RustIntrinsicIssue
        _mm256_srl_epi16(); //expect: RustIntrinsicIssue
        _mm256_srl_epi32(); //expect: RustIntrinsicIssue
        _mm256_srl_epi64(); //expect: RustIntrinsicIssue
        _mm256_srli_epi16(); //expect: RustIntrinsicIssue
        _mm256_srli_epi32(); //expect: RustIntrinsicIssue
        _mm256_srli_epi64(); //expect: RustIntrinsicIssue
        _mm256_srli_si256(); //expect: RustIntrinsicIssue
        _mm256_srlv_epi32(); //expect: RustIntrinsicIssue
        _mm256_srlv_epi64(); //expect: RustIntrinsicIssue
        _mm256_store_si256(); //expect: RustIntrinsicIssue
        _mm256_storeu2_m128(); //expect: RustIntrinsicIssue
        _mm256_storeu2_m128d(); //expect: RustIntrinsicIssue
        _mm256_storeu2_m128i(); //expect: RustIntrinsicIssue
        _mm256_storeu_si256(); //expect: RustIntrinsicIssue
        _mm256_stream_si256(); //expect: RustIntrinsicIssue
        _mm256_sub_epi8(); //expect: RustIntrinsicIssue
        _mm256_sub_epi16(); //expect: RustIntrinsicIssue
        _mm256_sub_epi32(); //expect: RustIntrinsicIssue
        _mm256_sub_epi64(); //expect: RustIntrinsicIssue
        _mm256_subs_epi8(); //expect: RustIntrinsicIssue
        _mm256_subs_epi16(); //expect: RustIntrinsicIssue
        _mm256_subs_epu8(); //expect: RustIntrinsicIssue
        _mm256_subs_epu16(); //expect: RustIntrinsicIssue
        _mm256_testc_si256(); //expect: RustIntrinsicIssue
        _mm256_testnzc_si256(); //expect: RustIntrinsicIssue
        _mm256_testz_si256(); //expect: RustIntrinsicIssue
        _mm256_undefined_si256(); //expect: RustIntrinsicIssue
        _mm256_unpackhi_epi8(); //expect: RustIntrinsicIssue
        _mm256_unpackhi_epi16(); //expect: RustIntrinsicIssue
        _mm256_unpackhi_epi32(); //expect: RustIntrinsicIssue
        _mm256_unpackhi_epi64(); //expect: RustIntrinsicIssue
        _mm256_unpacklo_epi8(); //expect: RustIntrinsicIssue
        _mm256_unpacklo_epi16(); //expect: RustIntrinsicIssue
        _mm256_unpacklo_epi32(); //expect: RustIntrinsicIssue
        _mm256_unpacklo_epi64(); //expect: RustIntrinsicIssue
        _mm256_xor_si256(); //expect: RustIntrinsicIssue
        _mm256_zextpd128_pd256(); //expect: RustIntrinsicIssue
        _mm256_zextps128_ps256(); //expect: RustIntrinsicIssue
        _mm256_zextsi128_si256(); //expect: RustIntrinsicIssue
        _mm_abs_epi8(); //expect: RustIntrinsicIssue
        _mm_abs_epi16(); //expect: RustIntrinsicIssue
        _mm_abs_epi32(); //expect: RustIntrinsicIssue
        _mm_add_epi8(); //expect: RustIntrinsicIssue
        _mm_add_epi16(); //expect: RustIntrinsicIssue
        _mm_add_epi32(); //expect: RustIntrinsicIssue
        _mm_add_epi64(); //expect: RustIntrinsicIssue
        _mm_add_pd(); //expect: RustIntrinsicIssue
        _mm_add_ps(); //expect: RustIntrinsicIssue
        _mm_add_sd(); //expect: RustIntrinsicIssue
        _mm_add_ss(); //expect: RustIntrinsicIssue
        _mm_adds_epi8(); //expect: RustIntrinsicIssue
        _mm_adds_epi16(); //expect: RustIntrinsicIssue
        _mm_adds_epu8(); //expect: RustIntrinsicIssue
        _mm_adds_epu16(); //expect: RustIntrinsicIssue
        _mm_addsub_pd(); //expect: RustIntrinsicIssue
        _mm_addsub_ps(); //expect: RustIntrinsicIssue
        _mm_aesdec_si128(); //expect: RustIntrinsicIssue
        _mm_aesdeclast_si128(); //expect: RustIntrinsicIssue
        _mm_aesenc_si128(); //expect: RustIntrinsicIssue
        _mm_aesenclast_si128(); //expect: RustIntrinsicIssue
        _mm_aesimc_si128(); //expect: RustIntrinsicIssue
        _mm_aeskeygenassist_si128(); //expect: RustIntrinsicIssue
        _mm_alignr_epi8(); //expect: RustIntrinsicIssue
        _mm_and_pd(); //expect: RustIntrinsicIssue
        _mm_and_ps(); //expect: RustIntrinsicIssue
        _mm_and_si128(); //expect: RustIntrinsicIssue
        _mm_andnot_pd(); //expect: RustIntrinsicIssue
        _mm_andnot_ps(); //expect: RustIntrinsicIssue
        _mm_andnot_si128(); //expect: RustIntrinsicIssue
        _mm_avg_epu8(); //expect: RustIntrinsicIssue
        _mm_avg_epu16(); //expect: RustIntrinsicIssue
        _mm_blend_epi16(); //expect: RustIntrinsicIssue
        _mm_blend_epi32(); //expect: RustIntrinsicIssue
        _mm_blend_pd(); //expect: RustIntrinsicIssue
        _mm_blend_ps(); //expect: RustIntrinsicIssue
        _mm_blendv_epi8(); //expect: RustIntrinsicIssue
        _mm_blendv_pd(); //expect: RustIntrinsicIssue
        _mm_blendv_ps(); //expect: RustIntrinsicIssue
        _mm_broadcast_ss(); //expect: RustIntrinsicIssue
        _mm_broadcastb_epi8(); //expect: RustIntrinsicIssue
        _mm_broadcastd_epi32(); //expect: RustIntrinsicIssue
        _mm_broadcastq_epi64(); //expect: RustIntrinsicIssue
        _mm_broadcastsd_pd(); //expect: RustIntrinsicIssue
        _mm_broadcastss_ps(); //expect: RustIntrinsicIssue
        _mm_broadcastw_epi16(); //expect: RustIntrinsicIssue
        _mm_bslli_si128(); //expect: RustIntrinsicIssue
        _mm_bsrli_si128(); //expect: RustIntrinsicIssue
        _mm_castpd_ps(); //expect: RustIntrinsicIssue
        _mm_castpd_si128(); //expect: RustIntrinsicIssue
        _mm_castps_pd(); //expect: RustIntrinsicIssue
        _mm_castps_si128(); //expect: RustIntrinsicIssue
        _mm_castsi128_pd(); //expect: RustIntrinsicIssue
        _mm_castsi128_ps(); //expect: RustIntrinsicIssue
        _mm_ceil_pd(); //expect: RustIntrinsicIssue
        _mm_ceil_ps(); //expect: RustIntrinsicIssue
        _mm_ceil_sd(); //expect: RustIntrinsicIssue
        _mm_ceil_ss(); //expect: RustIntrinsicIssue
        _mm_clflush(); //expect: RustIntrinsicIssue
        _mm_clmulepi64_si128(); //expect: RustIntrinsicIssue
        _mm_cmp_pd(); //expect: RustIntrinsicIssue
        _mm_cmp_ps(); //expect: RustIntrinsicIssue
        _mm_cmp_sd(); //expect: RustIntrinsicIssue
        _mm_cmp_ss(); //expect: RustIntrinsicIssue
        _mm_cmpeq_epi8(); //expect: RustIntrinsicIssue
        _mm_cmpeq_epi16(); //expect: RustIntrinsicIssue
        _mm_cmpeq_epi32(); //expect: RustIntrinsicIssue
        _mm_cmpeq_epi64(); //expect: RustIntrinsicIssue
        _mm_cmpeq_pd(); //expect: RustIntrinsicIssue
        _mm_cmpeq_ps(); //expect: RustIntrinsicIssue
        _mm_cmpeq_sd(); //expect: RustIntrinsicIssue
        _mm_cmpeq_ss(); //expect: RustIntrinsicIssue
        _mm_cmpestra(); //expect: RustIntrinsicIssue
        _mm_cmpestrc(); //expect: RustIntrinsicIssue
        _mm_cmpestri(); //expect: RustIntrinsicIssue
        _mm_cmpestrm(); //expect: RustIntrinsicIssue
        _mm_cmpestro(); //expect: RustIntrinsicIssue
        _mm_cmpestrs(); //expect: RustIntrinsicIssue
        _mm_cmpestrz(); //expect: RustIntrinsicIssue
        _mm_cmpge_pd(); //expect: RustIntrinsicIssue
        _mm_cmpge_ps(); //expect: RustIntrinsicIssue
        _mm_cmpge_sd(); //expect: RustIntrinsicIssue
        _mm_cmpge_ss(); //expect: RustIntrinsicIssue
        _mm_cmpgt_epi8(); //expect: RustIntrinsicIssue
        _mm_cmpgt_epi16(); //expect: RustIntrinsicIssue
        _mm_cmpgt_epi32(); //expect: RustIntrinsicIssue
        _mm_cmpgt_epi64(); //expect: RustIntrinsicIssue
        _mm_cmpgt_pd(); //expect: RustIntrinsicIssue
        _mm_cmpgt_ps(); //expect: RustIntrinsicIssue
        _mm_cmpgt_sd(); //expect: RustIntrinsicIssue
        _mm_cmpgt_ss(); //expect: RustIntrinsicIssue
        _mm_cmpistra(); //expect: RustIntrinsicIssue
        _mm_cmpistrc(); //expect: RustIntrinsicIssue
        _mm_cmpistri(); //expect: RustIntrinsicIssue
        _mm_cmpistrm(); //expect: RustIntrinsicIssue
        _mm_cmpistro(); //expect: RustIntrinsicIssue
        _mm_cmpistrs(); //expect: RustIntrinsicIssue
        _mm_cmpistrz(); //expect: RustIntrinsicIssue
        _mm_cmple_pd(); //expect: RustIntrinsicIssue
        _mm_cmple_ps(); //expect: RustIntrinsicIssue
        _mm_cmple_sd(); //expect: RustIntrinsicIssue
        _mm_cmple_ss(); //expect: RustIntrinsicIssue
        _mm_cmplt_epi8(); //expect: RustIntrinsicIssue
        _mm_cmplt_epi16(); //expect: RustIntrinsicIssue
        _mm_cmplt_epi32(); //expect: RustIntrinsicIssue
        _mm_cmplt_pd(); //expect: RustIntrinsicIssue
        _mm_cmplt_ps(); //expect: RustIntrinsicIssue
        _mm_cmplt_sd(); //expect: RustIntrinsicIssue
        _mm_cmplt_ss(); //expect: RustIntrinsicIssue
        _mm_cmpneq_pd(); //expect: RustIntrinsicIssue
        _mm_cmpneq_ps(); //expect: RustIntrinsicIssue
        _mm_cmpneq_sd(); //expect: RustIntrinsicIssue
        _mm_cmpneq_ss(); //expect: RustIntrinsicIssue
        _mm_cmpnge_pd(); //expect: RustIntrinsicIssue
        _mm_cmpnge_ps(); //expect: RustIntrinsicIssue
        _mm_cmpnge_sd(); //expect: RustIntrinsicIssue
        _mm_cmpnge_ss(); //expect: RustIntrinsicIssue
        _mm_cmpngt_pd(); //expect: RustIntrinsicIssue
        _mm_cmpngt_ps(); //expect: RustIntrinsicIssue
        _mm_cmpngt_sd(); //expect: RustIntrinsicIssue
        _mm_cmpngt_ss(); //expect: RustIntrinsicIssue
        _mm_cmpnle_pd(); //expect: RustIntrinsicIssue
        _mm_cmpnle_ps(); //expect: RustIntrinsicIssue
        _mm_cmpnle_sd(); //expect: RustIntrinsicIssue
        _mm_cmpnle_ss(); //expect: RustIntrinsicIssue
        _mm_cmpnlt_pd(); //expect: RustIntrinsicIssue
        _mm_cmpnlt_ps(); //expect: RustIntrinsicIssue
        _mm_cmpnlt_sd(); //expect: RustIntrinsicIssue
        _mm_cmpnlt_ss(); //expect: RustIntrinsicIssue
        _mm_cmpord_pd(); //expect: RustIntrinsicIssue
        _mm_cmpord_ps(); //expect: RustIntrinsicIssue
        _mm_cmpord_sd(); //expect: RustIntrinsicIssue
        _mm_cmpord_ss(); //expect: RustIntrinsicIssue
        _mm_cmpunord_pd(); //expect: RustIntrinsicIssue
        _mm_cmpunord_ps(); //expect: RustIntrinsicIssue
        _mm_cmpunord_sd(); //expect: RustIntrinsicIssue
        _mm_cmpunord_ss(); //expect: RustIntrinsicIssue
        _mm_comieq_sd(); //expect: RustIntrinsicIssue
        _mm_comieq_ss(); //expect: RustIntrinsicIssue
        _mm_comige_sd(); //expect: RustIntrinsicIssue
        _mm_comige_ss(); //expect: RustIntrinsicIssue
        _mm_comigt_sd(); //expect: RustIntrinsicIssue
        _mm_comigt_ss(); //expect: RustIntrinsicIssue
        _mm_comile_sd(); //expect: RustIntrinsicIssue
        _mm_comile_ss(); //expect: RustIntrinsicIssue
        _mm_comilt_sd(); //expect: RustIntrinsicIssue
        _mm_comilt_ss(); //expect: RustIntrinsicIssue
        _mm_comineq_sd(); //expect: RustIntrinsicIssue
        _mm_comineq_ss(); //expect: RustIntrinsicIssue
        _mm_crc32_u8(); //expect: RustIntrinsicIssue
        _mm_crc32_u16(); //expect: RustIntrinsicIssue
        _mm_crc32_u32(); //expect: RustIntrinsicIssue
        _mm_crc32_u64(); //expect: RustIntrinsicIssue
        _mm_cvt_si2ss(); //expect: RustIntrinsicIssue
        _mm_cvt_ss2si(); //expect: RustIntrinsicIssue
        _mm_cvtepi32_pd(); //expect: RustIntrinsicIssue
        _mm_cvtepi32_ps(); //expect: RustIntrinsicIssue
        _mm_cvtepi16_epi32(); //expect: RustIntrinsicIssue
        _mm_cvtepi16_epi64(); //expect: RustIntrinsicIssue
        _mm_cvtepi32_epi64(); //expect: RustIntrinsicIssue
        _mm_cvtepi8_epi16(); //expect: RustIntrinsicIssue
        _mm_cvtepi8_epi32(); //expect: RustIntrinsicIssue
        _mm_cvtepi8_epi64(); //expect: RustIntrinsicIssue
        _mm_cvtepu16_epi32(); //expect: RustIntrinsicIssue
        _mm_cvtepu16_epi64(); //expect: RustIntrinsicIssue
        _mm_cvtepu32_epi64(); //expect: RustIntrinsicIssue
        _mm_cvtepu8_epi16(); //expect: RustIntrinsicIssue
        _mm_cvtepu8_epi32(); //expect: RustIntrinsicIssue
        _mm_cvtepu8_epi64(); //expect: RustIntrinsicIssue
        _mm_cvtpd_epi32(); //expect: RustIntrinsicIssue
        _mm_cvtpd_ps(); //expect: RustIntrinsicIssue
        _mm_cvtps_epi32(); //expect: RustIntrinsicIssue
        _mm_cvtps_pd(); //expect: RustIntrinsicIssue
        _mm_cvtsd_f64(); //expect: RustIntrinsicIssue
        _mm_cvtsd_si32(); //expect: RustIntrinsicIssue
        _mm_cvtsd_si64(); //expect: RustIntrinsicIssue
        _mm_cvtsd_si64x(); //expect: RustIntrinsicIssue
        _mm_cvtsd_ss(); //expect: RustIntrinsicIssue
        _mm_cvtsi32_ss(); //expect: RustIntrinsicIssue
        _mm_cvtsi32_sd(); //expect: RustIntrinsicIssue
        _mm_cvtsi64_ss(); //expect: RustIntrinsicIssue
        _mm_cvtsi64_sd(); //expect: RustIntrinsicIssue
        _mm_cvtsi64x_sd(); //expect: RustIntrinsicIssue
        _mm_cvtsi128_si32(); //expect: RustIntrinsicIssue
        _mm_cvtsi128_si64(); //expect: RustIntrinsicIssue
        _mm_cvtsi128_si64x(); //expect: RustIntrinsicIssue
        _mm_cvtsi32_si128(); //expect: RustIntrinsicIssue
        _mm_cvtsi64_si128(); //expect: RustIntrinsicIssue
        _mm_cvtsi64x_si128(); //expect: RustIntrinsicIssue
        _mm_cvtss_f32(); //expect: RustIntrinsicIssue
        _mm_cvtss_sd(); //expect: RustIntrinsicIssue
        _mm_cvtss_si32(); //expect: RustIntrinsicIssue
        _mm_cvtss_si64(); //expect: RustIntrinsicIssue
        _mm_cvtt_ss2si(); //expect: RustIntrinsicIssue
        _mm_cvttpd_epi32(); //expect: RustIntrinsicIssue
        _mm_cvttps_epi32(); //expect: RustIntrinsicIssue
        _mm_cvttsd_si32(); //expect: RustIntrinsicIssue
        _mm_cvttsd_si64(); //expect: RustIntrinsicIssue
        _mm_cvttsd_si64x(); //expect: RustIntrinsicIssue
        _mm_cvttss_si32(); //expect: RustIntrinsicIssue
        _mm_cvttss_si64(); //expect: RustIntrinsicIssue
        _mm_div_pd(); //expect: RustIntrinsicIssue
        _mm_div_ps(); //expect: RustIntrinsicIssue
        _mm_div_sd(); //expect: RustIntrinsicIssue
        _mm_div_ss(); //expect: RustIntrinsicIssue
        _mm_dp_pd(); //expect: RustIntrinsicIssue
        _mm_dp_ps(); //expect: RustIntrinsicIssue
        _mm_extract_epi8(); //expect: RustIntrinsicIssue
        _mm_extract_epi16(); //expect: RustIntrinsicIssue
        _mm_extract_epi32(); //expect: RustIntrinsicIssue
        _mm_extract_epi64(); //expect: RustIntrinsicIssue
        _mm_extract_ps(); //expect: RustIntrinsicIssue
        _mm_extract_si64(); //expect: RustIntrinsicIssue
        _mm_floor_pd(); //expect: RustIntrinsicIssue
        _mm_floor_ps(); //expect: RustIntrinsicIssue
        _mm_floor_sd(); //expect: RustIntrinsicIssue
        _mm_floor_ss(); //expect: RustIntrinsicIssue
        _mm_fmadd_pd(); //expect: RustIntrinsicIssue
        _mm_fmadd_ps(); //expect: RustIntrinsicIssue
        _mm_fmadd_sd(); //expect: RustIntrinsicIssue
        _mm_fmadd_ss(); //expect: RustIntrinsicIssue
        _mm_fmaddsub_pd(); //expect: RustIntrinsicIssue
        _mm_fmaddsub_ps(); //expect: RustIntrinsicIssue
        _mm_fmsub_pd(); //expect: RustIntrinsicIssue
        _mm_fmsub_ps(); //expect: RustIntrinsicIssue
        _mm_fmsub_sd(); //expect: RustIntrinsicIssue
        _mm_fmsub_ss(); //expect: RustIntrinsicIssue
        _mm_fmsubadd_pd(); //expect: RustIntrinsicIssue
        _mm_fmsubadd_ps(); //expect: RustIntrinsicIssue
        _mm_fnmadd_pd(); //expect: RustIntrinsicIssue
        _mm_fnmadd_ps(); //expect: RustIntrinsicIssue
        _mm_fnmadd_sd(); //expect: RustIntrinsicIssue
        _mm_fnmadd_ss(); //expect: RustIntrinsicIssue
        _mm_fnmsub_pd(); //expect: RustIntrinsicIssue
        _mm_fnmsub_ps(); //expect: RustIntrinsicIssue
        _mm_fnmsub_sd(); //expect: RustIntrinsicIssue
        _mm_fnmsub_ss(); //expect: RustIntrinsicIssue
        _mm_getcsr(); //expect: RustIntrinsicIssue
        _mm_hadd_epi16(); //expect: RustIntrinsicIssue
        _mm_hadd_epi32(); //expect: RustIntrinsicIssue
        _mm_hadd_pd(); //expect: RustIntrinsicIssue
        _mm_hadd_ps(); //expect: RustIntrinsicIssue
        _mm_hadds_epi16(); //expect: RustIntrinsicIssue
        _mm_hsub_epi16(); //expect: RustIntrinsicIssue
        _mm_hsub_epi32(); //expect: RustIntrinsicIssue
        _mm_hsub_pd(); //expect: RustIntrinsicIssue
        _mm_hsub_ps(); //expect: RustIntrinsicIssue
        _mm_hsubs_epi16(); //expect: RustIntrinsicIssue
        _mm_i32gather_ps(); //expect: RustIntrinsicIssue
        _mm_i32gather_pd(); //expect: RustIntrinsicIssue
        _mm_i64gather_ps(); //expect: RustIntrinsicIssue
        _mm_i64gather_pd(); //expect: RustIntrinsicIssue
        _mm_i32gather_epi32(); //expect: RustIntrinsicIssue
        _mm_i32gather_epi64(); //expect: RustIntrinsicIssue
        _mm_i64gather_epi32(); //expect: RustIntrinsicIssue
        _mm_i64gather_epi64(); //expect: RustIntrinsicIssue
        _mm_insert_epi8(); //expect: RustIntrinsicIssue
        _mm_insert_epi16(); //expect: RustIntrinsicIssue
        _mm_insert_epi32(); //expect: RustIntrinsicIssue
        _mm_insert_epi64(); //expect: RustIntrinsicIssue
        _mm_insert_ps(); //expect: RustIntrinsicIssue
        _mm_insert_si64(); //expect: RustIntrinsicIssue
        _mm_lddqu_si128(); //expect: RustIntrinsicIssue
        _mm_lfence(); //expect: RustIntrinsicIssue
        _mm_load1_ps(); //expect: RustIntrinsicIssue
        _mm_load1_pd(); //expect: RustIntrinsicIssue
        _mm_load_pd(); //expect: RustIntrinsicIssue
        _mm_load_pd1(); //expect: RustIntrinsicIssue
        _mm_load_ps(); //expect: RustIntrinsicIssue
        _mm_load_ps1(); //expect: RustIntrinsicIssue
        _mm_load_sd(); //expect: RustIntrinsicIssue
        _mm_load_si128(); //expect: RustIntrinsicIssue
        _mm_load_ss(); //expect: RustIntrinsicIssue
        _mm_loaddup_pd(); //expect: RustIntrinsicIssue
        _mm_loadh_pd(); //expect: RustIntrinsicIssue
        _mm_loadl_epi64(); //expect: RustIntrinsicIssue
        _mm_loadl_pd(); //expect: RustIntrinsicIssue
        _mm_loadr_pd(); //expect: RustIntrinsicIssue
        _mm_loadr_ps(); //expect: RustIntrinsicIssue
        _mm_loadu_pd(); //expect: RustIntrinsicIssue
        _mm_loadu_ps(); //expect: RustIntrinsicIssue
        _mm_loadu_si128(); //expect: RustIntrinsicIssue
        _mm_madd_epi16(); //expect: RustIntrinsicIssue
        _mm_maddubs_epi16(); //expect: RustIntrinsicIssue
        _mm_mask_i32gather_ps(); //expect: RustIntrinsicIssue
        _mm_mask_i32gather_pd(); //expect: RustIntrinsicIssue
        _mm_mask_i64gather_ps(); //expect: RustIntrinsicIssue
        _mm_mask_i64gather_pd(); //expect: RustIntrinsicIssue
        _mm_mask_i32gather_epi32(); //expect: RustIntrinsicIssue
        _mm_mask_i32gather_epi64(); //expect: RustIntrinsicIssue
        _mm_mask_i64gather_epi32(); //expect: RustIntrinsicIssue
        _mm_mask_i64gather_epi64(); //expect: RustIntrinsicIssue
        _mm_maskload_epi32(); //expect: RustIntrinsicIssue
        _mm_maskload_epi64(); //expect: RustIntrinsicIssue
        _mm_maskload_pd(); //expect: RustIntrinsicIssue
        _mm_maskload_ps(); //expect: RustIntrinsicIssue
        _mm_maskmoveu_si128(); //expect: RustIntrinsicIssue
        _mm_maskstore_epi32(); //expect: RustIntrinsicIssue
        _mm_maskstore_epi64(); //expect: RustIntrinsicIssue
        _mm_maskstore_pd(); //expect: RustIntrinsicIssue
        _mm_maskstore_ps(); //expect: RustIntrinsicIssue
        _mm_max_epi8(); //expect: RustIntrinsicIssue
        _mm_max_epi16(); //expect: RustIntrinsicIssue
        _mm_max_epi32(); //expect: RustIntrinsicIssue
        _mm_max_epu8(); //expect: RustIntrinsicIssue
        _mm_max_epu16(); //expect: RustIntrinsicIssue
        _mm_max_epu32(); //expect: RustIntrinsicIssue
        _mm_max_pd(); //expect: RustIntrinsicIssue
        _mm_max_ps(); //expect: RustIntrinsicIssue
        _mm_max_sd(); //expect: RustIntrinsicIssue
        _mm_max_ss(); //expect: RustIntrinsicIssue
        _mm_mfence(); //expect: RustIntrinsicIssue
        _mm_min_epi8(); //expect: RustIntrinsicIssue
        _mm_min_epi16(); //expect: RustIntrinsicIssue
        _mm_min_epi32(); //expect: RustIntrinsicIssue
        _mm_min_epu8(); //expect: RustIntrinsicIssue
        _mm_min_epu16(); //expect: RustIntrinsicIssue
        _mm_min_epu32(); //expect: RustIntrinsicIssue
        _mm_min_pd(); //expect: RustIntrinsicIssue
        _mm_min_ps(); //expect: RustIntrinsicIssue
        _mm_min_sd(); //expect: RustIntrinsicIssue
        _mm_min_ss(); //expect: RustIntrinsicIssue
        _mm_minpos_epu16(); //expect: RustIntrinsicIssue
        _mm_move_epi64(); //expect: RustIntrinsicIssue
        _mm_move_sd(); //expect: RustIntrinsicIssue
        _mm_move_ss(); //expect: RustIntrinsicIssue
        _mm_movedup_pd(); //expect: RustIntrinsicIssue
        _mm_movehdup_ps(); //expect: RustIntrinsicIssue
        _mm_movehl_ps(); //expect: RustIntrinsicIssue
        _mm_moveldup_ps(); //expect: RustIntrinsicIssue
        _mm_movelh_ps(); //expect: RustIntrinsicIssue
        _mm_movemask_epi8(); //expect: RustIntrinsicIssue
        _mm_movemask_pd(); //expect: RustIntrinsicIssue
        _mm_movemask_ps(); //expect: RustIntrinsicIssue
        _mm_mpsadbw_epu8(); //expect: RustIntrinsicIssue
        _mm_mul_epi32(); //expect: RustIntrinsicIssue
        _mm_mul_epu32(); //expect: RustIntrinsicIssue
        _mm_mul_pd(); //expect: RustIntrinsicIssue
        _mm_mul_ps(); //expect: RustIntrinsicIssue
        _mm_mul_sd(); //expect: RustIntrinsicIssue
        _mm_mul_ss(); //expect: RustIntrinsicIssue
        _mm_mulhi_epi16(); //expect: RustIntrinsicIssue
        _mm_mulhi_epu16(); //expect: RustIntrinsicIssue
        _mm_mulhrs_epi16(); //expect: RustIntrinsicIssue
        _mm_mullo_epi16(); //expect: RustIntrinsicIssue
        _mm_mullo_epi32(); //expect: RustIntrinsicIssue
        _mm_or_pd(); //expect: RustIntrinsicIssue
        _mm_or_ps(); //expect: RustIntrinsicIssue
        _mm_or_si128(); //expect: RustIntrinsicIssue
        _mm_packs_epi16(); //expect: RustIntrinsicIssue
        _mm_packs_epi32(); //expect: RustIntrinsicIssue
        _mm_packus_epi16(); //expect: RustIntrinsicIssue
        _mm_packus_epi32(); //expect: RustIntrinsicIssue
        _mm_pause(); //expect: RustIntrinsicIssue
        _mm_permute_pd(); //expect: RustIntrinsicIssue
        _mm_permute_ps(); //expect: RustIntrinsicIssue
        _mm_permutevar_pd(); //expect: RustIntrinsicIssue
        _mm_permutevar_ps(); //expect: RustIntrinsicIssue
        _mm_prefetch(); //expect: RustIntrinsicIssue
        _mm_rcp_ps(); //expect: RustIntrinsicIssue
        _mm_rcp_ss(); //expect: RustIntrinsicIssue
        _mm_round_pd(); //expect: RustIntrinsicIssue
        _mm_round_ps(); //expect: RustIntrinsicIssue
        _mm_round_sd(); //expect: RustIntrinsicIssue
        _mm_round_ss(); //expect: RustIntrinsicIssue
        _mm_rsqrt_ps(); //expect: RustIntrinsicIssue
        _mm_rsqrt_ss(); //expect: RustIntrinsicIssue
        _mm_sad_epu8(); //expect: RustIntrinsicIssue
        _mm_set1_ps(); //expect: RustIntrinsicIssue
        _mm_set1_pd(); //expect: RustIntrinsicIssue
        _mm_set1_epi8(); //expect: RustIntrinsicIssue
        _mm_set1_epi16(); //expect: RustIntrinsicIssue
        _mm_set1_epi32(); //expect: RustIntrinsicIssue
        _mm_set1_epi64x(); //expect: RustIntrinsicIssue
        _mm_set_epi8(); //expect: RustIntrinsicIssue
        _mm_set_epi16(); //expect: RustIntrinsicIssue
        _mm_set_epi32(); //expect: RustIntrinsicIssue
        _mm_set_epi64x(); //expect: RustIntrinsicIssue
        _mm_set_pd(); //expect: RustIntrinsicIssue
        _mm_set_pd1(); //expect: RustIntrinsicIssue
        _mm_set_ps(); //expect: RustIntrinsicIssue
        _mm_set_ps1(); //expect: RustIntrinsicIssue
        _mm_set_sd(); //expect: RustIntrinsicIssue
        _mm_set_ss(); //expect: RustIntrinsicIssue
        _mm_setcsr(); //expect: RustIntrinsicIssue
        _mm_setr_epi8(); //expect: RustIntrinsicIssue
        _mm_setr_epi16(); //expect: RustIntrinsicIssue
        _mm_setr_epi32(); //expect: RustIntrinsicIssue
        _mm_setr_pd(); //expect: RustIntrinsicIssue
        _mm_setr_ps(); //expect: RustIntrinsicIssue
        _mm_setzero_pd(); //expect: RustIntrinsicIssue
        _mm_setzero_ps(); //expect: RustIntrinsicIssue
        _mm_setzero_si128(); //expect: RustIntrinsicIssue
        _mm_sfence(); //expect: RustIntrinsicIssue
        _mm_sha1msg1_epu32(); //expect: RustIntrinsicIssue
        _mm_sha1msg2_epu32(); //expect: RustIntrinsicIssue
        _mm_sha1nexte_epu32(); //expect: RustIntrinsicIssue
        _mm_sha1rnds4_epu32(); //expect: RustIntrinsicIssue
        _mm_sha256msg1_epu32(); //expect: RustIntrinsicIssue
        _mm_sha256msg2_epu32(); //expect: RustIntrinsicIssue
        _mm_sha256rnds2_epu32(); //expect: RustIntrinsicIssue
        _mm_shuffle_epi8(); //expect: RustIntrinsicIssue
        _mm_shuffle_epi32(); //expect: RustIntrinsicIssue
        _mm_shuffle_pd(); //expect: RustIntrinsicIssue
        _mm_shuffle_ps(); //expect: RustIntrinsicIssue
        _mm_shufflehi_epi16(); //expect: RustIntrinsicIssue
        _mm_shufflelo_epi16(); //expect: RustIntrinsicIssue
        _mm_sign_epi8(); //expect: RustIntrinsicIssue
        _mm_sign_epi16(); //expect: RustIntrinsicIssue
        _mm_sign_epi32(); //expect: RustIntrinsicIssue
        _mm_sll_epi16(); //expect: RustIntrinsicIssue
        _mm_sll_epi32(); //expect: RustIntrinsicIssue
        _mm_sll_epi64(); //expect: RustIntrinsicIssue
        _mm_slli_epi16(); //expect: RustIntrinsicIssue
        _mm_slli_epi32(); //expect: RustIntrinsicIssue
        _mm_slli_epi64(); //expect: RustIntrinsicIssue
        _mm_slli_si128(); //expect: RustIntrinsicIssue
        _mm_sllv_epi32(); //expect: RustIntrinsicIssue
        _mm_sllv_epi64(); //expect: RustIntrinsicIssue
        _mm_sqrt_pd(); //expect: RustIntrinsicIssue
        _mm_sqrt_ps(); //expect: RustIntrinsicIssue
        _mm_sqrt_sd(); //expect: RustIntrinsicIssue
        _mm_sqrt_ss(); //expect: RustIntrinsicIssue
        _mm_sra_epi16(); //expect: RustIntrinsicIssue
        _mm_sra_epi32(); //expect: RustIntrinsicIssue
        _mm_srai_epi16(); //expect: RustIntrinsicIssue
        _mm_srai_epi32(); //expect: RustIntrinsicIssue
        _mm_srav_epi32(); //expect: RustIntrinsicIssue
        _mm_srl_epi16(); //expect: RustIntrinsicIssue
        _mm_srl_epi32(); //expect: RustIntrinsicIssue
        _mm_srl_epi64(); //expect: RustIntrinsicIssue
        _mm_srli_epi16(); //expect: RustIntrinsicIssue
        _mm_srli_epi32(); //expect: RustIntrinsicIssue
        _mm_srli_epi64(); //expect: RustIntrinsicIssue
        _mm_srli_si128(); //expect: RustIntrinsicIssue
        _mm_srlv_epi32(); //expect: RustIntrinsicIssue
        _mm_srlv_epi64(); //expect: RustIntrinsicIssue
        _mm_store1_ps(); //expect: RustIntrinsicIssue
        _mm_store1_pd(); //expect: RustIntrinsicIssue
        _mm_store_pd(); //expect: RustIntrinsicIssue
        _mm_store_pd1(); //expect: RustIntrinsicIssue
        _mm_store_ps(); //expect: RustIntrinsicIssue
        _mm_store_ps1(); //expect: RustIntrinsicIssue
        _mm_store_sd(); //expect: RustIntrinsicIssue
        _mm_store_si128(); //expect: RustIntrinsicIssue
        _mm_store_ss(); //expect: RustIntrinsicIssue
        _mm_storeh_pd(); //expect: RustIntrinsicIssue
        _mm_storel_epi64(); //expect: RustIntrinsicIssue
        _mm_storel_pd(); //expect: RustIntrinsicIssue
        _mm_storer_pd(); //expect: RustIntrinsicIssue
        _mm_storer_ps(); //expect: RustIntrinsicIssue
        _mm_storeu_pd(); //expect: RustIntrinsicIssue
        _mm_storeu_ps(); //expect: RustIntrinsicIssue
        _mm_storeu_si128(); //expect: RustIntrinsicIssue
        _mm_stream_pd(); //expect: RustIntrinsicIssue
        _mm_stream_ps(); //expect: RustIntrinsicIssue
        _mm_stream_sd(); //expect: RustIntrinsicIssue
        _mm_stream_si32(); //expect: RustIntrinsicIssue
        _mm_stream_si64(); //expect: RustIntrinsicIssue
        _mm_stream_si128(); //expect: RustIntrinsicIssue
        _mm_stream_ss(); //expect: RustIntrinsicIssue
        _mm_sub_epi8(); //expect: RustIntrinsicIssue
        _mm_sub_epi16(); //expect: RustIntrinsicIssue
        _mm_sub_epi32(); //expect: RustIntrinsicIssue
        _mm_sub_epi64(); //expect: RustIntrinsicIssue
        _mm_sub_pd(); //expect: RustIntrinsicIssue
        _mm_sub_ps(); //expect: RustIntrinsicIssue
        _mm_sub_sd(); //expect: RustIntrinsicIssue
        _mm_sub_ss(); //expect: RustIntrinsicIssue
        _mm_subs_epi8(); //expect: RustIntrinsicIssue
        _mm_subs_epi16(); //expect: RustIntrinsicIssue
        _mm_subs_epu8(); //expect: RustIntrinsicIssue
        _mm_subs_epu16(); //expect: RustIntrinsicIssue
        _mm_test_all_ones(); //expect: RustIntrinsicIssue
        _mm_test_all_zeros(); //expect: RustIntrinsicIssue
        _mm_test_mix_ones_zeros(); //expect: RustIntrinsicIssue
        _mm_testc_pd(); //expect: RustIntrinsicIssue
        _mm_testc_ps(); //expect: RustIntrinsicIssue
        _mm_testc_si128(); //expect: RustIntrinsicIssue
        _mm_testnzc_pd(); //expect: RustIntrinsicIssue
        _mm_testnzc_ps(); //expect: RustIntrinsicIssue
        _mm_testnzc_si128(); //expect: RustIntrinsicIssue
        _mm_testz_pd(); //expect: RustIntrinsicIssue
        _mm_testz_ps(); //expect: RustIntrinsicIssue
        _mm_testz_si128(); //expect: RustIntrinsicIssue
        _mm_tzcnt_32(); //expect: RustIntrinsicIssue
        _mm_tzcnt_64(); //expect: RustIntrinsicIssue
        _mm_ucomieq_sd(); //expect: RustIntrinsicIssue
        _mm_ucomieq_ss(); //expect: RustIntrinsicIssue
        _mm_ucomige_sd(); //expect: RustIntrinsicIssue
        _mm_ucomige_ss(); //expect: RustIntrinsicIssue
        _mm_ucomigt_sd(); //expect: RustIntrinsicIssue
        _mm_ucomigt_ss(); //expect: RustIntrinsicIssue
        _mm_ucomile_sd(); //expect: RustIntrinsicIssue
        _mm_ucomile_ss(); //expect: RustIntrinsicIssue
        _mm_ucomilt_sd(); //expect: RustIntrinsicIssue
        _mm_ucomilt_ss(); //expect: RustIntrinsicIssue
        _mm_ucomineq_sd(); //expect: RustIntrinsicIssue
        _mm_ucomineq_ss(); //expect: RustIntrinsicIssue
        _mm_undefined_pd(); //expect: RustIntrinsicIssue
        _mm_undefined_ps(); //expect: RustIntrinsicIssue
        _mm_undefined_si128(); //expect: RustIntrinsicIssue
        _mm_unpackhi_epi8(); //expect: RustIntrinsicIssue
        _mm_unpackhi_epi16(); //expect: RustIntrinsicIssue
        _mm_unpackhi_epi32(); //expect: RustIntrinsicIssue
        _mm_unpackhi_epi64(); //expect: RustIntrinsicIssue
        _mm_unpackhi_pd(); //expect: RustIntrinsicIssue
        _mm_unpackhi_ps(); //expect: RustIntrinsicIssue
        _mm_unpacklo_epi8(); //expect: RustIntrinsicIssue
        _mm_unpacklo_epi16(); //expect: RustIntrinsicIssue
        _mm_unpacklo_epi32(); //expect: RustIntrinsicIssue
        _mm_unpacklo_epi64(); //expect: RustIntrinsicIssue
        _mm_unpacklo_pd(); //expect: RustIntrinsicIssue
        _mm_unpacklo_ps(); //expect: RustIntrinsicIssue
        _mm_xor_pd(); //expect: RustIntrinsicIssue
        _mm_xor_ps(); //expect: RustIntrinsicIssue
        _mm_xor_si128(); //expect: RustIntrinsicIssue
        _mulx_u32(); //expect: RustIntrinsicIssue
        _mulx_u64(); //expect: RustIntrinsicIssue
        _pdep_u32(); //expect: RustIntrinsicIssue
        _pdep_u64(); //expect: RustIntrinsicIssue
        _pext_u32(); //expect: RustIntrinsicIssue
        _pext_u64(); //expect: RustIntrinsicIssue
        _popcnt32(); //expect: RustIntrinsicIssue
        _popcnt64(); //expect: RustIntrinsicIssue
        _rdrand16_step(); //expect: RustIntrinsicIssue
        _rdrand32_step(); //expect: RustIntrinsicIssue
        _rdrand64_step(); //expect: RustIntrinsicIssue
        _rdseed16_step(); //expect: RustIntrinsicIssue
        _rdseed32_step(); //expect: RustIntrinsicIssue
        _rdseed64_step(); //expect: RustIntrinsicIssue
        _rdtsc(); //expect: RustIntrinsicIssue
        _subborrow_u32(); //expect: RustIntrinsicIssue
        _subborrow_u64(); //expect: RustIntrinsicIssue
        _t1mskc_u32(); //expect: RustIntrinsicIssue
        _t1mskc_u64(); //expect: RustIntrinsicIssue
        _tzcnt_u32(); //expect: RustIntrinsicIssue
        _tzcnt_u64(); //expect: RustIntrinsicIssue
        _tzmsk_u32(); //expect: RustIntrinsicIssue
        _tzmsk_u64(); //expect: RustIntrinsicIssue
        _xgetbv(); //expect: RustIntrinsicIssue
        _xrstor(); //expect: RustIntrinsicIssue
        _xrstor64(); //expect: RustIntrinsicIssue
        _xrstors(); //expect: RustIntrinsicIssue
        _xrstors64(); //expect: RustIntrinsicIssue
        _xsave(); //expect: RustIntrinsicIssue
        _xsave64(); //expect: RustIntrinsicIssue
        _xsavec(); //expect: RustIntrinsicIssue
        _xsavec64(); //expect: RustIntrinsicIssue
        _xsaveopt(); //expect: RustIntrinsicIssue
        _xsaveopt64(); //expect: RustIntrinsicIssue
        _xsaves(); //expect: RustIntrinsicIssue
        _xsaves64(); //expect: RustIntrinsicIssue
        _xsetbv(); //expect: RustIntrinsicIssue
        _MM_SHUFFLE(); //expect: RustIntrinsicIssue
        _bittest(); //expect: RustIntrinsicIssue
        _bittest64(); //expect: RustIntrinsicIssue
        _bittestandcomplement(); //expect: RustIntrinsicIssue
        _bittestandcomplement64(); //expect: RustIntrinsicIssue
        _bittestandreset(); //expect: RustIntrinsicIssue
        _bittestandreset64(); //expect: RustIntrinsicIssue
        _bittestandset(); //expect: RustIntrinsicIssue
        _bittestandset64(); //expect: RustIntrinsicIssue
        _m_empty(); //expect: RustIntrinsicIssue
        _m_maskmovq(); //expect: RustIntrinsicIssue
        _m_paddb(); //expect: RustIntrinsicIssue
        _m_paddd(); //expect: RustIntrinsicIssue
        _m_paddsb(); //expect: RustIntrinsicIssue
        _m_paddsw(); //expect: RustIntrinsicIssue
        _m_paddusb(); //expect: RustIntrinsicIssue
        _m_paddusw(); //expect: RustIntrinsicIssue
        _m_paddw(); //expect: RustIntrinsicIssue
        _m_pavgb(); //expect: RustIntrinsicIssue
        _m_pavgw(); //expect: RustIntrinsicIssue
        _m_pextrw(); //expect: RustIntrinsicIssue
        _m_pinsrw(); //expect: RustIntrinsicIssue
        _m_pmaxsw(); //expect: RustIntrinsicIssue
        _m_pmaxub(); //expect: RustIntrinsicIssue
        _m_pminsw(); //expect: RustIntrinsicIssue
        _m_pminub(); //expect: RustIntrinsicIssue
        _m_pmovmskb(); //expect: RustIntrinsicIssue
        _m_pmulhuw(); //expect: RustIntrinsicIssue
        _m_psadbw(); //expect: RustIntrinsicIssue
        _m_pshufw(); //expect: RustIntrinsicIssue
        _m_psubb(); //expect: RustIntrinsicIssue
        _m_psubd(); //expect: RustIntrinsicIssue
        _m_psubsb(); //expect: RustIntrinsicIssue
        _m_psubsw(); //expect: RustIntrinsicIssue
        _m_psubusb(); //expect: RustIntrinsicIssue
        _m_psubusw(); //expect: RustIntrinsicIssue
        _m_psubw(); //expect: RustIntrinsicIssue
        _mm256_madd52hi_epu64(); //expect: RustIntrinsicIssue
        _mm256_madd52lo_epu64(); //expect: RustIntrinsicIssue
        _mm512_abs_epi32(); //expect: RustIntrinsicIssue
        _mm512_madd52hi_epu64(); //expect: RustIntrinsicIssue
        _mm512_madd52lo_epu64(); //expect: RustIntrinsicIssue
        _mm512_mask_abs_epi32(); //expect: RustIntrinsicIssue
        _mm512_maskz_abs_epi32(); //expect: RustIntrinsicIssue
        _mm512_set1_epi64(); //expect: RustIntrinsicIssue
        _mm512_setr_epi32(); //expect: RustIntrinsicIssue
        _mm512_setzero_si512(); //expect: RustIntrinsicIssue
        _mm_abs_pi8(); //expect: RustIntrinsicIssue
        _mm_abs_pi16(); //expect: RustIntrinsicIssue
        _mm_abs_pi32(); //expect: RustIntrinsicIssue
        _mm_add_pi8(); //expect: RustIntrinsicIssue
        _mm_add_pi16(); //expect: RustIntrinsicIssue
        _mm_add_pi32(); //expect: RustIntrinsicIssue
        _mm_add_si64(); //expect: RustIntrinsicIssue
        _mm_adds_pi8(); //expect: RustIntrinsicIssue
        _mm_adds_pi16(); //expect: RustIntrinsicIssue
        _mm_adds_pu8(); //expect: RustIntrinsicIssue
        _mm_adds_pu16(); //expect: RustIntrinsicIssue
        _mm_alignr_pi8(); //expect: RustIntrinsicIssue
        _mm_avg_pu8(); //expect: RustIntrinsicIssue
        _mm_avg_pu16(); //expect: RustIntrinsicIssue
        _mm_cmpgt_pi8(); //expect: RustIntrinsicIssue
        _mm_cmpgt_pi16(); //expect: RustIntrinsicIssue
        _mm_cmpgt_pi32(); //expect: RustIntrinsicIssue
        _mm_cvt_pi2ps(); //expect: RustIntrinsicIssue
        _mm_cvt_ps2pi(); //expect: RustIntrinsicIssue
        _mm_cvtpd_pi32(); //expect: RustIntrinsicIssue
        _mm_cvtpi8_ps(); //expect: RustIntrinsicIssue
        _mm_cvtpi16_ps(); //expect: RustIntrinsicIssue
        _mm_cvtpi32_ps(); //expect: RustIntrinsicIssue
        _mm_cvtpi32_pd(); //expect: RustIntrinsicIssue
        _mm_cvtpi32x2_ps(); //expect: RustIntrinsicIssue
        _mm_cvtps_pi8(); //expect: RustIntrinsicIssue
        _mm_cvtps_pi16(); //expect: RustIntrinsicIssue
        _mm_cvtps_pi32(); //expect: RustIntrinsicIssue
        _mm_cvtpu8_ps(); //expect: RustIntrinsicIssue
        _mm_cvtpu16_ps(); //expect: RustIntrinsicIssue
        _mm_cvtsi32_si64(); //expect: RustIntrinsicIssue
        _mm_cvtsi64_si32(); //expect: RustIntrinsicIssue
        _mm_cvtt_ps2pi(); //expect: RustIntrinsicIssue
        _mm_cvttpd_pi32(); //expect: RustIntrinsicIssue
        _mm_cvttps_pi32(); //expect: RustIntrinsicIssue
        _mm_empty(); //expect: RustIntrinsicIssue
        _mm_extract_pi16(); //expect: RustIntrinsicIssue
        _mm_hadd_pi16(); //expect: RustIntrinsicIssue
        _mm_hadd_pi32(); //expect: RustIntrinsicIssue
        _mm_hadds_pi16(); //expect: RustIntrinsicIssue
        _mm_hsub_pi16(); //expect: RustIntrinsicIssue
        _mm_hsub_pi32(); //expect: RustIntrinsicIssue
        _mm_hsubs_pi16(); //expect: RustIntrinsicIssue
        _mm_insert_pi16(); //expect: RustIntrinsicIssue
        _mm_loadh_pi(); //expect: RustIntrinsicIssue
        _mm_loadl_pi(); //expect: RustIntrinsicIssue
        _mm_madd52hi_epu64(); //expect: RustIntrinsicIssue
        _mm_madd52lo_epu64(); //expect: RustIntrinsicIssue
        _mm_maddubs_pi16(); //expect: RustIntrinsicIssue
        _mm_maskmove_si64(); //expect: RustIntrinsicIssue
        _mm_max_pi16(); //expect: RustIntrinsicIssue
        _mm_max_pu8(); //expect: RustIntrinsicIssue
        _mm_min_pi16(); //expect: RustIntrinsicIssue
        _mm_min_pu8(); //expect: RustIntrinsicIssue
        _mm_movemask_pi8(); //expect: RustIntrinsicIssue
        _mm_movepi64_pi64(); //expect: RustIntrinsicIssue
        _mm_movpi64_epi64(); //expect: RustIntrinsicIssue
        _mm_mul_su32(); //expect: RustIntrinsicIssue
        _mm_mulhi_pu16(); //expect: RustIntrinsicIssue
        _mm_mulhrs_pi16(); //expect: RustIntrinsicIssue
        _mm_mullo_pi16(); //expect: RustIntrinsicIssue
        _mm_packs_pi16(); //expect: RustIntrinsicIssue
        _mm_packs_pi32(); //expect: RustIntrinsicIssue
        _mm_sad_pu8(); //expect: RustIntrinsicIssue
        _mm_set1_epi64(); //expect: RustIntrinsicIssue
        _mm_set1_pi8(); //expect: RustIntrinsicIssue
        _mm_set1_pi16(); //expect: RustIntrinsicIssue
        _mm_set1_pi32(); //expect: RustIntrinsicIssue
        _mm_set_epi64(); //expect: RustIntrinsicIssue
        _mm_set_pi8(); //expect: RustIntrinsicIssue
        _mm_set_pi16(); //expect: RustIntrinsicIssue
        _mm_set_pi32(); //expect: RustIntrinsicIssue
        _mm_setr_epi64(); //expect: RustIntrinsicIssue
        _mm_setr_pi8(); //expect: RustIntrinsicIssue
        _mm_setr_pi16(); //expect: RustIntrinsicIssue
        _mm_setr_pi32(); //expect: RustIntrinsicIssue
        _mm_setzero_si64(); //expect: RustIntrinsicIssue
        _mm_shuffle_pi8(); //expect: RustIntrinsicIssue
        _mm_shuffle_pi16(); //expect: RustIntrinsicIssue
        _mm_sign_pi8(); //expect: RustIntrinsicIssue
        _mm_sign_pi16(); //expect: RustIntrinsicIssue
        _mm_sign_pi32(); //expect: RustIntrinsicIssue
        _mm_storeh_pi(); //expect: RustIntrinsicIssue
        _mm_storel_pi(); //expect: RustIntrinsicIssue
        _mm_stream_pi(); //expect: RustIntrinsicIssue
        _mm_sub_pi8(); //expect: RustIntrinsicIssue
        _mm_sub_pi16(); //expect: RustIntrinsicIssue
        _mm_sub_pi32(); //expect: RustIntrinsicIssue
        _mm_sub_si64(); //expect: RustIntrinsicIssue
        _mm_subs_pi8(); //expect: RustIntrinsicIssue
        _mm_subs_pi16(); //expect: RustIntrinsicIssue
        _mm_subs_pu8(); //expect: RustIntrinsicIssue
        _mm_subs_pu16(); //expect: RustIntrinsicIssue
        _mm_unpackhi_pi8(); //expect: RustIntrinsicIssue
        _mm_unpackhi_pi16(); //expect: RustIntrinsicIssue
        _mm_unpackhi_pi32(); //expect: RustIntrinsicIssue
        _mm_unpacklo_pi8(); //expect: RustIntrinsicIssue
        _mm_unpacklo_pi16(); //expect: RustIntrinsicIssue
        _mm_unpacklo_pi32(); //expect: RustIntrinsicIssue
        cmpxchg16b(); //expect: RustIntrinsicIssue
        has_cpuid(); //expect: RustIntrinsicIssue
        ud2(); //expect: RustIntrinsicIssue
    }
}





