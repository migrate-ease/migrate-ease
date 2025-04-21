import cffi

ffi = cffi.FFI()

ffi.set_source('_ext', r"""
    int add(int a, int b)
    {
        #if defined(aarch64)
        #define barrier() __sync_synchronize()
        __asm__ __volatile__("dmb ish" : : : "memory"); 
        #endif

        #if defined(aarch64)
        __asm__ __volatile__("dmb ishst" : : : "memory");
        #endif

        #if defined(aarch64)
        __asm__ __volatile__("dmb ishld" : : : "memory");
        #endif

        #if defined(aarch64)
        __asm__ __volatile__("crc32cb %w[c], %w[c], %w[v]":[c]"+r"(crc):[v]"r"(value));
        #endif

        #if defined(aarch64)
        __asm__ __volatile__("crc32ch %w[c], %w[c], %w[v]":[c]"+r"(crc):[v]"r"(value));
        #endif

        #if defined(aarch64)
        __asm__ __volatile__("crc32cw %w[c], %w[c], %w[v]":[c]"+r"(crc):[v]"r"(value));
        #endif

        #if defined(aarch64)
        __asm__ __volatile__("crc32cx %w[c], %w[c], %x[v]":[c]"+r"(crc):[v]"r"(value));
        #endif

        #if defined(aarch64)
        __asm__("rev %w[dst], %w[src]" : [dst]"=r"(val) : [src]"r"(val));
        #endif

        #if defined(aarch64)
        #define __nops(n) ".rept " #n "\nnop\n.endr\n"
        #define nops(n) asm volatile(__nops(n))
        #endif

        #if defined(aarch64)
        __asm__ __volatile__("yield" : : : "memory");
        __asm__ __volatile__("yield");
        #endif

        #if defined(aarch64)
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

        #if defined(aarch64)
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

        #if defined(aarch64)
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

        #if defined(aarch64)
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

        #if defined(aarch64)
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

        #if defined(aarch64)
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

        #if defined(aarch64)
        static __inline__ long atomic64_add_and_return(long i, atomic64_t *v)
        {
        return __sync_add_and_fetch(&((v)->counter), i);
        }
        #endif

        #if defined(aarch64)
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
        // In Impala, the mode STRCHR_MODE = PCMPSTR_EQUAL_ANY | PCMPSTR_UBYTE_OPS is used.
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

        #if defined(aarch64)
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

        #if defined(aarch64)
        LDP Xt1, Xt2, addr
        STP Xt1, Xt2, addr
        #endif

        #if defined(aarch64)
        AND Vd.<T>, Vn.<T>, Vm.<T>
        #endif

        #if defined(aarch64)
        EOR Vd.<T>, Vn.<T>, Vm.<T>
        #endif

        #if defined(aarch64)
        TBL Vd.<T>, {Vn*.16B}, Vm.<T>2
        #endif
        
        return a + b;
        }
""")

ffi.cdef("""int add(int a, int b);""")

if __name__ == '__main__':
    ffi.compile(verbose=True)