from cffi import FFI
ffi = FFI()
# ffi.cdef is a method in Python's CFFI (C Foreign Function Interface) library
# used to define C types, functions, constants, and global variables.
# It allows you to call C code from Python.
# aarch64 intinsics:
ffi.cdef("""
    unsigned int __builtin_aarch64_get_fpcr ();
    void __builtin_aarch64_set_fpcr (unsigned int);
    unsigned int __builtin_aarch64_get_fpsr ();
    void __builtin_aarch64_set_fpsr (unsigned int);
    unsigned long long __builtin_aarch64_get_fpcr64 ();
    void __builtin_aarch64_set_fpcr64 (unsigned long long);
    unsigned long long __builtin_aarch64_get_fpsr64 ();
    void __builtin_aarch64_set_fpsr64 (unsigned long long);
    int __builtin_arm_getwcgr0 (void);
    void __builtin_arm_setwcgr0 (int);
    int __builtin_arm_getwcgr1 (void);
    void __builtin_arm_setwcgr1 (int);
    int __builtin_arm_getwcgr2 (void);
    void __builtin_arm_setwcgr2 (int);
    int __builtin_arm_getwcgr3 (void);
    void __builtin_arm_setwcgr3 (int);
    int __builtin_arm_textrmsb (v8qi, int);
    int __builtin_arm_textrmsh (v4hi, int);
    int __builtin_arm_textrmsw (v2si, int);
    int __builtin_arm_textrmub (v8qi, int);
    int __builtin_arm_textrmuh (v4hi, int);
    int __builtin_arm_textrmuw (v2si, int);
    v8qi __builtin_arm_tinsrb (v8qi, int, int);
    v4hi __builtin_arm_tinsrh (v4hi, int, int);
    v2si __builtin_arm_tinsrw (v2si, int, int);
    long long __builtin_arm_tmia (long long, int, int);
    long long __builtin_arm_tmiabb (long long, int, int);
    long long __builtin_arm_tmiabt (long long, int, int);
    long long __builtin_arm_tmiaph (long long, int, int);
    long long __builtin_arm_tmiatb (long long, int, int);
    long long __builtin_arm_tmiatt (long long, int, int);
    int __builtin_arm_tmovmskb (v8qi);
    int __builtin_arm_tmovmskh (v4hi);
    int __builtin_arm_tmovmskw (v2si);
    long long __builtin_arm_waccb (v8qi);
    long long __builtin_arm_wacch (v4hi);
    long long __builtin_arm_waccw (v2si);
    v8qi __builtin_arm_waddb (v8qi, v8qi);
    v8qi __builtin_arm_waddbss (v8qi, v8qi);
    v8qi __builtin_arm_waddbus (v8qi, v8qi);
    v4hi __builtin_arm_waddh (v4hi, v4hi);
    v4hi __builtin_arm_waddhss (v4hi, v4hi);
    v4hi __builtin_arm_waddhus (v4hi, v4hi);
    v2si __builtin_arm_waddw (v2si, v2si);
    v2si __builtin_arm_waddwss (v2si, v2si);
    v2si __builtin_arm_waddwus (v2si, v2si);
    v8qi __builtin_arm_walign (v8qi, v8qi, int);
    long long __builtin_arm_wand(long long, long long);
    long long __builtin_arm_wandn (long long, long long);
    v8qi __builtin_arm_wavg2b (v8qi, v8qi);
    v8qi __builtin_arm_wavg2br (v8qi, v8qi);
    v4hi __builtin_arm_wavg2h (v4hi, v4hi);
    v4hi __builtin_arm_wavg2hr (v4hi, v4hi);
    v8qi __builtin_arm_wcmpeqb (v8qi, v8qi);
    v4hi __builtin_arm_wcmpeqh (v4hi, v4hi);
    v2si __builtin_arm_wcmpeqw (v2si, v2si);
    v8qi __builtin_arm_wcmpgtsb (v8qi, v8qi);
    v4hi __builtin_arm_wcmpgtsh (v4hi, v4hi);
    v2si __builtin_arm_wcmpgtsw (v2si, v2si);
    v8qi __builtin_arm_wcmpgtub (v8qi, v8qi);
    v4hi __builtin_arm_wcmpgtuh (v4hi, v4hi);
    v2si __builtin_arm_wcmpgtuw (v2si, v2si);
    long long __builtin_arm_wmacs (long long, v4hi, v4hi);
    long long __builtin_arm_wmacsz (v4hi, v4hi);
    long long __builtin_arm_wmacu (long long, v4hi, v4hi);
    long long __builtin_arm_wmacuz (v4hi, v4hi);
    v4hi __builtin_arm_wmadds (v4hi, v4hi);
    v4hi __builtin_arm_wmaddu (v4hi, v4hi);
    v8qi __builtin_arm_wmaxsb (v8qi, v8qi);
    v4hi __builtin_arm_wmaxsh (v4hi, v4hi);
    v2si __builtin_arm_wmaxsw (v2si, v2si);
    v8qi __builtin_arm_wmaxub (v8qi, v8qi);
    v4hi __builtin_arm_wmaxuh (v4hi, v4hi);
    v2si __builtin_arm_wmaxuw (v2si, v2si);
    v8qi __builtin_arm_wminsb (v8qi, v8qi);
    v4hi __builtin_arm_wminsh (v4hi, v4hi);
    v2si __builtin_arm_wminsw (v2si, v2si);
    v8qi __builtin_arm_wminub (v8qi, v8qi);
    v4hi __builtin_arm_wminuh (v4hi, v4hi);
    v2si __builtin_arm_wminuw (v2si, v2si);
    v4hi __builtin_arm_wmulsm (v4hi, v4hi);
    v4hi __builtin_arm_wmulul (v4hi, v4hi);
    v4hi __builtin_arm_wmulum (v4hi, v4hi);
    long long __builtin_arm_wor (long long, long long);
    v2si __builtin_arm_wpackdss (long long, long long);
    v2si __builtin_arm_wpackdus (long long, long long);
    v8qi __builtin_arm_wpackhss (v4hi, v4hi);
    v8qi __builtin_arm_wpackhus (v4hi, v4hi);
    v4hi __builtin_arm_wpackwss (v2si, v2si);
    v4hi __builtin_arm_wpackwus (v2si, v2si);
    long long __builtin_arm_wrord (long long, long long);
    long long __builtin_arm_wrordi (long long, int);
    v4hi __builtin_arm_wrorh (v4hi, long long);
    v4hi __builtin_arm_wrorhi (v4hi, int);
    v2si __builtin_arm_wrorw (v2si, long long);
    v2si __builtin_arm_wrorwi (v2si, int);
    v2si __builtin_arm_wsadb (v2si, v8qi, v8qi);
    v2si __builtin_arm_wsadbz (v8qi, v8qi);
    v2si __builtin_arm_wsadh (v2si, v4hi, v4hi);
    v2si __builtin_arm_wsadhz (v4hi, v4hi);
    v4hi __builtin_arm_wshufh (v4hi, int);
    long long __builtin_arm_wslld (long long, long long);
    long long __builtin_arm_wslldi (long long, int);
    v4hi __builtin_arm_wsllh (v4hi, long long);
    v4hi __builtin_arm_wsllhi (v4hi, int);
    v2si __builtin_arm_wsllw (v2si, long long);
    v2si __builtin_arm_wsllwi (v2si, int);
    long long __builtin_arm_wsrad (long long, long long);
    long long __builtin_arm_wsradi (long long, int);
    v4hi __builtin_arm_wsrah (v4hi, long long);
    v4hi __builtin_arm_wsrahi (v4hi, int);
    v2si __builtin_arm_wsraw (v2si, long long);
    v2si __builtin_arm_wsrawi (v2si, int);
    long long __builtin_arm_wsrld (long long, long long);
    long long __builtin_arm_wsrldi (long long, int);
    v4hi __builtin_arm_wsrlh (v4hi, long long);
    v4hi __builtin_arm_wsrlhi (v4hi, int);
    v2si __builtin_arm_wsrlw (v2si, long long);
    v2si __builtin_arm_wsrlwi (v2si, int);
    v8qi __builtin_arm_wsubb (v8qi, v8qi);
    v8qi __builtin_arm_wsubbss (v8qi, v8qi);
    v8qi __builtin_arm_wsubbus (v8qi, v8qi);
    v4hi __builtin_arm_wsubh (v4hi, v4hi);
    v4hi __builtin_arm_wsubhss (v4hi, v4hi);
    v4hi __builtin_arm_wsubhus (v4hi, v4hi);
    v2si __builtin_arm_wsubw (v2si, v2si);
    v2si __builtin_arm_wsubwss (v2si, v2si);
    v2si __builtin_arm_wsubwus (v2si, v2si);
    v4hi __builtin_arm_wunpckehsb (v8qi);
    v2si __builtin_arm_wunpckehsh (v4hi);
    long long __builtin_arm_wunpckehsw (v2si);
    v4hi __builtin_arm_wunpckehub (v8qi);
    v2si __builtin_arm_wunpckehuh (v4hi);
    long long __builtin_arm_wunpckehuw (v2si);
    v4hi __builtin_arm_wunpckelsb (v8qi);
    v2si __builtin_arm_wunpckelsh (v4hi);
    long long __builtin_arm_wunpckelsw (v2si);
    v4hi __builtin_arm_wunpckelub (v8qi);
    v2si __builtin_arm_wunpckeluh (v4hi);
    long long __builtin_arm_wunpckeluw (v2si);
    v8qi __builtin_arm_wunpckihb (v8qi, v8qi);
    v4hi __builtin_arm_wunpckihh (v4hi, v4hi);
    v2si __builtin_arm_wunpckihw (v2si, v2si);
    v8qi __builtin_arm_wunpckilb (v8qi, v8qi);
    v4hi __builtin_arm_wunpckilh (v4hi, v4hi);
    v2si __builtin_arm_wunpckilw (v2si, v2si);
    long long __builtin_arm_wxor (long long, long long);
    long long __builtin_arm_wzero ();
    uint32x2_t vadd_u32 (uint32x2_t, uint32x2_t);
    help: |+
        built-in intrinsics for the ARM Advanced SIMD extension are available when the -mfpu=neon switch is used
    uint16x4_t vadd_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vadd_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vadd_s32 (int32x2_t, int32x2_t);
    int16x4_t vadd_s16 (int16x4_t, int16x4_t);
    int8x8_t vadd_s8 (int8x8_t, int8x8_t);
    float32x2_t vadd_f32 (float32x2_t, float32x2_t);
    uint64x1_t vadd_u64 (uint64x1_t, uint64x1_t);
    int64x1_t vadd_s64 (int64x1_t, int64x1_t);
    uint32x4_t vaddq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vaddq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vaddq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vaddq_s32 (int32x4_t, int32x4_t);
    int16x8_t vaddq_s16 (int16x8_t, int16x8_t);
    int8x16_t vaddq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vaddq_u64 (uint64x2_t, uint64x2_t);
    int64x2_t vaddq_s64 (int64x2_t, int64x2_t);
    float32x4_t vaddq_f32 (float32x4_t, float32x4_t);
    uint64x2_t vaddl_u32 (uint32x2_t, uint32x2_t);
    uint32x4_t vaddl_u16 (uint16x4_t, uint16x4_t);
    uint16x8_t vaddl_u8 (uint8x8_t, uint8x8_t);
    int64x2_t vaddl_s32 (int32x2_t, int32x2_t);
    int32x4_t vaddl_s16 (int16x4_t, int16x4_t);
    int16x8_t vaddl_s8 (int8x8_t, int8x8_t);
    uint64x2_t vaddw_u32 (uint64x2_t, uint32x2_t);
    uint32x4_t vaddw_u16 (uint32x4_t, uint16x4_t);
    uint16x8_t vaddw_u8 (uint16x8_t, uint8x8_t);
    int64x2_t vaddw_s32 (int64x2_t, int32x2_t);
    int32x4_t vaddw_s16 (int32x4_t, int16x4_t);
    int16x8_t vaddw_s8 (int16x8_t, int8x8_t);
    uint32x2_t vhadd_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vhadd_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vhadd_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vhadd_s32 (int32x2_t, int32x2_t);
    int16x4_t vhadd_s16 (int16x4_t, int16x4_t);
    int8x8_t vhadd_s8 (int8x8_t, int8x8_t);
    uint32x4_t vhaddq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vhaddq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vhaddq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vhaddq_s32 (int32x4_t, int32x4_t);
    int16x8_t vhaddq_s16 (int16x8_t, int16x8_t);
    int8x16_t vhaddq_s8 (int8x16_t, int8x16_t);
    uint32x2_t vrhadd_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vrhadd_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vrhadd_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vrhadd_s32 (int32x2_t, int32x2_t);
    int16x4_t vrhadd_s16 (int16x4_t, int16x4_t);
    int8x8_t vrhadd_s8 (int8x8_t, int8x8_t);
    uint32x4_t vrhaddq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vrhaddq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vrhaddq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vrhaddq_s32 (int32x4_t, int32x4_t);
    int16x8_t vrhaddq_s16 (int16x8_t, int16x8_t);
    int8x16_t vrhaddq_s8 (int8x16_t, int8x16_t);
    uint32x2_t vqadd_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vqadd_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vqadd_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vqadd_s32 (int32x2_t, int32x2_t);
    int16x4_t vqadd_s16 (int16x4_t, int16x4_t);
    int8x8_t vqadd_s8 (int8x8_t, int8x8_t);
    uint64x1_t vqadd_u64 (uint64x1_t, uint64x1_t);
    int64x1_t vqadd_s64 (int64x1_t, int64x1_t);
    uint32x4_t vqaddq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vqaddq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vqaddq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vqaddq_s32 (int32x4_t, int32x4_t);
    int16x8_t vqaddq_s16 (int16x8_t, int16x8_t);
    int8x16_t vqaddq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vqaddq_u64 (uint64x2_t, uint64x2_t);
    int64x2_t vqaddq_s64 (int64x2_t, int64x2_t);
    uint32x2_t vaddhn_u64 (uint64x2_t, uint64x2_t);
    uint16x4_t vaddhn_u32 (uint32x4_t, uint32x4_t);
    uint8x8_t vaddhn_u16 (uint16x8_t, uint16x8_t);
    int32x2_t vaddhn_s64 (int64x2_t, int64x2_t);
    int16x4_t vaddhn_s32 (int32x4_t, int32x4_t);
    int8x8_t vaddhn_s16 (int16x8_t, int16x8_t);
    uint32x2_t vraddhn_u64 (uint64x2_t, uint64x2_t);
    uint16x4_t vraddhn_u32 (uint32x4_t, uint32x4_t);
    uint8x8_t vraddhn_u16 (uint16x8_t, uint16x8_t);
    int32x2_t vraddhn_s64 (int64x2_t, int64x2_t);
    int16x4_t vraddhn_s32 (int32x4_t, int32x4_t);
    int8x8_t vraddhn_s16 (int16x8_t, int16x8_t);
    uint32x2_t vmul_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vmul_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vmul_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vmul_s32 (int32x2_t, int32x2_t);
    int16x4_t vmul_s16 (int16x4_t, int16x4_t);
    int8x8_t vmul_s8 (int8x8_t, int8x8_t);
    float32x2_t vmul_f32 (float32x2_t, float32x2_t);
    poly8x8_t vmul_p8 (poly8x8_t, poly8x8_t);
    uint32x4_t vmulq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vmulq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vmulq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vmulq_s32 (int32x4_t, int32x4_t);
    int16x8_t vmulq_s16 (int16x8_t, int16x8_t);
    int8x16_t vmulq_s8 (int8x16_t, int8x16_t);
    float32x4_t vmulq_f32 (float32x4_t, float32x4_t);
    poly8x16_t vmulq_p8 (poly8x16_t, poly8x16_t);
    int32x2_t vqdmulh_s32 (int32x2_t, int32x2_t);
    int16x4_t vqdmulh_s16 (int16x4_t, int16x4_t);
    int32x4_t vqdmulhq_s32 (int32x4_t, int32x4_t);
    int16x8_t vqdmulhq_s16 (int16x8_t, int16x8_t);
    int32x2_t vqrdmulh_s32 (int32x2_t, int32x2_t);
    int16x4_t vqrdmulh_s16 (int16x4_t, int16x4_t);
    int32x4_t vqrdmulhq_s32 (int32x4_t, int32x4_t);
    int16x8_t vqrdmulhq_s16 (int16x8_t, int16x8_t);
    uint64x2_t vmull_u32 (uint32x2_t, uint32x2_t);
    uint32x4_t vmull_u16 (uint16x4_t, uint16x4_t);
    uint16x8_t vmull_u8 (uint8x8_t, uint8x8_t);
    int64x2_t vmull_s32 (int32x2_t, int32x2_t);
    int32x4_t vmull_s16 (int16x4_t, int16x4_t);
    int16x8_t vmull_s8 (int8x8_t, int8x8_t);
    poly16x8_t vmull_p8 (poly8x8_t, poly8x8_t);
    int64x2_t vqdmull_s32 (int32x2_t, int32x2_t);
    int32x4_t vqdmull_s16 (int16x4_t, int16x4_t);
    uint32x2_t vmla_u32 (uint32x2_t, uint32x2_t, uint32x2_t);
    uint16x4_t vmla_u16 (uint16x4_t, uint16x4_t, uint16x4_t);
    uint8x8_t vmla_u8 (uint8x8_t, uint8x8_t, uint8x8_t);
    int32x2_t vmla_s32 (int32x2_t, int32x2_t, int32x2_t);
    int16x4_t vmla_s16 (int16x4_t, int16x4_t, int16x4_t);
    int8x8_t vmla_s8 (int8x8_t, int8x8_t, int8x8_t);
    float32x2_t vmla_f32 (float32x2_t, float32x2_t, float32x2_t);
    uint32x4_t vmlaq_u32 (uint32x4_t, uint32x4_t, uint32x4_t);
    uint16x8_t vmlaq_u16 (uint16x8_t, uint16x8_t, uint16x8_t);
    uint8x16_t vmlaq_u8 (uint8x16_t, uint8x16_t, uint8x16_t);
    int32x4_t vmlaq_s32 (int32x4_t, int32x4_t, int32x4_t);
    int16x8_t vmlaq_s16 (int16x8_t, int16x8_t, int16x8_t);
    int8x16_t vmlaq_s8 (int8x16_t, int8x16_t, int8x16_t);
    float32x4_t vmlaq_f32 (float32x4_t, float32x4_t, float32x4_t);
    uint64x2_t vmlal_u32 (uint64x2_t, uint32x2_t, uint32x2_t);
    uint32x4_t vmlal_u16 (uint32x4_t, uint16x4_t, uint16x4_t);
    uint16x8_t vmlal_u8 (uint16x8_t, uint8x8_t, uint8x8_t);
    int64x2_t vmlal_s32 (int64x2_t, int32x2_t, int32x2_t);
    int32x4_t vmlal_s16 (int32x4_t, int16x4_t, int16x4_t);
    int16x8_t vmlal_s8 (int16x8_t, int8x8_t, int8x8_t);
    int64x2_t vqdmlal_s32 (int64x2_t, int32x2_t, int32x2_t);
    int32x4_t vqdmlal_s16 (int32x4_t, int16x4_t, int16x4_t);
    uint32x2_t vmls_u32 (uint32x2_t, uint32x2_t, uint32x2_t);
    uint16x4_t vmls_u16 (uint16x4_t, uint16x4_t, uint16x4_t);
    uint8x8_t vmls_u8 (uint8x8_t, uint8x8_t, uint8x8_t);
    int32x2_t vmls_s32 (int32x2_t, int32x2_t, int32x2_t);
    int16x4_t vmls_s16 (int16x4_t, int16x4_t, int16x4_t);
    int8x8_t vmls_s8 (int8x8_t, int8x8_t, int8x8_t);
    float32x2_t vmls_f32 (float32x2_t, float32x2_t, float32x2_t);
    uint32x4_t vmlsq_u32 (uint32x4_t, uint32x4_t, uint32x4_t);
    uint16x8_t vmlsq_u16 (uint16x8_t, uint16x8_t, uint16x8_t);
    uint8x16_t vmlsq_u8 (uint8x16_t, uint8x16_t, uint8x16_t);
    int32x4_t vmlsq_s32 (int32x4_t, int32x4_t, int32x4_t);
    int16x8_t vmlsq_s16 (int16x8_t, int16x8_t, int16x8_t);
    int8x16_t vmlsq_s8 (int8x16_t, int8x16_t, int8x16_t);
    float32x4_t vmlsq_f32 (float32x4_t, float32x4_t, float32x4_t);
    uint64x2_t vmlsl_u32 (uint64x2_t, uint32x2_t, uint32x2_t);
    uint32x4_t vmlsl_u16 (uint32x4_t, uint16x4_t, uint16x4_t);
    uint16x8_t vmlsl_u8 (uint16x8_t, uint8x8_t, uint8x8_t);
    int64x2_t vmlsl_s32 (int64x2_t, int32x2_t, int32x2_t);
    int32x4_t vmlsl_s16 (int32x4_t, int16x4_t, int16x4_t);
    int16x8_t vmlsl_s8 (int16x8_t, int8x8_t, int8x8_t);
    int64x2_t vqdmlsl_s32 (int64x2_t, int32x2_t, int32x2_t);
    int32x4_t vqdmlsl_s16 (int32x4_t, int16x4_t, int16x4_t);
    float32x2_t vfma_f32 (float32x2_t, float32x2_t, float32x2_t);
    float32x4_t vfmaq_f32 (float32x4_t, float32x4_t, float32x4_t);
    float32x2_t vfms_f32 (float32x2_t, float32x2_t, float32x2_t);
    float32x4_t vfmsq_f32 (float32x4_t, float32x4_t, float32x4_t);
    float32x2_t vrndn_f32 (float32x2_t);
    float32x4_t vrndqn_f32 (float32x4_t);
    float32x2_t vrnda_f32 (float32x2_t);
    float32x4_t vrndqa_f32 (float32x4_t);
    float32x2_t vrndp_f32 (float32x2_t);
    float32x4_t vrndqp_f32 (float32x4_t);
    float32x2_t vrndm_f32 (float32x2_t);
    float32x4_t vrndqm_f32 (float32x4_t);
    float32x2_t vrnd_f32 (float32x2_t);
    float32x4_t vrndq_f32 (float32x4_t);
    uint32x2_t vsub_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vsub_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vsub_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vsub_s32 (int32x2_t, int32x2_t);
    int16x4_t vsub_s16 (int16x4_t, int16x4_t);
    int8x8_t vsub_s8 (int8x8_t, int8x8_t);
    float32x2_t vsub_f32 (float32x2_t, float32x2_t);
    uint64x1_t vsub_u64 (uint64x1_t, uint64x1_t);
    int64x1_t vsub_s64 (int64x1_t, int64x1_t);
    uint32x4_t vsubq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vsubq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vsubq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vsubq_s32 (int32x4_t, int32x4_t);
    int16x8_t vsubq_s16 (int16x8_t, int16x8_t);
    int8x16_t vsubq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vsubq_u64 (uint64x2_t, uint64x2_t);
    int64x2_t vsubq_s64 (int64x2_t, int64x2_t);
    float32x4_t vsubq_f32 (float32x4_t, float32x4_t);
    uint64x2_t vsubl_u32 (uint32x2_t, uint32x2_t);
    uint32x4_t vsubl_u16 (uint16x4_t, uint16x4_t);
    uint16x8_t vsubl_u8 (uint8x8_t, uint8x8_t);
    int64x2_t vsubl_s32 (int32x2_t, int32x2_t);
    int32x4_t vsubl_s16 (int16x4_t, int16x4_t);
    int16x8_t vsubl_s8 (int8x8_t, int8x8_t);
    uint64x2_t vsubw_u32 (uint64x2_t, uint32x2_t);
    uint32x4_t vsubw_u16 (uint32x4_t, uint16x4_t);
    uint16x8_t vsubw_u8 (uint16x8_t, uint8x8_t);
    int64x2_t vsubw_s32 (int64x2_t, int32x2_t);
    int32x4_t vsubw_s16 (int32x4_t, int16x4_t);
    int16x8_t vsubw_s8 (int16x8_t, int8x8_t);
    uint32x2_t vhsub_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vhsub_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vhsub_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vhsub_s32 (int32x2_t, int32x2_t);
    int16x4_t vhsub_s16 (int16x4_t, int16x4_t);
    int8x8_t vhsub_s8 (int8x8_t, int8x8_t);
    uint32x4_t vhsubq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vhsubq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vhsubq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vhsubq_s32 (int32x4_t, int32x4_t);
    int16x8_t vhsubq_s16 (int16x8_t, int16x8_t);
    int8x16_t vhsubq_s8 (int8x16_t, int8x16_t);
    uint32x2_t vqsub_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vqsub_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vqsub_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vqsub_s32 (int32x2_t, int32x2_t);
    int16x4_t vqsub_s16 (int16x4_t, int16x4_t);
    int8x8_t vqsub_s8 (int8x8_t, int8x8_t);
    uint64x1_t vqsub_u64 (uint64x1_t, uint64x1_t);
    int64x1_t vqsub_s64 (int64x1_t, int64x1_t);
    uint32x4_t vqsubq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vqsubq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vqsubq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vqsubq_s32 (int32x4_t, int32x4_t);
    int16x8_t vqsubq_s16 (int16x8_t, int16x8_t);
    int8x16_t vqsubq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vqsubq_u64 (uint64x2_t, uint64x2_t);
    int64x2_t vqsubq_s64 (int64x2_t, int64x2_t);
    uint32x2_t vsubhn_u64 (uint64x2_t, uint64x2_t);
    uint16x4_t vsubhn_u32 (uint32x4_t, uint32x4_t);
    uint8x8_t vsubhn_u16 (uint16x8_t, uint16x8_t);
    int32x2_t vsubhn_s64 (int64x2_t, int64x2_t);
    int16x4_t vsubhn_s32 (int32x4_t, int32x4_t);
    int8x8_t vsubhn_s16 (int16x8_t, int16x8_t);
    uint32x2_t vrsubhn_u64 (uint64x2_t, uint64x2_t);
    uint16x4_t vrsubhn_u32 (uint32x4_t, uint32x4_t);
    uint8x8_t vrsubhn_u16 (uint16x8_t, uint16x8_t);
    int32x2_t vrsubhn_s64 (int64x2_t, int64x2_t);
    int16x4_t vrsubhn_s32 (int32x4_t, int32x4_t);
    int8x8_t vrsubhn_s16 (int16x8_t, int16x8_t);
    uint32x2_t vceq_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vceq_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vceq_u8 (uint8x8_t, uint8x8_t);
    uint32x2_t vceq_s32 (int32x2_t, int32x2_t);
    uint16x4_t vceq_s16 (int16x4_t, int16x4_t);
    uint8x8_t vceq_s8 (int8x8_t, int8x8_t);
    uint32x2_t vceq_f32 (float32x2_t, float32x2_t);
    uint8x8_t vceq_p8 (poly8x8_t, poly8x8_t);
    uint32x4_t vceqq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vceqq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vceqq_u8 (uint8x16_t, uint8x16_t);
    uint32x4_t vceqq_s32 (int32x4_t, int32x4_t);
    uint16x8_t vceqq_s16 (int16x8_t, int16x8_t);
    uint8x16_t vceqq_s8 (int8x16_t, int8x16_t);
    uint32x4_t vceqq_f32 (float32x4_t, float32x4_t);
    uint8x16_t vceqq_p8 (poly8x16_t, poly8x16_t);
    uint32x2_t vcge_s32 (int32x2_t, int32x2_t);
    uint16x4_t vcge_s16 (int16x4_t, int16x4_t);
    uint8x8_t vcge_s8 (int8x8_t, int8x8_t);
    uint32x2_t vcge_f32 (float32x2_t, float32x2_t);
    uint32x2_t vcge_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vcge_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vcge_u8 (uint8x8_t, uint8x8_t);
    uint32x4_t vcgeq_s32 (int32x4_t, int32x4_t);
    uint16x8_t vcgeq_s16 (int16x8_t, int16x8_t);
    uint8x16_t vcgeq_s8 (int8x16_t, int8x16_t);
    uint32x4_t vcgeq_f32 (float32x4_t, float32x4_t);
    uint32x4_t vcgeq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vcgeq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vcgeq_u8 (uint8x16_t, uint8x16_t);
    uint32x2_t vcle_s32 (int32x2_t, int32x2_t);
    uint16x4_t vcle_s16 (int16x4_t, int16x4_t);
    uint8x8_t vcle_s8 (int8x8_t, int8x8_t);
    uint32x2_t vcle_f32 (float32x2_t, float32x2_t);
    uint32x2_t vcle_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vcle_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vcle_u8 (uint8x8_t, uint8x8_t);
    uint32x4_t vcleq_s32 (int32x4_t, int32x4_t);
    uint16x8_t vcleq_s16 (int16x8_t, int16x8_t);
    uint8x16_t vcleq_s8 (int8x16_t, int8x16_t);
    uint32x4_t vcleq_f32 (float32x4_t, float32x4_t);
    uint32x4_t vcleq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vcleq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vcleq_u8 (uint8x16_t, uint8x16_t);
    uint32x2_t vcgt_s32 (int32x2_t, int32x2_t);
    uint16x4_t vcgt_s16 (int16x4_t, int16x4_t);
    uint8x8_t vcgt_s8 (int8x8_t, int8x8_t);
    uint32x2_t vcgt_f32 (float32x2_t, float32x2_t);
    uint32x2_t vcgt_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vcgt_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vcgt_u8 (uint8x8_t, uint8x8_t);
    uint32x4_t vcgtq_s32 (int32x4_t, int32x4_t);
    uint16x8_t vcgtq_s16 (int16x8_t, int16x8_t);
    uint8x16_t vcgtq_s8 (int8x16_t, int8x16_t);
    uint32x4_t vcgtq_f32 (float32x4_t, float32x4_t);
    uint32x4_t vcgtq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vcgtq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vcgtq_u8 (uint8x16_t, uint8x16_t);
    uint32x2_t vclt_s32 (int32x2_t, int32x2_t);
    uint16x4_t vclt_s16 (int16x4_t, int16x4_t);
    uint8x8_t vclt_s8 (int8x8_t, int8x8_t);
    uint32x2_t vclt_f32 (float32x2_t, float32x2_t);
    uint32x2_t vclt_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vclt_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vclt_u8 (uint8x8_t, uint8x8_t);
    uint32x4_t vcltq_s32 (int32x4_t, int32x4_t);
    uint16x8_t vcltq_s16 (int16x8_t, int16x8_t);
    uint8x16_t vcltq_s8 (int8x16_t, int8x16_t);
    uint32x4_t vcltq_f32 (float32x4_t, float32x4_t);
    uint32x4_t vcltq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vcltq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vcltq_u8 (uint8x16_t, uint8x16_t);
    uint32x2_t vcage_f32 (float32x2_t, float32x2_t);
    uint32x4_t vcageq_f32 (float32x4_t, float32x4_t);
    uint32x2_t vcale_f32 (float32x2_t, float32x2_t);
    uint32x4_t vcaleq_f32 (float32x4_t, float32x4_t);
    uint32x2_t vcagt_f32 (float32x2_t, float32x2_t);
    uint32x4_t vcagtq_f32 (float32x4_t, float32x4_t);
    uint32x2_t vcalt_f32 (float32x2_t, float32x2_t);
    uint32x4_t vcaltq_f32 (float32x4_t, float32x4_t);
    uint32x2_t vtst_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vtst_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vtst_u8 (uint8x8_t, uint8x8_t);
    uint32x2_t vtst_s32 (int32x2_t, int32x2_t);
    uint16x4_t vtst_s16 (int16x4_t, int16x4_t);
    uint8x8_t vtst_s8 (int8x8_t, int8x8_t);
    uint8x8_t vtst_p8 (poly8x8_t, poly8x8_t);
    uint32x4_t vtstq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vtstq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vtstq_u8 (uint8x16_t, uint8x16_t);
    uint32x4_t vtstq_s32 (int32x4_t, int32x4_t);
    uint16x8_t vtstq_s16 (int16x8_t, int16x8_t);
    uint8x16_t vtstq_s8 (int8x16_t, int8x16_t);
    uint8x16_t vtstq_p8 (poly8x16_t, poly8x16_t);
    uint32x2_t vabd_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vabd_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vabd_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vabd_s32 (int32x2_t, int32x2_t);
    int16x4_t vabd_s16 (int16x4_t, int16x4_t);
    int8x8_t vabd_s8 (int8x8_t, int8x8_t);
    float32x2_t vabd_f32 (float32x2_t, float32x2_t);
    uint32x4_t vabdq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vabdq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vabdq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vabdq_s32 (int32x4_t, int32x4_t);
    int16x8_t vabdq_s16 (int16x8_t, int16x8_t);
    int8x16_t vabdq_s8 (int8x16_t, int8x16_t);
    float32x4_t vabdq_f32 (float32x4_t, float32x4_t);
    uint64x2_t vabdl_u32 (uint32x2_t, uint32x2_t);
    uint32x4_t vabdl_u16 (uint16x4_t, uint16x4_t);
    uint16x8_t vabdl_u8 (uint8x8_t, uint8x8_t);
    int64x2_t vabdl_s32 (int32x2_t, int32x2_t);
    int32x4_t vabdl_s16 (int16x4_t, int16x4_t);
    int16x8_t vabdl_s8 (int8x8_t, int8x8_t);
    uint32x2_t vaba_u32 (uint32x2_t, uint32x2_t, uint32x2_t);
    uint16x4_t vaba_u16 (uint16x4_t, uint16x4_t, uint16x4_t);
    uint8x8_t vaba_u8 (uint8x8_t, uint8x8_t, uint8x8_t);
    int32x2_t vaba_s32 (int32x2_t, int32x2_t, int32x2_t);
    int16x4_t vaba_s16 (int16x4_t, int16x4_t, int16x4_t);
    int8x8_t vaba_s8 (int8x8_t, int8x8_t, int8x8_t);
    uint32x4_t vabaq_u32 (uint32x4_t, uint32x4_t, uint32x4_t);
    uint16x8_t vabaq_u16 (uint16x8_t, uint16x8_t, uint16x8_t);
    uint8x16_t vabaq_u8 (uint8x16_t, uint8x16_t, uint8x16_t);
    int32x4_t vabaq_s32 (int32x4_t, int32x4_t, int32x4_t);
    int16x8_t vabaq_s16 (int16x8_t, int16x8_t, int16x8_t);
    int8x16_t vabaq_s8 (int8x16_t, int8x16_t, int8x16_t);
    uint64x2_t vabal_u32 (uint64x2_t, uint32x2_t, uint32x2_t);
    uint32x4_t vabal_u16 (uint32x4_t, uint16x4_t, uint16x4_t);
    uint16x8_t vabal_u8 (uint16x8_t, uint8x8_t, uint8x8_t);
    int64x2_t vabal_s32 (int64x2_t, int32x2_t, int32x2_t);
    int32x4_t vabal_s16 (int32x4_t, int16x4_t, int16x4_t);
    int16x8_t vabal_s8 (int16x8_t, int8x8_t, int8x8_t);
    uint32x2_t vmax_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vmax_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vmax_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vmax_s32 (int32x2_t, int32x2_t);
    int16x4_t vmax_s16 (int16x4_t, int16x4_t);
    int8x8_t vmax_s8 (int8x8_t, int8x8_t);
    float32x2_t vmax_f32 (float32x2_t, float32x2_t);
    uint32x4_t vmaxq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vmaxq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vmaxq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vmaxq_s32 (int32x4_t, int32x4_t);
    int16x8_t vmaxq_s16 (int16x8_t, int16x8_t);
    int8x16_t vmaxq_s8 (int8x16_t, int8x16_t);
    float32x4_t vmaxq_f32 (float32x4_t, float32x4_t);
    uint32x2_t vmin_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vmin_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vmin_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vmin_s32 (int32x2_t, int32x2_t);
    int16x4_t vmin_s16 (int16x4_t, int16x4_t);
    int8x8_t vmin_s8 (int8x8_t, int8x8_t);
    float32x2_t vmin_f32 (float32x2_t, float32x2_t);
    uint32x4_t vminq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vminq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vminq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vminq_s32 (int32x4_t, int32x4_t);
    int16x8_t vminq_s16 (int16x8_t, int16x8_t);
    int8x16_t vminq_s8 (int8x16_t, int8x16_t);
    float32x4_t vminq_f32 (float32x4_t, float32x4_t);
    uint32x2_t vpadd_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vpadd_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vpadd_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vpadd_s32 (int32x2_t, int32x2_t);
    int16x4_t vpadd_s16 (int16x4_t, int16x4_t);
    int8x8_t vpadd_s8 (int8x8_t, int8x8_t);
    float32x2_t vpadd_f32 (float32x2_t, float32x2_t);
    uint64x1_t vpaddl_u32 (uint32x2_t);
    uint32x2_t vpaddl_u16 (uint16x4_t);
    uint16x4_t vpaddl_u8 (uint8x8_t);
    int64x1_t vpaddl_s32 (int32x2_t);
    int32x2_t vpaddl_s16 (int16x4_t);
    int16x4_t vpaddl_s8 (int8x8_t);
    uint64x2_t vpaddlq_u32 (uint32x4_t);
    uint32x4_t vpaddlq_u16 (uint16x8_t);
    uint16x8_t vpaddlq_u8 (uint8x16_t);
    int64x2_t vpaddlq_s32 (int32x4_t);
    int32x4_t vpaddlq_s16 (int16x8_t);
    int16x8_t vpaddlq_s8 (int8x16_t);
    uint64x1_t vpadal_u32 (uint64x1_t, uint32x2_t);
    uint32x2_t vpadal_u16 (uint32x2_t, uint16x4_t);
    uint16x4_t vpadal_u8 (uint16x4_t, uint8x8_t);
    int64x1_t vpadal_s32 (int64x1_t, int32x2_t);
    int32x2_t vpadal_s16 (int32x2_t, int16x4_t);
    int16x4_t vpadal_s8 (int16x4_t, int8x8_t);
    uint64x2_t vpadalq_u32 (uint64x2_t, uint32x4_t);
    uint32x4_t vpadalq_u16 (uint32x4_t, uint16x8_t);
    uint16x8_t vpadalq_u8 (uint16x8_t, uint8x16_t);
    int64x2_t vpadalq_s32 (int64x2_t, int32x4_t);
    int32x4_t vpadalq_s16 (int32x4_t, int16x8_t);
    int16x8_t vpadalq_s8 (int16x8_t, int8x16_t);
    uint32x2_t vpmax_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vpmax_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vpmax_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vpmax_s32 (int32x2_t, int32x2_t);
    int16x4_t vpmax_s16 (int16x4_t, int16x4_t);
    int8x8_t vpmax_s8 (int8x8_t, int8x8_t);
    float32x2_t vpmax_f32 (float32x2_t, float32x2_t);
    uint32x2_t vpmin_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vpmin_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vpmin_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vpmin_s32 (int32x2_t, int32x2_t);
    int16x4_t vpmin_s16 (int16x4_t, int16x4_t);
    int8x8_t vpmin_s8 (int8x8_t, int8x8_t);
    float32x2_t vpmin_f32 (float32x2_t, float32x2_t);
    float32x2_t vrecps_f32 (float32x2_t, float32x2_t);
    float32x4_t vrecpsq_f32 (float32x4_t, float32x4_t);
    float32x2_t vrsqrts_f32 (float32x2_t, float32x2_t);
    float32x4_t vrsqrtsq_f32 (float32x4_t, float32x4_t);
    uint32x2_t vshl_u32 (uint32x2_t, int32x2_t);
    uint16x4_t vshl_u16 (uint16x4_t, int16x4_t);
    uint8x8_t vshl_u8 (uint8x8_t, int8x8_t);
    int32x2_t vshl_s32 (int32x2_t, int32x2_t);
    int16x4_t vshl_s16 (int16x4_t, int16x4_t);
    int8x8_t vshl_s8 (int8x8_t, int8x8_t);
    uint64x1_t vshl_u64 (uint64x1_t, int64x1_t);
    int64x1_t vshl_s64 (int64x1_t, int64x1_t);
    uint32x4_t vshlq_u32 (uint32x4_t, int32x4_t);
    uint16x8_t vshlq_u16 (uint16x8_t, int16x8_t);
    uint8x16_t vshlq_u8 (uint8x16_t, int8x16_t);
    int32x4_t vshlq_s32 (int32x4_t, int32x4_t);
    int16x8_t vshlq_s16 (int16x8_t, int16x8_t);
    int8x16_t vshlq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vshlq_u64 (uint64x2_t, int64x2_t);
    int64x2_t vshlq_s64 (int64x2_t, int64x2_t);
    uint32x2_t vrshl_u32 (uint32x2_t, int32x2_t);
    uint16x4_t vrshl_u16 (uint16x4_t, int16x4_t);
    uint8x8_t vrshl_u8 (uint8x8_t, int8x8_t);
    int32x2_t vrshl_s32 (int32x2_t, int32x2_t);
    int16x4_t vrshl_s16 (int16x4_t, int16x4_t);
    int8x8_t vrshl_s8 (int8x8_t, int8x8_t);
    uint64x1_t vrshl_u64 (uint64x1_t, int64x1_t);
    int64x1_t vrshl_s64 (int64x1_t, int64x1_t);
    uint32x4_t vrshlq_u32 (uint32x4_t, int32x4_t);
    uint16x8_t vrshlq_u16 (uint16x8_t, int16x8_t);
    uint8x16_t vrshlq_u8 (uint8x16_t, int8x16_t);
    int32x4_t vrshlq_s32 (int32x4_t, int32x4_t);
    int16x8_t vrshlq_s16 (int16x8_t, int16x8_t);
    int8x16_t vrshlq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vrshlq_u64 (uint64x2_t, int64x2_t);
    int64x2_t vrshlq_s64 (int64x2_t, int64x2_t);
    uint32x2_t vqshl_u32 (uint32x2_t, int32x2_t);
    uint16x4_t vqshl_u16 (uint16x4_t, int16x4_t);
    uint8x8_t vqshl_u8 (uint8x8_t, int8x8_t);
    int32x2_t vqshl_s32 (int32x2_t, int32x2_t);
    int16x4_t vqshl_s16 (int16x4_t, int16x4_t);
    int8x8_t vqshl_s8 (int8x8_t, int8x8_t);
    uint64x1_t vqshl_u64 (uint64x1_t, int64x1_t);
    int64x1_t vqshl_s64 (int64x1_t, int64x1_t);
    uint32x4_t vqshlq_u32 (uint32x4_t, int32x4_t);
    uint16x8_t vqshlq_u16 (uint16x8_t, int16x8_t);
    uint8x16_t vqshlq_u8 (uint8x16_t, int8x16_t);
    int32x4_t vqshlq_s32 (int32x4_t, int32x4_t);
    int16x8_t vqshlq_s16 (int16x8_t, int16x8_t);
    int8x16_t vqshlq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vqshlq_u64 (uint64x2_t, int64x2_t);
    int64x2_t vqshlq_s64 (int64x2_t, int64x2_t);
    uint32x2_t vqrshl_u32 (uint32x2_t, int32x2_t);
    uint16x4_t vqrshl_u16 (uint16x4_t, int16x4_t);
    uint8x8_t vqrshl_u8 (uint8x8_t, int8x8_t);
    int32x2_t vqrshl_s32 (int32x2_t, int32x2_t);
    int16x4_t vqrshl_s16 (int16x4_t, int16x4_t);
    int8x8_t vqrshl_s8 (int8x8_t, int8x8_t);
    uint64x1_t vqrshl_u64 (uint64x1_t, int64x1_t);
    int64x1_t vqrshl_s64 (int64x1_t, int64x1_t);
    uint32x4_t vqrshlq_u32 (uint32x4_t, int32x4_t);
    uint16x8_t vqrshlq_u16 (uint16x8_t, int16x8_t);
    uint8x16_t vqrshlq_u8 (uint8x16_t, int8x16_t);
    int32x4_t vqrshlq_s32 (int32x4_t, int32x4_t);
    int16x8_t vqrshlq_s16 (int16x8_t, int16x8_t);
    int8x16_t vqrshlq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vqrshlq_u64 (uint64x2_t, int64x2_t);
    int64x2_t vqrshlq_s64 (int64x2_t, int64x2_t);
    uint32x2_t vshl_n_u32 (uint32x2_t, const int);
    uint16x4_t vshl_n_u16 (uint16x4_t, const int);
    uint8x8_t vshl_n_u8 (uint8x8_t, const int);
    int32x2_t vshl_n_s32 (int32x2_t, const int);
    int16x4_t vshl_n_s16 (int16x4_t, const int);
    int8x8_t vshl_n_s8 (int8x8_t, const int);
    uint64x1_t vshl_n_u64 (uint64x1_t, const int);
    int64x1_t vshl_n_s64 (int64x1_t, const int);
    uint32x4_t vshlq_n_u32 (uint32x4_t, const int);
    uint16x8_t vshlq_n_u16 (uint16x8_t, const int);
    uint8x16_t vshlq_n_u8 (uint8x16_t, const int);
    int32x4_t vshlq_n_s32 (int32x4_t, const int);
    int16x8_t vshlq_n_s16 (int16x8_t, const int);
    int8x16_t vshlq_n_s8 (int8x16_t, const int);
    uint64x2_t vshlq_n_u64 (uint64x2_t, const int);
    int64x2_t vshlq_n_s64 (int64x2_t, const int);
    uint32x2_t vqshl_n_u32 (uint32x2_t, const int);
    uint16x4_t vqshl_n_u16 (uint16x4_t, const int);
    uint8x8_t vqshl_n_u8 (uint8x8_t, const int);
    int32x2_t vqshl_n_s32 (int32x2_t, const int);
    int16x4_t vqshl_n_s16 (int16x4_t, const int);
    int8x8_t vqshl_n_s8 (int8x8_t, const int);
    uint64x1_t vqshl_n_u64 (uint64x1_t, const int);
    int64x1_t vqshl_n_s64 (int64x1_t, const int);
    uint32x4_t vqshlq_n_u32 (uint32x4_t, const int);
    uint16x8_t vqshlq_n_u16 (uint16x8_t, const int);
    uint8x16_t vqshlq_n_u8 (uint8x16_t, const int);
    int32x4_t vqshlq_n_s32 (int32x4_t, const int);
    int16x8_t vqshlq_n_s16 (int16x8_t, const int);
    int8x16_t vqshlq_n_s8 (int8x16_t, const int);
    uint64x2_t vqshlq_n_u64 (uint64x2_t, const int);
    int64x2_t vqshlq_n_s64 (int64x2_t, const int);
    uint64x1_t vqshlu_n_s64 (int64x1_t, const int);
    uint32x2_t vqshlu_n_s32 (int32x2_t, const int);
    uint16x4_t vqshlu_n_s16 (int16x4_t, const int);
    uint8x8_t vqshlu_n_s8 (int8x8_t, const int);
    uint64x2_t vqshluq_n_s64 (int64x2_t, const int);
    uint32x4_t vqshluq_n_s32 (int32x4_t, const int);
    uint16x8_t vqshluq_n_s16 (int16x8_t, const int);
    uint8x16_t vqshluq_n_s8 (int8x16_t, const int);
    uint64x2_t vshll_n_u32 (uint32x2_t, const int);
    uint32x4_t vshll_n_u16 (uint16x4_t, const int);
    uint16x8_t vshll_n_u8 (uint8x8_t, const int);
    int64x2_t vshll_n_s32 (int32x2_t, const int);
    int32x4_t vshll_n_s16 (int16x4_t, const int);
    int16x8_t vshll_n_s8 (int8x8_t, const int);
    uint32x2_t vshr_n_u32 (uint32x2_t, const int);
    uint16x4_t vshr_n_u16 (uint16x4_t, const int);
    uint8x8_t vshr_n_u8 (uint8x8_t, const int);
    int32x2_t vshr_n_s32 (int32x2_t, const int);
    int16x4_t vshr_n_s16 (int16x4_t, const int);
    int8x8_t vshr_n_s8 (int8x8_t, const int);
    uint64x1_t vshr_n_u64 (uint64x1_t, const int);
    int64x1_t vshr_n_s64 (int64x1_t, const int);
    uint32x4_t vshrq_n_u32 (uint32x4_t, const int);
    uint16x8_t vshrq_n_u16 (uint16x8_t, const int);
    uint8x16_t vshrq_n_u8 (uint8x16_t, const int);
    int32x4_t vshrq_n_s32 (int32x4_t, const int);
    int16x8_t vshrq_n_s16 (int16x8_t, const int);
    int8x16_t vshrq_n_s8 (int8x16_t, const int);
    uint64x2_t vshrq_n_u64 (uint64x2_t, const int);
    int64x2_t vshrq_n_s64 (int64x2_t, const int);
    uint32x2_t vrshr_n_u32 (uint32x2_t, const int);
    uint16x4_t vrshr_n_u16 (uint16x4_t, const int);
    uint8x8_t vrshr_n_u8 (uint8x8_t, const int);
    int32x2_t vrshr_n_s32 (int32x2_t, const int);
    int16x4_t vrshr_n_s16 (int16x4_t, const int);
    int8x8_t vrshr_n_s8 (int8x8_t, const int);
    uint64x1_t vrshr_n_u64 (uint64x1_t, const int);
    int64x1_t vrshr_n_s64 (int64x1_t, const int);
    uint32x4_t vrshrq_n_u32 (uint32x4_t, const int);
    uint16x8_t vrshrq_n_u16 (uint16x8_t, const int);
    uint8x16_t vrshrq_n_u8 (uint8x16_t, const int);
    int32x4_t vrshrq_n_s32 (int32x4_t, const int);
    int16x8_t vrshrq_n_s16 (int16x8_t, const int);
    int8x16_t vrshrq_n_s8 (int8x16_t, const int);
    uint64x2_t vrshrq_n_u64 (uint64x2_t, const int);
    int64x2_t vrshrq_n_s64 (int64x2_t, const int);
    uint32x2_t vshrn_n_u64 (uint64x2_t, const int);
    uint16x4_t vshrn_n_u32 (uint32x4_t, const int);
    uint8x8_t vshrn_n_u16 (uint16x8_t, const int);
    int32x2_t vshrn_n_s64 (int64x2_t, const int);
    int16x4_t vshrn_n_s32 (int32x4_t, const int);
    int8x8_t vshrn_n_s16 (int16x8_t, const int);
    uint32x2_t vrshrn_n_u64 (uint64x2_t, const int);
    uint16x4_t vrshrn_n_u32 (uint32x4_t, const int);
    uint8x8_t vrshrn_n_u16 (uint16x8_t, const int);
    int32x2_t vrshrn_n_s64 (int64x2_t, const int);
    int16x4_t vrshrn_n_s32 (int32x4_t, const int);
    int8x8_t vrshrn_n_s16 (int16x8_t, const int);
    uint32x2_t vqshrn_n_u64 (uint64x2_t, const int);
    uint16x4_t vqshrn_n_u32 (uint32x4_t, const int);
    uint8x8_t vqshrn_n_u16 (uint16x8_t, const int);
    int32x2_t vqshrn_n_s64 (int64x2_t, const int);
    int16x4_t vqshrn_n_s32 (int32x4_t, const int);
    int8x8_t vqshrn_n_s16 (int16x8_t, const int);
    uint32x2_t vqrshrn_n_u64 (uint64x2_t, const int);
    uint16x4_t vqrshrn_n_u32 (uint32x4_t, const int);
    uint8x8_t vqrshrn_n_u16 (uint16x8_t, const int);
    int32x2_t vqrshrn_n_s64 (int64x2_t, const int);
    int16x4_t vqrshrn_n_s32 (int32x4_t, const int);
    int8x8_t vqrshrn_n_s16 (int16x8_t, const int);
    uint32x2_t vqshrun_n_s64 (int64x2_t, const int);
    uint16x4_t vqshrun_n_s32 (int32x4_t, const int);
    uint8x8_t vqshrun_n_s16 (int16x8_t, const int);
    uint32x2_t vqrshrun_n_s64 (int64x2_t, const int);
    uint16x4_t vqrshrun_n_s32 (int32x4_t, const int);
    uint8x8_t vqrshrun_n_s16 (int16x8_t, const int);
    uint32x2_t vsra_n_u32 (uint32x2_t, uint32x2_t, const int);
    uint16x4_t vsra_n_u16 (uint16x4_t, uint16x4_t, const int);
    uint8x8_t vsra_n_u8 (uint8x8_t, uint8x8_t, const int);
    int32x2_t vsra_n_s32 (int32x2_t, int32x2_t, const int);
    int16x4_t vsra_n_s16 (int16x4_t, int16x4_t, const int);
    int8x8_t vsra_n_s8 (int8x8_t, int8x8_t, const int);
    uint64x1_t vsra_n_u64 (uint64x1_t, uint64x1_t, const int);
    int64x1_t vsra_n_s64 (int64x1_t, int64x1_t, const int);
    uint32x4_t vsraq_n_u32 (uint32x4_t, uint32x4_t, const int);
    uint16x8_t vsraq_n_u16 (uint16x8_t, uint16x8_t, const int);
    uint8x16_t vsraq_n_u8 (uint8x16_t, uint8x16_t, const int);
    int32x4_t vsraq_n_s32 (int32x4_t, int32x4_t, const int);
    int16x8_t vsraq_n_s16 (int16x8_t, int16x8_t, const int);
    int8x16_t vsraq_n_s8 (int8x16_t, int8x16_t, const int);
    uint64x2_t vsraq_n_u64 (uint64x2_t, uint64x2_t, const int);
    int64x2_t vsraq_n_s64 (int64x2_t, int64x2_t, const int);
    uint32x2_t vrsra_n_u32 (uint32x2_t, uint32x2_t, const int);
    uint16x4_t vrsra_n_u16 (uint16x4_t, uint16x4_t, const int);
    uint8x8_t vrsra_n_u8 (uint8x8_t, uint8x8_t, const int);
    int32x2_t vrsra_n_s32 (int32x2_t, int32x2_t, const int);
    int16x4_t vrsra_n_s16 (int16x4_t, int16x4_t, const int);
    int8x8_t vrsra_n_s8 (int8x8_t, int8x8_t, const int);
    uint64x1_t vrsra_n_u64 (uint64x1_t, uint64x1_t, const int);
    int64x1_t vrsra_n_s64 (int64x1_t, int64x1_t, const int);
    uint32x4_t vrsraq_n_u32 (uint32x4_t, uint32x4_t, const int);
    uint16x8_t vrsraq_n_u16 (uint16x8_t, uint16x8_t, const int);
    uint8x16_t vrsraq_n_u8 (uint8x16_t, uint8x16_t, const int);
    int32x4_t vrsraq_n_s32 (int32x4_t, int32x4_t, const int);
    int16x8_t vrsraq_n_s16 (int16x8_t, int16x8_t, const int);
    int8x16_t vrsraq_n_s8 (int8x16_t, int8x16_t, const int);
    uint64x2_t vrsraq_n_u64 (uint64x2_t, uint64x2_t, const int);
    int64x2_t vrsraq_n_s64 (int64x2_t, int64x2_t, const int);
    uint32x2_t vsri_n_u32 (uint32x2_t, uint32x2_t, const int);
    uint16x4_t vsri_n_u16 (uint16x4_t, uint16x4_t, const int);
    uint8x8_t vsri_n_u8 (uint8x8_t, uint8x8_t, const int);
    int32x2_t vsri_n_s32 (int32x2_t, int32x2_t, const int);
    int16x4_t vsri_n_s16 (int16x4_t, int16x4_t, const int);
    int8x8_t vsri_n_s8 (int8x8_t, int8x8_t, const int);
    uint64x1_t vsri_n_u64 (uint64x1_t, uint64x1_t, const int);
    int64x1_t vsri_n_s64 (int64x1_t, int64x1_t, const int);
    poly16x4_t vsri_n_p16 (poly16x4_t, poly16x4_t, const int);
    poly8x8_t vsri_n_p8 (poly8x8_t, poly8x8_t, const int);
    uint32x4_t vsriq_n_u32 (uint32x4_t, uint32x4_t, const int);
    uint16x8_t vsriq_n_u16 (uint16x8_t, uint16x8_t, const int);
    uint8x16_t vsriq_n_u8 (uint8x16_t, uint8x16_t, const int);
    int32x4_t vsriq_n_s32 (int32x4_t, int32x4_t, const int);
    int16x8_t vsriq_n_s16 (int16x8_t, int16x8_t, const int);
    int8x16_t vsriq_n_s8 (int8x16_t, int8x16_t, const int);
    uint64x2_t vsriq_n_u64 (uint64x2_t, uint64x2_t, const int);
    int64x2_t vsriq_n_s64 (int64x2_t, int64x2_t, const int);
    poly16x8_t vsriq_n_p16 (poly16x8_t, poly16x8_t, const int);
    poly8x16_t vsriq_n_p8 (poly8x16_t, poly8x16_t, const int);
    uint32x2_t vsli_n_u32 (uint32x2_t, uint32x2_t, const int);
    uint16x4_t vsli_n_u16 (uint16x4_t, uint16x4_t, const int);
    uint8x8_t vsli_n_u8 (uint8x8_t, uint8x8_t, const int);
    int32x2_t vsli_n_s32 (int32x2_t, int32x2_t, const int);
    int16x4_t vsli_n_s16 (int16x4_t, int16x4_t, const int);
    int8x8_t vsli_n_s8 (int8x8_t, int8x8_t, const int);
    uint64x1_t vsli_n_u64 (uint64x1_t, uint64x1_t, const int);
    int64x1_t vsli_n_s64 (int64x1_t, int64x1_t, const int);
    poly16x4_t vsli_n_p16 (poly16x4_t, poly16x4_t, const int);
    poly8x8_t vsli_n_p8 (poly8x8_t, poly8x8_t, const int);
    uint32x4_t vsliq_n_u32 (uint32x4_t, uint32x4_t, const int);
    uint16x8_t vsliq_n_u16 (uint16x8_t, uint16x8_t, const int);
    uint8x16_t vsliq_n_u8 (uint8x16_t, uint8x16_t, const int);
    int32x4_t vsliq_n_s32 (int32x4_t, int32x4_t, const int);
    int16x8_t vsliq_n_s16 (int16x8_t, int16x8_t, const int);
    int8x16_t vsliq_n_s8 (int8x16_t, int8x16_t, const int);
    uint64x2_t vsliq_n_u64 (uint64x2_t, uint64x2_t, const int);
    int64x2_t vsliq_n_s64 (int64x2_t, int64x2_t, const int);
    poly16x8_t vsliq_n_p16 (poly16x8_t, poly16x8_t, const int);
    poly8x16_t vsliq_n_p8 (poly8x16_t, poly8x16_t, const int);
    float32x2_t vabs_f32 (float32x2_t);
    int32x2_t vabs_s32 (int32x2_t);
    int16x4_t vabs_s16 (int16x4_t);
    int8x8_t vabs_s8 (int8x8_t);
    float32x4_t vabsq_f32 (float32x4_t);
    int32x4_t vabsq_s32 (int32x4_t);
    int16x8_t vabsq_s16 (int16x8_t);
    int8x16_t vabsq_s8 (int8x16_t);
    int32x2_t vqabs_s32 (int32x2_t);
    int16x4_t vqabs_s16 (int16x4_t);
    int8x8_t vqabs_s8 (int8x8_t);
    int32x4_t vqabsq_s32 (int32x4_t);
    int16x8_t vqabsq_s16 (int16x8_t);
    int8x16_t vqabsq_s8 (int8x16_t);
    float32x2_t vneg_f32 (float32x2_t);
    int32x2_t vneg_s32 (int32x2_t);
    int16x4_t vneg_s16 (int16x4_t);
    int8x8_t vneg_s8 (int8x8_t);
    float32x4_t vnegq_f32 (float32x4_t);
    int32x4_t vnegq_s32 (int32x4_t);
    int16x8_t vnegq_s16 (int16x8_t);
    int8x16_t vnegq_s8 (int8x16_t);
    int32x2_t vqneg_s32 (int32x2_t);
    int16x4_t vqneg_s16 (int16x4_t);
    int8x8_t vqneg_s8 (int8x8_t);
    int32x4_t vqnegq_s32 (int32x4_t);
    int16x8_t vqnegq_s16 (int16x8_t);
    int8x16_t vqnegq_s8 (int8x16_t);
    uint32x2_t vmvn_u32 (uint32x2_t);
    uint16x4_t vmvn_u16 (uint16x4_t);
    uint8x8_t vmvn_u8 (uint8x8_t);
    int32x2_t vmvn_s32 (int32x2_t);
    int16x4_t vmvn_s16 (int16x4_t);
    int8x8_t vmvn_s8 (int8x8_t);
    poly8x8_t vmvn_p8 (poly8x8_t);
    uint32x4_t vmvnq_u32 (uint32x4_t);
    uint16x8_t vmvnq_u16 (uint16x8_t);
    uint8x16_t vmvnq_u8 (uint8x16_t);
    int32x4_t vmvnq_s32 (int32x4_t);
    int16x8_t vmvnq_s16 (int16x8_t);
    int8x16_t vmvnq_s8 (int8x16_t);
    poly8x16_t vmvnq_p8 (poly8x16_t);
    int32x2_t vcls_s32 (int32x2_t);
    int16x4_t vcls_s16 (int16x4_t);
    int8x8_t vcls_s8 (int8x8_t);
    int32x4_t vclsq_s32 (int32x4_t);
    int16x8_t vclsq_s16 (int16x8_t);
    int8x16_t vclsq_s8 (int8x16_t);
    uint32x2_t vclz_u32 (uint32x2_t);
    uint16x4_t vclz_u16 (uint16x4_t);
    uint8x8_t vclz_u8 (uint8x8_t);
    int32x2_t vclz_s32 (int32x2_t);
    int16x4_t vclz_s16 (int16x4_t);
    int8x8_t vclz_s8 (int8x8_t);
    uint32x4_t vclzq_u32 (uint32x4_t);
    uint16x8_t vclzq_u16 (uint16x8_t);
    uint8x16_t vclzq_u8 (uint8x16_t);
    int32x4_t vclzq_s32 (int32x4_t);
    int16x8_t vclzq_s16 (int16x8_t);
    int8x16_t vclzq_s8 (int8x16_t);
    uint8x8_t vcnt_u8 (uint8x8_t);
    int8x8_t vcnt_s8 (int8x8_t);
    poly8x8_t vcnt_p8 (poly8x8_t);
    uint8x16_t vcntq_u8 (uint8x16_t);
    int8x16_t vcntq_s8 (int8x16_t);
    poly8x16_t vcntq_p8 (poly8x16_t);
    float32x2_t vrecpe_f32 (float32x2_t);
    uint32x2_t vrecpe_u32 (uint32x2_t);
    float32x4_t vrecpeq_f32 (float32x4_t);
    uint32x4_t vrecpeq_u32 (uint32x4_t);
    float32x2_t vrsqrte_f32 (float32x2_t);
    uint32x2_t vrsqrte_u32 (uint32x2_t);
    float32x4_t vrsqrteq_f32 (float32x4_t);
    uint32x4_t vrsqrteq_u32 (uint32x4_t);
    uint32_t vget_lane_u32 (uint32x2_t, const int);
    uint16_t vget_lane_u16 (uint16x4_t, const int);
    uint8_t vget_lane_u8 (uint8x8_t, const int);
    int32_t vget_lane_s32 (int32x2_t, const int);
    int16_t vget_lane_s16 (int16x4_t, const int);
    int8_t vget_lane_s8 (int8x8_t, const int);
    float32_t vget_lane_f32 (float32x2_t, const int);
    poly16_t vget_lane_p16 (poly16x4_t, const int);
    poly8_t vget_lane_p8 (poly8x8_t, const int);
    uint64_t vget_lane_u64 (uint64x1_t, const int);
    int64_t vget_lane_s64 (int64x1_t, const int);
    uint32_t vgetq_lane_u32 (uint32x4_t, const int);
    uint16_t vgetq_lane_u16 (uint16x8_t, const int);
    uint8_t vgetq_lane_u8 (uint8x16_t, const int);
    int32_t vgetq_lane_s32 (int32x4_t, const int);
    int16_t vgetq_lane_s16 (int16x8_t, const int);
    int8_t vgetq_lane_s8 (int8x16_t, const int);
    float32_t vgetq_lane_f32 (float32x4_t, const int);
    poly16_t vgetq_lane_p16 (poly16x8_t, const int);
    poly8_t vgetq_lane_p8 (poly8x16_t, const int);
    uint64_t vgetq_lane_u64 (uint64x2_t, const int);
    int64_t vgetq_lane_s64 (int64x2_t, const int);
    uint32x2_t vset_lane_u32 (uint32_t, uint32x2_t, const int);
    uint16x4_t vset_lane_u16 (uint16_t, uint16x4_t, const int);
    uint8x8_t vset_lane_u8 (uint8_t, uint8x8_t, const int);
    int32x2_t vset_lane_s32 (int32_t, int32x2_t, const int);
    int16x4_t vset_lane_s16 (int16_t, int16x4_t, const int);
    int8x8_t vset_lane_s8 (int8_t, int8x8_t, const int);
    float32x2_t vset_lane_f32 (float32_t, float32x2_t, const int);
    poly16x4_t vset_lane_p16 (poly16_t, poly16x4_t, const int);
    poly8x8_t vset_lane_p8 (poly8_t, poly8x8_t, const int);
    uint64x1_t vset_lane_u64 (uint64_t, uint64x1_t, const int);
    int64x1_t vset_lane_s64 (int64_t, int64x1_t, const int);
    uint32x4_t vsetq_lane_u32 (uint32_t, uint32x4_t, const int);
    uint16x8_t vsetq_lane_u16 (uint16_t, uint16x8_t, const int);
    uint8x16_t vsetq_lane_u8 (uint8_t, uint8x16_t, const int);
    int32x4_t vsetq_lane_s32 (int32_t, int32x4_t, const int);
    int16x8_t vsetq_lane_s16 (int16_t, int16x8_t, const int);
    int8x16_t vsetq_lane_s8 (int8_t, int8x16_t, const int);
    float32x4_t vsetq_lane_f32 (float32_t, float32x4_t, const int);
    poly16x8_t vsetq_lane_p16 (poly16_t, poly16x8_t, const int);
    poly8x16_t vsetq_lane_p8 (poly8_t, poly8x16_t, const int);
    uint64x2_t vsetq_lane_u64 (uint64_t, uint64x2_t, const int);
    int64x2_t vsetq_lane_s64 (int64_t, int64x2_t, const int);
    uint32x2_t vcreate_u32 (uint64_t);
    uint16x4_t vcreate_u16 (uint64_t);
    uint8x8_t vcreate_u8 (uint64_t);
    int32x2_t vcreate_s32 (uint64_t);
    int16x4_t vcreate_s16 (uint64_t);
    int8x8_t vcreate_s8 (uint64_t);
    uint64x1_t vcreate_u64 (uint64_t);
    int64x1_t vcreate_s64 (uint64_t);
    float32x2_t vcreate_f32 (uint64_t);
    poly16x4_t vcreate_p16 (uint64_t);
    poly8x8_t vcreate_p8 (uint64_t);
    uint32x2_t vdup_n_u32 (uint32_t);
    uint16x4_t vdup_n_u16 (uint16_t);
    uint8x8_t vdup_n_u8 (uint8_t);
    int32x2_t vdup_n_s32 (int32_t);
    int16x4_t vdup_n_s16 (int16_t);
    int8x8_t vdup_n_s8 (int8_t);
    float32x2_t vdup_n_f32 (float32_t);
    poly16x4_t vdup_n_p16 (poly16_t);
    poly8x8_t vdup_n_p8 (poly8_t);
    uint64x1_t vdup_n_u64 (uint64_t);
    int64x1_t vdup_n_s64 (int64_t);
    uint32x4_t vdupq_n_u32 (uint32_t);
    uint16x8_t vdupq_n_u16 (uint16_t);
    uint8x16_t vdupq_n_u8 (uint8_t);
    int32x4_t vdupq_n_s32 (int32_t);
    int16x8_t vdupq_n_s16 (int16_t);
    int8x16_t vdupq_n_s8 (int8_t);
    float32x4_t vdupq_n_f32 (float32_t);
    poly16x8_t vdupq_n_p16 (poly16_t);
    poly8x16_t vdupq_n_p8 (poly8_t);
    uint64x2_t vdupq_n_u64 (uint64_t);
    int64x2_t vdupq_n_s64 (int64_t);
    uint32x2_t vmov_n_u32 (uint32_t);
    uint16x4_t vmov_n_u16 (uint16_t);
    uint8x8_t vmov_n_u8 (uint8_t);
    int32x2_t vmov_n_s32 (int32_t);
    int16x4_t vmov_n_s16 (int16_t);
    int8x8_t vmov_n_s8 (int8_t);
    float32x2_t vmov_n_f32 (float32_t);
    poly16x4_t vmov_n_p16 (poly16_t);
    poly8x8_t vmov_n_p8 (poly8_t);
    uint64x1_t vmov_n_u64 (uint64_t);
    int64x1_t vmov_n_s64 (int64_t);
    uint32x4_t vmovq_n_u32 (uint32_t);
    uint16x8_t vmovq_n_u16 (uint16_t);
    uint8x16_t vmovq_n_u8 (uint8_t);
    int32x4_t vmovq_n_s32 (int32_t);
    int16x8_t vmovq_n_s16 (int16_t);
    int8x16_t vmovq_n_s8 (int8_t);
    float32x4_t vmovq_n_f32 (float32_t);
    poly16x8_t vmovq_n_p16 (poly16_t);
    poly8x16_t vmovq_n_p8 (poly8_t);
    uint64x2_t vmovq_n_u64 (uint64_t);
    int64x2_t vmovq_n_s64 (int64_t);
    uint32x2_t vdup_lane_u32 (uint32x2_t, const int);
    uint16x4_t vdup_lane_u16 (uint16x4_t, const int);
    uint8x8_t vdup_lane_u8 (uint8x8_t, const int);
    int32x2_t vdup_lane_s32 (int32x2_t, const int);
    int16x4_t vdup_lane_s16 (int16x4_t, const int);
    int8x8_t vdup_lane_s8 (int8x8_t, const int);
    float32x2_t vdup_lane_f32 (float32x2_t, const int);
    poly16x4_t vdup_lane_p16 (poly16x4_t, const int);
    poly8x8_t vdup_lane_p8 (poly8x8_t, const int);
    uint64x1_t vdup_lane_u64 (uint64x1_t, const int);
    int64x1_t vdup_lane_s64 (int64x1_t, const int);
    uint32x4_t vdupq_lane_u32 (uint32x2_t, const int);
    uint16x8_t vdupq_lane_u16 (uint16x4_t, const int);
    uint8x16_t vdupq_lane_u8 (uint8x8_t, const int);
    int32x4_t vdupq_lane_s32 (int32x2_t, const int);
    int16x8_t vdupq_lane_s16 (int16x4_t, const int);
    int8x16_t vdupq_lane_s8 (int8x8_t, const int);
    float32x4_t vdupq_lane_f32 (float32x2_t, const int);
    poly16x8_t vdupq_lane_p16 (poly16x4_t, const int);
    poly8x16_t vdupq_lane_p8 (poly8x8_t, const int);
    uint64x2_t vdupq_lane_u64 (uint64x1_t, const int);
    int64x2_t vdupq_lane_s64 (int64x1_t, const int);
    uint32x4_t vcombine_u32 (uint32x2_t, uint32x2_t);
    uint16x8_t vcombine_u16 (uint16x4_t, uint16x4_t);
    uint8x16_t vcombine_u8 (uint8x8_t, uint8x8_t);
    int32x4_t vcombine_s32 (int32x2_t, int32x2_t);
    int16x8_t vcombine_s16 (int16x4_t, int16x4_t);
    int8x16_t vcombine_s8 (int8x8_t, int8x8_t);
    uint64x2_t vcombine_u64 (uint64x1_t, uint64x1_t);
    int64x2_t vcombine_s64 (int64x1_t, int64x1_t);
    float32x4_t vcombine_f32 (float32x2_t, float32x2_t);
    poly16x8_t vcombine_p16 (poly16x4_t, poly16x4_t);
    poly8x16_t vcombine_p8 (poly8x8_t, poly8x8_t);
    uint32x2_t vget_high_u32 (uint32x4_t);
    uint16x4_t vget_high_u16 (uint16x8_t);
    uint8x8_t vget_high_u8 (uint8x16_t);
    int32x2_t vget_high_s32 (int32x4_t);
    int16x4_t vget_high_s16 (int16x8_t);
    int8x8_t vget_high_s8 (int8x16_t);
    uint64x1_t vget_high_u64 (uint64x2_t);
    int64x1_t vget_high_s64 (int64x2_t);
    float32x2_t vget_high_f32 (float32x4_t);
    poly16x4_t vget_high_p16 (poly16x8_t);
    poly8x8_t vget_high_p8 (poly8x16_t);
    uint32x2_t vget_low_u32 (uint32x4_t);
    uint16x4_t vget_low_u16 (uint16x8_t);
    uint8x8_t vget_low_u8 (uint8x16_t);
    int32x2_t vget_low_s32 (int32x4_t);
    int16x4_t vget_low_s16 (int16x8_t);
    int8x8_t vget_low_s8 (int8x16_t);
    float32x2_t vget_low_f32 (float32x4_t);
    poly16x4_t vget_low_p16 (poly16x8_t);
    poly8x8_t vget_low_p8 (poly8x16_t);
    uint64x1_t vget_low_u64 (uint64x2_t);
    int64x1_t vget_low_s64 (int64x2_t);
    float32x2_t vcvt_f32_u32 (uint32x2_t);
    float32x2_t vcvt_f32_s32 (int32x2_t);
    uint32x2_t vcvt_u32_f32 (float32x2_t);
    int32x2_t vcvt_s32_f32 (float32x2_t);
    float32x4_t vcvtq_f32_u32 (uint32x4_t);
    float32x4_t vcvtq_f32_s32 (int32x4_t);
    uint32x4_t vcvtq_u32_f32 (float32x4_t);
    int32x4_t vcvtq_s32_f32 (float32x4_t);
    float32x2_t vcvt_n_f32_u32 (uint32x2_t, const int);
    float32x2_t vcvt_n_f32_s32 (int32x2_t, const int);
    uint32x2_t vcvt_n_u32_f32 (float32x2_t, const int);
    int32x2_t vcvt_n_s32_f32 (float32x2_t, const int);
    float32x4_t vcvtq_n_f32_u32 (uint32x4_t, const int);
    float32x4_t vcvtq_n_f32_s32 (int32x4_t, const int);
    uint32x4_t vcvtq_n_u32_f32 (float32x4_t, const int);
    int32x4_t vcvtq_n_s32_f32 (float32x4_t, const int);
    uint32x2_t vmovn_u64 (uint64x2_t);
    uint16x4_t vmovn_u32 (uint32x4_t);
    uint8x8_t vmovn_u16 (uint16x8_t);
    int32x2_t vmovn_s64 (int64x2_t);
    int16x4_t vmovn_s32 (int32x4_t);
    int8x8_t vmovn_s16 (int16x8_t);
    uint32x2_t vqmovn_u64 (uint64x2_t);
    uint16x4_t vqmovn_u32 (uint32x4_t);
    uint8x8_t vqmovn_u16 (uint16x8_t);
    int32x2_t vqmovn_s64 (int64x2_t);
    int16x4_t vqmovn_s32 (int32x4_t);
    int8x8_t vqmovn_s16 (int16x8_t);
    uint32x2_t vqmovun_s64 (int64x2_t);
    uint16x4_t vqmovun_s32 (int32x4_t);
    uint8x8_t vqmovun_s16 (int16x8_t);
    uint64x2_t vmovl_u32 (uint32x2_t);
    uint32x4_t vmovl_u16 (uint16x4_t);
    uint16x8_t vmovl_u8 (uint8x8_t);
    int64x2_t vmovl_s32 (int32x2_t);
    int32x4_t vmovl_s16 (int16x4_t);
    int16x8_t vmovl_s8 (int8x8_t);
    poly8x8_t vtbl1_p8 (poly8x8_t, uint8x8_t);
    int8x8_t vtbl1_s8 (int8x8_t, int8x8_t);
    uint8x8_t vtbl1_u8 (uint8x8_t, uint8x8_t);
    poly8x8_t vtbl2_p8 (poly8x8x2_t, uint8x8_t);
    int8x8_t vtbl2_s8 (int8x8x2_t, int8x8_t);
    uint8x8_t vtbl2_u8 (uint8x8x2_t, uint8x8_t);
    poly8x8_t vtbl3_p8 (poly8x8x3_t, uint8x8_t);
    int8x8_t vtbl3_s8 (int8x8x3_t, int8x8_t);
    uint8x8_t vtbl3_u8 (uint8x8x3_t, uint8x8_t);
    poly8x8_t vtbl4_p8 (poly8x8x4_t, uint8x8_t);
    int8x8_t vtbl4_s8 (int8x8x4_t, int8x8_t);
    uint8x8_t vtbl4_u8 (uint8x8x4_t, uint8x8_t);
    poly8x8_t vtbx1_p8 (poly8x8_t, poly8x8_t, uint8x8_t);
    int8x8_t vtbx1_s8 (int8x8_t, int8x8_t, int8x8_t);
    uint8x8_t vtbx1_u8 (uint8x8_t, uint8x8_t, uint8x8_t);
    poly8x8_t vtbx2_p8 (poly8x8_t, poly8x8x2_t, uint8x8_t);
    int8x8_t vtbx2_s8 (int8x8_t, int8x8x2_t, int8x8_t);
    uint8x8_t vtbx2_u8 (uint8x8_t, uint8x8x2_t, uint8x8_t);
    poly8x8_t vtbx3_p8 (poly8x8_t, poly8x8x3_t, uint8x8_t);
    int8x8_t vtbx3_s8 (int8x8_t, int8x8x3_t, int8x8_t);
    uint8x8_t vtbx3_u8 (uint8x8_t, uint8x8x3_t, uint8x8_t);
    poly8x8_t vtbx4_p8 (poly8x8_t, poly8x8x4_t, uint8x8_t);
    int8x8_t vtbx4_s8 (int8x8_t, int8x8x4_t, int8x8_t);
    uint8x8_t vtbx4_u8 (uint8x8_t, uint8x8x4_t, uint8x8_t);
    float32x2_t vmul_lane_f32 (float32x2_t, float32x2_t, const int);
    uint32x2_t vmul_lane_u32 (uint32x2_t, uint32x2_t, const int);
    uint16x4_t vmul_lane_u16 (uint16x4_t, uint16x4_t, const int);
    int32x2_t vmul_lane_s32 (int32x2_t, int32x2_t, const int);
    int16x4_t vmul_lane_s16 (int16x4_t, int16x4_t, const int);
    float32x4_t vmulq_lane_f32 (float32x4_t, float32x2_t, const int);
    uint32x4_t vmulq_lane_u32 (uint32x4_t, uint32x2_t, const int);
    uint16x8_t vmulq_lane_u16 (uint16x8_t, uint16x4_t, const int);
    int32x4_t vmulq_lane_s32 (int32x4_t, int32x2_t, const int);
    int16x8_t vmulq_lane_s16 (int16x8_t, int16x4_t, const int);
    uint64x2_t vmull_lane_u32 (uint32x2_t, uint32x2_t, const int);
    uint32x4_t vmull_lane_u16 (uint16x4_t, uint16x4_t, const int);
    int64x2_t vmull_lane_s32 (int32x2_t, int32x2_t, const int);
    int32x4_t vmull_lane_s16 (int16x4_t, int16x4_t, const int);
    int64x2_t vqdmull_lane_s32 (int32x2_t, int32x2_t, const int);
    int32x4_t vqdmull_lane_s16 (int16x4_t, int16x4_t, const int);
    int32x4_t vqdmulhq_lane_s32 (int32x4_t, int32x2_t, const int);
    int16x8_t vqdmulhq_lane_s16 (int16x8_t, int16x4_t, const int);
    int32x2_t vqdmulh_lane_s32 (int32x2_t, int32x2_t, const int);
    int16x4_t vqdmulh_lane_s16 (int16x4_t, int16x4_t, const int);
    int32x4_t vqrdmulhq_lane_s32 (int32x4_t, int32x2_t, const int);
    int16x8_t vqrdmulhq_lane_s16 (int16x8_t, int16x4_t, const int);
    int32x2_t vqrdmulh_lane_s32 (int32x2_t, int32x2_t, const int);
    int16x4_t vqrdmulh_lane_s16 (int16x4_t, int16x4_t, const int);
    float32x2_t vmla_lane_f32 (float32x2_t, float32x2_t, float32x2_t, const int);
    uint32x2_t vmla_lane_u32 (uint32x2_t, uint32x2_t, uint32x2_t, const int);
    uint16x4_t vmla_lane_u16 (uint16x4_t, uint16x4_t, uint16x4_t, const int);
    int32x2_t vmla_lane_s32 (int32x2_t, int32x2_t, int32x2_t, const int);
    int16x4_t vmla_lane_s16 (int16x4_t, int16x4_t, int16x4_t, const int);
    float32x4_t vmlaq_lane_f32 (float32x4_t, float32x4_t, float32x2_t, const int);
    uint32x4_t vmlaq_lane_u32 (uint32x4_t, uint32x4_t, uint32x2_t, const int);
    uint16x8_t vmlaq_lane_u16 (uint16x8_t, uint16x8_t, uint16x4_t, const int);
    int32x4_t vmlaq_lane_s32 (int32x4_t, int32x4_t, int32x2_t, const int);
    int16x8_t vmlaq_lane_s16 (int16x8_t, int16x8_t, int16x4_t, const int);
    uint64x2_t vmlal_lane_u32 (uint64x2_t, uint32x2_t, uint32x2_t, const int);
    uint32x4_t vmlal_lane_u16 (uint32x4_t, uint16x4_t, uint16x4_t, const int);
    int64x2_t vmlal_lane_s32 (int64x2_t, int32x2_t, int32x2_t, const int);
    int32x4_t vmlal_lane_s16 (int32x4_t, int16x4_t, int16x4_t, const int);
    int64x2_t vqdmlal_lane_s32 (int64x2_t, int32x2_t, int32x2_t, const int);
    int32x4_t vqdmlal_lane_s16 (int32x4_t, int16x4_t, int16x4_t, const int);
    float32x2_t vmls_lane_f32 (float32x2_t, float32x2_t, float32x2_t, const int);
    uint32x2_t vmls_lane_u32 (uint32x2_t, uint32x2_t, uint32x2_t, const int);
    uint16x4_t vmls_lane_u16 (uint16x4_t, uint16x4_t, uint16x4_t, const int);
    int32x2_t vmls_lane_s32 (int32x2_t, int32x2_t, int32x2_t, const int);
    int16x4_t vmls_lane_s16 (int16x4_t, int16x4_t, int16x4_t, const int);
    float32x4_t vmlsq_lane_f32 (float32x4_t, float32x4_t, float32x2_t, const int);
    uint32x4_t vmlsq_lane_u32 (uint32x4_t, uint32x4_t, uint32x2_t, const int);
    uint16x8_t vmlsq_lane_u16 (uint16x8_t, uint16x8_t, uint16x4_t, const int);
    int32x4_t vmlsq_lane_s32 (int32x4_t, int32x4_t, int32x2_t, const int);
    int16x8_t vmlsq_lane_s16 (int16x8_t, int16x8_t, int16x4_t, const int);
    uint64x2_t vmlsl_lane_u32 (uint64x2_t, uint32x2_t, uint32x2_t, const int);
    uint32x4_t vmlsl_lane_u16 (uint32x4_t, uint16x4_t, uint16x4_t, const int);
    int64x2_t vmlsl_lane_s32 (int64x2_t, int32x2_t, int32x2_t, const int);
    int32x4_t vmlsl_lane_s16 (int32x4_t, int16x4_t, int16x4_t, const int);
    int64x2_t vqdmlsl_lane_s32 (int64x2_t, int32x2_t, int32x2_t, const int);
    int32x4_t vqdmlsl_lane_s16 (int32x4_t, int16x4_t, int16x4_t, const int);
    float32x2_t vmul_n_f32 (float32x2_t, float32_t);
    uint32x2_t vmul_n_u32 (uint32x2_t, uint32_t);
    uint16x4_t vmul_n_u16 (uint16x4_t, uint16_t);
    int32x2_t vmul_n_s32 (int32x2_t, int32_t);
    int16x4_t vmul_n_s16 (int16x4_t, int16_t);
    float32x4_t vmulq_n_f32 (float32x4_t, float32_t);
    uint32x4_t vmulq_n_u32 (uint32x4_t, uint32_t);
    uint16x8_t vmulq_n_u16 (uint16x8_t, uint16_t);
    int32x4_t vmulq_n_s32 (int32x4_t, int32_t);
    int16x8_t vmulq_n_s16 (int16x8_t, int16_t);
    uint64x2_t vmull_n_u32 (uint32x2_t, uint32_t);
    uint32x4_t vmull_n_u16 (uint16x4_t, uint16_t);
    int64x2_t vmull_n_s32 (int32x2_t, int32_t);
    int32x4_t vmull_n_s16 (int16x4_t, int16_t);
    int64x2_t vqdmull_n_s32 (int32x2_t, int32_t);
    int32x4_t vqdmull_n_s16 (int16x4_t, int16_t);
    int32x4_t vqdmulhq_n_s32 (int32x4_t, int32_t);
    int16x8_t vqdmulhq_n_s16 (int16x8_t, int16_t);
    int32x2_t vqdmulh_n_s32 (int32x2_t, int32_t);
    int16x4_t vqdmulh_n_s16 (int16x4_t, int16_t);
    int32x4_t vqrdmulhq_n_s32 (int32x4_t, int32_t);
    int16x8_t vqrdmulhq_n_s16 (int16x8_t, int16_t);
    int32x2_t vqrdmulh_n_s32 (int32x2_t, int32_t);
    int16x4_t vqrdmulh_n_s16 (int16x4_t, int16_t);
    float32x2_t vmla_n_f32 (float32x2_t, float32x2_t, float32_t);
    uint32x2_t vmla_n_u32 (uint32x2_t, uint32x2_t, uint32_t);
    uint16x4_t vmla_n_u16 (uint16x4_t, uint16x4_t, uint16_t);
    int32x2_t vmla_n_s32 (int32x2_t, int32x2_t, int32_t);
    int16x4_t vmla_n_s16 (int16x4_t, int16x4_t, int16_t);
    float32x4_t vmlaq_n_f32 (float32x4_t, float32x4_t, float32_t);
    uint32x4_t vmlaq_n_u32 (uint32x4_t, uint32x4_t, uint32_t);
    uint16x8_t vmlaq_n_u16 (uint16x8_t, uint16x8_t, uint16_t);
    int32x4_t vmlaq_n_s32 (int32x4_t, int32x4_t, int32_t);
    int16x8_t vmlaq_n_s16 (int16x8_t, int16x8_t, int16_t);
    uint64x2_t vmlal_n_u32 (uint64x2_t, uint32x2_t, uint32_t);
    uint32x4_t vmlal_n_u16 (uint32x4_t, uint16x4_t, uint16_t);
    int64x2_t vmlal_n_s32 (int64x2_t, int32x2_t, int32_t);
    int32x4_t vmlal_n_s16 (int32x4_t, int16x4_t, int16_t);
    int64x2_t vqdmlal_n_s32 (int64x2_t, int32x2_t, int32_t);
    int32x4_t vqdmlal_n_s16 (int32x4_t, int16x4_t, int16_t);
    float32x2_t vmls_n_f32 (float32x2_t, float32x2_t, float32_t);
    uint32x2_t vmls_n_u32 (uint32x2_t, uint32x2_t, uint32_t);
    uint16x4_t vmls_n_u16 (uint16x4_t, uint16x4_t, uint16_t);
    int32x2_t vmls_n_s32 (int32x2_t, int32x2_t, int32_t);
    int16x4_t vmls_n_s16 (int16x4_t, int16x4_t, int16_t);
    float32x4_t vmlsq_n_f32 (float32x4_t, float32x4_t, float32_t);
    uint32x4_t vmlsq_n_u32 (uint32x4_t, uint32x4_t, uint32_t);
    uint16x8_t vmlsq_n_u16 (uint16x8_t, uint16x8_t, uint16_t);
    int32x4_t vmlsq_n_s32 (int32x4_t, int32x4_t, int32_t);
    int16x8_t vmlsq_n_s16 (int16x8_t, int16x8_t, int16_t);
    uint64x2_t vmlsl_n_u32 (uint64x2_t, uint32x2_t, uint32_t);
    uint32x4_t vmlsl_n_u16 (uint32x4_t, uint16x4_t, uint16_t);
    int64x2_t vmlsl_n_s32 (int64x2_t, int32x2_t, int32_t);
    int32x4_t vmlsl_n_s16 (int32x4_t, int16x4_t, int16_t);
    int64x2_t vqdmlsl_n_s32 (int64x2_t, int32x2_t, int32_t);
    int32x4_t vqdmlsl_n_s16 (int32x4_t, int16x4_t, int16_t);
    uint32x2_t vext_u32 (uint32x2_t, uint32x2_t, const int);
    uint16x4_t vext_u16 (uint16x4_t, uint16x4_t, const int);
    uint8x8_t vext_u8 (uint8x8_t, uint8x8_t, const int);
    int32x2_t vext_s32 (int32x2_t, int32x2_t, const int);
    int16x4_t vext_s16 (int16x4_t, int16x4_t, const int);
    int8x8_t vext_s8 (int8x8_t, int8x8_t, const int);
    uint64x1_t vext_u64 (uint64x1_t, uint64x1_t, const int);
    int64x1_t vext_s64 (int64x1_t, int64x1_t, const int);
    float32x2_t vext_f32 (float32x2_t, float32x2_t, const int);
    poly16x4_t vext_p16 (poly16x4_t, poly16x4_t, const int);
    poly8x8_t vext_p8 (poly8x8_t, poly8x8_t, const int);
    uint32x4_t vextq_u32 (uint32x4_t, uint32x4_t, const int);
    uint16x8_t vextq_u16 (uint16x8_t, uint16x8_t, const int);
    uint8x16_t vextq_u8 (uint8x16_t, uint8x16_t, const int);
    int32x4_t vextq_s32 (int32x4_t, int32x4_t, const int);
    int16x8_t vextq_s16 (int16x8_t, int16x8_t, const int);
    int8x16_t vextq_s8 (int8x16_t, int8x16_t, const int);
    uint64x2_t vextq_u64 (uint64x2_t, uint64x2_t, const int);
    int64x2_t vextq_s64 (int64x2_t, int64x2_t, const int);
    float32x4_t vextq_f32 (float32x4_t, float32x4_t, const int);
    poly16x8_t vextq_p16 (poly16x8_t, poly16x8_t, const int);
    poly8x16_t vextq_p8 (poly8x16_t, poly8x16_t, const int);
    uint32x2_t vrev64_u32 (uint32x2_t);
    uint16x4_t vrev64_u16 (uint16x4_t);
    uint8x8_t vrev64_u8 (uint8x8_t);
    int32x2_t vrev64_s32 (int32x2_t);
    int16x4_t vrev64_s16 (int16x4_t);
    int8x8_t vrev64_s8 (int8x8_t);
    float32x2_t vrev64_f32 (float32x2_t);
    poly16x4_t vrev64_p16 (poly16x4_t);
    poly8x8_t vrev64_p8 (poly8x8_t);
    uint32x4_t vrev64q_u32 (uint32x4_t);
    uint16x8_t vrev64q_u16 (uint16x8_t);
    uint8x16_t vrev64q_u8 (uint8x16_t);
    int32x4_t vrev64q_s32 (int32x4_t);
    int16x8_t vrev64q_s16 (int16x8_t);
    int8x16_t vrev64q_s8 (int8x16_t);
    float32x4_t vrev64q_f32 (float32x4_t);
    poly16x8_t vrev64q_p16 (poly16x8_t);
    poly8x16_t vrev64q_p8 (poly8x16_t);
    uint16x4_t vrev32_u16 (uint16x4_t);
    int16x4_t vrev32_s16 (int16x4_t);
    uint8x8_t vrev32_u8 (uint8x8_t);
    int8x8_t vrev32_s8 (int8x8_t);
    poly16x4_t vrev32_p16 (poly16x4_t);
    poly8x8_t vrev32_p8 (poly8x8_t);
    uint16x8_t vrev32q_u16 (uint16x8_t);
    int16x8_t vrev32q_s16 (int16x8_t);
    uint8x16_t vrev32q_u8 (uint8x16_t);
    int8x16_t vrev32q_s8 (int8x16_t);
    poly16x8_t vrev32q_p16 (poly16x8_t);
    poly8x16_t vrev32q_p8 (poly8x16_t);
    uint8x8_t vrev16_u8 (uint8x8_t);
    int8x8_t vrev16_s8 (int8x8_t);
    poly8x8_t vrev16_p8 (poly8x8_t);
    uint8x16_t vrev16q_u8 (uint8x16_t);
    int8x16_t vrev16q_s8 (int8x16_t);
    poly8x16_t vrev16q_p8 (poly8x16_t);
    uint32x2_t vbsl_u32 (uint32x2_t, uint32x2_t, uint32x2_t);
    uint16x4_t vbsl_u16 (uint16x4_t, uint16x4_t, uint16x4_t);
    uint8x8_t vbsl_u8 (uint8x8_t, uint8x8_t, uint8x8_t);
    int32x2_t vbsl_s32 (uint32x2_t, int32x2_t, int32x2_t);
    int16x4_t vbsl_s16 (uint16x4_t, int16x4_t, int16x4_t);
    int8x8_t vbsl_s8 (uint8x8_t, int8x8_t, int8x8_t);
    uint64x1_t vbsl_u64 (uint64x1_t, uint64x1_t, uint64x1_t);
    int64x1_t vbsl_s64 (uint64x1_t, int64x1_t, int64x1_t);
    float32x2_t vbsl_f32 (uint32x2_t, float32x2_t, float32x2_t);
    poly16x4_t vbsl_p16 (uint16x4_t, poly16x4_t, poly16x4_t);
    poly8x8_t vbsl_p8 (uint8x8_t, poly8x8_t, poly8x8_t);
    uint32x4_t vbslq_u32 (uint32x4_t, uint32x4_t, uint32x4_t);
    uint16x8_t vbslq_u16 (uint16x8_t, uint16x8_t, uint16x8_t);
    uint8x16_t vbslq_u8 (uint8x16_t, uint8x16_t, uint8x16_t);
    int32x4_t vbslq_s32 (uint32x4_t, int32x4_t, int32x4_t);
    int16x8_t vbslq_s16 (uint16x8_t, int16x8_t, int16x8_t);
    int8x16_t vbslq_s8 (uint8x16_t, int8x16_t, int8x16_t);
    uint64x2_t vbslq_u64 (uint64x2_t, uint64x2_t, uint64x2_t);
    int64x2_t vbslq_s64 (uint64x2_t, int64x2_t, int64x2_t);
    float32x4_t vbslq_f32 (uint32x4_t, float32x4_t, float32x4_t);
    poly16x8_t vbslq_p16 (uint16x8_t, poly16x8_t, poly16x8_t);
    poly8x16_t vbslq_p8 (uint8x16_t, poly8x16_t, poly8x16_t);
    uint16x4x2_t vtrn_u16 (uint16x4_t, uint16x4_t);
    uint8x8x2_t vtrn_u8 (uint8x8_t, uint8x8_t);
    int16x4x2_t vtrn_s16 (int16x4_t, int16x4_t);
    int8x8x2_t vtrn_s8 (int8x8_t, int8x8_t);
    poly16x4x2_t vtrn_p16 (poly16x4_t, poly16x4_t);
    poly8x8x2_t vtrn_p8 (poly8x8_t, poly8x8_t);
    float32x2x2_t vtrn_f32 (float32x2_t, float32x2_t);
    uint32x2x2_t vtrn_u32 (uint32x2_t, uint32x2_t);
    int32x2x2_t vtrn_s32 (int32x2_t, int32x2_t);
    uint32x4x2_t vtrnq_u32 (uint32x4_t, uint32x4_t);
    uint16x8x2_t vtrnq_u16 (uint16x8_t, uint16x8_t);
    uint8x16x2_t vtrnq_u8 (uint8x16_t, uint8x16_t);
    int32x4x2_t vtrnq_s32 (int32x4_t, int32x4_t);
    int16x8x2_t vtrnq_s16 (int16x8_t, int16x8_t);
    int8x16x2_t vtrnq_s8 (int8x16_t, int8x16_t);
    float32x4x2_t vtrnq_f32 (float32x4_t, float32x4_t);
    poly16x8x2_t vtrnq_p16 (poly16x8_t, poly16x8_t);
    poly8x16x2_t vtrnq_p8 (poly8x16_t, poly8x16_t);
    uint16x4x2_t vzip_u16 (uint16x4_t, uint16x4_t);
    uint8x8x2_t vzip_u8 (uint8x8_t, uint8x8_t);
    int16x4x2_t vzip_s16 (int16x4_t, int16x4_t);
    int8x8x2_t vzip_s8 (int8x8_t, int8x8_t);
    poly16x4x2_t vzip_p16 (poly16x4_t, poly16x4_t);
    poly8x8x2_t vzip_p8 (poly8x8_t, poly8x8_t);
    float32x2x2_t vzip_f32 (float32x2_t, float32x2_t);
    uint32x2x2_t vzip_u32 (uint32x2_t, uint32x2_t);
    int32x2x2_t vzip_s32 (int32x2_t, int32x2_t);
    uint32x4x2_t vzipq_u32 (uint32x4_t, uint32x4_t);
    uint16x8x2_t vzipq_u16 (uint16x8_t, uint16x8_t);
    uint8x16x2_t vzipq_u8 (uint8x16_t, uint8x16_t);
    int32x4x2_t vzipq_s32 (int32x4_t, int32x4_t);
    int16x8x2_t vzipq_s16 (int16x8_t, int16x8_t);
    int8x16x2_t vzipq_s8 (int8x16_t, int8x16_t);
    float32x4x2_t vzipq_f32 (float32x4_t, float32x4_t);
    poly16x8x2_t vzipq_p16 (poly16x8_t, poly16x8_t);
    poly8x16x2_t vzipq_p8 (poly8x16_t, poly8x16_t);
    uint32x2x2_t vuzp_u32 (uint32x2_t, uint32x2_t);
    uint16x4x2_t vuzp_u16 (uint16x4_t, uint16x4_t);
    uint8x8x2_t vuzp_u8 (uint8x8_t, uint8x8_t);
    int32x2x2_t vuzp_s32 (int32x2_t, int32x2_t);
    int16x4x2_t vuzp_s16 (int16x4_t, int16x4_t);
    int8x8x2_t vuzp_s8 (int8x8_t, int8x8_t);
    float32x2x2_t vuzp_f32 (float32x2_t, float32x2_t);
    poly16x4x2_t vuzp_p16 (poly16x4_t, poly16x4_t);
    poly8x8x2_t vuzp_p8 (poly8x8_t, poly8x8_t);
    uint32x4x2_t vuzpq_u32 (uint32x4_t, uint32x4_t);
    uint16x8x2_t vuzpq_u16 (uint16x8_t, uint16x8_t);
    uint8x16x2_t vuzpq_u8 (uint8x16_t, uint8x16_t);
    int32x4x2_t vuzpq_s32 (int32x4_t, int32x4_t);
    int16x8x2_t vuzpq_s16 (int16x8_t, int16x8_t);
    int8x16x2_t vuzpq_s8 (int8x16_t, int8x16_t);
    float32x4x2_t vuzpq_f32 (float32x4_t, float32x4_t);
    poly16x8x2_t vuzpq_p16 (poly16x8_t, poly16x8_t);
    poly8x16x2_t vuzpq_p8 (poly8x16_t, poly8x16_t);
    uint32x2_t vld1_u32 (const uint32_t *);
    uint16x4_t vld1_u16 (const uint16_t *);
    uint8x8_t vld1_u8 (const uint8_t *);
    int32x2_t vld1_s32 (const int32_t *);
    int16x4_t vld1_s16 (const int16_t *);
    int8x8_t vld1_s8 (const int8_t *);
    uint64x1_t vld1_u64 (const uint64_t *);
    int64x1_t vld1_s64 (const int64_t *);
    float32x2_t vld1_f32 (const float32_t *);
    poly16x4_t vld1_p16 (const poly16_t *);
    poly8x8_t vld1_p8 (const poly8_t *);
    uint32x4_t vld1q_u32 (const uint32_t *);
    uint16x8_t vld1q_u16 (const uint16_t *);
    uint8x16_t vld1q_u8 (const uint8_t *);
    int32x4_t vld1q_s32 (const int32_t *);
    int16x8_t vld1q_s16 (const int16_t *);
    int8x16_t vld1q_s8 (const int8_t *);
    uint64x2_t vld1q_u64 (const uint64_t *);
    int64x2_t vld1q_s64 (const int64_t *);
    float32x4_t vld1q_f32 (const float32_t *);
    poly16x8_t vld1q_p16 (const poly16_t *);
    poly8x16_t vld1q_p8 (const poly8_t *);
    uint32x2_t vld1_lane_u32 (const uint32_t *, uint32x2_t, const int);
    uint16x4_t vld1_lane_u16 (const uint16_t *, uint16x4_t, const int);
    uint8x8_t vld1_lane_u8 (const uint8_t *, uint8x8_t, const int);
    int32x2_t vld1_lane_s32 (const int32_t *, int32x2_t, const int);
    int16x4_t vld1_lane_s16 (const int16_t *, int16x4_t, const int);
    int8x8_t vld1_lane_s8 (const int8_t *, int8x8_t, const int);
    float32x2_t vld1_lane_f32 (const float32_t *, float32x2_t, const int);
    poly16x4_t vld1_lane_p16 (const poly16_t *, poly16x4_t, const int);
    poly8x8_t vld1_lane_p8 (const poly8_t *, poly8x8_t, const int);
    uint64x1_t vld1_lane_u64 (const uint64_t *, uint64x1_t, const int);
    int64x1_t vld1_lane_s64 (const int64_t *, int64x1_t, const int);
    uint32x4_t vld1q_lane_u32 (const uint32_t *, uint32x4_t, const int);
    uint16x8_t vld1q_lane_u16 (const uint16_t *, uint16x8_t, const int);
    uint8x16_t vld1q_lane_u8 (const uint8_t *, uint8x16_t, const int);
    int32x4_t vld1q_lane_s32 (const int32_t *, int32x4_t, const int);
    int16x8_t vld1q_lane_s16 (const int16_t *, int16x8_t, const int);
    int8x16_t vld1q_lane_s8 (const int8_t *, int8x16_t, const int);
    float32x4_t vld1q_lane_f32 (const float32_t *, float32x4_t, const int);
    poly16x8_t vld1q_lane_p16 (const poly16_t *, poly16x8_t, const int);
    poly8x16_t vld1q_lane_p8 (const poly8_t *, poly8x16_t, const int);
    uint64x2_t vld1q_lane_u64 (const uint64_t *, uint64x2_t, const int);
    int64x2_t vld1q_lane_s64 (const int64_t *, int64x2_t, const int);
    uint32x2_t vld1_dup_u32 (const uint32_t *);
    uint16x4_t vld1_dup_u16 (const uint16_t *);
    uint8x8_t vld1_dup_u8 (const uint8_t *);
    int32x2_t vld1_dup_s32 (const int32_t *);
    int16x4_t vld1_dup_s16 (const int16_t *);
    int8x8_t vld1_dup_s8 (const int8_t *);
    float32x2_t vld1_dup_f32 (const float32_t *);
    poly16x4_t vld1_dup_p16 (const poly16_t *);
    poly8x8_t vld1_dup_p8 (const poly8_t *);
    uint64x1_t vld1_dup_u64 (const uint64_t *);
    int64x1_t vld1_dup_s64 (const int64_t *);
    uint32x4_t vld1q_dup_u32 (const uint32_t *);
    uint16x8_t vld1q_dup_u16 (const uint16_t *);
    uint8x16_t vld1q_dup_u8 (const uint8_t *);
    int32x4_t vld1q_dup_s32 (const int32_t *);
    int16x8_t vld1q_dup_s16 (const int16_t *);
    int8x16_t vld1q_dup_s8 (const int8_t *);
    float32x4_t vld1q_dup_f32 (const float32_t *);
    poly16x8_t vld1q_dup_p16 (const poly16_t *);
    poly8x16_t vld1q_dup_p8 (const poly8_t *);
    uint64x2_t vld1q_dup_u64 (const uint64_t *);
    int64x2_t vld1q_dup_s64 (const int64_t *);
    void vst1_u32 (uint32_t *, uint32x2_t);
    void vst1_u16 (uint16_t *, uint16x4_t);
    void vst1_u8 (uint8_t *, uint8x8_t);
    void vst1_s32 (int32_t *, int32x2_t);
    void vst1_s16 (int16_t *, int16x4_t);
    void vst1_s8 (int8_t *, int8x8_t);
    void vst1_u64 (uint64_t *, uint64x1_t);
    void vst1_s64 (int64_t *, int64x1_t);
    void vst1_f32 (float32_t *, float32x2_t);
    void vst1_p16 (poly16_t *, poly16x4_t);
    void vst1_p8 (poly8_t *, poly8x8_t);
    void vst1q_u32 (uint32_t *, uint32x4_t);
    void vst1q_u16 (uint16_t *, uint16x8_t);
    void vst1q_u8 (uint8_t *, uint8x16_t);
    void vst1q_s32 (int32_t *, int32x4_t);
    void vst1q_s16 (int16_t *, int16x8_t);
    void vst1q_s8 (int8_t *, int8x16_t);
    void vst1q_u64 (uint64_t *, uint64x2_t);
    void vst1q_s64 (int64_t *, int64x2_t);
    void vst1q_f32 (float32_t *, float32x4_t);
    void vst1q_p16 (poly16_t *, poly16x8_t);
    void vst1q_p8 (poly8_t *, poly8x16_t);
    void vst1_lane_u32 (uint32_t *, uint32x2_t, const int);
    void vst1_lane_u16 (uint16_t *, uint16x4_t, const int);
    void vst1_lane_u8 (uint8_t *, uint8x8_t, const int);
    void vst1_lane_s32 (int32_t *, int32x2_t, const int);
    void vst1_lane_s16 (int16_t *, int16x4_t, const int);
    void vst1_lane_s8 (int8_t *, int8x8_t, const int);
    void vst1_lane_f32 (float32_t *, float32x2_t, const int);
    void vst1_lane_p16 (poly16_t *, poly16x4_t, const int);
    void vst1_lane_p8 (poly8_t *, poly8x8_t, const int);
    void vst1_lane_s64 (int64_t *, int64x1_t, const int);
    void vst1_lane_u64 (uint64_t *, uint64x1_t, const int);
    void vst1q_lane_u32 (uint32_t *, uint32x4_t, const int);
    void vst1q_lane_u16 (uint16_t *, uint16x8_t, const int);
    void vst1q_lane_u8 (uint8_t *, uint8x16_t, const int);
    void vst1q_lane_s32 (int32_t *, int32x4_t, const int);
    void vst1q_lane_s16 (int16_t *, int16x8_t, const int);
    void vst1q_lane_s8 (int8_t *, int8x16_t, const int);
    void vst1q_lane_f32 (float32_t *, float32x4_t, const int);
    void vst1q_lane_p16 (poly16_t *, poly16x8_t, const int);
    void vst1q_lane_p8 (poly8_t *, poly8x16_t, const int);
    void vst1q_lane_s64 (int64_t *, int64x2_t, const int);
    void vst1q_lane_u64 (uint64_t *, uint64x2_t, const int);
    uint32x2x2_t vld2_u32 (const uint32_t *);
    uint16x4x2_t vld2_u16 (const uint16_t *);
    uint8x8x2_t vld2_u8 (const uint8_t *);
    int32x2x2_t vld2_s32 (const int32_t *);
    int16x4x2_t vld2_s16 (const int16_t *);
    int8x8x2_t vld2_s8 (const int8_t *);
    float32x2x2_t vld2_f32 (const float32_t *);
    poly16x4x2_t vld2_p16 (const poly16_t *);
    poly8x8x2_t vld2_p8 (const poly8_t *);
    uint64x1x2_t vld2_u64 (const uint64_t *);
    int64x1x2_t vld2_s64 (const int64_t *);
    uint32x4x2_t vld2q_u32 (const uint32_t *);
    uint16x8x2_t vld2q_u16 (const uint16_t *);
    uint8x16x2_t vld2q_u8 (const uint8_t *);
    int32x4x2_t vld2q_s32 (const int32_t *);
    int16x8x2_t vld2q_s16 (const int16_t *);
    int8x16x2_t vld2q_s8 (const int8_t *);
    float32x4x2_t vld2q_f32 (const float32_t *);
    poly16x8x2_t vld2q_p16 (const poly16_t *);
    poly8x16x2_t vld2q_p8 (const poly8_t *);
    uint32x2x2_t vld2_lane_u32 (const uint32_t *, uint32x2x2_t, const int);
    uint16x4x2_t vld2_lane_u16 (const uint16_t *, uint16x4x2_t, const int);
    uint8x8x2_t vld2_lane_u8 (const uint8_t *, uint8x8x2_t, const int);
    int32x2x2_t vld2_lane_s32 (const int32_t *, int32x2x2_t, const int);
    int16x4x2_t vld2_lane_s16 (const int16_t *, int16x4x2_t, const int);
    int8x8x2_t vld2_lane_s8 (const int8_t *, int8x8x2_t, const int);
    float32x2x2_t vld2_lane_f32 (const float32_t *, float32x2x2_t, const int);
    poly16x4x2_t vld2_lane_p16 (const poly16_t *, poly16x4x2_t, const int);
    poly8x8x2_t vld2_lane_p8 (const poly8_t *, poly8x8x2_t, const int);
    int32x4x2_t vld2q_lane_s32 (const int32_t *, int32x4x2_t, const int);
    int16x8x2_t vld2q_lane_s16 (const int16_t *, int16x8x2_t, const int);
    uint32x4x2_t vld2q_lane_u32 (const uint32_t *, uint32x4x2_t, const int);
    uint16x8x2_t vld2q_lane_u16 (const uint16_t *, uint16x8x2_t, const int);
    float32x4x2_t vld2q_lane_f32 (const float32_t *, float32x4x2_t, const int);
    poly16x8x2_t vld2q_lane_p16 (const poly16_t *, poly16x8x2_t, const int);
    uint32x2x2_t vld2_dup_u32 (const uint32_t *);
    uint16x4x2_t vld2_dup_u16 (const uint16_t *);
    uint8x8x2_t vld2_dup_u8 (const uint8_t *);
    int32x2x2_t vld2_dup_s32 (const int32_t *);
    int16x4x2_t vld2_dup_s16 (const int16_t *);
    int8x8x2_t vld2_dup_s8 (const int8_t *);
    float32x2x2_t vld2_dup_f32 (const float32_t *);
    poly16x4x2_t vld2_dup_p16 (const poly16_t *);
    poly8x8x2_t vld2_dup_p8 (const poly8_t *);
    uint64x1x2_t vld2_dup_u64 (const uint64_t *);
    int64x1x2_t vld2_dup_s64 (const int64_t *);
    void vst2_u32 (uint32_t *, uint32x2x2_t);
    void vst2_u16 (uint16_t *, uint16x4x2_t);
    void vst2_u8 (uint8_t *, uint8x8x2_t);
    void vst2_s32 (int32_t *, int32x2x2_t);
    void vst2_s16 (int16_t *, int16x4x2_t);
    void vst2_s8 (int8_t *, int8x8x2_t);
    void vst2_f32 (float32_t *, float32x2x2_t);
    void vst2_p16 (poly16_t *, poly16x4x2_t);
    void vst2_p8 (poly8_t *, poly8x8x2_t);
    void vst2_u64 (uint64_t *, uint64x1x2_t);
    void vst2_s64 (int64_t *, int64x1x2_t);
    void vst2q_u32 (uint32_t *, uint32x4x2_t);
    void vst2q_u16 (uint16_t *, uint16x8x2_t);
    void vst2q_u8 (uint8_t *, uint8x16x2_t);
    void vst2q_s32 (int32_t *, int32x4x2_t);
    void vst2q_s16 (int16_t *, int16x8x2_t);
    void vst2q_s8 (int8_t *, int8x16x2_t);
    void vst2q_f32 (float32_t *, float32x4x2_t);
    void vst2q_p16 (poly16_t *, poly16x8x2_t);
    void vst2q_p8 (poly8_t *, poly8x16x2_t);
    void vst2_lane_u32 (uint32_t *, uint32x2x2_t, const int);
    void vst2_lane_u16 (uint16_t *, uint16x4x2_t, const int);
    void vst2_lane_u8 (uint8_t *, uint8x8x2_t, const int);
    void vst2_lane_s32 (int32_t *, int32x2x2_t, const int);
    void vst2_lane_s16 (int16_t *, int16x4x2_t, const int);
    void vst2_lane_s8 (int8_t *, int8x8x2_t, const int);
    void vst2_lane_f32 (float32_t *, float32x2x2_t, const int);
    void vst2_lane_p16 (poly16_t *, poly16x4x2_t, const int);
    void vst2_lane_p8 (poly8_t *, poly8x8x2_t, const int);
    void vst2q_lane_s32 (int32_t *, int32x4x2_t, const int);
    void vst2q_lane_s16 (int16_t *, int16x8x2_t, const int);
    void vst2q_lane_u32 (uint32_t *, uint32x4x2_t, const int);
    void vst2q_lane_u16 (uint16_t *, uint16x8x2_t, const int);
    void vst2q_lane_f32 (float32_t *, float32x4x2_t, const int);
    void vst2q_lane_p16 (poly16_t *, poly16x8x2_t, const int);
    uint32x2x3_t vld3_u32 (const uint32_t *);
    uint16x4x3_t vld3_u16 (const uint16_t *);
    uint8x8x3_t vld3_u8 (const uint8_t *);
    int32x2x3_t vld3_s32 (const int32_t *);
    int16x4x3_t vld3_s16 (const int16_t *);
    int8x8x3_t vld3_s8 (const int8_t *);
    float32x2x3_t vld3_f32 (const float32_t *);
    poly16x4x3_t vld3_p16 (const poly16_t *);
    poly8x8x3_t vld3_p8 (const poly8_t *);
    uint64x1x3_t vld3_u64 (const uint64_t *);
    int64x1x3_t vld3_s64 (const int64_t *);
    uint32x4x3_t vld3q_u32 (const uint32_t *);
    uint16x8x3_t vld3q_u16 (const uint16_t *);
    uint8x16x3_t vld3q_u8 (const uint8_t *);
    int32x4x3_t vld3q_s32 (const int32_t *);
    int16x8x3_t vld3q_s16 (const int16_t *);
    int8x16x3_t vld3q_s8 (const int8_t *);
    float32x4x3_t vld3q_f32 (const float32_t *);
    poly16x8x3_t vld3q_p16 (const poly16_t *);
    poly8x16x3_t vld3q_p8 (const poly8_t *);
    uint32x2x3_t vld3_lane_u32 (const uint32_t *, uint32x2x3_t, const int);
    uint16x4x3_t vld3_lane_u16 (const uint16_t *, uint16x4x3_t, const int);
    uint8x8x3_t vld3_lane_u8 (const uint8_t *, uint8x8x3_t, const int);
    int32x2x3_t vld3_lane_s32 (const int32_t *, int32x2x3_t, const int);
    int16x4x3_t vld3_lane_s16 (const int16_t *, int16x4x3_t, const int);
    int8x8x3_t vld3_lane_s8 (const int8_t *, int8x8x3_t, const int);
    float32x2x3_t vld3_lane_f32 (const float32_t *, float32x2x3_t, const int);
    poly16x4x3_t vld3_lane_p16 (const poly16_t *, poly16x4x3_t, const int);
    poly8x8x3_t vld3_lane_p8 (const poly8_t *, poly8x8x3_t, const int);
    int32x4x3_t vld3q_lane_s32 (const int32_t *, int32x4x3_t, const int);
    int16x8x3_t vld3q_lane_s16 (const int16_t *, int16x8x3_t, const int);
    uint32x4x3_t vld3q_lane_u32 (const uint32_t *, uint32x4x3_t, const int);
    uint16x8x3_t vld3q_lane_u16 (const uint16_t *, uint16x8x3_t, const int);
    float32x4x3_t vld3q_lane_f32 (const float32_t *, float32x4x3_t, const int);
    poly16x8x3_t vld3q_lane_p16 (const poly16_t *, poly16x8x3_t, const int);
    uint32x2x3_t vld3_dup_u32 (const uint32_t *);
    uint16x4x3_t vld3_dup_u16 (const uint16_t *);
    uint8x8x3_t vld3_dup_u8 (const uint8_t *);
    int32x2x3_t vld3_dup_s32 (const int32_t *);
    int16x4x3_t vld3_dup_s16 (const int16_t *);
    int8x8x3_t vld3_dup_s8 (const int8_t *);
    float32x2x3_t vld3_dup_f32 (const float32_t *);
    poly16x4x3_t vld3_dup_p16 (const poly16_t *);
    poly8x8x3_t vld3_dup_p8 (const poly8_t *);
    uint64x1x3_t vld3_dup_u64 (const uint64_t *);
    int64x1x3_t vld3_dup_s64 (const int64_t *);
    void vst3_u32 (uint32_t *, uint32x2x3_t);
    void vst3_u16 (uint16_t *, uint16x4x3_t);
    void vst3_u8 (uint8_t *, uint8x8x3_t);
    void vst3_s32 (int32_t *, int32x2x3_t);
    void vst3_s16 (int16_t *, int16x4x3_t);
    void vst3_s8 (int8_t *, int8x8x3_t);
    void vst3_f32 (float32_t *, float32x2x3_t);
    void vst3_p16 (poly16_t *, poly16x4x3_t);
    void vst3_p8 (poly8_t *, poly8x8x3_t);
    void vst3_u64 (uint64_t *, uint64x1x3_t);
    void vst3_s64 (int64_t *, int64x1x3_t);
    void vst3q_u32 (uint32_t *, uint32x4x3_t);
    void vst3q_u16 (uint16_t *, uint16x8x3_t);
    void vst3q_u8 (uint8_t *, uint8x16x3_t);
    void vst3q_s32 (int32_t *, int32x4x3_t);
    void vst3q_s16 (int16_t *, int16x8x3_t);
    void vst3q_s8 (int8_t *, int8x16x3_t);
    void vst3q_f32 (float32_t *, float32x4x3_t);
    void vst3q_p16 (poly16_t *, poly16x8x3_t);
    void vst3q_p8 (poly8_t *, poly8x16x3_t);
    void vst3_lane_u32 (uint32_t *, uint32x2x3_t, const int);
    void vst3_lane_u16 (uint16_t *, uint16x4x3_t, const int);
    void vst3_lane_u8 (uint8_t *, uint8x8x3_t, const int);
    void vst3_lane_s32 (int32_t *, int32x2x3_t, const int);
    void vst3_lane_s16 (int16_t *, int16x4x3_t, const int);
    void vst3_lane_s8 (int8_t *, int8x8x3_t, const int);
    void vst3_lane_f32 (float32_t *, float32x2x3_t, const int);
    void vst3_lane_p16 (poly16_t *, poly16x4x3_t, const int);
    void vst3_lane_p8 (poly8_t *, poly8x8x3_t, const int);
    void vst3q_lane_s32 (int32_t *, int32x4x3_t, const int);
    void vst3q_lane_s16 (int16_t *, int16x8x3_t, const int);
    void vst3q_lane_u32 (uint32_t *, uint32x4x3_t, const int);
    void vst3q_lane_u16 (uint16_t *, uint16x8x3_t, const int);
    void vst3q_lane_f32 (float32_t *, float32x4x3_t, const int);
    void vst3q_lane_p16 (poly16_t *, poly16x8x3_t, const int);
    uint32x2x4_t vld4_u32 (const uint32_t *);
    uint16x4x4_t vld4_u16 (const uint16_t *);
    uint8x8x4_t vld4_u8 (const uint8_t *);
    int32x2x4_t vld4_s32 (const int32_t *);
    int16x4x4_t vld4_s16 (const int16_t *);
    int8x8x4_t vld4_s8 (const int8_t *);
    float32x2x4_t vld4_f32 (const float32_t *);
    poly16x4x4_t vld4_p16 (const poly16_t *);
    poly8x8x4_t vld4_p8 (const poly8_t *);
    uint64x1x4_t vld4_u64 (const uint64_t *);
    int64x1x4_t vld4_s64 (const int64_t *);
    uint32x4x4_t vld4q_u32 (const uint32_t *);
    uint16x8x4_t vld4q_u16 (const uint16_t *);
    uint8x16x4_t vld4q_u8 (const uint8_t *);
    int32x4x4_t vld4q_s32 (const int32_t *);
    int16x8x4_t vld4q_s16 (const int16_t *);
    int8x16x4_t vld4q_s8 (const int8_t *);
    float32x4x4_t vld4q_f32 (const float32_t *);
    poly16x8x4_t vld4q_p16 (const poly16_t *);
    poly8x16x4_t vld4q_p8 (const poly8_t *);
    uint32x2x4_t vld4_lane_u32 (const uint32_t *, uint32x2x4_t, const int);
    uint16x4x4_t vld4_lane_u16 (const uint16_t *, uint16x4x4_t, const int);
    uint8x8x4_t vld4_lane_u8 (const uint8_t *, uint8x8x4_t, const int);
    int32x2x4_t vld4_lane_s32 (const int32_t *, int32x2x4_t, const int);
    int16x4x4_t vld4_lane_s16 (const int16_t *, int16x4x4_t, const int);
    int8x8x4_t vld4_lane_s8 (const int8_t *, int8x8x4_t, const int);
    float32x2x4_t vld4_lane_f32 (const float32_t *, float32x2x4_t, const int);
    poly16x4x4_t vld4_lane_p16 (const poly16_t *, poly16x4x4_t, const int);
    poly8x8x4_t vld4_lane_p8 (const poly8_t *, poly8x8x4_t, const int);
    int32x4x4_t vld4q_lane_s32 (const int32_t *, int32x4x4_t, const int);
    int16x8x4_t vld4q_lane_s16 (const int16_t *, int16x8x4_t, const int);
    uint32x4x4_t vld4q_lane_u32 (const uint32_t *, uint32x4x4_t, const int);
    uint16x8x4_t vld4q_lane_u16 (const uint16_t *, uint16x8x4_t, const int);
    float32x4x4_t vld4q_lane_f32 (const float32_t *, float32x4x4_t, const int);
    poly16x8x4_t vld4q_lane_p16 (const poly16_t *, poly16x8x4_t, const int);
    uint32x2x4_t vld4_dup_u32 (const uint32_t *);
    uint16x4x4_t vld4_dup_u16 (const uint16_t *);
    uint8x8x4_t vld4_dup_u8 (const uint8_t *);
    int32x2x4_t vld4_dup_s32 (const int32_t *);
    int16x4x4_t vld4_dup_s16 (const int16_t *);
    int8x8x4_t vld4_dup_s8 (const int8_t *);
    float32x2x4_t vld4_dup_f32 (const float32_t *);
    poly16x4x4_t vld4_dup_p16 (const poly16_t *);
    poly8x8x4_t vld4_dup_p8 (const poly8_t *);
    uint64x1x4_t vld4_dup_u64 (const uint64_t *);
    int64x1x4_t vld4_dup_s64 (const int64_t *);
    void vst4_u32 (uint32_t *, uint32x2x4_t);
    void vst4_u16 (uint16_t *, uint16x4x4_t);
    void vst4_u8 (uint8_t *, uint8x8x4_t);
    void vst4_s32 (int32_t *, int32x2x4_t);
    void vst4_s16 (int16_t *, int16x4x4_t);
    void vst4_s8 (int8_t *, int8x8x4_t);
    void vst4_f32 (float32_t *, float32x2x4_t);
    void vst4_p16 (poly16_t *, poly16x4x4_t);
    void vst4_p8 (poly8_t *, poly8x8x4_t);
    void vst4_u64 (uint64_t *, uint64x1x4_t);
    void vst4_s64 (int64_t *, int64x1x4_t);
    void vst4q_u32 (uint32_t *, uint32x4x4_t);
    void vst4q_u16 (uint16_t *, uint16x8x4_t);
    void vst4q_u8 (uint8_t *, uint8x16x4_t);
    void vst4q_s32 (int32_t *, int32x4x4_t);
    void vst4q_s16 (int16_t *, int16x8x4_t);
    void vst4q_s8 (int8_t *, int8x16x4_t);
    void vst4q_f32 (float32_t *, float32x4x4_t);
    void vst4q_p16 (poly16_t *, poly16x8x4_t);
    void vst4q_p8 (poly8_t *, poly8x16x4_t);
    void vst4_lane_u32 (uint32_t *, uint32x2x4_t, const int);
    void vst4_lane_u16 (uint16_t *, uint16x4x4_t, const int);
    void vst4_lane_u8 (uint8_t *, uint8x8x4_t, const int);
    void vst4_lane_s32 (int32_t *, int32x2x4_t, const int);
    void vst4_lane_s16 (int16_t *, int16x4x4_t, const int);
    void vst4_lane_s8 (int8_t *, int8x8x4_t, const int);
    void vst4_lane_f32 (float32_t *, float32x2x4_t, const int);
    void vst4_lane_p16 (poly16_t *, poly16x4x4_t, const int);
    void vst4_lane_p8 (poly8_t *, poly8x8x4_t, const int);
    void vst4q_lane_s32 (int32_t *, int32x4x4_t, const int);
    void vst4q_lane_s16 (int16_t *, int16x8x4_t, const int);
    void vst4q_lane_u32 (uint32_t *, uint32x4x4_t, const int);
    void vst4q_lane_u16 (uint16_t *, uint16x8x4_t, const int);
    void vst4q_lane_f32 (float32_t *, float32x4x4_t, const int);
    void vst4q_lane_p16 (poly16_t *, poly16x8x4_t, const int);
    uint32x2_t vand_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vand_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vand_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vand_s32 (int32x2_t, int32x2_t);
    int16x4_t vand_s16 (int16x4_t, int16x4_t);
    int8x8_t vand_s8 (int8x8_t, int8x8_t);
    uint64x1_t vand_u64 (uint64x1_t, uint64x1_t);
    int64x1_t vand_s64 (int64x1_t, int64x1_t);
    uint32x4_t vandq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vandq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vandq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vandq_s32 (int32x4_t, int32x4_t);
    int16x8_t vandq_s16 (int16x8_t, int16x8_t);
    int8x16_t vandq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vandq_u64 (uint64x2_t, uint64x2_t);
    int64x2_t vandq_s64 (int64x2_t, int64x2_t);
    uint32x2_t vorr_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vorr_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vorr_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vorr_s32 (int32x2_t, int32x2_t);
    int16x4_t vorr_s16 (int16x4_t, int16x4_t);
    int8x8_t vorr_s8 (int8x8_t, int8x8_t);
    uint64x1_t vorr_u64 (uint64x1_t, uint64x1_t);
    int64x1_t vorr_s64 (int64x1_t, int64x1_t);
    uint32x4_t vorrq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vorrq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vorrq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vorrq_s32 (int32x4_t, int32x4_t);
    int16x8_t vorrq_s16 (int16x8_t, int16x8_t);
    int8x16_t vorrq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vorrq_u64 (uint64x2_t, uint64x2_t);
    int64x2_t vorrq_s64 (int64x2_t, int64x2_t);
    uint32x2_t veor_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t veor_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t veor_u8 (uint8x8_t, uint8x8_t);
    int32x2_t veor_s32 (int32x2_t, int32x2_t);
    int16x4_t veor_s16 (int16x4_t, int16x4_t);
    int8x8_t veor_s8 (int8x8_t, int8x8_t);
    uint64x1_t veor_u64 (uint64x1_t, uint64x1_t);
    int64x1_t veor_s64 (int64x1_t, int64x1_t);
    uint32x4_t veorq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t veorq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t veorq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t veorq_s32 (int32x4_t, int32x4_t);
    int16x8_t veorq_s16 (int16x8_t, int16x8_t);
    int8x16_t veorq_s8 (int8x16_t, int8x16_t);
    uint64x2_t veorq_u64 (uint64x2_t, uint64x2_t);
    int64x2_t veorq_s64 (int64x2_t, int64x2_t);
    uint32x2_t vbic_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vbic_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vbic_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vbic_s32 (int32x2_t, int32x2_t);
    int16x4_t vbic_s16 (int16x4_t, int16x4_t);
    int8x8_t vbic_s8 (int8x8_t, int8x8_t);
    uint64x1_t vbic_u64 (uint64x1_t, uint64x1_t);
    int64x1_t vbic_s64 (int64x1_t, int64x1_t);
    uint32x4_t vbicq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vbicq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vbicq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vbicq_s32 (int32x4_t, int32x4_t);
    int16x8_t vbicq_s16 (int16x8_t, int16x8_t);
    int8x16_t vbicq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vbicq_u64 (uint64x2_t, uint64x2_t);
    int64x2_t vbicq_s64 (int64x2_t, int64x2_t);
    uint32x2_t vorn_u32 (uint32x2_t, uint32x2_t);
    uint16x4_t vorn_u16 (uint16x4_t, uint16x4_t);
    uint8x8_t vorn_u8 (uint8x8_t, uint8x8_t);
    int32x2_t vorn_s32 (int32x2_t, int32x2_t);
    int16x4_t vorn_s16 (int16x4_t, int16x4_t);
    int8x8_t vorn_s8 (int8x8_t, int8x8_t);
    uint64x1_t vorn_u64 (uint64x1_t, uint64x1_t);
    int64x1_t vorn_s64 (int64x1_t, int64x1_t);
    uint32x4_t vornq_u32 (uint32x4_t, uint32x4_t);
    uint16x8_t vornq_u16 (uint16x8_t, uint16x8_t);
    uint8x16_t vornq_u8 (uint8x16_t, uint8x16_t);
    int32x4_t vornq_s32 (int32x4_t, int32x4_t);
    int16x8_t vornq_s16 (int16x8_t, int16x8_t);
    int8x16_t vornq_s8 (int8x16_t, int8x16_t);
    uint64x2_t vornq_u64 (uint64x2_t, uint64x2_t);
    int64x2_t vornq_s64 (int64x2_t, int64x2_t);
    poly8x8_t vreinterpret_p8_u32 (uint32x2_t);
    poly8x8_t vreinterpret_p8_u16 (uint16x4_t);
    poly8x8_t vreinterpret_p8_u8 (uint8x8_t);
    poly8x8_t vreinterpret_p8_s32 (int32x2_t);
    poly8x8_t vreinterpret_p8_s16 (int16x4_t);
    poly8x8_t vreinterpret_p8_s8 (int8x8_t);
    poly8x8_t vreinterpret_p8_u64 (uint64x1_t);
    poly8x8_t vreinterpret_p8_s64 (int64x1_t);
    poly8x8_t vreinterpret_p8_f32 (float32x2_t);
    poly8x8_t vreinterpret_p8_p16 (poly16x4_t);
    poly8x16_t vreinterpretq_p8_u32 (uint32x4_t);
    poly8x16_t vreinterpretq_p8_u16 (uint16x8_t);
    poly8x16_t vreinterpretq_p8_u8 (uint8x16_t);
    poly8x16_t vreinterpretq_p8_s32 (int32x4_t);
    poly8x16_t vreinterpretq_p8_s16 (int16x8_t);
    poly8x16_t vreinterpretq_p8_s8 (int8x16_t);
    poly8x16_t vreinterpretq_p8_u64 (uint64x2_t);
    poly8x16_t vreinterpretq_p8_s64 (int64x2_t);
    poly8x16_t vreinterpretq_p8_f32 (float32x4_t);
    poly8x16_t vreinterpretq_p8_p16 (poly16x8_t);
    poly16x4_t vreinterpret_p16_u32 (uint32x2_t);
    poly16x4_t vreinterpret_p16_u16 (uint16x4_t);
    poly16x4_t vreinterpret_p16_u8 (uint8x8_t);
    poly16x4_t vreinterpret_p16_s32 (int32x2_t);
    poly16x4_t vreinterpret_p16_s16 (int16x4_t);
    poly16x4_t vreinterpret_p16_s8 (int8x8_t);
    poly16x4_t vreinterpret_p16_u64 (uint64x1_t);
    poly16x4_t vreinterpret_p16_s64 (int64x1_t);
    poly16x4_t vreinterpret_p16_f32 (float32x2_t);
    poly16x4_t vreinterpret_p16_p8 (poly8x8_t);
    poly16x8_t vreinterpretq_p16_u32 (uint32x4_t);
    poly16x8_t vreinterpretq_p16_u16 (uint16x8_t);
    poly16x8_t vreinterpretq_p16_u8 (uint8x16_t);
    poly16x8_t vreinterpretq_p16_s32 (int32x4_t);
    poly16x8_t vreinterpretq_p16_s16 (int16x8_t);
    poly16x8_t vreinterpretq_p16_s8 (int8x16_t);
    poly16x8_t vreinterpretq_p16_u64 (uint64x2_t);
    poly16x8_t vreinterpretq_p16_s64 (int64x2_t);
    poly16x8_t vreinterpretq_p16_f32 (float32x4_t);
    poly16x8_t vreinterpretq_p16_p8 (poly8x16_t);
    float32x2_t vreinterpret_f32_u32 (uint32x2_t);
    float32x2_t vreinterpret_f32_u16 (uint16x4_t);
    float32x2_t vreinterpret_f32_u8 (uint8x8_t);
    float32x2_t vreinterpret_f32_s32 (int32x2_t);
    float32x2_t vreinterpret_f32_s16 (int16x4_t);
    float32x2_t vreinterpret_f32_s8 (int8x8_t);
    float32x2_t vreinterpret_f32_u64 (uint64x1_t);
    float32x2_t vreinterpret_f32_s64 (int64x1_t);
    float32x2_t vreinterpret_f32_p16 (poly16x4_t);
    float32x2_t vreinterpret_f32_p8 (poly8x8_t);
    float32x4_t vreinterpretq_f32_u32 (uint32x4_t);
    float32x4_t vreinterpretq_f32_u16 (uint16x8_t);
    float32x4_t vreinterpretq_f32_u8 (uint8x16_t);
    float32x4_t vreinterpretq_f32_s32 (int32x4_t);
    float32x4_t vreinterpretq_f32_s16 (int16x8_t);
    float32x4_t vreinterpretq_f32_s8 (int8x16_t);
    float32x4_t vreinterpretq_f32_u64 (uint64x2_t);
    float32x4_t vreinterpretq_f32_s64 (int64x2_t);
    float32x4_t vreinterpretq_f32_p16 (poly16x8_t);
    float32x4_t vreinterpretq_f32_p8 (poly8x16_t);
    int64x1_t vreinterpret_s64_u32 (uint32x2_t);
    int64x1_t vreinterpret_s64_u16 (uint16x4_t);
    int64x1_t vreinterpret_s64_u8 (uint8x8_t);
    int64x1_t vreinterpret_s64_s32 (int32x2_t);
    int64x1_t vreinterpret_s64_s16 (int16x4_t);
    int64x1_t vreinterpret_s64_s8 (int8x8_t);
    int64x1_t vreinterpret_s64_u64 (uint64x1_t);
    int64x1_t vreinterpret_s64_f32 (float32x2_t);
    int64x1_t vreinterpret_s64_p16 (poly16x4_t);
    int64x1_t vreinterpret_s64_p8 (poly8x8_t);
    int64x2_t vreinterpretq_s64_u32 (uint32x4_t);
    int64x2_t vreinterpretq_s64_u16 (uint16x8_t);
    int64x2_t vreinterpretq_s64_u8 (uint8x16_t);
    int64x2_t vreinterpretq_s64_s32 (int32x4_t);
    int64x2_t vreinterpretq_s64_s16 (int16x8_t);
    int64x2_t vreinterpretq_s64_s8 (int8x16_t);
    int64x2_t vreinterpretq_s64_u64 (uint64x2_t);
    int64x2_t vreinterpretq_s64_f32 (float32x4_t);
    int64x2_t vreinterpretq_s64_p16 (poly16x8_t);
    int64x2_t vreinterpretq_s64_p8 (poly8x16_t);
    uint64x1_t vreinterpret_u64_u32 (uint32x2_t);
    uint64x1_t vreinterpret_u64_u16 (uint16x4_t);
    uint64x1_t vreinterpret_u64_u8 (uint8x8_t);
    uint64x1_t vreinterpret_u64_s32 (int32x2_t);
    uint64x1_t vreinterpret_u64_s16 (int16x4_t);
    uint64x1_t vreinterpret_u64_s8 (int8x8_t);
    uint64x1_t vreinterpret_u64_s64 (int64x1_t);
    uint64x1_t vreinterpret_u64_f32 (float32x2_t);
    uint64x1_t vreinterpret_u64_p16 (poly16x4_t);
    uint64x1_t vreinterpret_u64_p8 (poly8x8_t);
    uint64x2_t vreinterpretq_u64_u32 (uint32x4_t);
    uint64x2_t vreinterpretq_u64_u16 (uint16x8_t);
    uint64x2_t vreinterpretq_u64_u8 (uint8x16_t);
    uint64x2_t vreinterpretq_u64_s32 (int32x4_t);
    uint64x2_t vreinterpretq_u64_s16 (int16x8_t);
    uint64x2_t vreinterpretq_u64_s8 (int8x16_t);
    uint64x2_t vreinterpretq_u64_s64 (int64x2_t);
    uint64x2_t vreinterpretq_u64_f32 (float32x4_t);
    uint64x2_t vreinterpretq_u64_p16 (poly16x8_t);
    uint64x2_t vreinterpretq_u64_p8 (poly8x16_t);
    int8x8_t vreinterpret_s8_u32 (uint32x2_t);
    int8x8_t vreinterpret_s8_u16 (uint16x4_t);
    int8x8_t vreinterpret_s8_u8 (uint8x8_t);
    int8x8_t vreinterpret_s8_s32 (int32x2_t);
    int8x8_t vreinterpret_s8_s16 (int16x4_t);
    int8x8_t vreinterpret_s8_u64 (uint64x1_t);
    int8x8_t vreinterpret_s8_s64 (int64x1_t);
    int8x8_t vreinterpret_s8_f32 (float32x2_t);
    int8x8_t vreinterpret_s8_p16 (poly16x4_t);
    int8x8_t vreinterpret_s8_p8 (poly8x8_t);
    int8x16_t vreinterpretq_s8_u32 (uint32x4_t);
    int8x16_t vreinterpretq_s8_u16 (uint16x8_t);
    int8x16_t vreinterpretq_s8_u8 (uint8x16_t);
    int8x16_t vreinterpretq_s8_s32 (int32x4_t);
    int8x16_t vreinterpretq_s8_s16 (int16x8_t);
    int8x16_t vreinterpretq_s8_u64 (uint64x2_t);
    int8x16_t vreinterpretq_s8_s64 (int64x2_t);
    int8x16_t vreinterpretq_s8_f32 (float32x4_t);
    int8x16_t vreinterpretq_s8_p16 (poly16x8_t);
    int8x16_t vreinterpretq_s8_p8 (poly8x16_t);
    int16x4_t vreinterpret_s16_u32 (uint32x2_t);
    int16x4_t vreinterpret_s16_u16 (uint16x4_t);
    int16x4_t vreinterpret_s16_u8 (uint8x8_t);
    int16x4_t vreinterpret_s16_s32 (int32x2_t);
    int16x4_t vreinterpret_s16_s8 (int8x8_t);
    int16x4_t vreinterpret_s16_u64 (uint64x1_t);
    int16x4_t vreinterpret_s16_s64 (int64x1_t);
    int16x4_t vreinterpret_s16_f32 (float32x2_t);
    int16x4_t vreinterpret_s16_p16 (poly16x4_t);
    int16x4_t vreinterpret_s16_p8 (poly8x8_t);
    int16x8_t vreinterpretq_s16_u32 (uint32x4_t);
    int16x8_t vreinterpretq_s16_u16 (uint16x8_t);
    int16x8_t vreinterpretq_s16_u8 (uint8x16_t);
    int16x8_t vreinterpretq_s16_s32 (int32x4_t);
    int16x8_t vreinterpretq_s16_s8 (int8x16_t);
    int16x8_t vreinterpretq_s16_u64 (uint64x2_t);
    int16x8_t vreinterpretq_s16_s64 (int64x2_t);
    int16x8_t vreinterpretq_s16_f32 (float32x4_t);
    int16x8_t vreinterpretq_s16_p16 (poly16x8_t);
    int16x8_t vreinterpretq_s16_p8 (poly8x16_t);
    int32x2_t vreinterpret_s32_u32 (uint32x2_t);
    int32x2_t vreinterpret_s32_u16 (uint16x4_t);
    int32x2_t vreinterpret_s32_u8 (uint8x8_t);
    int32x2_t vreinterpret_s32_s16 (int16x4_t);
    int32x2_t vreinterpret_s32_s8 (int8x8_t);
    int32x2_t vreinterpret_s32_u64 (uint64x1_t);
    int32x2_t vreinterpret_s32_s64 (int64x1_t);
    int32x2_t vreinterpret_s32_f32 (float32x2_t);
    int32x2_t vreinterpret_s32_p16 (poly16x4_t);
    int32x2_t vreinterpret_s32_p8 (poly8x8_t);
    int32x4_t vreinterpretq_s32_u32 (uint32x4_t);
    int32x4_t vreinterpretq_s32_u16 (uint16x8_t);
    int32x4_t vreinterpretq_s32_u8 (uint8x16_t);
    int32x4_t vreinterpretq_s32_s16 (int16x8_t);
    int32x4_t vreinterpretq_s32_s8 (int8x16_t);
    int32x4_t vreinterpretq_s32_u64 (uint64x2_t);
    int32x4_t vreinterpretq_s32_s64 (int64x2_t);
    int32x4_t vreinterpretq_s32_f32 (float32x4_t);
    int32x4_t vreinterpretq_s32_p16 (poly16x8_t);
    int32x4_t vreinterpretq_s32_p8 (poly8x16_t);
    uint8x8_t vreinterpret_u8_u32 (uint32x2_t);
    uint8x8_t vreinterpret_u8_u16 (uint16x4_t);
    uint8x8_t vreinterpret_u8_s32 (int32x2_t);
    uint8x8_t vreinterpret_u8_s16 (int16x4_t);
    uint8x8_t vreinterpret_u8_s8 (int8x8_t);
    uint8x8_t vreinterpret_u8_u64 (uint64x1_t);
    uint8x8_t vreinterpret_u8_s64 (int64x1_t);
    uint8x8_t vreinterpret_u8_f32 (float32x2_t);
    uint8x8_t vreinterpret_u8_p16 (poly16x4_t);
    uint8x8_t vreinterpret_u8_p8 (poly8x8_t);
    uint8x16_t vreinterpretq_u8_u32 (uint32x4_t);
    uint8x16_t vreinterpretq_u8_u16 (uint16x8_t);
    uint8x16_t vreinterpretq_u8_s32 (int32x4_t);
    uint8x16_t vreinterpretq_u8_s16 (int16x8_t);
    uint8x16_t vreinterpretq_u8_s8 (int8x16_t);
    uint8x16_t vreinterpretq_u8_u64 (uint64x2_t);
    uint8x16_t vreinterpretq_u8_s64 (int64x2_t);
    uint8x16_t vreinterpretq_u8_f32 (float32x4_t);
    uint8x16_t vreinterpretq_u8_p16 (poly16x8_t);
    uint8x16_t vreinterpretq_u8_p8 (poly8x16_t);
    uint16x4_t vreinterpret_u16_u32 (uint32x2_t);
    uint16x4_t vreinterpret_u16_u8 (uint8x8_t);
    uint16x4_t vreinterpret_u16_s32 (int32x2_t);
    uint16x4_t vreinterpret_u16_s16 (int16x4_t);
    uint16x4_t vreinterpret_u16_s8 (int8x8_t);
    uint16x4_t vreinterpret_u16_u64 (uint64x1_t);
    uint16x4_t vreinterpret_u16_s64 (int64x1_t);
    uint16x4_t vreinterpret_u16_f32 (float32x2_t);
    uint16x4_t vreinterpret_u16_p16 (poly16x4_t);
    uint16x4_t vreinterpret_u16_p8 (poly8x8_t);
    uint16x8_t vreinterpretq_u16_u32 (uint32x4_t);
    uint16x8_t vreinterpretq_u16_u8 (uint8x16_t);
    uint16x8_t vreinterpretq_u16_s32 (int32x4_t);
    uint16x8_t vreinterpretq_u16_s16 (int16x8_t);
    uint16x8_t vreinterpretq_u16_s8 (int8x16_t);
    uint16x8_t vreinterpretq_u16_u64 (uint64x2_t);
    uint16x8_t vreinterpretq_u16_s64 (int64x2_t);
    uint16x8_t vreinterpretq_u16_f32 (float32x4_t);
    uint16x8_t vreinterpretq_u16_p16 (poly16x8_t);
    uint16x8_t vreinterpretq_u16_p8 (poly8x16_t);
    uint32x2_t vreinterpret_u32_u16 (uint16x4_t);
    uint32x2_t vreinterpret_u32_u8 (uint8x8_t);
    uint32x2_t vreinterpret_u32_s32 (int32x2_t);
    uint32x2_t vreinterpret_u32_s16 (int16x4_t);
    uint32x2_t vreinterpret_u32_s8 (int8x8_t);
    uint32x2_t vreinterpret_u32_u64 (uint64x1_t);
    uint32x2_t vreinterpret_u32_s64 (int64x1_t);
    uint32x2_t vreinterpret_u32_f32 (float32x2_t);
    uint32x2_t vreinterpret_u32_p16 (poly16x4_t);
    uint32x2_t vreinterpret_u32_p8 (poly8x8_t);
    uint32x4_t vreinterpretq_u32_u16 (uint16x8_t);
    uint32x4_t vreinterpretq_u32_u8 (uint8x16_t);
    uint32x4_t vreinterpretq_u32_s32 (int32x4_t);
    uint32x4_t vreinterpretq_u32_s16 (int16x8_t);
    uint32x4_t vreinterpretq_u32_s8 (int8x16_t);
    uint32x4_t vreinterpretq_u32_u64 (uint64x2_t);
    uint32x4_t vreinterpretq_u32_s64 (int64x2_t);
    uint32x4_t vreinterpretq_u32_f32 (float32x4_t);
    uint32x4_t vreinterpretq_u32_p16 (poly16x8_t);
    uint32x4_t vreinterpretq_u32_p8 (poly8x16_t);
    __int64 _arm_smlal(__int64 _RdHiLo, int _Rn, int _Rm);
    unsigned __int64 _arm_umlal(unsigned __int64 _RdHiLo, unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_clz(unsigned int _Rm);
    int _arm_qadd(int _Rm, int _Rn);
    int _arm_qdadd(int _Rm, int _Rn);
    int _arm_qdsub(int _Rm, int _Rn);
    int _arm_qsub(int _Rm, int _Rn);
    int _arm_smlabb(int _Rn, int _Rm, int _Ra);
    int _arm_smlabt(int _Rn, int _Rm, int _Ra);
    int _arm_smlatb(int _Rn, int _Rm, int _Ra);
    int _arm_smlatt(int _Rn, int _Rm, int _Ra);
    __int64 _arm_smlalbb(__int64 _RdHiLo, int _Rn, int _Rm);
    __int64 _arm_smlalbt(__int64 _RdHiLo, int _Rn, int _Rm);
    __int64 _arm_smlaltb(__int64 _RdHiLo, int _Rn, int _Rm);
    __int64 _arm_smlaltt(__int64 _RdHiLo, int _Rn, int _Rm);
    int _arm_smlawb(int _Rn, int _Rm, int _Ra);
    int _arm_smlawt(int _Rn, int _Rm, int _Ra);
    int _arm_smulbb(int _Rn, int _Rm);
    int _arm_smulbt(int _Rn, int _Rm);
    int _arm_smultb(int _Rn, int _Rm);
    int _arm_smultt(int _Rn, int _Rm);
    int _arm_smulwb(int _Rn, int _Rm);
    int _arm_smulwt(int _Rn, int _Rm);
    int _arm_sadd16(int _Rn, int _Rm);
    int _arm_sadd8(int _Rn, int _Rm);
    int _arm_sasx(int _Rn, int _Rm);
    int _arm_ssax(int _Rn, int _Rm);
    int _arm_ssub16(int _Rn, int _Rm);
    int _arm_ssub8(int _Rn, int _Rm);
    int _arm_shadd16(int _Rn, int _Rm);
    int _arm_shadd8(int _Rn, int _Rm);
    int _arm_shasx(int _Rn, int _Rm);
    int _arm_shsax(int _Rn, int _Rm);
    int _arm_shsub16(int _Rn, int _Rm);
    int _arm_shsub8(int _Rn, int _Rm);
    int _arm_qadd16(int _Rn, int _Rm);
    int _arm_qadd8(int _Rn, int _Rm);
    int _arm_qasx(int _Rn, int _Rm);
    int _arm_qsax(int _Rn, int _Rm);
    int _arm_qsub16(int _Rn, int _Rm);
    int _arm_qsub8(int _Rn, int _Rm);
    unsigned int _arm_uadd16(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uadd8(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uasx(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_usax(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_usub16(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_usub8(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uhadd16(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uhadd8(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uhasx(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uhsax(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uhsub16(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uhsub8(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uqadd16(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uqadd8(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uqasx(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uqsax(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uqsub16(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_uqsub8(unsigned int _Rn, unsigned int _Rm);
    int _arm_sxtab(int _Rn, int _Rm, unsigned int _Rotation);
    int _arm_sxtab16(int _Rn, int _Rm, unsigned int _Rotation);
    int _arm_sxtah(int _Rn, int _Rm, unsigned int _Rotation);
    unsigned int _arm_uxtab(unsigned int _Rn, unsigned int _Rm, unsigned int _Rotation);
    unsigned int _arm_uxtab16(unsigned int _Rn, unsigned int _Rm, unsigned int _Rotation);
    unsigned int _arm_uxtah(unsigned int _Rn, unsigned int _Rm, unsigned int _Rotation);
    int _arm_sxtb(int _Rn, unsigned int _Rotation);
    int _arm_sxtb16(int _Rn, unsigned int _Rotation);
    int _arm_sxth(int _Rn, unsigned int _Rotation);
    unsigned int _arm_uxtb(unsigned int _Rn, unsigned int _Rotation);
    unsigned int _arm_uxtb16(unsigned int _Rn, unsigned int _Rotation);
    unsigned int _arm_uxth(unsigned int _Rn, unsigned int _Rotation);
    int _arm_pkhbt(int _Rn, int _Rm, unsigned int _Lsl_imm);
    int _arm_pkhtb(int _Rn, int _Rm, unsigned int _Asr_imm);
    unsigned int _arm_usad8(unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_usada8(unsigned int _Rn, unsigned int _Rm, unsigned int _Ra);
    int _arm_ssat(unsigned int _Sat_imm, _int _Rn, _ARMINTR_SHIFT_T _Shift_type, unsigned int _Shift_imm);
    int _arm_usat(unsigned int _Sat_imm, _int _Rn, _ARMINTR_SHIFT_T _Shift_type, unsigned int _Shift_imm);
    int _arm_ssat16(unsigned int _Sat_imm, _int _Rn);
    int _arm_usat16(unsigned int _Sat_imm, _int _Rn);
    unsigned int _arm_rev(unsigned int _Rm);
    unsigned int _arm_rev16(unsigned int _Rm);
    unsigned int _arm_revsh(unsigned int _Rm);
    int _arm_smlad(int _Rn, int _Rm, int _Ra);
    int _arm_smladx(int _Rn, int _Rm, int _Ra);
    int _arm_smlsd(int _Rn, int _Rm, int _Ra);
    int _arm_smlsdx(int _Rn, int _Rm, int _Ra);
    int _arm_smmla(int _Rn, int _Rm, int _Ra);
    int _arm_smmlar(int _Rn, int _Rm, int _Ra);
    int _arm_smmls(int _Rn, int _Rm, int _Ra);
    int _arm_smmlsr(int _Rn, int _Rm, int _Ra);
    int _arm_smmul(int _Rn, int _Rm);
    int _arm_smmulr(int _Rn, int _Rm);
    __int64 _arm_smlald(__int64 _RdHiLo, int _Rn, int _Rm);
    __int64 _arm_smlaldx(__int64 _RdHiLo, int _Rn, int _Rm);
    __int64 _arm_smlsld(__int64 _RdHiLo, int _Rn, int _Rm);
    __int64 _arm_smlsldx(__int64 _RdHiLo, int _Rn, int _Rm);
    int _arm_smuad(int _Rn, int _Rm);
    int _arm_smuadx(int _Rn, int _Rm);
    int _arm_smusd(int _Rn, int _Rm);
    int _arm_smusdx(int _Rn, int _Rm);
    __int64 _arm_smull(int _Rn, int _Rm);
    unsigned __int64 _arm_umaal(unsigned int _RdLo, unsigned int _RdHi, unsigned int _Rn, unsigned int _Rm);
    unsigned int _arm_bfc(unsigned int _Rd, unsigned int _Lsb, unsigned int _Width);
    unsigned int _arm_bfi(unsigned int _Rd, unsigned int _Rn, unsigned int _Lsb, unsigned int _Width);
    unsigned int _arm_rbit(unsigned int _Rm);
    int _arm_sbfx(int _Rn, unsigned int _Lsb, unsigned int _Width);
    unsigned int _arm_ubfx(unsigned int _Rn, unsigned int _Lsb, unsigned int _Width);
    int _arm_sdiv(int _Rn, int _Rm);
    unsigned int _arm_udiv(unsigned int _Rn, unsigned int _Rm);
    void __cps(unsigned int _Ops, unsigned int _Flags, unsigned int _Mode);
    void __dmb(unsigned int _Type );
    void __dsb(unsigned int _Type);
    void __isb(unsigned int _Type);
    void __emit(unsigned __int32 opcode);
    unsigned int __hvc(unsigned int, ...);
    __int16 __iso_volatile_load16(const volatile__int16 *);
    __int32 __iso_volatile_load32(const volatile__int32 *);
    __int64 __iso_volatile_load64(const volatile__int64 *);
    __int8 __iso_volatile_load8(const volatile __int8 *);
    void __iso_volatile_store16(volatile __int16 *, __int16);
    void __iso_volatile_store32(volatile __int32 *, __int32);
    void __iso_volatile_store64(volatile __int64 *, __int64);
    void __iso_volatile_store8(volatile__int8 *, __int8);
    __int64 __ldrexd(const volatile__int64 *);
    void __cdecl __prefetch(const void *);
    unsigned __int64 __rdpmccntr64(void);
    void __sev(void);
    void __static_assert(int, const char *);
    unsigned int __swi(unsigned int, ...);
    int __trap(int, ...);
    void __wfe(void);
    void __wfi(void);
    int _AddSatInt(int, int);
    double _CopyDoubleFromInt64(__int64);
    float _CopyFloatFromInt32(__int32);
    __int32 _CopyInt32FromFloat(float);
    __int64 _CopyInt64FromDouble(double);
    unsigned int _CountLeadingOnes(unsigned long);
    unsigned int _CountLeadingOnes64(unsigned __int64);
    unsigned int _CountLeadingSigns(long);
    unsigned int _CountLeadingSigns64(__int64);
    unsigned int _CountLeadingZeros(unsigned long);
    unsigned int _CountLeadingZeros64(unsigned __int64);
    unsigned int _CountOneBits(unsigned long);
    unsigned int _CountOneBits64(unsigned __int64);
    int _DAddSatInt(int, int);
    int _DSubSatInt(int, int);
    int _isunordered(double, double);
    int _isunorderedf(float, float);
    unsigned int _MoveFromCoprocessor(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int);
    unsigned int _MoveFromCoprocessor2(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int);
    unsigned __int64 _MoveFromCoprocessor64(unsigned int, unsigned int, unsigned int);
    void _MoveToCoprocessor(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int);
    void _MoveToCoprocessor2(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, unsigned int);
    void _MoveToCoprocessor64(unsigned __int64, unsigned int, unsigned int, unsigned int);
    long _MulHigh(long, long);
    unsigned long _MulUnsignedHigh(unsigned long, unsigned long);
    int _ReadBankedReg(int _Reg);
    int _ReadStatusReg(int);
    int _SubSatInt(int, int);
    void _WriteBankedReg(int _Value, int _Reg);
    void _WriteStatusReg(int, int, int);

    void __assume(int);
    void __code_seg(const char *);
    void __cdecl __debugbreak(void);
    void __fastfail(unsigned int);
    void __nop(void);
    void __yield(void);
    void * _AddressOfReturnAddress(void);
    unsigned char _BitScanForward(unsigned long *, unsigned long);
    unsigned char _BitScanForward64(unsigned long *, unsigned __int64);
    unsigned char _BitScanReverse(unsigned long *, unsigned long);
    unsigned char _BitScanReverse64(unsigned long *, unsigned __int64);
    unsigned char _bittest(long const *, long);
    unsigned char _bittest64(__int64 const *, __int64);
    unsigned char _bittestandcomplement(long *, long);
    unsigned char _bittestandreset(long *, long);
    unsigned char _bittestandset(long *, long);
    unsigned __int64 __cdecl _byteswap_uint64(unsigned __int64);
    unsigned long __cdecl _byteswap_ulong(unsigned long);
    unsigned short __cdecl _byteswap_ushort(unsigned short);
    void __cdecl _disable(void);
    void __cdecl _enable(void);
    unsigned long __cdecl _lrotl(unsigned long, int);
    unsigned long __cdecl _lrotr(unsigned long, int);
    void _ReadBarrier(void);
    void _ReadWriteBarrier(void);
    void * _ReturnAddress(void);
    unsigned int __cdecl _rotl(unsigned int _Value, int _Shift);
    unsigned short _rotl16(unsigned short _Value, unsigned char _Shift);
    unsigned __int64 __cdecl _rotl64(unsigned __int64 _Value, int _Shift);
    unsigned char _rotl8(unsigned char _Value, unsigned char _Shift);
    unsigned int __cdecl _rotr(unsigned int _Value, int _Shift);
    unsigned short _rotr16(unsigned short _Value, unsigned char _Shift);
    unsigned __int64 __cdecl _rotr64(unsigned __int64 _Value, int _Shift);
    unsigned char _rotr8(unsigned char _Value, unsigned char _Shift);
    int __cdecl _setjmpex(jmp_buf);
    void _WriteBarrier(void);

    long _InterlockedAdd(long _volatile*, long);
    __int64 _InterlockedAdd64(__int64 volatile*, __int64);
    __int64 _InterlockedAdd64_acq(__int64 volatile*, __int64);
    __int64 _InterlockedAdd64_nf(__int64 volatile*, __int64);
    __int64 _InterlockedAdd64_rel(__int64 volatile*, __int64);
    long _InterlockedAdd_acq(long volatile*, long);
    long _InterlockedAdd_nf(long volatile*, long);
    long _InterlockedAdd_rel(long volatile*, long);
    long _InterlockedAnd(long volatile*, long);
    short _InterlockedAnd16(short volatile*, short);
    short _InterlockedAnd16_acq(short volatile*, short);
    short _InterlockedAnd16_nf(short volatile*, short);
    short _InterlockedAnd16_rel(short volatile*, short);
    __int64 _InterlockedAnd64(__int64 volatile*, __int64);
    __int64 _InterlockedAnd64_acq(__int64 volatile*, __int64);
    __int64 _InterlockedAnd64_nf(__int64 volatile*, __int64);
    __int64 _InterlockedAnd64_rel(__int64 volatile*, __int64);
    char _InterlockedAnd8(char volatile*, char);
    char _InterlockedAnd8_acq(char volatile*, char);
    char _InterlockedAnd8_nf(char volatile*, char);
    char _InterlockedAnd8_rel(char volatile*, char);
    long _InterlockedAnd_acq(long volatile*, long);
    long _InterlockedAnd_nf(long volatile*, long);
    long _InterlockedAnd_rel(long volatile*, long);
    long __cdecl _InterlockedCompareExchange(long volatile*, long, long);
    short _InterlockedCompareExchange16(short volatile*, short, short);
    short _InterlockedCompareExchange16_acq(short volatile*, short, short);
    short _InterlockedCompareExchange16_nf(short volatile*, short, short);
    short _InterlockedCompareExchange16_rel(short volatile*, short, short);
    __int64 _InterlockedCompareExchange64(__int64 volatile*, __int64, __int64);
    __int64 _InterlockedCompareExchange64_acq(__int64 volatile *, __int64, __int64);
    __int64 _InterlockedCompareExchange64_nf(__int64 volatile*, __int64, __int64);
    __int64 _InterlockedCompareExchange64_rel(__int64 volatile*, __int64, __int64);
    char _InterlockedCompareExchange8(char volatile*, char, char);
    char _InterlockedCompareExchange8_acq(char volatile*, char, char);
    char _InterlockedCompareExchange8_nf(char volatile*, char, char);
    char _InterlockedCompareExchange8_rel(char volatile*, char, char);
    void * _InterlockedCompareExchangePointer(void * volatile*, void *, void *);
    void * _InterlockedCompareExchangePointer_acq(void * volatile*, void *, void *);
    void * _InterlockedCompareExchangePointer_nf(void * volatile *, void *, void *);
    void * _InterlockedCompareExchangePointer_rel(void * volatile *, void *, void *);
    long _InterlockedCompareExchange_acq(long volatile*, long, long);
    long _InterlockedCompareExchange_nf(long volatile*, long, long);
    long _InterlockedCompareExchange_rel(long volatile*, long, long);
    long __cdecl _InterlockedDecrement(long volatile*);
    short _InterlockedDecrement16(short volatile*);
    short _InterlockedDecrement16_acq(short volatile*);
    short _InterlockedDecrement16_nf(short volatile*);
    short _InterlockedDecrement16_rel(short volatile*);
    __int64 _InterlockedDecrement64(__int64 volatile*);
    __int64 _InterlockedDecrement64_acq(__int64 volatile*);
    __int64 _InterlockedDecrement64_nf(__int64 volatile*);
    __int64 _InterlockedDecrement64_rel(__int64 volatile*);
    long _InterlockedDecrement_acq(long volatile*);
    long _InterlockedDecrement_nf(long volatile*);
    long _InterlockedDecrement_rel(long volatile*);
    long __cdecl _InterlockedExchange(long volatile* _Target, long);
    short _InterlockedExchange16(short volatile* _Target, short);
    short _InterlockedExchange16_acq(short volatile* _Target, short);
    short _InterlockedExchange16_nf(short volatile* _Target, short);
    __int64 _InterlockedExchange64(__int64 volatile* _Target, __int64);
    __int64 _InterlockedExchange64_acq(__int64 volatile* _Target, __int64);
    __int64 _InterlockedExchange64_nf(__int64 volatile* _Target, __int64);
    char _InterlockedExchange8(char volatile* _Target, char);
    char _InterlockedExchange8_acq(char volatile* _Target, char);
    char _InterlockedExchange8_nf(char volatile* _Target, char);
    ong __cdecl _InterlockedExchangeAdd(long volatile*, long);
    short _InterlockedExchangeAdd16(short volatile*, short);
    short _InterlockedExchangeAdd16_acq(short volatile*, short);
    short _InterlockedExchangeAdd16_nf(short volatile*, short);
    short _InterlockedExchangeAdd16_rel(short volatile*, short);
    __int64 _InterlockedExchangeAdd64(__int64 volatile*, __int64);
    __int64 _InterlockedExchangeAdd64_acq(__int64 volatile*, __int64);
    __int64 _InterlockedExchangeAdd64_nf(__int64 volatile*, __int64);
    __int64 _InterlockedExchangeAdd64_rel(__int64 volatile*, __int64);
    char _InterlockedExchangeAdd8(char volatile*, char);
    char _InterlockedExchangeAdd8_acq(char volatile*, char);
    char _InterlockedExchangeAdd8_nf(char volatile*, char);
    char _InterlockedExchangeAdd8_rel(char volatile*, char);
    long _InterlockedExchangeAdd_acq(long volatile*, long);
    long _InterlockedExchangeAdd_nf(long volatile*, long);
    long _InterlockedExchangeAdd_rel(long volatile*, long);
    void * _InterlockedExchangePointer(void * volatile* _Target, void *);
    void * _InterlockedExchangePointer_acq(void * volatile* _Target, void *);
    void * _InterlockedExchangePointer_nf(void * volatile* _Target, void *);
    long _InterlockedExchange_acq(long volatile* _Target, long);
    long _InterlockedExchange_nf(long volatile* _Target, long);
    long __cdecl _InterlockedIncrement(long volatile*);
    short _InterlockedIncrement16(short volatile*);
    short _InterlockedIncrement16_acq(short volatile*);
    short _InterlockedIncrement16_nf(short volatile*);
    short _InterlockedIncrement16_rel(short volatile*);
    __int64 _InterlockedIncrement64(__int64 volatile*);
    __int64 _InterlockedIncrement64_acq(__int64 volatile*);
    __int64 _InterlockedIncrement64_nf(__int64 volatile*);
    __int64 _InterlockedIncrement64_rel(__int64 volatile*);
    long _InterlockedIncrement_acq(long volatile*);
    long _InterlockedIncrement_nf(long volatile*);
    long _InterlockedIncrement_rel(long volatile*);
    long _InterlockedOr(long volatile*, long);
    short _InterlockedOr16(short volatile*, short);
    short _InterlockedOr16_acq(short volatile*, short);
    short _InterlockedOr16_nf(short volatile*, short);
    short _InterlockedOr16_rel(short volatile*, short);
    __int64 _InterlockedOr64(__int64 volatile*, __int64);
    __int64 _InterlockedOr64_acq(__int64 volatile*, __int64);
    __int64 _InterlockedOr64_nf(__int64 volatile*, __int64);
    __int64 _InterlockedOr64_rel(__int64 volatile*, __int64);
    char _InterlockedOr8(char volatile*, char);
    char _InterlockedOr8_acq(char volatile*, char);
    char _InterlockedOr8_nf(char volatile*, char);
    char _InterlockedOr8_rel(char volatile*, char);
    long _InterlockedOr_acq(long volatile*, long);
    long _InterlockedOr_nf(long volatile*, long);
    long _InterlockedOr_rel(long volatile*, long);
    long _InterlockedXor(long volatile*, long);
    short _InterlockedXor16(short volatile*, short);
    short _InterlockedXor16_acq(short volatile*, short);
    short _InterlockedXor16_nf(short volatile*, short);
    short _InterlockedXor16_rel(short volatile*, short);
    __int64 _InterlockedXor64(__int64 volatile*, __int64);
    __int64 _InterlockedXor64_acq(__int64 volatile*, __int64);
    __int64 _InterlockedXor64_nf(__int64 volatile*, __int64);
    __int64 _InterlockedXor64_rel(__int64 volatile*, __int64);
    char _InterlockedXor8(char volatile*, char);
    char _InterlockedXor8_acq(char volatile*, char);
    char _InterlockedXor8_nf(char volatile*, char);
    char _InterlockedXor8_rel(char volatile*, char);
    long _InterlockedXor_acq(long volatile*, long);
    long _InterlockedXor_nf(long volatile*, long);
    long _InterlockedXor_rel(long volatile*, long);
    unsigned char _interlockedbittestandreset(long volatile*, long);
    unsigned char _interlockedbittestandreset_acq(long volatile*, long);
    unsigned char _interlockedbittestandreset_nf(long volatile*, long);
    unsigned char _interlockedbittestandreset_rel(long volatile*, long);
    unsigned char _interlockedbittestandset(long volatile*, long);
    unsigned char _interlockedbittestandset_acq(long volatile*, long);
    unsigned char _interlockedbittestandset_nf(long volatile*, long);
    unsigned char _interlockedbittestandset_rel(long volatile*, long);
    
    // common intrinsics
    void * __builtin_apply_args ();
    void * __builtin_apply (void (*function);();, void *arguments, size_t size);
    void __builtin_return (void *result);
    __builtin_va_arg_pack ();
    size_t __builtin_va_arg_pack_len ();
    void * __builtin_return_address (unsigned int level);
    void * __builtin_extract_return_addr (void *addr);
    void * __builtin_frob_return_address (void *addr);
    void * __builtin_frame_address (unsigned int level);
    type __atomic_load_n (type *ptr, int memmodel);
    void __atomic_load (type *ptr, type *ret, int memmodel);
    void __atomic_store_n (type *ptr, type val, int memmodel);
    void __atomic_store (type *ptr, type *val, int memmodel);
    type __atomic_exchange_n (type *ptr, type val, int memmodel);
    void __atomic_exchange (type *ptr, type *val, type *ret, int memmodel);
    bool __atomic_compare_exchange_n (type *ptr, type *expected, type desired, bool weak, int success_memmodel, int failure_memmodel);
    bool __atomic_compare_exchange (type *ptr, type *expected, type *desired, bool weak, int success_memmodel, int failure_memmodel);
    type __atomic_add_fetch (type *ptr, type val, int memmodel);
    type __atomic_sub_fetch (type *ptr, type val, int memmodel);
    type __atomic_and_fetch (type *ptr, type val, int memmodel);
    type __atomic_xor_fetch (type *ptr, type val, int memmodel);
    type __atomic_or_fetch (type *ptr, type val, int memmodel);
    type __atomic_nand_fetch (type *ptr, type val, int memmodel);
    type __atomic_fetch_add (type *ptr, type val, int memmodel);
    type __atomic_fetch_sub (type *ptr, type val, int memmodel);
    type __atomic_fetch_and (type *ptr, type val, int memmodel);
    type __atomic_fetch_xor (type *ptr, type val, int memmodel);
    type __atomic_fetch_or (type *ptr, type val, int memmodel);
    type __atomic_fetch_nand (type *ptr, type val, int memmodel);
    bool __atomic_test_and_set (void *ptr, int memmodel);
    void __atomic_clear (bool *ptr, int memmodel);
    void __atomic_thread_fence (int memmodel);
    void __atomic_signal_fence (int memmodel);
    bool __atomic_always_lock_free (size_t size, void *ptr);
    bool __atomic_is_lock_free (size_t size, void *ptr);
    size_t __builtin_object_size (void * ptr, int type);
    int __builtin_types_compatible_p (type1, type2);
    type __builtin_choose_expr (const_exp, exp1, exp2);
    type __builtin_complex (real, imag);
    int __builtin_constant_p (exp);
    long __builtin_expect (long exp, long c);
    void __builtin_trap (void);
    void __builtin_unreachable (void);
    void *__builtin_assume_aligned (const void *exp, size_t align, ...);
    int __builtin_LINE ();
    int __builtin_FUNCTION ();
    int __builtin_FILE ();
    void __builtin___clear_cache (char *begin, char *end);
    void __builtin_prefetch (const void *addr, ...);
    double __builtin_huge_val (void);
    float __builtin_huge_valf (void);
    long double __builtin_huge_vall (void);
    int __builtin_fpclassify (int, int, int, int, int, ...);
    double __builtin_inf (void);
    _Decimal32 __builtin_infd32 (void);
    _Decimal64 __builtin_infd64 (void);
    _Decimal128 __builtin_infd128 (void);
    float __builtin_inff (void);
    long double __builtin_infl (void);
    int __builtin_isinf_sign (...);
    double __builtin_nan (const char *str);
    _Decimal32 __builtin_nand32 (const char *str);
    _Decimal64 __builtin_nand64 (const char *str);
    _Decimal128 __builtin_nand128 (const char *str);
    float __builtin_nanf (const char *str);
    long double __builtin_nanl (const char *str);
    double __builtin_nans (const char *str);
    float __builtin_nansf (const char *str);
    long double __builtin_nansl (const char *str);
    int __builtin_ffs (unsigned int x);
    int __builtin_clz (unsigned int x);
    int __builtin_ctz (unsigned int x);
    int __builtin_clrsb (int x);
    int __builtin_parity (unsigned int x);
    int __builtin_ffsl (unsigned long);
    int __builtin_clzl (unsigned long);
    int __builtin_ctzl (unsigned long);
    int __builtin_clrsbl (long);
    int __builtin_parityl (unsigned long);
    int __builtin_ffsll (unsigned long long);
    int __builtin_clzll (unsigned long long);
    int __builtin_ctzll (unsigned long long);
    int __builtin_clrsbll (long long);
    int __builtin_parityll (unsigned long long);
    double __builtin_powi (double, int);
    float __builtin_powif (float, int);
    long double __builtin_powil (long double, int);
    uint16_t __builtin_bswap16 (uint16_t x);
    uint32_t __builtin_bswap32 (uint32_t x);
    uint64_t __builtin_bswap64 (uint64_t x);
    void *__builtin_alloca (size_t size);
    void *__builtin_alloca_with_align (size_t size, size_t alignment);
    void *__builtin_alloca_with_align_and_max (size_t size, size_t alignment, size_t max_size);
    bool __builtin_has_attribute (type-or-expression, attribute);
    type __builtin_speculation_safe_value (type val, type failval);
    type __builtin_call_with_static_chain (call_exp, pointer_exp);
    type __builtin_tgmath (functions, arguments);
    bool __builtin_is_constant_evaluated (void);
    long __builtin_expect_with_probability (long exp, long c, double probability);
    void * __builtin_assume_aligned (const void *exp, size_t align, ...);
    const char * __builtin_FUNCTION ();
    const char * __builtin_FILE ();
    void __builtin___clear_cache (void *begin, void *end);
    size_t __builtin_object_size (const void * ptr, int type);
    _Floatn __builtin_huge_valfn (void);
    _Floatnx __builtin_huge_valfnx (void);
    _Floatn __builtin_inffn (void);
    _Floatn __builtin_inffnx (void);
    _Floatn __builtin_nanfn (const char *str);
    _Floatnx __builtin_nanfnx (const char *str);
    _Floatn __builtin_nansfn (const char *str);
    _Floatnx __builtin_nansfnx (const char *str);
    int __builtin_ffs (int x);
    int __builtin_ffsl (long);
    int __builtin_ffsll (long long);
    uint128_t __builtin_bswap128 (uint128_t x);
    Pmode __builtin_extend_pointer (void * x);
    int __builtin_goacc_parlevel_id (int x);
    int __builtin_goacc_parlevel_size (int x);
    int __builtin_popcount (unsigned int);
    int __builtin_popcountl (unsigned long);
    int __builtin_popcountll (unsigned long long);
    __sync_synchronize (...);
    type __sync_lock_test_and_set (type *ptr, type value, ...);
    void __sync_lock_release (type *ptr, ...);
    type __sync_fetch_and_add (type *ptr, type value, ...);
    type __sync_fetch_and_sub (type *ptr, type value, ...);
    type __sync_fetch_and_or (type *ptr, type value, ...);
    type __sync_fetch_and_and (type *ptr, type value, ...);
    type __sync_fetch_and_xor (type *ptr, type value, ...);
    type __sync_fetch_and_nand (type *ptr, type value, ...);
    type __sync_add_and_fetch (type *ptr, type value, ...);
    type __sync_sub_and_fetch (type *ptr, type value, ...);
    type __sync_or_and_fetch (type *ptr, type value, ...);
    type __sync_and_and_fetch (type *ptr, type value, ...);
    type __sync_xor_and_fetch (type *ptr, type value, ...);
    type __sync_nand_and_fetch (type *ptr, type value, ...);
    bool __sync_bool_compare_and_swap (type *ptr, type oldval, type newval, ...);
    type __sync_val_compare_and_swap (type *ptr, type oldval, type newval, ...);
         
    // Non-AArch64 intrinsics
    char _InterlockedAnd8(char volatile *, char);
    char _InterlockedAnd8_np(char *, char); //expect: PythonIntrinsicIssue
    char _InterlockedCompareExchange8(char volatile *, char, char);
    char _InterlockedExchange8(char volatile *, char);
    char _InterlockedExchangeAdd8(char volatile *, char);
    char _InterlockedOr8(char volatile *, char);
    char _InterlockedOr8_np(char *, char); //expect: PythonIntrinsicIssue
    char _InterlockedXor8(char volatile *, char);
    char _InterlockedXor8_np(char *, char); //expect: PythonIntrinsicIssue
    di __builtin_ia32_pand(di, di); //expect: PythonIntrinsicIssue
    di __builtin_ia32_pandn(di,di); //expect: PythonIntrinsicIssue
    di __builtin_ia32_por(di, di); //expect: PythonIntrinsicIssue
    di __builtin_ia32_pxor(di, di); //expect: PythonIntrinsicIssue
    double _mm_cvtsd_f64(__m128d); //expect: PythonIntrinsicIssue
    __float128 __builtin_copysignq(__float128, __float128); //expect: PythonIntrinsicIssue
    __float128 __builtin_huge_valq(void); //expect: PythonIntrinsicIssue
    __float128 __builtin_infq(void); //expect: PythonIntrinsicIssue
    __float128 __builtin_fabsq(__float128); //expect: PythonIntrinsicIssue
    float __builtin_ia32_vec_ext_v4sf(v4sf, const int); //expect: PythonIntrinsicIssue
    float _mm_cvtss_f32(__m128); //expect: PythonIntrinsicIssue
    float _m_to_float(__m64); //expect: PythonIntrinsicIssue
    __int64 _div128(__int64, __int64, __int64, __int64 *); //expect: PythonIntrinsicIssue
    __int64 _InterlockedAnd64_HLEAcquire(__int64 volatile *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedAnd64_HLERelease(__int64 volatile *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedAnd64(__int64 volatile *, __int64);
    __int64 _InterlockedAnd64_np(__int64 *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedCompareExchange64_HLEAcquire(__int64 volatile *, __int64, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedCompareExchange64_HLERelease(__int64 volatile *, __int64, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedCompareExchange64(__int64 volatile *, __int64, __int64);
    __int64 _InterlockedCompareExchange64_np(__int64 *, __int64, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedDecrement64(__int64 volatile *);
    __int64 _InterlockedExchange64_HLEAcquire(__int64 volatile *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedExchange64_HLERelease(__int64 volatile *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedExchange64(__int64 volatile *, __int64);
    __int64 _InterlockedExchangeAdd64_HLEAcquire(__int64 volatile *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedExchangeAdd64_HLERelease(__int64 volatile *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedExchangeAdd64(__int64 volatile *, __int64);
    __int64 _InterlockedIncrement64(__int64 volatile *);
    __int64 _InterlockedOr64_HLEAcquire(__int64 volatile *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedOr64_HLERelease(__int64 volatile *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedOr64(__int64 volatile *, __int64);
    __int64 _InterlockedOr64_np(__int64 *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedXor64_HLEAcquire(__int64 volatile *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedXor64_HLERelease(__int64 volatile *, __int64); //expect: PythonIntrinsicIssue
    __int64 _InterlockedXor64(__int64 volatile *, __int64);
    __int64 _InterlockedXor64_np(__int64 *, __int64); //expect: PythonIntrinsicIssue
    __int64 _loadbe_i64(void const *); //expect: PythonIntrinsicIssue
    __int64 _mm_cvtsd_si64(__m128d); //expect: PythonIntrinsicIssue
    __int64 _mm_cvtsd_si64x(__m128d); //expect: PythonIntrinsicIssue
    __int64 _mm_cvtsi128_si64(__m128i); //expect: PythonIntrinsicIssue
    __int64 _mm_cvtsi128_si64x(__m128i); //expect: PythonIntrinsicIssue
    __int64 _mm_cvtss_si64(__m128); //expect: PythonIntrinsicIssue
    __int64 _mm_cvtss_si64x(__m128); //expect: PythonIntrinsicIssue
    __int64 _mm_cvttsd_si64(__m128d); //expect: PythonIntrinsicIssue
    __int64 _mm_cvttsd_si64x(__m128d); //expect: PythonIntrinsicIssue
    __int64 _mm_cvttss_si64(__m128); //expect: PythonIntrinsicIssue
    __int64 _mm_cvttss_si64x(__m128); //expect: PythonIntrinsicIssue
    __int64 _mm_extract_epi64(__m128i, const int); //expect: PythonIntrinsicIssue
    __int64 _mm_popcnt_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    __int64 _mul128(__int64, __int64, __int64 *); //expect: PythonIntrinsicIssue
    __int64 __mulh(__int64, __int64); //expect: PythonIntrinsicIssue
    __int64 __emul(int, int); //expect: PythonIntrinsicIssue
    __int64 __ll_rshift(__int64, int); //expect: PythonIntrinsicIssue
    __int64 _sarx_i64(__int64, unsigned int); //expect: PythonIntrinsicIssue
    int __builtin_cpu_is(const char *); //expect: PythonIntrinsicIssue
    int __builtin_cpu_supports(const char *); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comieq(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comige(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comigt(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comile(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comilt(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comineq(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comisdeq(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comisdge(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comisdgt(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comisdle(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comisdlt(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_comisdneq(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_cvtsd2si(v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_cvtss2si(v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_cvttsd2si(v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_cvttss2si(v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_movmskpd256(v4df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_movmskpd(v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_movmskps256(v8sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_movmskps(v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpestri128(v16qi, int, v16qi, int, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpestria128(v16qi, int, v16qi, int, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpestric128(v16qi, int, v16qi, int, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpestrio128(v16qi, int, v16qi, int, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpestris128(v16qi, int, v16qi, int, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpestriz128(v16qi, int, v16qi, int, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpistri128(v16qi, v16qi, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpistria128(v16qi, v16qi, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpistric128(v16qi, v16qi, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpistrio128(v16qi, v16qi, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpistris128(v16qi, v16qi, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pcmpistriz128(v16qi, v16qi, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pextrw(v4hi, int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pmovmskb128(v16qi); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pmovmskb256(v32qi); //expect: PythonIntrinsicIssue
    int __builtin_ia32_pmovmskb(v8qi); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ptestc128(v2di, v2di); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ptestc256(v4di, v4di, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ptestnzc128(v2di, v2di); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ptestnzc256(v4di, v4di, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ptestz128(v2di, v2di); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ptestz256(v4di, v4di, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomieq(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomige(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomigt(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomile(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomilt(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomineq(v4sf, v4sf); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomisdeq(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomisdge(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomisdgt(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomisdle(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomisdlt(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_ucomisdneq(v2df, v2df); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vec_ext_v16qi(v16qi, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vec_ext_v4si(v4si, const int); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestcpd256(v4df, v4df, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestcpd(v2df, v2df, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestcps256(v8sf, v8sf, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestcps(v4sf, v4sf, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestnzcpd256(v4df, v4df, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestnzcpd(v2df, v2df, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestnzcps256(v8sf, v8sf, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestnzcps(v4sf, v4sf, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestzpd256(v4df, v4df, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestzpd(v2df, v2df, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestzps256(v8sf, v8sf, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_vtestzps(v4sf, v4sf, ptest); //expect: PythonIntrinsicIssue
    int __builtin_ia32_xbegin(); //expect: PythonIntrinsicIssue
    int __builtin_ia32_xtest(); //expect: PythonIntrinsicIssue
    int _div64(__int64, int, int *); //expect: PythonIntrinsicIssue
    int _loadbe_i32(void const *); //expect: PythonIntrinsicIssue
    int _mm256_movemask_epi8(__m256i); //expect: PythonIntrinsicIssue
    int _mm256_movemask_pd(__m256d); //expect: PythonIntrinsicIssue
    int _mm256_movemask_ps(__m256); //expect: PythonIntrinsicIssue
    int _mm256_testc_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    int _mm256_testc_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    int _mm256_testc_si256(__m256i, __m256i); //expect: PythonIntrinsicIssue
    int _mm256_testnzc_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    int _mm256_testnzc_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    int _mm256_testnzc_si256(__m256i, __m256i); //expect: PythonIntrinsicIssue
    int _mm256_testz_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    int _mm256_testz_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    int _mm256_testz_si256(__m256i, __m256i); //expect: PythonIntrinsicIssue
    int _mm_cmpestra(__m128i, int, __m128i, int, const int); //expect: PythonIntrinsicIssue
    int _mm_cmpestrc(__m128i, int, __m128i, int, const int); //expect: PythonIntrinsicIssue
    int _mm_cmpestri(__m128i, int, __m128i, int, const int); //expect: PythonIntrinsicIssue
    int _mm_cmpestro(__m128i, int, __m128i, int, const int); //expect: PythonIntrinsicIssue
    int _mm_cmpestrs(__m128i, int, __m128i, int, const int); //expect: PythonIntrinsicIssue
    int _mm_cmpestrz(__m128i, int, __m128i, int, const int); //expect: PythonIntrinsicIssue
    int _mm_cmpistra(__m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    int _mm_cmpistrc(__m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    int _mm_cmpistri(__m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    int _mm_cmpistro(__m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    int _mm_cmpistrs(__m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    int _mm_cmpistrz(__m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    int _mm_comieq_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_comieq_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_comige_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_comige_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_comigt_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_comigt_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_comile_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_comile_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_comilt_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_comilt_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_comineq_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_comineq_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_cvtsd_si32(__m128d); //expect: PythonIntrinsicIssue
    int _mm_cvtsi128_si32(__m128i); //expect: PythonIntrinsicIssue
    int _mm_cvt_ss2si(__m128); //expect: PythonIntrinsicIssue
    int _mm_cvttsd_si32(__m128d); //expect: PythonIntrinsicIssue
    int _mm_cvtt_ss2si(__m128); //expect: PythonIntrinsicIssue
    int _mm_extract_epi16(__m128i, int); //expect: PythonIntrinsicIssue
    int _mm_extract_epi32(__m128i, const int); //expect: PythonIntrinsicIssue
    int _mm_extract_epi8(__m128i, const int); //expect: PythonIntrinsicIssue
    int _mm_extract_ps(__m128, const int); //expect: PythonIntrinsicIssue
    int _mm_movemask_epi8(__m128i); //expect: PythonIntrinsicIssue
    int _mm_movemask_pd(__m128d); //expect: PythonIntrinsicIssue
    int _mm_movemask_ps(__m128); //expect: PythonIntrinsicIssue
    int _mm_popcnt_u32(unsigned int); //expect: PythonIntrinsicIssue
    int _mm_testc_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_testc_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_testc_si128(__m128i, __m128i); //expect: PythonIntrinsicIssue
    int _mm_testnzc_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_testnzc_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_testnzc_si128(__m128i, __m128i); //expect: PythonIntrinsicIssue
    int _mm_testz_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_testz_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_testz_si128(__m128i, __m128i); //expect: PythonIntrinsicIssue
    int _mm_ucomieq_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_ucomieq_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_ucomige_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_ucomige_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_ucomigt_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_ucomigt_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_ucomile_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_ucomile_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_ucomilt_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_ucomilt_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _mm_ucomineq_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    int _mm_ucomineq_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    int _m_pextrw(__m64, int); //expect: PythonIntrinsicIssue
    int _m_pmovmskb(__m64); //expect: PythonIntrinsicIssue
    int _m_to_int(__m64); //expect: PythonIntrinsicIssue
    int _rdrand16_step(unsigned short *); //expect: PythonIntrinsicIssue
    int _rdrand32_step(unsigned int *); //expect: PythonIntrinsicIssue
    int _rdrand64_step(unsigned __int64 *); //expect: PythonIntrinsicIssue
    int _rdseed16_step(unsigned short *); //expect: PythonIntrinsicIssue
    int _rdseed32_step(unsigned int *); //expect: PythonIntrinsicIssue
    int _rdseed64_step(unsigned __int64 *); //expect: PythonIntrinsicIssue
    int _sarx_i32(int, unsigned int); //expect: PythonIntrinsicIssue
    long _InterlockedAddLargeStatistic(__int64 volatile *, long); //expect: PythonIntrinsicIssue
    long _InterlockedAnd_HLEAcquire(long volatile *, long); //expect: PythonIntrinsicIssue
    long _InterlockedAnd_HLERelease(long volatile *, long); //expect: PythonIntrinsicIssue
    long _InterlockedAnd(long volatile *, long);
    long _InterlockedAnd_np(long *, long); //expect: PythonIntrinsicIssue
    long _InterlockedCompareExchange_HLEAcquire(long volatile *, long, long); //expect: PythonIntrinsicIssue
    long _InterlockedCompareExchange_HLERelease(long volatile *, long, long); //expect: PythonIntrinsicIssue
    long _InterlockedCompareExchange(long volatile *, long, long);
    long _InterlockedCompareExchange_np(long *, long, long); //expect: PythonIntrinsicIssue
    long _InterlockedDecrement(long volatile *);
    long _InterlockedExchangeAdd_HLEAcquire(long volatile *, long); //expect: PythonIntrinsicIssue
    long _InterlockedExchangeAdd_HLERelease(long volatile *, long); //expect: PythonIntrinsicIssue
    long _InterlockedExchangeAdd(long volatile *, long);
    long _InterlockedExchange_HLEAcquire(long volatile *, long); //expect: PythonIntrinsicIssue
    long _InterlockedExchange_HLERelease(long volatile *, long); //expect: PythonIntrinsicIssue
    long _InterlockedExchange(long volatile *, long);
    long _InterlockedIncrement(long volatile *);
    long _InterlockedOr_HLEAcquire(long volatile *, long); //expect: PythonIntrinsicIssue
    long _InterlockedOr_HLERelease(long volatile *, long); //expect: PythonIntrinsicIssue
    long _InterlockedOr(long volatile *, long);
    long _InterlockedOr_np(long *, long); //expect: PythonIntrinsicIssue
    long _InterlockedXor_HLEAcquire(long volatile *, long); //expect: PythonIntrinsicIssue
    long _InterlockedXor_HLERelease(long volatile *, long); //expect: PythonIntrinsicIssue
    long _InterlockedXor(long volatile *, long);
    long _InterlockedXor_np(long *, long); //expect: PythonIntrinsicIssue
    long long __builtin_ia32_cvtsd2si64(v2df); //expect: PythonIntrinsicIssue
    long long __builtin_ia32_cvttsd2si64(v2df); //expect: PythonIntrinsicIssue
    long long __builtin_ia32_vec_ext_v2di(v2di, const int); //expect: PythonIntrinsicIssue
    __m128d _mm256_castpd256_pd128(__m256d); //expect: PythonIntrinsicIssue
    __m128d _mm256_extractf128_pd(__m256d, const int); //expect: PythonIntrinsicIssue
    __m128d _mm_add_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_add_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_addsub_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_andnot_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_and_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_blend_pd(__m128d, __m128d, const int); //expect: PythonIntrinsicIssue
    __m128d _mm_blendv_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_broadcastsd_pd(__m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_castps_pd(__m128); //expect: PythonIntrinsicIssue
    __m128d _mm_castsi128_pd(__m128i); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpeq_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpeq_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpge_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpge_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpgt_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpgt_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmple_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmple_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmplt_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmplt_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpneq_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpneq_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpnge_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpnge_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpngt_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpngt_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpnle_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpnle_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpnlt_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpnlt_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpord_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpord_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmp_pd(__m128d, __m128d, const int); //expect: PythonIntrinsicIssue
    __m128d _mm_cmp_sd(__m128d, __m128d, const int); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpunord_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cmpunord_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_cvtepi32_pd(__m128i); //expect: PythonIntrinsicIssue
    __m128d _mm_cvtpi32_pd(__m64); //expect: PythonIntrinsicIssue
    __m128d _mm_cvtps_pd(__m128); //expect: PythonIntrinsicIssue
    __m128d _mm_cvtsi32_sd(__m128d, int); //expect: PythonIntrinsicIssue
    __m128d _mm_cvtsi64_sd(__m128d, __int64); //expect: PythonIntrinsicIssue
    __m128d _mm_cvtsi64x_sd(__m128d, __int64); //expect: PythonIntrinsicIssue
    __m128d _mm_cvtss_sd(__m128d, __m128); //expect: PythonIntrinsicIssue
    __m128d _mm_div_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_div_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_dp_pd(__m128d, __m128d, const int); //expect: PythonIntrinsicIssue
    __m128d _mm_fmadd_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_fmadd_sd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_fmaddsub_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_fmsubadd_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_fmsub_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_fmsub_sd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_fnmadd_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_fnmadd_sd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_fnmsub_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_fnmsub_sd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_frcz_pd(__m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_frcz_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_hadd_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_hsub_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_i32gather_pd(double const *, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128d _mm_i64gather_pd(double const *, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128d _mm_load1_pd(double *); //expect: PythonIntrinsicIssue
    __m128d _mm_loaddup_pd(double const *); //expect: PythonIntrinsicIssue
    __m128d _mm_loadh_pd(__m128d, double *); //expect: PythonIntrinsicIssue
    __m128d _mm_loadl_pd(__m128d, double *); //expect: PythonIntrinsicIssue
    __m128d _mm_load_pd(double *); //expect: PythonIntrinsicIssue
    __m128d _mm_loadr_pd(double *); //expect: PythonIntrinsicIssue
    __m128d _mm_load_sd(double *); //expect: PythonIntrinsicIssue
    __m128d _mm_loadu_pd(double *); //expect: PythonIntrinsicIssue
    __m128d _mm_macc_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_macc_sd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_maddsub_pd(__m128d , __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_mask_i32gather_pd(__m128d, double const *, __m128i, __m128d, const int); //expect: PythonIntrinsicIssue
    __m128d _mm_mask_i64gather_pd(__m128d, double const *, __m128i, __m128d, const int); //expect: PythonIntrinsicIssue
    __m128d _mm_maskload_pd(double const *, __m128i); //expect: PythonIntrinsicIssue
    __m128d _mm_max_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_max_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_min_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_min_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_movedup_pd(__m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_move_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_msubadd_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_msub_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_msub_sd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_mul_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_mul_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_nmacc_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_nmacc_sd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_nmsub_pd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_nmsub_sd(__m128d, __m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_or_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_permute2_pd(__m128d, __m128d, __m128i, int); //expect: PythonIntrinsicIssue
    __m128d _mm_permute_pd(__m128d, int); //expect: PythonIntrinsicIssue
    __m128d _mm_permutevar_pd(__m128d, __m128i); //expect: PythonIntrinsicIssue
    __m128d _mm_round_pd(__m128d, const int); //expect: PythonIntrinsicIssue
    __m128d _mm_round_sd(__m128d, __m128d, const int); //expect: PythonIntrinsicIssue
    __m128d _mm_set1_pd(double); //expect: PythonIntrinsicIssue
    __m128d _mm_set_pd(double, double); //expect: PythonIntrinsicIssue
    __m128d _mm_setr_pd(double, double); //expect: PythonIntrinsicIssue
    __m128d _mm_set_sd(double); //expect: PythonIntrinsicIssue
    __m128d _mm_setzero_pd(void); //expect: PythonIntrinsicIssue
    __m128d _mm_shuffle_pd(__m128d, __m128d, int); //expect: PythonIntrinsicIssue
    __m128d _mm_sqrt_pd(__m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_sqrt_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_sub_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_sub_sd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_unpackhi_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_unpacklo_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128d _mm_xor_pd(__m128d, __m128d); //expect: PythonIntrinsicIssue
    __m128i _mm256_castsi256_si128(__m256i); //expect: PythonIntrinsicIssue
    __m128i _mm256_cvtpd_epi32(__m256d); //expect: PythonIntrinsicIssue
    __m128i _mm256_cvtps_ph(__m256, const int); //expect: PythonIntrinsicIssue
    __m128i _mm256_cvttpd_epi32(__m256d); //expect: PythonIntrinsicIssue
    __m128i _mm256_extractf128_si256(__m256i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm256_extracti128_si256(__m256i, int); //expect: PythonIntrinsicIssue
    __m128i _mm256_mask_i64gather_epi32(__m128i, int const *, __m256i, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_abs_epi16(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_abs_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_abs_epi8(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_add_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_add_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_add_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_add_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_adds_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_adds_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_adds_epu16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_adds_epu8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_aesdeclast_si128(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_aesdec_si128(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_aesenclast_si128(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_aesenc_si128(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_aesimc_si128(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_aeskeygenassist_si128(__m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_alignr_epi8(__m128i, __m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_andnot_si128(__m128i , __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_andnot_si128(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_and_si128(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_avg_epu16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_avg_epu8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_blend_epi16(__m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_blend_epi32(__m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_blendv_epi8(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_broadcastb_epi8(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_broadcastd_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_broadcastq_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_broadcastw_epi16(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_castpd_si128(__m128d); //expect: PythonIntrinsicIssue
    __m128i _mm_castps_si128(__m128); //expect: PythonIntrinsicIssue
    __m128i _mm_clmulepi64_si128(__m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_cmov_si128(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cmpeq_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cmpeq_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cmpeq_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cmpeq_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cmpestrm(__m128i, int, __m128i, int, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_cmpgt_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cmpgt_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cmpgt_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cmpgt_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cmpistrm(__m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_cmplt_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cmplt_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cmplt_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_com_epi16(__m128i, __m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_com_epi32(__m128i, __m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_com_epi64(__m128i, __m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_com_epi8(__m128i, __m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_com_epu16(__m128i, __m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_com_epu32(__m128i, __m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_com_epu64(__m128i, __m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_com_epu8(__m128i, __m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepi16_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepi16_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepi32_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepi8_epi16(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepi8_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepi8_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepu16_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepu16_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepu32_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepu8_epi16(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepu8_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtepu8_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtpd_epi32(__m128d); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtps_epi32(__m128); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtps_ph(__m128, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtsi32_si128(int); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtsi64_si128(__int64); //expect: PythonIntrinsicIssue
    __m128i _mm_cvtsi64x_si128(__int64); //expect: PythonIntrinsicIssue
    __m128i _mm_cvttpd_epi32(__m128d); //expect: PythonIntrinsicIssue
    __m128i _mm_cvttps_epi32(__m128); //expect: PythonIntrinsicIssue
    __m128i _mm_extracti_si64(__m128i, int, int); //expect: PythonIntrinsicIssue
    __m128i _mm_extract_si64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddd_epi16(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddd_epi8(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddd_epu16(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddd_epu8(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_hadd_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_hadd_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddq_epi16(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddq_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddq_epi8(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddq_epu16(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddq_epu32(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddq_epu8(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_hadds_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddw_epi8(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_haddw_epu8(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_hsubd_epi16(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_hsub_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_hsub_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_hsubq_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_hsubs_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_hsubw_epi8(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_i32gather_epi32(int const *, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_i32gather_epi64(__int64 const *, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_i64gather_epi32(int const *, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_i64gather_epi64(__int64 const *, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_insert_epi16(__m128i, int, int); //expect: PythonIntrinsicIssue
    __m128i _mm_insert_epi32(__m128i, int, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_insert_epi64(__m128i, __int64, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_insert_epi8(__m128i, int, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_inserti_si64(__m128i, __m128i, int, int); //expect: PythonIntrinsicIssue
    __m128i _mm_insert_si64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_lddqu_si128(__m128i const *); //expect: PythonIntrinsicIssue
    __m128i _mm_loadl_epi64(__m128i *); //expect: PythonIntrinsicIssue
    __m128i _mm_load_si128(__m128i *); //expect: PythonIntrinsicIssue
    __m128i _mm_loadu_si128(__m128i *); //expect: PythonIntrinsicIssue
    __m128i _mm_maccd_epi16(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_macc_epi16(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_macc_epi32(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_macchi_epi32(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_macclo_epi32(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_maccsd_epi16(__m128i , __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_maccs_epi16(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_maccs_epi32(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_maccshi_epi32(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_maccslo_epi32(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_maddd_epi16(__m128i , __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_madd_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_maddsd_epi16(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_maddubs_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_mask_i32gather_epi32(__m128i, int const *, __m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_mask_i32gather_epi64(__m128i, __int64 const *, __m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_mask_i64gather_epi32(__m128i, int const *, __m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_mask_i64gather_epi64(__m128i, __int64 const *, __m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_maskload_epi32(int const *, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_maskload_epi64(__int64 const *, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_max_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_max_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_max_epi8 (__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_max_epu16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_max_epu32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_max_epu8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_min_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_min_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_min_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_min_epu16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_min_epu32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_min_epu8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_minpos_epu16(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_move_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_movpi64_epi64(__m64); //expect: PythonIntrinsicIssue
    __m128i _mm_mpsadbw_epu8(__m128i, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128i _mm_mul_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_mul_epu32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_mulhi_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_mulhi_epu16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_mulhrs_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_mullo_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_mullo_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_or_si128(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_packs_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_packs_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_packus_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_packus_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_perm_epi8(__m128i, __m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_rot_epi16(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_rot_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_rot_epi32(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_rot_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_rot_epi64(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_rot_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_rot_epi8(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_rot_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_roti_epi16(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_roti_epi32(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_roti_epi64(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_roti_epi8(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_sad_epu8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_set1_epi16(short); //expect: PythonIntrinsicIssue
    __m128i _mm_set1_epi32(int); //expect: PythonIntrinsicIssue
    __m128i _mm_set1_epi64(__m64); //expect: PythonIntrinsicIssue
    __m128i _mm_set1_epi64x(__int64); //expect: PythonIntrinsicIssue
    __m128i _mm_set1_epi8(char); //expect: PythonIntrinsicIssue
    __m128i _mm_set_epi16(short, short, short, short, short, short, short, short); //expect: PythonIntrinsicIssue
    __m128i _mm_set_epi32(int, int, int, int); //expect: PythonIntrinsicIssue
    __m128i _mm_set_epi64(__m64, __m64); //expect: PythonIntrinsicIssue
    __m128i _mm_set_epi64x(__int64, __int64); //expect: PythonIntrinsicIssue
    __m128i _mm_set_epi8(char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char); //expect: PythonIntrinsicIssue
    __m128i _mm_setl_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_setr_epi16(short, short, short, short, short, short, short, short); //expect: PythonIntrinsicIssue
    __m128i _mm_setr_epi32(int, int, int, int); //expect: PythonIntrinsicIssue
    __m128i _mm_setr_epi64(__m64, __m64); //expect: PythonIntrinsicIssue
    __m128i _mm_setr_epi8(char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char); //expect: PythonIntrinsicIssue
    __m128i _mm_setzero_si128(void); //expect: PythonIntrinsicIssue
    __m128i _mm_sha_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sha_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sha_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sha_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_shl_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_shl_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_shl_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_shl_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_shuffle_epi32(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_shuffle_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_shufflehi_epi16(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_shufflelo_epi16(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_sign_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sign_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sign_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sll_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sll_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sll_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_slli_epi16(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_slli_epi32(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_slli_epi64(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_slli_si128(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_sllv_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sllv_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sra_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sra_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_srai_epi16(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_srai_epi32(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_srav_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_srl_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_srl_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_srl_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_srli_epi16(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_srli_epi32(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_srli_epi64(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_srli_si128(__m128i, int); //expect: PythonIntrinsicIssue
    __m128i _mm_srlv_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_srlv_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_stream_load_si128(__m128i *); //expect: PythonIntrinsicIssue
    __m128i _mm_sub_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sub_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sub_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_sub_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_subs_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_subs_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_subs_epu16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_subs_epu8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_unpackhi_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_unpackhi_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_unpackhi_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_unpackhi_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_unpacklo_epi16(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_unpacklo_epi32(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_unpacklo_epi64(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_unpacklo_epi8(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128i _mm_xor_si128(__m128i, __m128i); //expect: PythonIntrinsicIssue
    __m128 _mm256_castps256_ps128(__m256); //expect: PythonIntrinsicIssue
    __m128 _mm256_cvtpd_ps(__m256d); //expect: PythonIntrinsicIssue
    __m128 _mm256_extractf128_ps(__m256, const int); //expect: PythonIntrinsicIssue
    __m128 _mm256_i64gather_ps(float const *, __m256i, const int); //expect: PythonIntrinsicIssue
    __m128 _mm256_mask_i64gather_ps(__m128, float const *, __m256i, __m128, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_add_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_add_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_addsub_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_andnot_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_and_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_blend_ps(__m128, __m128, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_blendv_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_broadcast_ss(float const *); //expect: PythonIntrinsicIssue
    __m128 _mm_broadcastss_ps(__m128); //expect: PythonIntrinsicIssue
    __m128 _mm_castpd_ps(__m128d); //expect: PythonIntrinsicIssue
    __m128 _mm_castsi128_ps(__m128i); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpeq_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpeq_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpge_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpge_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpgt_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpgt_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmple_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmple_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmplt_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmplt_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpneq_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpneq_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpnge_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpnge_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpngt_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpngt_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpnle_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpnle_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpnlt_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpnlt_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpord_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpord_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmp_ps(__m128, __m128, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_cmp_ss(__m128, __m128, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpunord_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cmpunord_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_cvtepi32_ps(__m128i); //expect: PythonIntrinsicIssue
    __m128 _mm_cvtpd_ps(__m128d); //expect: PythonIntrinsicIssue
    __m128 _mm_cvtph_ps(__m128i); //expect: PythonIntrinsicIssue
    __m128 _mm_cvt_pi2ps(__m128, __m64); //expect: PythonIntrinsicIssue
    __m128 _mm_cvtsd_ss(__m128, __m128d); //expect: PythonIntrinsicIssue
    __m128 _mm_cvt_si2ss(__m128, int); //expect: PythonIntrinsicIssue
    __m128 _mm_cvtsi64_ss(__m128, __int64); //expect: PythonIntrinsicIssue
    __m128 _mm_cvtsi64x_ss(__m128, __int64); //expect: PythonIntrinsicIssue
    __m128 _mm_div_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_div_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_dp_ps(__m128, __m128, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_fmadd_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_fmadd_ss(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_fmaddsub_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_fmsubadd_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_fmsub_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_fmsub_ss(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_fnmadd_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_fnmadd_ss(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_fnmsub_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_fnmsub_ss(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_frcz_ps(__m128); //expect: PythonIntrinsicIssue
    __m128 _mm_frcz_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_hadd_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_hsub_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_i32gather_ps(float const *, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_i64gather_ps(float const *, __m128i, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_insert_ps(__m128, __m128, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_loadh_pi(__m128, __m64*); //expect: PythonIntrinsicIssue
    __m128 _mm_loadl_pi(__m128, __m64*); //expect: PythonIntrinsicIssue
    __m128 _mm_load_ps1(float*); //expect: PythonIntrinsicIssue
    __m128 _mm_load_ps(float*); //expect: PythonIntrinsicIssue
    __m128 _mm_loadr_ps(float*); //expect: PythonIntrinsicIssue
    __m128 _mm_load_ss(float*); //expect: PythonIntrinsicIssue
    __m128 _mm_loadu_ps(float*); //expect: PythonIntrinsicIssue
    __m128 _mm_macc_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_macc_ss(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_maddsub_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_mask_i32gather_ps(__m128, float const *, __m128i, __m128, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_mask_i64gather_ps(__m128, float const *, __m128i, __m128, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_maskload_ps(float const *, __m128i); //expect: PythonIntrinsicIssue
    __m128 _mm_max_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_max_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_min_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_min_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_movehdup_ps(__m128); //expect: PythonIntrinsicIssue
    __m128 _mm_movehl_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_moveldup_ps(__m128); //expect: PythonIntrinsicIssue
    __m128 _mm_movelh_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_move_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_msubadd_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_msub_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_msub_ss(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_mul_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_mul_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_nmacc_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_nmacc_ss(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_nmsub_ps(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_nmsub_ss(__m128, __m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_or_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_permute2_ps(__m128, __m128, __m128i, int); //expect: PythonIntrinsicIssue
    __m128 _mm_permute_ps(__m128, int); //expect: PythonIntrinsicIssue
    __m128 _mm_permutevar_ps(__m128, __m128i); //expect: PythonIntrinsicIssue
    __m128 _mm_rcp_ps(__m128); //expect: PythonIntrinsicIssue
    __m128 _mm_rcp_ss(__m128); //expect: PythonIntrinsicIssue
    __m128 _mm_round_ps(__m128, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_round_ss(__m128, __m128, const int); //expect: PythonIntrinsicIssue
    __m128 _mm_rsqrt_ps(__m128); //expect: PythonIntrinsicIssue
    __m128 _mm_rsqrt_ss(__m128); //expect: PythonIntrinsicIssue
    __m128 _mm_set_ps1(float); //expect: PythonIntrinsicIssue
    __m128 _mm_set_ps(float, float, float, float); //expect: PythonIntrinsicIssue
    __m128 _mm_setr_ps(float, float, float, float); //expect: PythonIntrinsicIssue
    __m128 _mm_set_ss(float); //expect: PythonIntrinsicIssue
    __m128 _mm_setzero_ps(void); //expect: PythonIntrinsicIssue
    __m128 _mm_shuffle_ps(__m128, __m128, unsigned int); //expect: PythonIntrinsicIssue
    __m128 _mm_sqrt_ps(__m128); //expect: PythonIntrinsicIssue
    __m128 _mm_sqrt_ss(__m128); //expect: PythonIntrinsicIssue
    __m128 _mm_sub_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_sub_ss(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_unpackhi_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_unpacklo_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m128 _mm_xor_ps(__m128, __m128); //expect: PythonIntrinsicIssue
    __m256d _mm256_add_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_addsub_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_andnot_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_and_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_blend_pd(__m256d, __m256d, const int); //expect: PythonIntrinsicIssue
    __m256d _mm256_blendv_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_broadcast_pd(__m128d const*); //expect: PythonIntrinsicIssue
    __m256d _mm256_broadcast_sd(double const*); //expect: PythonIntrinsicIssue
    __m256d _mm256_broadcastsd_pd(__m128d); //expect: PythonIntrinsicIssue
    __m256d _mm256_castpd128_pd256(__m128d); //expect: PythonIntrinsicIssue
    __m256d _mm256_castps_pd(__m256); //expect: PythonIntrinsicIssue
    __m256d _mm256_castsi256_pd(__m256i); //expect: PythonIntrinsicIssue
    __m256d _mm256_cmp_pd(__m256d, __m256d, const int); //expect: PythonIntrinsicIssue
    __m256d _mm256_cvtepi32_pd(__m128i); //expect: PythonIntrinsicIssue
    __m256d _mm256_cvtps_pd(__m128); //expect: PythonIntrinsicIssue
    __m256d _mm256_div_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_fmadd_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_fmaddsub_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_fmsubadd_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_fmsub_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_fnmadd_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_fnmsub_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_frcz_pd(__m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_hadd_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_hsub_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_i32gather_pd(double const *, __m128i, const int); //expect: PythonIntrinsicIssue
    __m256d _mm256_i64gather_pd(double const *, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256d _mm256_insertf128_pd(__m256d, __m128d, int); //expect: PythonIntrinsicIssue
    __m256d _mm256_load_pd(double const *); //expect: PythonIntrinsicIssue
    __m256d _mm256_loadu_pd(double const *); //expect: PythonIntrinsicIssue
    __m256d _mm256_macc_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_maddsub_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_mask_i32gather_pd(__m256d, double const *, __m128i, __m256d, const int); //expect: PythonIntrinsicIssue
    __m256d _mm256_mask_i64gather_pd(__m256d, double const *, __m256i, __m256d, const int); //expect: PythonIntrinsicIssue
    __m256d _mm256_maskload_pd(double const *, __m256i); //expect: PythonIntrinsicIssue
    __m256d _mm256_max_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_min_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_movedup_pd(__m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_msubadd_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_msub_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_mul_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_nmacc_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_nmsub_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_or_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_permute2f128_pd(__m256d, __m256d, int); //expect: PythonIntrinsicIssue
    __m256d _mm256_permute2_pd(__m256d, __m256d, __m256i, int); //expect: PythonIntrinsicIssue
    __m256d _mm256_permute4x64_pd(__m256d, const int); //expect: PythonIntrinsicIssue
    __m256d _mm256_permute_pd(__m256d, int); //expect: PythonIntrinsicIssue
    __m256d _mm256_permutevar_pd(__m256d, __m256i); //expect: PythonIntrinsicIssue
    __m256d _mm256_round_pd(__m256d, int); //expect: PythonIntrinsicIssue
    __m256d _mm256_set1_pd(double); //expect: PythonIntrinsicIssue
    __m256d _mm256_set_pd(double, double, double, double); //expect: PythonIntrinsicIssue
    __m256d _mm256_setr_pd(double, double, double, double); //expect: PythonIntrinsicIssue
    __m256d _mm256_setzero_pd(void); //expect: PythonIntrinsicIssue
    __m256d _mm256_shuffle_pd(__m256d, __m256d, const int); //expect: PythonIntrinsicIssue
    __m256d _mm256_sqrt_pd(__m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_sub_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_unpackhi_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_unpacklo_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm256_xor_pd(__m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm_macc_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm_maddsub_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm_msubadd_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm_msub_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm_nmacc_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256d _mm_nmsub_pd(__m256d, __m256d, __m256d); //expect: PythonIntrinsicIssue
    __m256i _mm256_abs_epi16(__m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_abs_epi32(__m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_abs_epi8(__m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_add_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_add_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_add_epi64(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_add_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_adds_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_adds_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_adds_epu16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_adds_epu8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_alignr_epi8(__m256i, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_andnot_si256(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_and_si256(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_avg_epu16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_avg_epu8(__m256i , __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_avg_epu8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_blend_epi16(__m256i, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_blend_epi32(__m256i, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_blendv_epi8(__m256i, __m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_broadcastb_epi8(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_broadcastd_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_broadcastq_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_broadcastsi128_si256(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_broadcastw_epi16(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_castpd_si256(__m256d); //expect: PythonIntrinsicIssue
    __m256i _mm256_castps_si256(__m256); //expect: PythonIntrinsicIssue
    __m256i _mm256_castsi128_si256(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cmov_si256(__m256i, __m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cmpeq_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cmpeq_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cmpeq_epi64(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cmpeq_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cmpgt_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cmpgt_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cmpgt_epi64(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cmpgt_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepi16_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepi16_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepi32_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepi8_epi16(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepi8_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepi8_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepu16_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepu16_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepu32_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepu8_epi16(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepu8_epi32(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtepu8_epi64(__m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvtps_epi32(__m256); //expect: PythonIntrinsicIssue
    __m256i _mm256_cvttps_epi32(__m256); //expect: PythonIntrinsicIssue
    __m256i _mm256_hadd_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_hadd_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_hadds_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_hsub_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_hsub_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_hsubs_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_i32gather_epi32(int const *, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_i32gather_epi64(__int64 const *, __m128i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_i64gather_epi32(int const *, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_i64gather_epi64(__int64 const *, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_insertf128_si256(__m256i, __m128i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_inserti128_si256(__m256i, __m128i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_lddqu_si256(__m256i*); //expect: PythonIntrinsicIssue
    __m256i _mm256_load_si256(__m256i*); //expect: PythonIntrinsicIssue
    __m256i _mm256_loadu_si256(__m256i*); //expect: PythonIntrinsicIssue
    __m256i _mm256_madd_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_maddubs_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_mask_i32gather_epi32(__m256i, int const *, __m256i, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_mask_i32gather_epi64(__m256i, __int64 const *, __m128i, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_mask_i64gather_epi64(__m256i, __int64 const *, __m256i, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_maskload_epi32(int const *, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_maskload_epi64(__int64 const *, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_max_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_max_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_max_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_max_epu16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_max_epu32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_max_epu8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_min_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_min_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_min_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_min_epu16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_min_epu32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_min_epu8(__m256i , __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_mpsadbw_epu8(__m256i, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_mul_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_mul_epu32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_mulhi_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_mulhi_epu16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_mulhrs_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_mullo_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_mullo_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_or_si256(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_packs_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_packs_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_packus_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_packus_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_permute2f128_si256(__m256i, __m256i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_permute2x128_si256(__m256i, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_permute4x64_epi64(__m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_permutevar8x32_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sad_epu8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_set1_epi16(short); //expect: PythonIntrinsicIssue
    __m256i _mm256_set1_epi32(int); //expect: PythonIntrinsicIssue
    __m256i _mm256_set1_epi64x(long long); //expect: PythonIntrinsicIssue
    __m256i _mm256_set1_epi8(char); //expect: PythonIntrinsicIssue
    __m256i _mm256_set_epi16(short); //expect: PythonIntrinsicIssue
    __m256i _mm256_set_epi32(int, int, int, int, int, int, int, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_set_epi64x(long long, long long, long long, long long); //expect: PythonIntrinsicIssue
    __m256i _mm256_set_epi8(char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char, char); //expect: PythonIntrinsicIssue
    __m256i _mm256_setr_epi16(short); //expect: PythonIntrinsicIssue
    __m256i _mm256_setr_epi32(int, int, int, int, int, int, int, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_setr_epi64x(long long, long long, long long, long long); //expect: PythonIntrinsicIssue
    __m256i _mm256_setr_epi8(char); //expect: PythonIntrinsicIssue
    __m256i _mm256_setzero_si256(void); //expect: PythonIntrinsicIssue
    __m256i _mm256_shuffle_epi32(__m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_shuffle_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_shufflehi_epi16(__m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_shufflelo_epi16(__m256i, const int); //expect: PythonIntrinsicIssue
    __m256i _mm256_sign_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sign_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sign_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sll_epi16(__m256i, __m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sll_epi32(__m256i, __m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sll_epi64(__m256i, __m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_slli_epi16(__m256i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_slli_epi32(__m256i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_slli_epi64(__m256i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_slli_si256(__m256i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_sllv_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sllv_epi64(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sra_epi16(__m256i, __m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sra_epi32(__m256i, __m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_srai_epi16(__m256i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_srai_epi32(__m256i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_srav_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_srl_epi16(__m256i, __m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_srl_epi32(__m256i, __m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_srl_epi64(__m256i, __m128i); //expect: PythonIntrinsicIssue
    __m256i _mm256_srli_epi16(__m256i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_srli_epi32(__m256i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_srli_epi64(__m256i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_srli_si256(__m256i, int); //expect: PythonIntrinsicIssue
    __m256i _mm256_srlv_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_srlv_epi64(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_stream_load_si256(__m256i const*); //expect: PythonIntrinsicIssue
    __m256i _mm256_sub_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sub_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sub_epi64(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_sub_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_subs_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_subs_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_subs_epu16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_subs_epu8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_unpackhi_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_unpackhi_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_unpackhi_epi64(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_unpackhi_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_unpacklo_epi16(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_unpacklo_epi32(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_unpacklo_epi64(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_unpacklo_epi8(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256i _mm256_xor_si256(__m256i, __m256i); //expect: PythonIntrinsicIssue
    __m256 _mm256_add_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_addsub_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_andnot_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_and_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_blend_ps(__m256, __m256, const int); //expect: PythonIntrinsicIssue
    __m256 _mm256_blendv_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_broadcast_ps(__m128 const*); //expect: PythonIntrinsicIssue
    __m256 _mm256_broadcast_ss(float const*); //expect: PythonIntrinsicIssue
    __m256 _mm256_broadcastss_ps(__m128); //expect: PythonIntrinsicIssue
    __m256 _mm256_castpd_ps(__m256d); //expect: PythonIntrinsicIssue
    __m256 _mm256_castps128_ps256(__m128); //expect: PythonIntrinsicIssue
    __m256 _mm256_castsi256_ps(__m256i); //expect: PythonIntrinsicIssue
    __m256 _mm256_cmp_ps(__m256, __m256, const int); //expect: PythonIntrinsicIssue
    __m256 _mm256_cvtepi32_ps(__m256i); //expect: PythonIntrinsicIssue
    __m256 _mm256_cvtph_ps(__m128i); //expect: PythonIntrinsicIssue
    __m256 _mm256_div_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_dp_ps(__m256, __m256, const int); //expect: PythonIntrinsicIssue
    __m256 _mm256_fmadd_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_fmaddsub_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_fmsubadd_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_fmsub_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_fnmadd_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_fnmsub_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_frcz_ps(__m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_hadd_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_hsub_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_i32gather_ps(float const *, __m256i, const int); //expect: PythonIntrinsicIssue
    __m256 _mm256_insertf128_ps(__m256, __m128, int); //expect: PythonIntrinsicIssue
    __m256 _mm256_load_ps(float const*); //expect: PythonIntrinsicIssue
    __m256 _mm256_loadu_ps(float const*); //expect: PythonIntrinsicIssue
    __m256 _mm256_macc_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_maddsub_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_mask_i32gather_ps(__m256, float const *, __m256i, __m256, const int); //expect: PythonIntrinsicIssue
    __m256 _mm256_maskload_ps(float const *, __m256i); //expect: PythonIntrinsicIssue
    __m256 _mm256_max_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_min_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_movehdup_ps(__m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_moveldup_ps(__m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_msubadd_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_msub_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_mul_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_nmacc_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_nmsub_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_or_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_permute2f128_ps(__m256, __m256, int); //expect: PythonIntrinsicIssue
    __m256 _mm256_permute2_ps(__m256, __m256, __m256i, int); //expect: PythonIntrinsicIssue
    __m256 _mm256_permute_ps(__m256, int); //expect: PythonIntrinsicIssue
    __m256 _mm256_permutevar8x32_ps(__m256, __m256i); //expect: PythonIntrinsicIssue
    __m256 _mm256_permutevar_ps(__m256, __m256i); //expect: PythonIntrinsicIssue
    __m256 _mm256_rcp_ps(__m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_round_ps(__m256, int); //expect: PythonIntrinsicIssue
    __m256 _mm256_rsqrt_ps(__m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_set1_ps(float); //expect: PythonIntrinsicIssue
    __m256 _mm256_set_ps(float, float, float, float, float, float, float, float); //expect: PythonIntrinsicIssue
    __m256 _mm256_setr_ps(float, float, float, float, float, float, float, float); //expect: PythonIntrinsicIssue
    __m256 _mm256_setzero_ps(void); //expect: PythonIntrinsicIssue
    __m256 _mm256_shuffle_ps(__m256, __m256, const int); //expect: PythonIntrinsicIssue
    __m256 _mm256_sqrt_ps(__m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_sub_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_unpackhi_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_unpacklo_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm256_xor_ps(__m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm_macc_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm_maddsub_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm_msubadd_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm_msub_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm_nmacc_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m256 _mm_nmsub_ps(__m256, __m256, __m256); //expect: PythonIntrinsicIssue
    __m64 _m_from_float(float); //expect: PythonIntrinsicIssue
    __m64 _m_from_int(int); //expect: PythonIntrinsicIssue
    __m64 _mm_abs_pi16(__m64); //expect: PythonIntrinsicIssue
    __m64 _mm_abs_pi32(__m64); //expect: PythonIntrinsicIssue
    __m64 _mm_abs_pi8(__m64); //expect: PythonIntrinsicIssue
    __m64 _mm_add_si64(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_alignr_pi8(__m64, __m64, int); //expect: PythonIntrinsicIssue
    __m64 _mm_cvtpd_pi32(__m128d); //expect: PythonIntrinsicIssue
    __m64 _mm_cvt_ps2pi(__m128); //expect: PythonIntrinsicIssue
    __m64 _mm_cvttpd_pi32(__m128d); //expect: PythonIntrinsicIssue
    __m64 _mm_cvtt_ps2pi(__m128); //expect: PythonIntrinsicIssue
    __m64 _mm_hadd_pi16(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_hadd_pi32(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_hadds_pi16(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_hsub_pi16(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_hsub_pi32(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_hsubs_pi16(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_maddubs_pi16(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_movepi64_pi64(__m128i); //expect: PythonIntrinsicIssue
    __m64 _mm_mulhrs_pi16(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_mul_su32(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_set1_pi16(short); //expect: PythonIntrinsicIssue
    __m64 _mm_set1_pi32(int); //expect: PythonIntrinsicIssue
    __m64 _mm_set1_pi8(char); //expect: PythonIntrinsicIssue
    __m64 _mm_set_pi16(short, short, short, short); //expect: PythonIntrinsicIssue
    __m64 _mm_set_pi32(int, int); //expect: PythonIntrinsicIssue
    __m64 _mm_set_pi8(char, char, char, char, char, char, char, char); //expect: PythonIntrinsicIssue
    __m64 _mm_setr_pi16(short, short, short, short); //expect: PythonIntrinsicIssue
    __m64 _mm_setr_pi32(int, int); //expect: PythonIntrinsicIssue
    __m64 _mm_setr_pi8(char, char, char, char, char, char, char, char); //expect: PythonIntrinsicIssue
    __m64 _mm_setzero_si64(void); //expect: PythonIntrinsicIssue
    __m64 _mm_shuffle_pi8(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_sign_pi16(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_sign_pi32(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_sign_pi8(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _mm_sub_si64(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_packssdw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_packsswb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_packuswb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_paddb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_paddd(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_paddsb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_paddsw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_paddusb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_paddusw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_paddw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pand(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pandn(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pavgb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pavgusb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pavgw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pcmpeqb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pcmpeqd(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pcmpeqw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pcmpgtb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pcmpgtd(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pcmpgtw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pf2id(__m64); //expect: PythonIntrinsicIssue
    __m64 _m_pf2iw(__m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfacc(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfadd(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfcmpeq(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfcmpge(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfcmpgt(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfmax(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfmin(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfmul(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfnacc(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfpnacc(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfrcpit1(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfrcpit2(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfrcp(__m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfrsqit1(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfrsqrt(__m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfsub(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pfsubr(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pi2fd(__m64); //expect: PythonIntrinsicIssue
    __m64 _m_pi2fw(__m64); //expect: PythonIntrinsicIssue
    __m64 _m_pinsrw(__m64, int, int); //expect: PythonIntrinsicIssue
    __m64 _m_pmaddwd(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pmaxsw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pmaxub(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pminsw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pminub(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pmulhrw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pmulhuw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pmulhw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pmullw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_por(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psadbw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pshufw(__m64, int); //expect: PythonIntrinsicIssue
    __m64 _m_pslldi(__m64, int); //expect: PythonIntrinsicIssue
    __m64 _m_pslld(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psllqi(__m64, int); //expect: PythonIntrinsicIssue
    __m64 _m_psllq(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psllwi(__m64, int); //expect: PythonIntrinsicIssue
    __m64 _m_psllw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psradi(__m64, int); //expect: PythonIntrinsicIssue
    __m64 _m_psrad(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psrawi(__m64, int); //expect: PythonIntrinsicIssue
    __m64 _m_psraw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psrldi(__m64, int); //expect: PythonIntrinsicIssue
    __m64 _m_psrld(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psrlqi(__m64, int); //expect: PythonIntrinsicIssue
    __m64 _m_psrlq(__m64, __m64); //expect: PythonIntrinsicIssue
    m64 _m_psrlwi(__m64, int); //expect: PythonIntrinsicIssue
    __m64 _m_psrlw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psubb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psubd(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psubsb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psubsw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psubusb(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psubusw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_psubw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pswapd(__m64); //expect: PythonIntrinsicIssue
    __m64 _m_punpckhbw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_punpckhdq(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_punpckhwd(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_punpcklbw(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_punpckldq(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_punpcklwd(__m64, __m64); //expect: PythonIntrinsicIssue
    __m64 _m_pxor(__m64, __m64); //expect: PythonIntrinsicIssue
    short _InterlockedAnd16_np(short *, short); //expect: PythonIntrinsicIssue
    short _InterlockedAnd16(short volatile *, short);
    short _InterlockedCompareExchange16_np(short volatile *, short, short); //expect: PythonIntrinsicIssue
    short _InterlockedCompareExchange16(short volatile *, short, short);
    short _InterlockedDecrement16(short volatile *);
    short _InterlockedExchange16(short volatile *, short);
    short _InterlockedExchangeAdd16(short volatile *, short);
    short _InterlockedIncrement16(short volatile *);
    short _InterlockedOr16_np(short *, short); //expect: PythonIntrinsicIssue
    short _InterlockedOr16(short volatile *, short);
    short _InterlockedXor16_np(short *, short); //expect: PythonIntrinsicIssue
    short _InterlockedXor16(short volatile *, short);
    short _loadbe_i16(void const *); //expect: PythonIntrinsicIssue
    unsigned char _addcarry_u16(unsigned char, unsigned short, unsigned short, unsigned short *); //expect: PythonIntrinsicIssue
    unsigned char _addcarry_u32(unsigned char, unsigned int, unsigned int, unsigned int *); //expect: PythonIntrinsicIssue
    unsigned char _addcarry_u64(unsigned char, unsigned __int64, unsigned __int64, unsigned __int64 *); //expect: PythonIntrinsicIssue
    unsigned char _addcarry_u8(unsigned char, unsigned char, unsigned char, unsigned char *); //expect: PythonIntrinsicIssue
    unsigned char _addcarryx_u32(unsigned char, unsigned int, unsigned int, unsigned int *); //expect: PythonIntrinsicIssue
    unsigned char _addcarryx_u64(unsigned char, unsigned __int64, unsigned __int64, unsigned __int64 *); //expect: PythonIntrinsicIssue
    unsigned char _BitScanForward(unsigned long *, unsigned long);
    unsigned char _BitScanForward64(unsigned long *, unsigned __int64);
    unsigned char _BitScanReverse(unsigned long *, unsigned long);
    unsigned char _BitScanReverse64(unsigned long *, unsigned __int64);
    unsigned char _bittest(long const *, long);
    unsigned char _bittest64(__int64 const *, __int64);
    unsigned char _bittestandcomplement(long *, long);
    unsigned char _bittestandcomplement64(__int64 *, __int64); //expect: PythonIntrinsicIssue
    unsigned char _bittestandreset(long *, long);
    unsigned char _bittestandreset64(__int64 *, __int64); //expect: PythonIntrinsicIssue
    unsigned char _bittestandset64(__int64 *, __int64); //expect: PythonIntrinsicIssue
    unsigned char _bittestandset(long *, long);
    unsigned char __builtin_ia32_lwpins16(unsigned short, unsigned int, unsigned short); //expect: PythonIntrinsicIssue
    unsigned char __builtin_ia32_lwpins32(unsigned int, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned char __builtin_ia32_lwpins64(unsigned __int64, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned char __inbyte(unsigned short); //expect: PythonIntrinsicIssue
    unsigned char _interlockedbittestandreset64_HLEAcquire(__int64 *, __int64); //expect: PythonIntrinsicIssue
    unsigned char _interlockedbittestandreset64_HLERelease(__int64 *, __int64); //expect: PythonIntrinsicIssue
    unsigned char _interlockedbittestandreset64(__int64 *, __int64); //expect: PythonIntrinsicIssue
    unsigned char _interlockedbittestandreset_HLEAcquire(long *, long); //expect: PythonIntrinsicIssue
    unsigned char _interlockedbittestandreset_HLERelease(long *, long); //expect: PythonIntrinsicIssue
    unsigned char _interlockedbittestandreset(long *, long);
    unsigned char _interlockedbittestandset64_HLEAcquire(__int64 *, __int64); //expect: PythonIntrinsicIssue
    unsigned char _interlockedbittestandset64_HLERelease(__int64 *, __int64); //expect: PythonIntrinsicIssue
    unsigned char _interlockedbittestandset64(__int64 *, __int64); //expect: PythonIntrinsicIssue
    unsigned char _interlockedbittestandset_HLEAcquire(long *, long); //expect: PythonIntrinsicIssue
    unsigned char _interlockedbittestandset_HLERelease(long *, long); //expect: PythonIntrinsicIssue
    unsigned char _interlockedbittestandset(long *, long);
    unsigned char _InterlockedCompareExchange128(__int64 volatile *, __int64, __int64, __int64 *); //expect: PythonIntrinsicIssue
    unsigned char __lwpins32(unsigned int, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned char __lwpins64(unsigned __int64, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned char __readfsbyte(unsigned long); //expect: PythonIntrinsicIssue
    unsigned char __readgsbyte(unsigned long); //expect: PythonIntrinsicIssue
    unsigned char _rotl8(unsigned char, unsigned char);
    unsigned char _rotr8(unsigned char, unsigned char);
    unsigned char _subborrow_u16(unsigned char, unsigned short, unsigned short, unsigned short *); //expect: PythonIntrinsicIssue
    unsigned char _subborrow_u32(unsigned char, unsigned int, unsigned int, unsigned int *); //expect: PythonIntrinsicIssue
    unsigned char _subborrow_u64(unsigned char, unsigned __int64, unsigned __int64, unsigned __int64 *); //expect: PythonIntrinsicIssue
    unsigned char _subborrow_u8(unsigned char, unsigned char, unsigned char, unsigned char *); //expect: PythonIntrinsicIssue
    unsigned char __vmx_on(unsigned __int64 *); //expect: PythonIntrinsicIssue
    unsigned char __vmx_vmclear(unsigned __int64 *); //expect: PythonIntrinsicIssue
    unsigned char __vmx_vmlaunch(void); //expect: PythonIntrinsicIssue
    unsigned char __vmx_vmptrld(unsigned __int64 *); //expect: PythonIntrinsicIssue
    unsigned char __vmx_vmread(size_t, size_t *); //expect: PythonIntrinsicIssue
    unsigned char __vmx_vmresume(void); //expect: PythonIntrinsicIssue
    unsigned char __vmx_vmwrite(size_t, size_t); //expect: PythonIntrinsicIssue
    unsigned __int64 _andn_u64(unsigned __int64, unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _bextri_u64(unsigned __int64, unsigned int); //expect: PythonIntrinsicIssue
    unsigned __int64 _bextr_u64(unsigned __int64, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned __int64 _blcfill_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _blcic_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _blci_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _blcmsk_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _blcs_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _blsfill_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _blsic_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _blsi_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _blsmsk_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _blsr_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _bzhi_u64(unsigned __int64, unsigned int); //expect: PythonIntrinsicIssue
    unsigned __int64 _load_be_u64(void const *); //expect: PythonIntrinsicIssue
    unsigned __int64 __lzcnt64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _lzcnt_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _mm_crc32_u64(unsigned __int64, unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _mulx_u64(unsigned __int64, unsigned __int64, unsigned __int64*); //expect: PythonIntrinsicIssue
    unsigned __int64 __emulu(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned __int64 __ll_lshift(unsigned __int64, int); //expect: PythonIntrinsicIssue
    unsigned __int64 __ull_rshift(unsigned __int64, int); //expect: PythonIntrinsicIssue
    unsigned __int64 _pdep_u64(unsigned __int64, unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _pext_u64(unsigned __int64, unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 __popcnt64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 __rdtscp(unsigned int *); //expect: PythonIntrinsicIssue
    unsigned __int64 __rdtsc(void); //expect: PythonIntrinsicIssue
    unsigned __int64 __readcr0(void); //expect: PythonIntrinsicIssue
    unsigned __int64 __readcr2(void); //expect: PythonIntrinsicIssue
    unsigned __int64 __readcr3(void); //expect: PythonIntrinsicIssue
    unsigned __int64 __readcr4(void); //expect: PythonIntrinsicIssue
    unsigned __int64 __readcr8(void); //expect: PythonIntrinsicIssue
    unsigned __int64 __readdr(unsigned); //expect: PythonIntrinsicIssue
    unsigned __int64 __readeflags(void); //expect: PythonIntrinsicIssue
    unsigned __int64 _readfsbase_u64(void); //expect: PythonIntrinsicIssue
    unsigned __int64 _readgsbase_u64(void); //expect: PythonIntrinsicIssue
    unsigned __int64 __readgsqword(unsigned long); //expect: PythonIntrinsicIssue
    unsigned __int64 __readmsr(unsigned long); //expect: PythonIntrinsicIssue
    unsigned __int64 __readpmc(unsigned long); //expect: PythonIntrinsicIssue
    unsigned __int64 _rorx_u64(unsigned __int64, const unsigned int); //expect: PythonIntrinsicIssue
    unsigned __int64 __shiftleft128(unsigned __int64, unsigned __int64, unsigned char); //expect: PythonIntrinsicIssue
    unsigned __int64 __shiftright128(unsigned __int64, unsigned __int64, unsigned char); //expect: PythonIntrinsicIssue
    unsigned __int64 _shlx_u64(unsigned __int64, unsigned int); //expect: PythonIntrinsicIssue
    unsigned __int64 _shrx_u64(unsigned __int64, unsigned int); //expect: PythonIntrinsicIssue
    unsigned __int64 _t1mskc_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _tzcnt_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _tzmsk_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _udiv128(unsigned __int64, unsigned __int64, unsigned __int64, unsigned __int64 *); //expect: PythonIntrinsicIssue
    unsigned __int64 _umul128(unsigned __int64, unsigned __int64, unsigned __int64 *); //expect: PythonIntrinsicIssue
    unsigned __int64 __umulh(unsigned __int64, unsigned __int64); //expect: PythonIntrinsicIssue
    unsigned __int64 _xgetbv(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _andn_u32(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _bextri_u32(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _bextr_u32(unsigned int, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _blcfill_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _blcic_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _blci_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _blcmsk_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _blcs_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _blsfill_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _blsic_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _blsi_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _blsmsk_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _blsr_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int __builtin_ia32_bextri_u32(unsigned int, const unsigned int); //expect: PythonIntrinsicIssue
    unsigned int __builtin_ia32_bextr_u32(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned int __builtin_ia32_crc32hi(unsigned int, unsigned short); //expect: PythonIntrinsicIssue
    unsigned int __builtin_ia32_crc32qi(unsigned int, unsigned char); //expect: PythonIntrinsicIssue
    unsigned int __builtin_ia32_crc32si(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned int __builtin_ia32_lzcnt_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int __builtin_ia32_rdfsbase32(void); //expect: PythonIntrinsicIssue
    unsigned int __builtin_ia32_rdgsbase32(void); //expect: PythonIntrinsicIssue
    unsigned int __builtin_ia32_rdrand16_step(unsigned short *); //expect: PythonIntrinsicIssue
    unsigned int __builtin_ia32_rdrand32_step(unsigned int *); //expect: PythonIntrinsicIssue
    unsigned int __builtin_ia32_rdrand64_step(unsigned long long *); //expect: PythonIntrinsicIssue
    unsigned int _bzhi_u32(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned int __getcallerseflags(); //expect: PythonIntrinsicIssue
    unsigned int _load_be_u32(void const *); //expect: PythonIntrinsicIssue
    unsigned int _lzcnt_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int __lzcnt(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _mm_crc32_u16(unsigned int, unsigned short); //expect: PythonIntrinsicIssue
    unsigned int _mm_crc32_u32(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _mm_crc32_u8(unsigned int, unsigned char); //expect: PythonIntrinsicIssue
    unsigned int _mm_getcsr(void); //expect: PythonIntrinsicIssue
    unsigned int _mulx_u32(unsigned int, unsigned int, unsigned int *); //expect: PythonIntrinsicIssue
    unsigned int _pdep_u32(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _pext_u32(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned int __popcnt(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _readfsbase_u32(void); //expect: PythonIntrinsicIssue
    unsigned int _readgsbase_u32(void); //expect: PythonIntrinsicIssue
    unsigned int _rorx_u32(unsigned int, const unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _shlx_u32(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _shrx_u32(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _t1mskc_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _tzcnt_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _tzmsk_u32(unsigned int); //expect: PythonIntrinsicIssue
    unsigned int _udiv64(unsigned __int64, unsigned int, unsigned int *); //expect: PythonIntrinsicIssue
    unsigned long __indword(unsigned short); //expect: PythonIntrinsicIssue
    unsigned long long __builtin_ia32_bextri_u64(unsigned long long, const unsigned long long); //expect: PythonIntrinsicIssue
    unsigned long long __builtin_ia32_bextr_u64(unsigned long long, unsigned long long); //expect: PythonIntrinsicIssue
    unsigned long long __builtin_ia32_crc32di(unsigned long long, unsigned long long); //expect: PythonIntrinsicIssue
    unsigned long long __builtin_ia32_lzcnt_u64(unsigned long long); //expect: PythonIntrinsicIssue
    unsigned long long __builtin_ia32_rdfsbase64(void); //expect: PythonIntrinsicIssue
    unsigned long long __builtin_ia32_rdgsbase64(void); //expect: PythonIntrinsicIssue
    unsigned long long _bzhi_u64(unsigned long long, unsigned long long); //expect: PythonIntrinsicIssue
    unsigned long long _pdep_u64(unsigned long long, unsigned long long); //expect: PythonIntrinsicIssue
    unsigned long long _pext_u64(unsigned long long, unsigned long long); //expect: PythonIntrinsicIssue
    unsigned long __readcr0(void); //expect: PythonIntrinsicIssue
    unsigned long __readcr2(void); //expect: PythonIntrinsicIssue
    unsigned long __readcr3(void); //expect: PythonIntrinsicIssue
    unsigned long __readcr4(void); //expect: PythonIntrinsicIssue
    unsigned long __readcr8(void); //expect: PythonIntrinsicIssue
    unsigned long __readfsdword(unsigned long); //expect: PythonIntrinsicIssue
    unsigned long __readgsdword(unsigned long); //expect: PythonIntrinsicIssue
    unsigned long __segmentlimit(unsigned long); //expect: PythonIntrinsicIssue
    unsigned __readdr(unsigned); //expect: PythonIntrinsicIssue
    unsigned __readeflags(void); //expect: PythonIntrinsicIssue
    unsigned short __builtin_ia32_lzcnt_16(unsigned short); //expect: PythonIntrinsicIssue
    unsigned short _load_be_u16(void const *); //expect: PythonIntrinsicIssue
    unsigned short __lzcnt16(unsigned short); //expect: PythonIntrinsicIssue
    unsigned short __popcnt16(unsigned short); //expect: PythonIntrinsicIssue
    unsigned short __readfsword(unsigned long); //expect: PythonIntrinsicIssue
    unsigned short __readgsword(unsigned long); //expect: PythonIntrinsicIssue
    unsigned short _rotl16(unsigned short, unsigned char);
    unsigned short _rotr16(unsigned short, unsigned char);
    v16hi __builtin_ia32_pabsw256(v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_packssdw256(v8si, v8si); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_packusdw256(v8si, v8si); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_paddsw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_paddusw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_paddw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pavgw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pblendw256(v16hi, v16hi, int); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pbroadcastw256(v8hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pcmpeqw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pcmpgtw256(16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_phaddsw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_phaddw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_phsubsw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_phsubw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pmaddwd256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pmaxsw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pmaxuw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pminsw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pminuw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pmovsxbw256 (v16qi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pmovzxbw256(v16qi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pmulhrsw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pmulhuw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pmulhw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pmullw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_psadbw256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pshufhw256(v16hi, int); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_pshuflw256(v16hi, int); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_psignw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_psllw256(v16hi, v8hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_psllwi256(16hi, int); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_psraw256(v16hi, v8hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_psrawi256(v16hi, int); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_psrlw256(v16hi, v8hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_psrlwi256(v16hi, int); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_psubsw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_psubusw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_punpckhwd256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_punpcklwd256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16hi __builtin_ia32_vpcmov_v16hi256(v16hi, v16hi, v16hi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_lddqu(char const *); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_loaddqu(const char *); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_mpsadbw128(v16qi, v16qi, const int); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pabsb128(v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_packsswb128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_packuswb128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_paddb128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pavgb128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pblendvb128(v16qi, v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pbroadcastb128(v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pcmpeqb128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pcmpestrm128(v16qi, int, v16qi, int, const int); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pcmpgtb128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pcmpistrm128(v16qi, v16qi, const int); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pmaxsb128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pmaxub128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pminsb128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pminub128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_pshufb128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_psignb128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_psubb128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_punpckhbw128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_punpcklbw128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vec_set_v16qi(v16qi, int, const int); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcmov_v16qi(v16qi, v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomeqb(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomequb(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomfalseb(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomfalseub(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomgeb(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomgeub(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomgtb(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomgtub(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomleb(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomleub(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomltb(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomltub(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomneb(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomneub(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomtrueb(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpcomtrueub(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpperm(v16qi, v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vprotb(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpshab(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v16qi __builtin_ia32_vpshlb(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v1di __builtin_ia32_palignr(v1di, v1di, int); //expect: PythonIntrinsicIssue
    v1di __builtin_ia32_pmuludq(v2si, v2si); //expect: PythonIntrinsicIssue
    v1di __builtin_ia32_psadbw(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v1di __builtin_ia32_psllqi(v1di, int); //expect: PythonIntrinsicIssue
    v1di __builtin_ia32_psllq(v1di, v1di); //expect: PythonIntrinsicIssue
    v1di __builtin_ia32_psrlqi(v1di, int); //expect: PythonIntrinsicIssue
    v1di __builtin_ia32_psrlq(v1di, v1di); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_addpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_addsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_addsubpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_andnpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_andpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_blendpd(v2df, v2df, const int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_blendvpd(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpeqpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpeqsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpgepd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpgtpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmplepd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmplesd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpltpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpltsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpneqpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpneqsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpngepd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpngtpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpnlepd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpnlesd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpnltpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpnltsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpordpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpordsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmppd(v2df, v2df, int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpsd(v2df, v2df, int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpunordpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cmpunordsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cvtdq2pd(v4si); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cvtpi2pd(v2si); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cvtps2pd(v4sf); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cvtsi2sd(v2df, int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cvtsi642sd(v2df, long long); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_cvtss2sd(v2df, v4sf); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_divpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_divsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_dppd(v2df, v2df, const int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_fmaddpd(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_fmaddsd(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_fmaddsubpd(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_fmsubaddpd(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_fmsubpd(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_fmsubsd(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_fnmaddpd(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_fnmaddsd(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_fnmsubpd(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_fnmsubsd(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_gatherdiv2df(v2df, pcdouble, v2di, v2df, int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_gathersiv2df(v2df, pcdouble, v4si, v2df, int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_haddpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_hsubpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_loadddup(double const *); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_loadhpd(v2df, double const *); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_loadlpd(v2df, double const *); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_loadupd(double *); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_maskloadpd(pcv2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_maxpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_maxsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_minpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_minsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_movddup(v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_movsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_mulpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_mulsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_orpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_pd_pd256(v4df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_roundpd(v2df, const int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_roundsd(v2df, v2df, const int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_shufpd(v2df, v2df, int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_sqrtpd(v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_sqrtsd(v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_subpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_subsd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_unpckhpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_unpcklpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_vextractf128_pd256(v4df, int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_vfrczpd(v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_vfrczsd(v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_vpcmov_v2df(v2df, v2df, v2df); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_vpermil2pd(v2df, v2df, v2di, int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_vpermilpd(v2df, int); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_vpermilvarpd(v2df, v2di); //expect: PythonIntrinsicIssue
    v2df __builtin_ia32_xorpd(v2df, v2df); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_aesdec128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_aesdeclast128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_aesenc128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_aesenclast128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_aesimc128(v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_aeskeygenassist128(v2di, const int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_extrqi(v2di, const unsigned int, const unsigned int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_extrq(v2di, v16qi); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_gatherdiv2di(v2di, pcint64, v2di, v2di, int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_gathersiv2di(v2di, pcint64, v4si, v2di, int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_insertqi(v2di, v2di, const unsigned int, const unsigned int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_insertq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_maskloadq(pcv2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_movntdqa(v2di *); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_movq128(v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_paddq128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_paddq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_palignr128(v2di, v2di, int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pand128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pandn128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pbroadcastq128(v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pclmulqdq128(v2di, v2di, const int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pcmpeqq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pcmpgtq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pmovsxbq128(v16qi); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pmovsxdq128(v4si); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pmovsxwq128(v8hi); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pmovzxbq128(v16qi); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pmovzxdq128(v4si); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pmovzxwq128(v8hi); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pmuldq128(v4si, v4si); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pmuludq128(v4si, v4si); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_por128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_psadbw128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pslldqi128(v2di, int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_psllq128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_psllqi128(v2di, int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_psllv2di(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_psrldqi128(v2di, int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_psrlq128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_psrlqi128(v2di, int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_psrlv2di(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_psubq128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_psubq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_punpckhqdq128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_punpcklqdq128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_pxor128(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vec_set_v2di(v2di, long long, const int); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcmov(v2di, v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcmov_v2di(v2di, v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomeqq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomequq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomfalseq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomfalseuq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomgeq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomgeuq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomgtq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomgtuq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomleq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomleuq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomltq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomltuq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomneq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomneuq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomtrueq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpcomtrueuq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vphaddbq(v16qi); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vphadddq(v4si); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vphaddubq(v16qi); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vphaddudq(v4si); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vphadduwq(v8hi); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vphaddwq(v8hi); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vphsubdq(v4si); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpmacsdqh(v4si, v4si, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpmacsdql(v4si, v4si, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpmacssdqh(v4si, v4si, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpmacssdql(v4si, v4si, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vprotq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpshaq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2di __builtin_ia32_vpshlq(v2di, v2di); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfacc(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfadd(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfmax(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfmin(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfmul(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfnacc(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfpnacc(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfrcpit1(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfrcpit2(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfrcp(v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfrsqrtit1 (v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfrsqrt(v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfsubr(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pfsub(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pi2fd(v2si); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pi2fw(v2si); //expect: PythonIntrinsicIssue
    v2sf __builtin_ia32_pswapdsf(v2sf); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_cvtpd2pi(v2df); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_cvtps2pi(v4sf); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_cvttpd2pi(v2df); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_cvttps2pi(v4sf); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_pabsd(v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_paddd(v2si, v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_pcmpeqd(v2si, v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_pcmpgtd(v2si, v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_pf2id(v2sf); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_pf2iw(v2sf); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_pfcmpeq(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_pfcmpge(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_pfcmpgt(v2sf, v2sf); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_phaddd(v2si, v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_phsubd(v2si, v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_psignd(v2si, v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_pslldi(v2si, int); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_pslld(v2si, v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_psradi(v2si, int); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_psrad(v2si, v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_psrldi(v2si, int); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_psrld(v2si, v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_psubd(v2si, v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_pswapdsi(v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_punpckhdq(v2si, v2si); //expect: PythonIntrinsicIssue
    v2si __builtin_ia32_punpckldq(v2si, v2si); //expect: PythonIntrinsicIssue
    v32hi __builtin_ia32_psubw256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_lddqu256(pcchar); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_loaddqu256(pcchar); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_mpsadbw256(v32qi, v32qi, int); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pabsb256(v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_packsswb256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_packuswb256(v16hi, v16hi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_paddb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_paddsb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_paddusb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pavgb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pblendvb256(v32qi, v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pbroadcastb256(v16qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pcmpeqb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pcmpgtb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pmaddubsw256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pmaxsb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pmaxub256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pminsb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pminub256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_pshufb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_psignb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_psubb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_psubsb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_psubusb256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_punpckhbw256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_punpcklbw256(v32qi, v32qi); //expect: PythonIntrinsicIssue
    v32qi __builtin_ia32_vpcmov_v32qi256(v32qi, v32qi, v32qi); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_addpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_addsubpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_andnpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_andpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_blendpd256(v4df, v4df, int); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_blendvpd256(v4df, v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_cmppd256(v4df, v4df, int); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_cvtdq2pd256(v4si); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_cvtps2pd256(v4sf); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_divpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_fmaddpd256(v4df, v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_fmaddsubpd256(v4df, v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_fmsubaddpd256(v4df, v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_fmsubpd256(v4df, v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_fnmaddpd256(v4df, v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_fnmsubpd256(v4df, v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_gatherdiv4df(v4df, pcdouble, v4di, v4df, int); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_gathersiv4df(v4df, pcdouble, v4si, v4df, int); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_haddpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_hsubpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_loadupd256(pcdouble); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_maskloadpd256(pcv4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_maxpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_minpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_movddup256(v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_mulpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_orpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_pd256_pd(v2df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_permdf256(v4df, int); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_roundpd256(v4df, int); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_shufpd256(v4df, v4df, int); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_sqrtpd256(v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_subpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_unpckhpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_unpcklpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_vbroadcastf128_pd256(pcv2df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_vbroadcastsd256(pcdouble); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_vbroadcastsd_pd256(v2df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_vfrczpd256(v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_vinsertf128_pd256(v4df, v2df, int); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_vpcmov_v4df256(v4df, v4df, v4df); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_vperm2f128_pd256(v4df, v4df, int); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_vpermil2pd256(v4df, v4df, v4di, int); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_vpermilpd256(v4df, int); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_vpermilvarpd256(v4df, v4di); //expect: PythonIntrinsicIssue
    v4df __builtin_ia32_xorpd256(v4df, v4df); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_andnotsi256(v4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_andsi256(v4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_extract128i256(v4di, int); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_gatherdiv4di(v4di, pcint64, v4di, v4di, int); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_gathersiv4di(v4di, pcint64, v4si, v4di, int); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_insert128i256(v4di, v2di, int); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_maskloadq256(pcv4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_movntdqa256(pv4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_paddq256(v4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_palignr256(v4di, v4di, int); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pbroadcastq256(v2di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pcmpeqq256(v4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pcmpgtq256(v4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_permdi256(v4di, int); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_permti256(v4di, v4di, int); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pmovsxbq256(v16qi); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pmovsxdq256(v4si); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pmovsxwq256(v8hi); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pmovzxbq256(v16qi); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pmovzxdq256(v4si); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pmovzxwq256(v8hi); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pmuldq256(v8si, v8si); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pmuludq256(v8si, v8si); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_por256(v4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pslldqi256(v4di, int); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_psllq256(v4di, v2di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_psllqi256(v4di, int); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_psllv4di(v4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_psrldqi256(v4di, int); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_psrlq256(v4di, v2di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_psrlqi256(v4di, int); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_psrlv4di(v4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_psubq256(v4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_punpckhqdq256(v4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_punpcklqdq256(v4di, v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_pxor256(v4di,v4di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_vbroadcastsi256(v2di); //expect: PythonIntrinsicIssue
    v4di __builtin_ia32_vpcmov_v4di256(v4di, v4di, v4di); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pabsw(v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_packssdw(v2si, v2si); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_paddsw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_paddusw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_paddw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pavgw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pcmpeqw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pcmpgtw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_phaddsw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_phaddw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_phsubsw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_phsubw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pinsrw(v4hi, int, int); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pmaddubsw(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pmaxsw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pminsw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pmulhrsw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pmulhrw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pmulhuw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pmulhw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_pmullw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_psignw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_psllwi(v4hi, int); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_psllw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_psrawi(v4hi, int); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_psraw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_psrlwi(v4hi, int); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_psrlw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_psubsw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_psubusw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_psubw(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_punpckhwd(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4hi __builtin_ia32_punpcklwd(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_addps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_addss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_addsubps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_andnps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_andps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_blendps(v4sf, v4sf, const int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_blendvps(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_cmpps(v4sf, v4sf, int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_cmpss(v4sf, v4sf, int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_cvtdq2ps(v4si); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_cvtpd2ps256(v4df); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_cvtpd2ps(v2df); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_cvtpi2ps(v4sf, v2si); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_cvtsd2ss(v4sf, v2df); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_cvtsi2ss(v4sf, int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_divps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_divss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_dpps(v4sf, v4sf, const int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_fmaddps(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_fmaddss(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_fmaddsubps(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_fmsubaddps(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_fmsubps(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_fmsubss(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_fnmaddps(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_fnmaddss(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_fnmsubps(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_fnmsubss(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_gatherdiv4sf256(v4sf, pcfloat, v4di, v4sf, int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_gatherdiv4sf(v4sf, pcfloat, v2di, v4sf, int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_gathersiv4sf(v4sf, pcfloat, v4si, v4sf, int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_haddps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_hsubps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_insertps128(v4sf, v4sf, const int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_loadaps(float *); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_loadhps(v4sf, const v2sf *); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_loadlps(v4sf, const v2sf *); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_loadsss(float *); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_loadups(float *); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_maskloadps(pcv4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_maxps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_maxss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_minps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_minss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_movhlps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_movlhps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_movshdup(v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_movsldup(v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_movss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_mulps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_mulss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_orps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_ps_ps256(v8sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_rcpps(v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_rcpss(v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_roundps(v4sf, const int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_roundss(v4sf, v4sf, const int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_rsqrtps(v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_rsqrtss(v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_shufps(v4sf, v4sf, int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_sqrtps(v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_sqrtss(v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_subps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_subss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_unpckhps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_unpcklps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_vbroadcastss(pcfloat); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_vbroadcastss_ps(v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_vec_set_v4sf(v4sf, float, const int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_vextractf128_ps256(v8sf, int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_vfrczps(v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_vfrczss(v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_vpcmov_v4sf(v4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_vpermil2ps(v4sf, v4sf, v4si, int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_vpermilps(v4sf, int); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_vpermilvarps(v4sf, v4si); //expect: PythonIntrinsicIssue
    v4sf __builtin_ia32_xorps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpeqps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpeqss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpgeps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpgtps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpleps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpless(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpltps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpltss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpneqps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpneqss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpngeps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpngtps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpnleps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpnless(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpnltps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpnlts(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpordps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpordss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpunordps(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cmpunordss(v4sf, v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cvtpd2dq256(v4df); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cvtpd2dq(v2df); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cvtps2dq(v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cvttpd2dq256(v4df); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cvttpd2dq(v2df); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_cvttps2dq(v4sf); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_gatherdiv4si256(v4si, pcint, v4di, v4si, int); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_gatherdiv4si(v4si, pcint, v2di, v4si, int); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_gathersiv4si(v4si, pcint, v4si, v4si, int); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_maskloadd(pcv4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pabsd128(v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_paddd128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pblendd128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pbroadcastd128(v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pcmpeqd128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pcmpgtd128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_phaddd128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_phsubd128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pmaddwd128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pmaxsd128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pmaxud128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pminsd128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pminud128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pmovsxbd128(v16qi); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pmovsxwd128(v8hi); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pmovzxbd128(v16qi); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pmovzxwd128(v8hi); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pmulld128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pshufd(v4si, int); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_psignd128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pslld128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_pslldi128(v4si, int); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_psllv4si(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_psrad128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_psradi128(v4si, int); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_psrav4si(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_psrld128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_psrldi128(v4si, int); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_psrlv4si(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_psubd128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_punpckhdq128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_punpckldq128(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_si_si256(v8si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vec_set_v4si(v4si, int, const int); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vextractf128_si256(v8si, int); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcmov_v4si(v4si, v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomeqd(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomequd(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomfalsed(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomfalseud(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomged(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomgeud(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomgtd(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomgtud(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomled(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomleud(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomltd(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomltud(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomned(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomneud(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomtrued(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpcomtrueud(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vphaddbd(v16qi); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vphaddubd(v16qi); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vphadduwd(v8hi); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vphaddwd(v8hi); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vphsubwd(v8hi); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpmacsdd(v4si, v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpmacssdd(v4si, v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpmacsswd(v8hi, v8hi, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpmacswd(v8hi, v8hi, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpmadcsswd(v8hi, v8hi, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpmadcswd(v8hi, v8hi, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vprotd(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpshad(v4si, v4si); //expect: PythonIntrinsicIssue
    v4si __builtin_ia32_vpshld(v4si, v4si); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pabsw128(v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_packssdw128(v4si, v4si); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_packusdw128(v4si, v4si); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_paddw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pavgw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pblendw128(v8hi, v8hi, const int); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pbroadcastw128(v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pcmpeqw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pcmpgtw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_phaddsw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_phaddw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_phminposuw128(v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_phsubsw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_phsubw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pmaddubsw128(v16qi, v16qi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pmaxsw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pmaxuw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pminsw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pminuw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pmovsxbw128(v16qi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pmovzxbw128(v16qi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pmulhrsw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pmulhuw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pmulhw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pmullw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pshufhw(v8hi, int); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_pshuflw(v8hi, int); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_psignw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_psllw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_psllwi128(v8hi, int); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_psraw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_psrawi128(v8hi, int); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_psrlw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_psrlwi128(v8hi, int); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_psubw128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_punpckhwd128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_punpcklwd128(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcmov_v8hi(v8hi, v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomequw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomeqw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomfalseuw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomfalsew(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomgeuw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomgew(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomgtuw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomgtw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomleuw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomlew(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomltuw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomltw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomneuw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomnew(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomtrueuw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpcomtruew(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vphaddbw(v16qi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vphaddubw(v16qi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vphsubbw(v16qi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpmacssww(v8hi, v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpmacsww(v8hi, v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vprotw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpshaw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8hi __builtin_ia32_vpshlw(v8hi, v8hi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_pabsb(v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_packsswb(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_packuswb(v4hi, v4hi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_paddb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_paddsb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_paddusb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_pavgb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_pavgusb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_pcmpeqb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_pcmpgtb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_pmaxub(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_pminub(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_pshufb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_psignb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_psubb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_psubsb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_psubusb(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_punpckhbw(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8qi __builtin_ia32_punpcklbw(v8qi, v8qi); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_addps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_addsubps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_andnps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_andps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_blendps256(v8sf, v8sf, int); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_blendvps256(v8sf, v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_cmpps256(v8sf, v8sf, int); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_cvtdq2ps256(v8si); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_divps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_dpps256(v8sf, v8sf, int); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_fmaddps256(v8sf, v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_fmaddsubps256(v8sf, v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_fmsubaddps256(v8sf, v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_fmsubps256(v8sf, v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_fnmaddps256(v8sf, v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_fnmsubps256(v8sf, v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_gathersiv8sf(v8sf, pcfloat, v8si, v8sf, int); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_haddps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_hsubps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_loadups256(pcfloat); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_maskloadps256(pcv8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_maxps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_minps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_movshdup256(v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_movsldup256(v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_mulps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_orps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_permvarsf256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_ps256_ps(v4sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_rcpps256(v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_roundps256(v8sf, int); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_rsqrtps256(v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_rsqrtps_nr256(v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_shufps256(v8sf, v8sf, int); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_sqrtps256(v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_sqrtps_nr256(v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_subps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_unpckhps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_unpcklps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_vbroadcastf128_ps256(pcv4sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_vbroadcastss256(pcfloat); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_vbroadcastss_ps256(v4sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_vfrczps256(v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_vinsertf128_ps256(v8sf, v4sf, int); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_vpcmov_v8sf256(v8sf, v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_vperm2f128_ps256(v8sf, v8sf, int); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_vpermil2ps256(v8sf, v8sf, v8si, int); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_vpermilps256(v8sf, int); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_vpermilvarps256(v8sf, v8si); //expect: PythonIntrinsicIssue
    v8sf __builtin_ia32_xorps256(v8sf, v8sf); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_cvtps2dq256(v8sf); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_cvttps2dq256(v8sf); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_gathersiv8si(v8si, pcint, v8si, v8si, int); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_maskloadd256(pcv8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pabsd256(v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_paddd256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pblendd256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pbroadcastd256(v4si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pcmpeqd256(c8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pcmpgtd256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_permvarsi256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_phaddd256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_phsubd256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pmaxsd256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pmaxud256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pminsd256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pminud256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pmovsxbd256(v16qi); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pmovsxwd256(v8hi); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pmovzxbd256(v16qi); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pmovzxwd256(v8hi); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pmulld256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pshufd256(v8si, int); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_psignd256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pslld256(v8si, v4si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_pslldi256(v8si, int); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_psllv8si(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_psrad256(v8si, v4si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_psradi256(v8si, int); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_psrav8si(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_psrld256(v8si, v4si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_psrldi256(v8si, int); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_psrlv8si(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_psubd256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_punpckhdq256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_punpckldq256(v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_si256_si(v4si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_vinsertf128_si256(v8si, v4si, int); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_vpcmov_v8si256(v8si, v8si, v8si); //expect: PythonIntrinsicIssue
    v8si __builtin_ia32_vperm2f128_si256(v8si, v8si, int); //expect: PythonIntrinsicIssue
    void __addfsbyte(unsigned long, unsigned char); //expect: PythonIntrinsicIssue
    void __addfsdword(unsigned long, unsigned long); //expect: PythonIntrinsicIssue
    void __addfsword(unsigned long, unsigned short); //expect: PythonIntrinsicIssue
    void __addgsbyte(unsigned long, unsigned char); //expect: PythonIntrinsicIssue
    void __addgsdword(unsigned long, unsigned int); //expect: PythonIntrinsicIssue
    void __addgsqword(unsigned long, unsigned __int64); //expect: PythonIntrinsicIssue
    void __addgsword(unsigned long, unsigned short); //expect: PythonIntrinsicIssue
    void * _AddressOfReturnAddress(void);
    void __builtin_cpu_init(void); //expect: PythonIntrinsicIssue
    void __builtin_ia32_clflush(const void *); //expect: PythonIntrinsicIssue
    void __builtin_ia32_femms(void); //expect: PythonIntrinsicIssue
    void __builtin_ia32_lfence(void); //expect: PythonIntrinsicIssue
    void __builtin_ia32_llwpcb16(void *); //expect: PythonIntrinsicIssue
    void * __builtin_ia32_llwpcb16(void); //expect: PythonIntrinsicIssue
    void __builtin_ia32_llwpcb32(void *); //expect: PythonIntrinsicIssue
    void * __builtin_ia32_llwpcb32(void); //expect: PythonIntrinsicIssue
    void __builtin_ia32_llwpcb64(void *); //expect: PythonIntrinsicIssue
    void * __builtin_ia32_llwpcb64(void);  //expect: PythonIntrinsicIssue
    void __builtin_ia32_lwpval16(unsigned short, unsigned int, unsigned short); //expect: PythonIntrinsicIssue
    void __builtin_ia32_lwpval32(unsigned int, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    void __builtin_ia32_lwpval64(unsigned __int64, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    void __builtin_ia32_maskmovdqu(v16qi, v16qi); //expect: PythonIntrinsicIssue
    void __builtin_ia32_maskmovq(v8qi, v8qi, char *); //expect: PythonIntrinsicIssue
    void __builtin_ia32_maskstored256(pv8si, v8si, v8si); //expect: PythonIntrinsicIssue
    void __builtin_ia32_maskstored(pv4si, v4si, v4si); //expect: PythonIntrinsicIssue
    void __builtin_ia32_maskstorepd256(pv4df, v4df, v4df); //expect: PythonIntrinsicIssue
    void __builtin_ia32_maskstorepd(pv2df, v2df, v2df); //expect: PythonIntrinsicIssue
    void __builtin_ia32_maskstoreps256(pv8sf, v8sf, v8sf); //expect: PythonIntrinsicIssue
    void __builtin_ia32_maskstoreps(pv4sf, v4sf, v4sf); //expect: PythonIntrinsicIssue
    void __builtin_ia32_maskstoreq256(pv4di, v4di, v4di); //expect: PythonIntrinsicIssue
    void __builtin_ia32_maskstoreq(pv2di, v2di, v2di); //expect: PythonIntrinsicIssue
    void __builtin_ia32_mfence(void); //expect: PythonIntrinsicIssue
    void __builtin_ia32_monitor(void *, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    void __builtin_ia32_movntdq(v2df *, v2df); //expect: PythonIntrinsicIssue
    void __builtin_ia32_movnti64(long long int *, long long int); //expect: PythonIntrinsicIssue
    void __builtin_ia32_movnti(int *, int); //expect: PythonIntrinsicIssue
    void __builtin_ia32_movntpd(double *, v2df); //expect: PythonIntrinsicIssue
    void __builtin_ia32_movntps(float *, v4sf); //expect: PythonIntrinsicIssue
    void __builtin_ia32_movntq(di *, di); //expect: PythonIntrinsicIssue
    void __builtin_ia32_movntsd(double *, v2df); //expect: PythonIntrinsicIssue
    void __builtin_ia32_movntss(float *, v4sf); //expect: PythonIntrinsicIssue
    void __builtin_ia32_mwait(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    void __builtin_ia32_pause(void); //expect: PythonIntrinsicIssue
    void __builtin_ia32_sfence(void); //expect: PythonIntrinsicIssue
    void __builtin_ia32_storeaps(float *, v4sf); //expect: PythonIntrinsicIssue
    void __builtin_ia32_storedqu256(pchar, v32qi); //expect: PythonIntrinsicIssue
    void __builtin_ia32_storedqu(char *, v16qi); //expect: PythonIntrinsicIssue
    void __builtin_ia32_storehps(v2sf *, v4sf); //expect: PythonIntrinsicIssue
    void __builtin_ia32_storelps(v2sf *, v4sf); //expect: PythonIntrinsicIssue
    void __builtin_ia32_storess(float *, v4sf); //expect: PythonIntrinsicIssue
    void __builtin_ia32_storeupd256(pdouble, v4df); //expect: PythonIntrinsicIssue
    void __builtin_ia32_storeupd(double *, v2df); //expect: PythonIntrinsicIssue
    void __builtin_ia32_storeups256(pfloat, v8sf); //expect: PythonIntrinsicIssue
    void __builtin_ia32_storeups(float *, v4sf); //expect: PythonIntrinsicIssue
    void __builtin_ia32_vzeroall(void); //expect: PythonIntrinsicIssue
    void __builtin_ia32_vzeroupper(void); //expect: PythonIntrinsicIssue
    void __builtin_ia32_xabort(status); //expect: PythonIntrinsicIssue
    void __builtin_ia32_xend(); //expect: PythonIntrinsicIssue
    void _clac(void); //expect: PythonIntrinsicIssue
    void __cpuidex(int *, int, int); //expect: PythonIntrinsicIssue
    void __cpuid(int *, int); //expect: PythonIntrinsicIssue
    void __debugbreak(void);
    void _disable(void);
    void _enable(void);
    void __fastfail(unsigned int);
    void __faststorefence(void); //expect: PythonIntrinsicIssue
    void _fxrstor64(void const *); //expect: PythonIntrinsicIssue
    void _fxrstor(void const *); //expect: PythonIntrinsicIssue
    void _fxsave64(void *); //expect: PythonIntrinsicIssue
    void _fxsave(void *); //expect: PythonIntrinsicIssue
    void __halt(void); //expect: PythonIntrinsicIssue
    void __inbytestring(unsigned short, unsigned char *, unsigned long); //expect: PythonIntrinsicIssue
    void __incfsbyte(unsigned long); //expect: PythonIntrinsicIssue
    void __incfsdword(unsigned long); //expect: PythonIntrinsicIssue
    void __incfsword(unsigned long); //expect: PythonIntrinsicIssue
    void __incgsbyte(unsigned long); //expect: PythonIntrinsicIssue
    void __incgsdword(unsigned long); //expect: PythonIntrinsicIssue
    void __incgsqword(unsigned long); //expect: PythonIntrinsicIssue
    void __incgsword(unsigned long); //expect: PythonIntrinsicIssue
    void __indwordstring(unsigned short, unsigned long *, unsigned long); //expect: PythonIntrinsicIssue
    void __int2c(void); //expect: PythonIntrinsicIssue
    void * _InterlockedCompareExchangePointer_HLEAcquire(void * volatile *, void *, void *); //expect: PythonIntrinsicIssue
    void * _InterlockedCompareExchangePointer_HLERelease(void * volatile *, void *, void *); //expect: PythonIntrinsicIssue
    void * _InterlockedCompareExchangePointer_np(void **, void *, void *); //expect: PythonIntrinsicIssue
    void * _InterlockedCompareExchangePointer(void * volatile *, void *, void *);
    void * _InterlockedExchangePointer_HLEAcquire(void * volatile *, void *); //expect: PythonIntrinsicIssue
    void * _InterlockedExchangePointer_HLERelease(void * volatile *, void *); //expect: PythonIntrinsicIssue
    void * _InterlockedExchangePointer(void * volatile *, void *);
    void __invlpg(void *); //expect: PythonIntrinsicIssue
    void _invpcid(unsigned int, void *); //expect: PythonIntrinsicIssue
    void __inwordstring(unsigned short, unsigned short *, unsigned long); //expect: PythonIntrinsicIssue
    void _lgdt(void *); //expect: PythonIntrinsicIssue
    void __lidt(void *); //expect: PythonIntrinsicIssue
    void __llwpcb(void *); //expect: PythonIntrinsicIssue
    void __lwpval32(unsigned int, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    void __lwpval64(unsigned __int64, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    void _m_empty(void); //expect: PythonIntrinsicIssue
    void _m_femms(void); //expect: PythonIntrinsicIssue
    void _mm256_maskstore_epi32(int *, __m256i, __m256i); //expect: PythonIntrinsicIssue
    void _mm256_maskstore_epi64(__int64 *, __m256i, __m256i); //expect: PythonIntrinsicIssue
    void _mm256_maskstore_pd(double *, __m256i, __m256d); //expect: PythonIntrinsicIssue
    void _mm256_maskstore_ps(float *, __m256i, __m256); //expect: PythonIntrinsicIssue
    void _mm256_store_pd(double *, __m256d); //expect: PythonIntrinsicIssue
    void _mm256_store_ps(float *, __m256); //expect: PythonIntrinsicIssue
    void _mm256_store_si256(__m256i *, __m256i); //expect: PythonIntrinsicIssue
    void _mm256_storeu_pd(double *, __m256d); //expect: PythonIntrinsicIssue
    void _mm256_storeu_ps(float *, __m256); //expect: PythonIntrinsicIssue
    void _mm256_storeu_si256(__m256i *, __m256i); //expect: PythonIntrinsicIssue
    void __mm256_stream_pd(double *, __m256d); //expect: PythonIntrinsicIssue
    void _mm256_stream_ps(float *, __m256); //expect: PythonIntrinsicIssue
    void __mm256_stream_si256(__m256i *, __m256i); //expect: PythonIntrinsicIssue
    void _mm256_zeroall(void); //expect: PythonIntrinsicIssue
    void _mm256_zeroupper(void); //expect: PythonIntrinsicIssue
    void _m_maskmovq(__m64, __m64, char *); //expect: PythonIntrinsicIssue
    void _mm_clflush(void const *); //expect: PythonIntrinsicIssue
    void _mm_lfence(void); //expect: PythonIntrinsicIssue
    void _mm_maskmoveu_si128(__m128i, __m128i, char *); //expect: PythonIntrinsicIssue
    void _mm_maskstore_epi32(int *, __m128i, __m128i); //expect: PythonIntrinsicIssue
    void _mm_maskstore_epi64(__int64 *, __m128i, __m128i); //expect: PythonIntrinsicIssue
    void _mm_maskstore_pd(double *, __m128i, __m128d); //expect: PythonIntrinsicIssue
    void _mm_maskstore_ps(float *, __m128i, __m128); //expect: PythonIntrinsicIssue
    void _mm_mfence(void); //expect: PythonIntrinsicIssue
    void _mm_monitor(void const *, unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    void _mm_mwait(unsigned int, unsigned int); //expect: PythonIntrinsicIssue
    void _mm_pause(void); //expect: PythonIntrinsicIssue
    void _mm_prefetch(char *, int); //expect: PythonIntrinsicIssue
    void _mm_setcsr(unsigned int); //expect: PythonIntrinsicIssue
    void _mm_sfence(void); //expect: PythonIntrinsicIssue
    void _mm_store1_pd(double *, __m128d); //expect: PythonIntrinsicIssue
    void _mm_storeh_pd(double *, __m128d); //expect: PythonIntrinsicIssue
    void _mm_storeh_pi(__m64 *, __m128); //expect: PythonIntrinsicIssue
    void _mm_storel_epi64(__m128i *, __m128i); //expect: PythonIntrinsicIssue
    void _mm_storel_pd(double *, __m128d); //expect: PythonIntrinsicIssue
    void _mm_storel_pi(__m64 *, __m128); //expect: PythonIntrinsicIssue
    void _mm_store_pd(double *, __m128d); //expect: PythonIntrinsicIssue
    void _mm_store_ps1(float *, __m128); //expect: PythonIntrinsicIssue
    void _mm_store_ps(float *, __m128); //expect: PythonIntrinsicIssue
    void _mm_storer_pd(double *, __m128d); //expect: PythonIntrinsicIssue
    void _mm_storer_ps(float *, __m128); //expect: PythonIntrinsicIssue
    void _mm_store_sd(double *, __m128d); //expect: PythonIntrinsicIssue
    void _mm_store_si128(__m128i *, __m128i); //expect: PythonIntrinsicIssue
    void _mm_store_ss(float *, __m128); //expect: PythonIntrinsicIssue
    void _mm_storeu_pd(double *, __m128d); //expect: PythonIntrinsicIssue
    void _mm_storeu_ps(float *, __m128); //expect: PythonIntrinsicIssue
    void _mm_storeu_si128(__m128i *, __m128i); //expect: PythonIntrinsicIssue
    void _mm_stream_pd(double *, __m128d); //expect: PythonIntrinsicIssue
    void _mm_stream_pi(__m64 *, __m64); //expect: PythonIntrinsicIssue
    void _mm_stream_ps(float *, __m128); //expect: PythonIntrinsicIssue
    void _mm_stream_sd(double *, __m128d); //expect: PythonIntrinsicIssue
    void _mm_stream_si128(__m128i *, __m128i); //expect: PythonIntrinsicIssue
    void _mm_stream_si32(int *, int); //expect: PythonIntrinsicIssue
    void _mm_stream_si64x(__int64 *, __int64); //expect: PythonIntrinsicIssue
    void _mm_stream_ss(float *, __m128); //expect: PythonIntrinsicIssue
    void __movsb(unsigned char *, unsigned char const *, size_t); //expect: PythonIntrinsicIssue
    void __movsd(unsigned long *, unsigned long const *, size_t); //expect: PythonIntrinsicIssue
    void __movsq(unsigned __int64 *, unsigned __int64 const *, size_t); //expect: PythonIntrinsicIssue
    void __movsw(unsigned short *, unsigned short const *, size_t); //expect: PythonIntrinsicIssue
    void _m_prefetch(void *); //expect: PythonIntrinsicIssue
    void _m_prefetchw(void *); //expect: PythonIntrinsicIssue
    void __nop(void);
    void __nvreg_restore_fence(void); //expect: PythonIntrinsicIssue
    void __nvreg_save_fence(void); //expect: PythonIntrinsicIssue
    void __outbytestring(unsigned short, unsigned char *, unsigned long); //expect: PythonIntrinsicIssue
    void __outbyte(unsigned short, unsigned char); //expect: PythonIntrinsicIssue
    void __outdwordstring(unsigned short, unsigned long *, unsigned long); //expect: PythonIntrinsicIssue
    void __outdword(unsigned short, unsigned long); //expect: PythonIntrinsicIssue
    void __outwordstring(unsigned short, unsigned short *, unsigned long); //expect: PythonIntrinsicIssue
    void __outword(unsigned short, unsigned short); //expect: PythonIntrinsicIssue
    void _ReadBarrier(void);
    void _ReadWriteBarrier(void);
    void * _ReturnAddress(void);
    void _rsm(void); //expect: PythonIntrinsicIssue
    void _sgdt(void *); //expect: PythonIntrinsicIssue
    void _sgdt(void*); //expect: PythonIntrinsicIssue
    void __sidt(void *); //expect: PythonIntrinsicIssue
    void * __slwpcb(void); //expect: PythonIntrinsicIssue
    void _stac(void); //expect: PythonIntrinsicIssue
    void _Store64_HLERelease(__int64 volatile *, __int64); //expect: PythonIntrinsicIssue
    void _storebe_i16(void *, short); //expect: PythonIntrinsicIssue
    void _storebe_i32(void *, int); //expect: PythonIntrinsicIssue
    void _storebe_i64(void *, __int64); //expect: PythonIntrinsicIssue
    void _store_be_u16(void *, unsigned short); //expect: PythonIntrinsicIssue
    void _store_be_u32(void *, unsigned int); //expect: PythonIntrinsicIssue
    void _store_be_u64(void *, unsigned __int64); //expect: PythonIntrinsicIssue
    void _Store_HLERelease(long volatile *, long); //expect: PythonIntrinsicIssue
    void _StorePointer_HLERelease(void * volatile *, void *); //expect: PythonIntrinsicIssue
    void __stosb(unsigned char *, unsigned char, size_t); //expect: PythonIntrinsicIssue
    void __stosd(unsigned long *, unsigned long, size_t); //expect: PythonIntrinsicIssue
    void __stosq(unsigned __int64 *, unsigned __int64, size_t); //expect: PythonIntrinsicIssue
    void __stosw(unsigned short *, unsigned short, size_t); //expect: PythonIntrinsicIssue
    void __svm_clgi(void); //expect: PythonIntrinsicIssue
    void __svm_invlpga(void *, int); //expect: PythonIntrinsicIssue
    void __svm_skinit(int); //expect: PythonIntrinsicIssue
    void __svm_stgi(void); //expect: PythonIntrinsicIssue
    void __svm_vmload(size_t); //expect: PythonIntrinsicIssue
    void __svm_vmrun(size_t); //expect: PythonIntrinsicIssue
    void __svm_vmsave(size_t); //expect: PythonIntrinsicIssue
    void __ud2(void); //expect: PythonIntrinsicIssue
    void __vmx_off(void); //expect: PythonIntrinsicIssue
    void __vmx_vmptrst(unsigned __int64 *); //expect: PythonIntrinsicIssue
    void __wbinvd(void); //expect: PythonIntrinsicIssue
    void _WriteBarrier(void);
    void __writecr0(unsigned __int64); //expect: PythonIntrinsicIssue
    void __writecr0(unsigned long); //expect: PythonIntrinsicIssue
    void __writecr3(unsigned __int64); //expect: PythonIntrinsicIssue
    void __writecr3(unsigned long); //expect: PythonIntrinsicIssue
    void __writecr4(unsigned __int64); //expect: PythonIntrinsicIssue
    void __writecr4(unsigned long); //expect: PythonIntrinsicIssue
    void __writecr8(unsigned __int64); //expect: PythonIntrinsicIssue
    void __writecr8(unsigned long); //expect: PythonIntrinsicIssue
    void __writedr(unsigned, unsigned); //expect: PythonIntrinsicIssue
    void __writedr(unsigned, unsigned __int64); //expect: PythonIntrinsicIssue
    void __writeeflags(unsigned); //expect: PythonIntrinsicIssue
    void __writeeflags(unsigned __int64); //expect: PythonIntrinsicIssue
    void _writefsbase_u32(unsigned int); //expect: PythonIntrinsicIssue
    void _writefsbase_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    void _writefsbase_u64(unsigned long long); //expect: PythonIntrinsicIssue
    void __writefsbyte(unsigned long, unsigned char); //expect: PythonIntrinsicIssue
    void __writefsdword(unsigned long, unsigned long); //expect: PythonIntrinsicIssue
    void __writefsword(unsigned long, unsigned short); //expect: PythonIntrinsicIssue
    void _writegsbase_u32(unsigned int); //expect: PythonIntrinsicIssue
    void _writegsbase_u64(unsigned __int64); //expect: PythonIntrinsicIssue
    void _writegsbase_u64(unsigned long long); //expect: PythonIntrinsicIssue
    void __writegsbyte(unsigned long, unsigned char); //expect: PythonIntrinsicIssue
    void __writegsdword(unsigned long, unsigned long); //expect: PythonIntrinsicIssue
    void __writegsqword(unsigned long, unsigned __int64); //expect: PythonIntrinsicIssue
    void __writegsword(unsigned long, unsigned short); //expect: PythonIntrinsicIssue
    void __writemsr(unsigned long, unsigned __int64); //expect: PythonIntrinsicIssue
    void _xrstor64(void const *, unsigned __int64); //expect: PythonIntrinsicIssue
    void _xrstor(void const *, unsigned __int64); //expect: PythonIntrinsicIssue
    void _xsave64(void *, unsigned __int64); //expect: PythonIntrinsicIssue
    void _xsaveopt64(void *, unsigned __int64); //expect: PythonIntrinsicIssue
    void _xsaveopt(void *, unsigned __int64); //expect: PythonIntrinsicIssue
    void _xsave(void *, unsigned __int64); //expect: PythonIntrinsicIssue
    void _xsetbv(unsigned int, unsigned __int64); //expect: PythonIntrinsicIssue
      
    int printf(const char *format, ...);
""")
# Load shared library.
# None means loading the entire C namespace.
C = ffi.dlopen(None)
# Call a function from the shared library.
arg = ffi.new("char[]", b"dsklfsd")
C.printf(b"hello %s!\n", arg)