from cffi import FFI
ffi = FFI()
#cdef用来定义结构体,变量,或者方法的声明
#hygon_intrinsics:
ffi.cdef("""
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
#dlopen是ABI模式的的基本读取方式
C = ffi.dlopen(None) # 加载整个C命名空间
arg = ffi.new("char[]", b"dsklfsd") # 等于C代码: char arg[] = "world";
C.printf(b"hello %s!\n", arg)