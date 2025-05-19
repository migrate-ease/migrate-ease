import cffi

ffi = cffi.FFI()

ffi.cdef("""int add(int a, int b);""")

ffi.set_source('_ext', r"""
int add(int a, int b)
{
//aarch64 inline assembly
#if defined(__aarch64__)
#define barrier() __sync_synchronize()
__asm__ __volatile__("dmb ish" : : : "memory");
#endif

#if defined(__aarch64__)
__asm__ __volatile__("dmb ishst" : : : "memory");
#endif

#if defined(__aarch64__)
__asm__ __volatile__("dmb ishld" : : : "memory");
#endif

#if defined(__aarch64__)
__asm__ __volatile__("crc32cb %w[c], %w[c], %w[v]":[c]"+r"(crc):[v]"r"(value));
#endif

#if defined(__aarch64__)
__asm__ __volatile__("crc32ch %w[c], %w[c], %w[v]":[c]"+r"(crc):[v]"r"(value));
#endif

#if defined(__aarch64__)
__asm__ __volatile__("crc32cw %w[c], %w[c], %w[v]":[c]"+r"(crc):[v]"r"(value));
#endif

#if defined(__aarch64__)
__asm__ __volatile__("crc32cx %w[c], %w[c], %x[v]":[c]"+r"(crc):[v]"r"(value));
#endif

#if defined(__aarch64__)
__asm__ __volatile__("rev %w[dst], %w[src]" : [dst]"=r"(val) : [src]"r"(val));
#endif


#if defined(__aarch64__)
#define __nops(n) ".rept " #n "\nnop\n.endr\n"
#define nops(n) asm volatile(__nops(n))
#endif

#if defined(__aarch64__)
__asm__ __volatile__("yield" : : : "memory");//there esist an error
__asm__ __volatile__("yield");
#endif

#if defined(__aarch64__)
__asm__ __volatile__("mrs %0, cntvct_el0" : "=r" (count_num));
static uint64_t Rdtsc()
    {
        struct timespec tmp;
        clock_gettime(CLOCK_MONOTONIC, &tmp);
        return tmp.tv_sec * 2400000000 + (uint64_t)tmp.tv_nsec * 2.4; 
    }
static uint64_t Rdtsc()
    {
        uint64_t count_num;
        __asm__ __volatile__("mrs %0, PMCCNTR_EL0" : "+r" (count_num));
        return count_num；
    }
#endif

#if defined(__aarch64__)
#include <arm_neon.h>
static inline int POPCNT_popcnt_u64(uint64_t x)
    {
    uint64_t count_result = 0;
    uint64_t count[1];
    uint8x8_t input_val,count8x8_val;
    uint16x4_t count16x4_val;
    uint32x2_t count32x2_val;
    uint64x1_t count64x1_val;
    input_val = vld1_u8((unsigned char *) &x);
    count8x8_val = vcnt_u8(input_val);
    count16x4_val = vpaddl_u8(count8x8_val);
    count32x2_val = vpaddl_u16(count16x4_val);
    count64x1_val = vpaddl_u32(count32x2_val);
    vst1_u64(count, count64x1_val);
    count_result=count[0];
    return count_result;
}
#endif

#if defined(__aarch64__)
__sync_add_and_fetch(&_value.counter,1)
void atomic_add(int i)
{
    unsigned int tmp;
    int result;
    __asm__ volatile(" prfm pstl1strm, %2\n"
        "1: ldaxr %w0, %2\n"
        " add %w0, %w0, %w3\n"
        " stlxr %w1, %w0, %2\n"
        " cbnz %w1, 1b"
        : "=&r"(result), "=&r"(tmp), "+Q"(_value.counter)
        : "Ir"(i)
    )
}
#endif

#if defined(__aarch64__)
__sync_sub_and_fetch(&_value.counter,1);
void atomic_sub (int i)
{
    unsigned int tmp;
    int result;
    __asm__ volatile(" prfm pstl1strm, %2\n"
        "1: ldaxr %w0, %2\n"
        " sub %w0, %w0, %w3\n"
        " stlxr %w1, %w0, %2\n"
        " cbnz %w1, 1b"
        : "=&r"(result), "=&r"(tmp), "+Q"(_value.counter)
        : "Ir"(i)
    )
}
#endif

#if defined(__aarch64__)
__sync_sub_and_fetch(&_value.counter, i)
static inline int atomic_sub_return(int i, atomic_t *v)
{
    unsigned long tmp;
    int result;
    prefetchw(&v->counter);
    __asm__ volatile("\n\t"
        "@ atomic_sub\n\t"
        "1: ldrex %0, [%3]\n\t"
        " sub %0, %0, %4\n\t"
        " strex %1, %0, [%3]\n\t"
        " teq %1, #0\n\t"
        " bne 1b"
        : "=&r" (result), "=&r" (tmp), "+Qo" (v->counter)
        : "r" (&v->counter), "Ir" (i)
        : "cc");
    return result;
}
#endif

#if defined(__aarch64__)
__sync_add_and_fetch(&_value.counter, i)
{
    unsigned long tmp;
    int result, val;
    prefetchw(&v->counter);
    __asm__ volatile("\n\t"
        "@ atomic_fetch\n\t"
        "1: ldrex %0, [%4]\n\t" @result, tmp
        " add %1, %0, %5\n\t" @result,
        " strex %2, %1, [%4]\n\t" @tmp, result, tmp
        " teq %2, #0\n\t" @tmp
        " bne 1b"
        : "=&r"(result), "=&r"(val), "=&r"(tmp), "+Qo"(v->counter)
        : "r"(&v->counter), "Ir"(i)
        : "cc");
    return result;
}
#endif

#if defined(__aarch64__)
static __inline__ long atomic64_add_and_return(long i, atomic64_t *v)
{
    return __sync_add_and_fetch(&((v)->counter), i); //expect: PythonCPPStdCodes
}
#endif

#if defined(__aarch64__)
#include <arm_neon.h>
typedef union __attribute__((aligned(16))) __oword
{
    int32x4_t m128i;
    uint8_t m128i_u8[16];
} __oword;
template<int MODE>
static inline uint16_t SSE4_cmpestrm(int32x4_t str1, int len1, int32x4_t str2, int len2)
{
    __oword a, b;
    a.m128i = str1;
    b.m128i = str2;
    uint16_t result = 0;
    uint16_t i = 0;
    uint16_t j = 0;
    // In Impala, STRCHR_MODE = PCMPSTR_EQUAL_ANY | PCMPSTR_UBYTE_OPS
    for (i = 0; i < len2; i++) {
        for ( j = 0; j < len1; j++) {
            if (a.m128i_u8[j] == b.m128i_u8[i]) {
                result |= (1 << i);
            }
        }
    }
    return result;
}
#endif

#if defined(__aarch64__)
#include <arm_neon.h>
template<int MODE>
static inline int SSE4_cmpestri(int32x4_t str1, int len1, int32x4_t str2, int len2)
{
    __oword a, b;
    a.m128i = str1;
    b.m128i = str2;
    int len_s, len_l;
    if (len1 > len2) {
        len_s = len2;
        len_l = len1;
    } else {
        len_s = len1;
        len_l = len2;
    }
    int result;
    int i;
    // STRCMP_MODE = PCMPSTR_EQUAL_EACH | PCMPSTR_UBYTE_OPS | PCMPSTR_NEG_POLARITY
    for(i = 0; i < len_s; i++)
    {
        if (a.m128i_u8[i] == b.m128i_u8[i])
        {
            break;
        }
    }
    result = i;
    if (result == len_s) result = len_l;
    return result;
}
#endif

#if defined(__aarch64__)
LDP Xt1, Xt2, addr
STP Xt1, Xt2, addr
#endif

#if defined(__aarch64__)
AND Vd.<T>, Vn.<T>, Vm.<T>
#endif

#if defined(__aarch64__)
EOR Vd.<T>, Vn.<T>, Vm.<T>
#endif

#if defined(__aarch64__)
TBL Vd.<T>, {Vn*.16B}, Vm.<T>2
#endif

// non-aarch64 inline assembly
// case1:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*memory.*
#if defined(__aarch64__)
__asm__ __volatile__("" : : : "memory"); // expect: PythonInlineAsmIssue
   __asm__ __volatile__("" : : : "memory");// expect: PythonInlineAsmIssue
asm__ __volatile__("" : : : "memory"); // expect: PythonInlineAsmIssue
_asm_ __volatile__("" : : : "memory");// expect: PythonInlineAsmIssue
__asm __volatile__("" : : : "memory");// expect: PythonInlineAsmIssue
__asm__      __volatile__("" : : : "memory");// expect: PythonInlineAsmIssue
__asm__ volatile__("" : : : "memory");// expect: PythonInlineAsmIssue
__asm__ __volatile("" : : : "memory");// expect: PythonInlineAsmIssue
__asm__("" : : : "memory");// expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("" : : : "memory");// expect: PythonInlineAsmIssue
__asm__ __volatile__("" // expect: PythonInlineAsmIssue
: : : "memory");
#endif

// case2:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*sfence.*
#if defined(__aarch64__)
__asm__ __volatile__("" : : : "sfence"); // expect: PythonInlineAsmIssue
   __asm__ __volatile__("" : : : "sfence");// expect: PythonInlineAsmIssue
asm__ __volatile__("" : : : "sfence"); // expect: PythonInlineAsmIssue
_asm_ __volatile__("" : : : "sfence");// expect: PythonInlineAsmIssue
__asm __volatile__("" : : : "sfence");// expect: PythonInlineAsmIssue
__asm__      __volatile__("" : : : "sfence");// expect: PythonInlineAsmIssue
__asm__ volatile__("" : : : "sfence");// expect: PythonInlineAsmIssue
__asm__ __volatile("" : : : "sfence");// expect: PythonInlineAsmIssue
__asm__("" : : : "sfence");// expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("" : : : "sfence");// expect: PythonInlineAsmIssue
__asm__ __volatile__("" : : :  // expect: PythonInlineAsmIssue
                                "sfence");
#endif

// case3:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*lfence.*
#if defined(__aarch64__)
__asm__ __volatile__("" : : : "lfence"); // expect: PythonInlineAsmIssue
   __asm__ __volatile__("" : : : "lfence");// expect: PythonInlineAsmIssue
asm__ __volatile__("" : : : "lfence"); // expect: PythonInlineAsmIssue
_asm_ __volatile__("" : : : "lfence");// expect: PythonInlineAsmIssue
__asm __volatile__("" : : : "lfence");// expect: PythonInlineAsmIssue
__asm__      __volatile__("" : : : "lfence");// expect: PythonInlineAsmIssue
__asm__ volatile__("" : : : "lfence");// expect: PythonInlineAsmIssue
__asm__ __volatile("" : : : "lfence");// expect: PythonInlineAsmIssue
__asm__("" : : : "lfence");// expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("" : : : "lfence");// expect: PythonInlineAsmIssue
__asm__ __volatile__("" : : : "lfence");// expect: PythonInlineAsmIssue
__asm__ __volatile__("" : : :  // expect: PythonInlineAsmIssue
                                "lfence");
#endif

// case4:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*mfence.*
#if defined(__aarch64__)
__asm__ __volatile__("" : : : "mfence"); // expect: PythonInlineAsmIssue
   __asm__ __volatile__("" : : : "mfence");// expect: PythonInlineAsmIssue
asm__ __volatile__("" : : : "mfence"); // expect: PythonInlineAsmIssue
_asm_ __volatile__("" : : : "mfence");// expect: PythonInlineAsmIssue
__asm __volatile__("" : : : "mfence");// expect: PythonInlineAsmIssue
__asm__      __volatile__("" : : : "mfence");// expect: PythonInlineAsmIssue
__asm__ volatile__("" : : : "mfence");// expect: PythonInlineAsmIssue
__asm__ __volatile("" : : : "mfence");// expect: PythonInlineAsmIssue
__asm__("" : : : "mfence");// expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("" : : : "mfence");// expect: PythonInlineAsmIssue
__asm__ __volatile__("" : : :  // expect: PythonInlineAsmIssue
                                "mfence");
#endif

// case5:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*crc32l.*
#if defined(__aarch64__)
__asm__ __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
    __asm__ __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
asm__ __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v)); // expect: PythonInlineAsmIssue
_asm_ __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
asm__ __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
__asm__      __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
__asm__ volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
__asm__ __volatile("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
__asm__("crc32l %1, %0" : "+r"(crc) : "rm"(v)); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
__asm__ __volatile__(  // expect: PythonInlineAsmIssue
                        "crc32l %1, %0" : "+r"(crc) : "rm"(v));
#endif

// case6:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*crc32q.*
#if defined(__aarch64__)
__asm__ __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: PythonInlineAsmIssue
    __asm__ __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: PythonInlineAsmIssue
asm__ __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v)); // expect: PythonInlineAsmIssue
_asm_ __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: PythonInlineAsmIssue
asm__ __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: PythonInlineAsmIssue
__asm__      __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: PythonInlineAsmIssue
__asm__ volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: PythonInlineAsmIssue
__asm__ __volatile("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: PythonInlineAsmIssue
__asm__("crc32q %1, %0" : "+r"(result) : "rm"(v)); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: PythonInlineAsmIssue
__asm__ __volatile__(  // expect: PythonInlineAsmIssue
                        "crc32q %1, %0" : "+r"(result) : "rm"(v));
#endif

// case7:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*bswap.*
#if defined(__aarch64__)
__asm__ __volatile__("bswap %0" : "=r" (val) : "0" (val)); // expect: PythonInlineAsmIssue
    __asm__ __volatile__("bswap %0" : "=r" (val) : "0" (val)); // expect: PythonInlineAsmIssue
asm__ __volatile__("bswap %0" : "=r" (val) : "0" (val)); // expect: PythonInlineAsmIssue
_asm_ __volatile__("bswap %0" : "=r" (val) : "0" (val));// expect: PythonInlineAsmIssue
asm__ __volatile__("bswap %0" : "=r" (val) : "0" (val));// expect: PythonInlineAsmIssue
__asm__      __volatile__("bswap %0" : "=r" (val) : "0" (val)); // expect: PythonInlineAsmIssue
__asm__ volatile__("bswap %0" : "=r" (val) : "0" (val));// expect: PythonInlineAsmIssue
__asm__ __volatile("bswap %0" : "=r" (val) : "0" (val));// expect: PythonInlineAsmIssue
__asm__("bswap %0" : "=r" (val) : "0" (val)); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("bswap %0" : "=r" (val) : "0" (val));// expect: PythonInlineAsmIssue
__asm__ __volatile__  // expect: PythonInlineAsmIssue
    ("bswap %0" : "=r" (val) : "0" (val));
#endif

#if defined(__aarch64__) // case8:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*rep.*
__asm__ __volatile__  // expect: PythonInlineAsmIssue
("rep;nop"
    ::: "memory");
#define nop __asm__ __volatile__("rep;nop" ::: "memory"); // expect: PythonInlineAsmIssue
asm__ __volatile__("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
_asm_ __volatile__("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
asm__ __volatile__("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
__asm__      __volatile__("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
__asm__ volatile__("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
__asm__ __volatile("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
__asm__("rep;nop" ::: "memory"); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
__asm__ __volatile__(  // expect: PythonInlineAsmIssue
                        "rep;nop" ::: "memory");
int main()
{
    unsigned int var_1 = 0;
    unsigned int var_2 = 999;
    unsigned int var_3 = 0;

    __asm__ __volatile__    // expect: PythonInlineAsmIssue
    (
        "mov %0, #20;" //asm code
        "rep stos %0, %1;"
        "mov %2, %1;"
        : "=r" (var_1), "=r"(var_3)
        : "r" (var_2)
        : "memory"
    )
}
#endif

// case9:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*pause.*
#if defined(__aarch64__)
__asm__ __volatile__(  // expect: PythonInlineAsmIssue
"pause" ::: "memory");
            __asm__ __volatile__("pause" ::: "memory"); // expect: PythonInlineAsmIssue
asm__ __volatile__("pause" ::: "memory"); // expect: PythonInlineAsmIssue
_asm_ __volatile__("pause" ::: "memory");// expect: PythonInlineAsmIssue
asm__ __volatile__("pause" ::: "memory");// expect: PythonInlineAsmIssue
__asm__      __volatile__("pause" ::: "memory");// expect: PythonInlineAsmIssue
__asm__ volatile__("pause" ::: "memory");// expect: PythonInlineAsmIssue
__asm__ __volatile("pause" ::: "memory");// expect: PythonInlineAsmIssue
__asm__("pause" ::: "memory"); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("pause" ::: "memory");// expect: PythonInlineAsmIssue
__asm__ __volatile__( // expect: PythonInlineAsmIssue
                        "pause" ::: "memory");
#endif

// case10:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*rdtsc.*
#if defined(__aarch64__)
__asm__ __volatile__("rdtsc" : "=a" (lo), "=d" (hi)); // expect: PythonInlineAsmIssue
            __asm__ __volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: PythonInlineAsmIssue
asm__ __volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: PythonInlineAsmIssue
_asm_ __volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: PythonInlineAsmIssue
asm__ __volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: PythonInlineAsmIssue
__asm__      __volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: PythonInlineAsmIssue
__asm__ volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: PythonInlineAsmIssue
__asm__ __volatile("rdtsc" : "=a" (lo), "=d" (hi));// expect: PythonInlineAsmIssue
__asm__("rdtsc" : "=a" (lo), "=d" (hi)); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("rdtsc" : "=a" (lo), "=d" (hi));// expect: PythonInlineAsmIssue
__asm__ __volatile__( // expect: PythonInlineAsmIssue
                        "rdtsc" : "=a" (lo), "=d" (hi));
#endif

 // case11:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*popcntq.*
#if defined(__aarch64__)
__asm__ __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: PythonInlineAsmIssue
            __asm__ __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: PythonInlineAsmIssue
asm__ __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: PythonInlineAsmIssue
_asm_ __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: PythonInlineAsmIssue
asm__ __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: PythonInlineAsmIssue
__asm__      __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: PythonInlineAsmIssue
__asm__ volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: PythonInlineAsmIssue
__asm__ __volatile("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: PythonInlineAsmIssue
__asm__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: PythonInlineAsmIssue
__asm__ __volatile__(  // expect: PythonInlineAsmIssue
                        "popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc");
#endif

// case12:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*addl.*
#if defined(__aarch64__)
__asm__ __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
            __asm__ __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
_asm_ __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__      __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__ volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__ __volatile(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__ __volatile__(  // expect: PythonInlineAsmIssue
                        LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i));
asm volatile(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
#endif

// case13:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*subl.*
#if defined(__aarch64__)
__asm__ __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
            __asm__ __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
_asm_ __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__      __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__ volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__ __volatile(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
__asm__ __volatile__(  // expect: PythonInlineAsmIssue
                        LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i));
asm volatile(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue
#endif

// case14:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*decl.*
#if defined(__aarch64__)
__asm__ __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
            __asm__ __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
_asm_ __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue 
asm__ __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__      __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__ volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__ __volatile(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__ __volatile__( // expect: PythonInlineAsmIssue
                        LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory");
asm volatile(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
#endif

// case15:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*incl.*
#if defined(__aarch64__)
__asm__ __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
            __asm__ __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
_asm_ __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__      __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__ volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__ __volatile(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
__asm__ __volatile__(   // expect: PythonInlineAsmIssue
                        LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory");
asm volatile(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue
#endif

// case16:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*xaddq.*
#if defined(__aarch64__)
__asm__ __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: PythonInlineAsmIssue
            __asm__ __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: PythonInlineAsmIssue
asm__ __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: PythonInlineAsmIssue
_asm_ __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: PythonInlineAsmIssue
asm__ __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: PythonInlineAsmIssue
__asm__      __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: PythonInlineAsmIssue
__asm__ volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: PythonInlineAsmIssue
__asm__ __volatile("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: PythonInlineAsmIssue
__asm__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: PythonInlineAsmIssue
__asm__ __volatile__(   // expect: PythonInlineAsmIssue
                        "lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i));
asm _volatile_("lock ; " "xaddq %0, %1;"   // expect: PythonInlineAsmIssue
:"=r"(i)  
:"m"(v->counter), "0"(i));
#endif

// case17:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*pcmpestrm.*
#if defined(__aarch64__)
__asm__ __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
            __asm__ __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
asm__ __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
_asm_ __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
asm__ __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
__asm__      __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
__asm__ volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
__asm__ __volatile("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
__asm__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
__asm__ __volatile__(  // expect: PythonInlineAsmIssue
                        "pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc");
#endif

// case18:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*pcmpestri.*
#if defined(__aarch64__)
__asm__ __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc");// expect: PythonInlineAsmIssue
            __asm__ __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
asm__ __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
_asm_ __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
asm__ __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
__asm__      __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc");// expect: PythonInlineAsmIssue
__asm__ volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
__asm__ __volatile("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
__asm__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: PythonInlineAsmIssue
__asm__ __volatile__ goto("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc");// expect: PythonInlineAsmIssue
__asm__ __volatile__(  // expect: PythonInlineAsmIssue
                        "pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc");
#endif

// case19:.*MOVDQU .*
#if defined(__aarch64__)
    __asm__ __volatile__(   // expect: PythonInlineAsmIssue
       "MOVDQU %1, %%xmm0\n\t"
       "MOVDQU %%xmm0, %0"
       :"=g"(sArrayB)
       :"x"(sArrayA)
       :"%xmm0"
    );
#endif

// case20:.* PAND .*
#if defined(__aarch64__)
    asm volatile("pand %0, s3, s4" : "=w"(sum) : :);   // expect: PythonInlineAsmIssue
#endif

// case21:.*Pxor .*,.*
#if defined(__aarch64__)
    asm volatile("PXOR %xmm0, %xmm0\n"  // expect: PythonInlineAsmIssue
                 "PXOR %xmm1, %xmm1\n"
                 "PXOR %xmm2, %xmm2\n"
                 "PXOR %xmm3, %xmm3\n"
                 "PXOR %xmm4, %xmm4\n"
                 "PXOR %xmm5, %xmm5\n"
                 "PXOR %xmm6, %xmm6\n"
                 "PXOR %xmm7, %xmm7\n"
                 "PXOR %xmm8, %xmm8\n"
                 "PXOR %xmm9, %xmm9\n"
                 "PXOR %xmm10, %xmm10\n"
                 "PXOR %xmm11, %xmm11\n"
                 "PXOR %xmm12, %xmm12\n"
                 "PXOR %xmm13, %xmm13\n"
                 "PXOR %xmm14, %xmm14\n"
                 "PXOR %xmm15, %xmm15\n");
#endif

// case22:.*PSHUFB .*,.*
#if defined(__aarch64__)
    asm volatile (   // expect: PythonInlineAsmIssue
        "movdqu     (%0),%%xmm1\n"
        "pshufb     %2,%%xmm1\n"
        "movdqu     %%xmm1,(%1)\n"
        :   "+r" (src),
            "+r" (dst),
            "+r" (map)
        :
        :   "memory", "cc", "xmm0", "xmm1", "xmm2", "xmm3", "xmm4"
);
#endif

        return a + b;
        }
""")


if __name__ == '__main__':
    ffi.compile(verbose=True)
