// x86平台下实现
#[cfg(all(any(target_arch = "aarch64"), target_feature = "neon"))]
fn add()
{
    use std::arch::aarch64::*;
    unsafe {
        __breakpoint(); //expect: RustIntrinsicIssue
        __crc32b(); //expect: RustIntrinsicIssue
        __crc32h(); //expect: RustIntrinsicIssue
        __crc32w(); //expect: RustIntrinsicIssue
        __crc32d(); //expect: RustIntrinsicIssue
        __crc32cb(); //expect: RustIntrinsicIssue
        __crc32ch(); //expect: RustIntrinsicIssue
        __crc32cw(); //expect: RustIntrinsicIssue
        __crc32cd(); //expect: RustIntrinsicIssue
        __dmb(); //expect: RustIntrinsicIssue
        __dsb(); //expect: RustIntrinsicIssue
        __isb(); //expect: RustIntrinsicIssue
        __nop(); //expect: RustIntrinsicIssue
        __rsr(); //expect: RustIntrinsicIssue
        __rsrp(); //expect: RustIntrinsicIssue
        __wsr(); //expect: RustIntrinsicIssue
        __wsrp(); //expect: RustIntrinsicIssue
        _cls_u32(); //expect: RustIntrinsicIssue
        _cls_u64(); //expect: RustIntrinsicIssue
        _clz_u64(); //expect: RustIntrinsicIssue
        _rbit_u64(); //expect: RustIntrinsicIssue
        _rev_u16(); //expect: RustIntrinsicIssue
        _rev_u32(); //expect: RustIntrinsicIssue
        _rev_u64(); //expect: RustIntrinsicIssue
        brk(); //expect: RustIntrinsicIssue
        vadd_f32(); //expect: RustIntrinsicIssue
        vadd_f64(); //expect: RustIntrinsicIssue
        vadd_s8(); //expect: RustIntrinsicIssue
        vadd_s16(); //expect: RustIntrinsicIssue
        vadd_s32(); //expect: RustIntrinsicIssue
        vadd_u8(); //expect: RustIntrinsicIssue
        vadd_u16(); //expect: RustIntrinsicIssue
        vadd_u32(); //expect: RustIntrinsicIssue
        vaddd_s64(); //expect: RustIntrinsicIssue
        vaddd_u64(); //expect: RustIntrinsicIssue
        vaddl_s8(); //expect: RustIntrinsicIssue
        vaddl_s16(); //expect: RustIntrinsicIssue
        vaddl_s32(); //expect: RustIntrinsicIssue
        vaddl_u8(); //expect: RustIntrinsicIssue
        vaddl_u16(); //expect: RustIntrinsicIssue
        vaddl_u32(); //expect: RustIntrinsicIssue
        vaddq_f32(); //expect: RustIntrinsicIssue
        vaddq_f64(); //expect: RustIntrinsicIssue
        vaddq_s8(); //expect: RustIntrinsicIssue
        vaddq_s16(); //expect: RustIntrinsicIssue
        vaddq_s32(); //expect: RustIntrinsicIssue
        vaddq_s64(); //expect: RustIntrinsicIssue
        vaddq_u8(); //expect: RustIntrinsicIssue
        vaddq_u16(); //expect: RustIntrinsicIssue
        vaddq_u32(); //expect: RustIntrinsicIssue
        vaddq_u64(); //expect: RustIntrinsicIssue
        vaesdq_u8(); //expect: RustIntrinsicIssue
        vaeseq_u8(); //expect: RustIntrinsicIssue
        vaesimcq_u8(); //expect: RustIntrinsicIssue
        vaesmcq_u8(); //expect: RustIntrinsicIssue
        vcombine_f32(); //expect: RustIntrinsicIssue
        vcombine_f64(); //expect: RustIntrinsicIssue
        vcombine_p8(); //expect: RustIntrinsicIssue
        vcombine_p16(); //expect: RustIntrinsicIssue
        vcombine_p64(); //expect: RustIntrinsicIssue
        vcombine_s8(); //expect: RustIntrinsicIssue
        vcombine_s16(); //expect: RustIntrinsicIssue
        vcombine_s32(); //expect: RustIntrinsicIssue
        vcombine_s64(); //expect: RustIntrinsicIssue
        vcombine_u8(); //expect: RustIntrinsicIssue
        vcombine_u16(); //expect: RustIntrinsicIssue
        vcombine_u32(); //expect: RustIntrinsicIssue
        vcombine_u64(); //expect: RustIntrinsicIssue
        vmaxv_f32(); //expect: RustIntrinsicIssue
        vmaxv_s8(); //expect: RustIntrinsicIssue
        vmaxv_s16(); //expect: RustIntrinsicIssue
        vmaxv_s32(); //expect: RustIntrinsicIssue
        vmaxv_u8(); //expect: RustIntrinsicIssue
        vmaxv_u16(); //expect: RustIntrinsicIssue
        vmaxv_u32(); //expect: RustIntrinsicIssue
        vmaxvq_f32(); //expect: RustIntrinsicIssue
        vmaxvq_f64(); //expect: RustIntrinsicIssue
        vmaxvq_s8(); //expect: RustIntrinsicIssue
        vmaxvq_s16(); //expect: RustIntrinsicIssue
        vmaxvq_s32(); //expect: RustIntrinsicIssue
        vmaxvq_u8(); //expect: RustIntrinsicIssue
        vmaxvq_u16(); //expect: RustIntrinsicIssue
        vmaxvq_u32(); //expect: RustIntrinsicIssue
        vminv_f32(); //expect: RustIntrinsicIssue
        vminv_s8(); //expect: RustIntrinsicIssue
        vminv_s16(); //expect: RustIntrinsicIssue
        vminv_s32(); //expect: RustIntrinsicIssue
        vminv_u8(); //expect: RustIntrinsicIssue
        vminv_u16(); //expect: RustIntrinsicIssue
        vminv_u32(); //expect: RustIntrinsicIssue
        vminvq_f32(); //expect: RustIntrinsicIssue
        vminvq_f64(); //expect: RustIntrinsicIssue
        vminvq_s8(); //expect: RustIntrinsicIssue
        vminvq_s16(); //expect: RustIntrinsicIssue
        vminvq_s32(); //expect: RustIntrinsicIssue
        vminvq_u8(); //expect: RustIntrinsicIssue
        vminvq_u16(); //expect: RustIntrinsicIssue
        vminvq_u32(); //expect: RustIntrinsicIssue
        vmovl_s8(); //expect: RustIntrinsicIssue
        vmovl_s16(); //expect: RustIntrinsicIssue
        vmovl_s32(); //expect: RustIntrinsicIssue
        vmovl_u8(); //expect: RustIntrinsicIssue
        vmovl_u16(); //expect: RustIntrinsicIssue
        vmovl_u32(); //expect: RustIntrinsicIssue
        vmovn_s16(); //expect: RustIntrinsicIssue
        vmovn_s32(); //expect: RustIntrinsicIssue
        vmovn_s64(); //expect: RustIntrinsicIssue
        vmovn_u16(); //expect: RustIntrinsicIssue
        vmovn_u32(); //expect: RustIntrinsicIssue
        vmovn_u64(); //expect: RustIntrinsicIssue
        vpmax_f32(); //expect: RustIntrinsicIssue
        vpmax_s8(); //expect: RustIntrinsicIssue
        vpmax_s16(); //expect: RustIntrinsicIssue
        vpmax_s32(); //expect: RustIntrinsicIssue
        vpmax_u8(); //expect: RustIntrinsicIssue
        vpmax_u16(); //expect: RustIntrinsicIssue
        vpmax_u32(); //expect: RustIntrinsicIssue
        vpmaxq_f32(); //expect: RustIntrinsicIssue
        vpmaxq_f64(); //expect: RustIntrinsicIssue
        vpmaxq_s8(); //expect: RustIntrinsicIssue
        vpmaxq_s16(); //expect: RustIntrinsicIssue
        vpmaxq_s32(); //expect: RustIntrinsicIssue
        vpmaxq_u8(); //expect: RustIntrinsicIssue
        vpmaxq_u16(); //expect: RustIntrinsicIssue
        vpmaxq_u32(); //expect: RustIntrinsicIssue
        vpmin_f32(); //expect: RustIntrinsicIssue
        vpmin_s8(); //expect: RustIntrinsicIssue
        vpmin_s16(); //expect: RustIntrinsicIssue
        vpmin_s32(); //expect: RustIntrinsicIssue
        vpmin_u8(); //expect: RustIntrinsicIssue
        vpmin_u16(); //expect: RustIntrinsicIssue
        vpmin_u32(); //expect: RustIntrinsicIssue
        vpminq_f32(); //expect: RustIntrinsicIssue
        vpminq_f64(); //expect: RustIntrinsicIssue
        vpminq_s8(); //expect: RustIntrinsicIssue
        vpminq_s16(); //expect: RustIntrinsicIssue
        vpminq_s32(); //expect: RustIntrinsicIssue
        vpminq_u8(); //expect: RustIntrinsicIssue
        vpminq_u16(); //expect: RustIntrinsicIssue
        vpminq_u32(); //expect: RustIntrinsicIssue
        vqtbl1_p8(); //expect: RustIntrinsicIssue
        vqtbl1_s8(); //expect: RustIntrinsicIssue
        vqtbl1_u8(); //expect: RustIntrinsicIssue
        vqtbl1q_p8(); //expect: RustIntrinsicIssue
        vqtbl1q_s8(); //expect: RustIntrinsicIssue
        vqtbl1q_u8(); //expect: RustIntrinsicIssue
        vqtbl2_p8(); //expect: RustIntrinsicIssue
        vqtbl2_s8(); //expect: RustIntrinsicIssue
        vqtbl2_u8(); //expect: RustIntrinsicIssue
        vqtbl2q_p8(); //expect: RustIntrinsicIssue
        vqtbl2q_s8(); //expect: RustIntrinsicIssue
        vqtbl2q_u8(); //expect: RustIntrinsicIssue
        vqtbl3_p8(); //expect: RustIntrinsicIssue
        vqtbl3_s8(); //expect: RustIntrinsicIssue
        vqtbl3_u8(); //expect: RustIntrinsicIssue
        vqtbl3q_p8(); //expect: RustIntrinsicIssue
        vqtbl3q_s8(); //expect: RustIntrinsicIssue
        vqtbl3q_u8(); //expect: RustIntrinsicIssue
        vqtbl4_p8(); //expect: RustIntrinsicIssue
        vqtbl4_s8(); //expect: RustIntrinsicIssue
        vqtbl4_u8(); //expect: RustIntrinsicIssue
        vqtbl4q_p8(); //expect: RustIntrinsicIssue
        vqtbl4q_s8(); //expect: RustIntrinsicIssue
        vqtbl4q_u8(); //expect: RustIntrinsicIssue
        vqtbx1_p8(); //expect: RustIntrinsicIssue
        vqtbx1_s8(); //expect: RustIntrinsicIssue
        vqtbx1_u8(); //expect: RustIntrinsicIssue
        vqtbx1q_p8(); //expect: RustIntrinsicIssue
        vqtbx1q_s8(); //expect: RustIntrinsicIssue
        vqtbx1q_u8(); //expect: RustIntrinsicIssue
        vqtbx2_p8(); //expect: RustIntrinsicIssue
        vqtbx2_s8(); //expect: RustIntrinsicIssue
        vqtbx2_u8(); //expect: RustIntrinsicIssue
        vqtbx2q_p8(); //expect: RustIntrinsicIssue
        vqtbx2q_s8(); //expect: RustIntrinsicIssue
        vqtbx2q_u8(); //expect: RustIntrinsicIssue
        vqtbx3_p8(); //expect: RustIntrinsicIssue
        vqtbx3_s8(); //expect: RustIntrinsicIssue
        vqtbx3_u8(); //expect: RustIntrinsicIssue
        vqtbx3q_p8(); //expect: RustIntrinsicIssue
        vqtbx3q_s8(); //expect: RustIntrinsicIssue
        vqtbx3q_u8(); //expect: RustIntrinsicIssue
        vqtbx4_p8(); //expect: RustIntrinsicIssue
        vqtbx4_s8(); //expect: RustIntrinsicIssue
        vqtbx4_u8(); //expect: RustIntrinsicIssue
        vqtbx4q_p8(); //expect: RustIntrinsicIssue
        vqtbx4q_s8(); //expect: RustIntrinsicIssue
        vqtbx4q_u8(); //expect: RustIntrinsicIssue
        vrsqrte_f32(); //expect: RustIntrinsicIssue
        vsha1cq_u32(); //expect: RustIntrinsicIssue
        vsha1h_u32(); //expect: RustIntrinsicIssue
        vsha1mq_u32(); //expect: RustIntrinsicIssue
        vsha1pq_u32(); //expect: RustIntrinsicIssue
        vsha1su0q_u32(); //expect: RustIntrinsicIssue
        vsha1su1q_u32(); //expect: RustIntrinsicIssue
        vsha256h2q_u32(); //expect: RustIntrinsicIssue
        vsha256hq_u32(); //expect: RustIntrinsicIssue
        vsha256su0q_u32(); //expect: RustIntrinsicIssue
        vsha256su1q_u32(); //expect: RustIntrinsicIssue
        vtbl1_p8(); //expect: RustIntrinsicIssue
        vtbl1_s8(); //expect: RustIntrinsicIssue
        vtbl1_u8(); //expect: RustIntrinsicIssue
        vtbl2_p8(); //expect: RustIntrinsicIssue
        vtbl2_s8(); //expect: RustIntrinsicIssue
        vtbl2_u8(); //expect: RustIntrinsicIssue
        vtbl3_p8(); //expect: RustIntrinsicIssue
        vtbl3_s8(); //expect: RustIntrinsicIssue
        vtbl3_u8(); //expect: RustIntrinsicIssue
        vtbl4_p8(); //expect: RustIntrinsicIssue
        vtbl4_s8(); //expect: RustIntrinsicIssue
        vtbl4_u8(); //expect: RustIntrinsicIssue
        vtbx1_p8(); //expect: RustIntrinsicIssue
        vtbx1_s8(); //expect: RustIntrinsicIssue
        vtbx1_u8(); //expect: RustIntrinsicIssue
        vtbx2_p8(); //expect: RustIntrinsicIssue
        vtbx2_s8(); //expect: RustIntrinsicIssue
        vtbx2_u8(); //expect: RustIntrinsicIssue
        vtbx3_p8(); //expect: RustIntrinsicIssue
        vtbx3_s8(); //expect: RustIntrinsicIssue
        vtbx3_u8(); //expect: RustIntrinsicIssue
        vtbx4_p8(); //expect: RustIntrinsicIssue
        vtbx4_s8(); //expect: RustIntrinsicIssue
        vtbx4_u8(); //expect: RustIntrinsicIssue
    }
}




