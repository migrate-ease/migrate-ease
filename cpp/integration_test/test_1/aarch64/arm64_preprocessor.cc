/*
 * 1. Test non-arm arch specific macros
 * 2. test #error preprocessor directive
 */
#if defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (aarch64) test FAILED!!"
#endif

#if defined(_aarch64_)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (aarch64) test FAILED!!"
#endif

#if defined(__aarch64__)
#error "macro (sw64) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (aarch64) test FAILED!!"
#else
#error "macro (aarch64) test FAILED!!"
#endif

#if defined(arm64)
#error "macro (arm64) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (arm64) test FAILED!!"
#endif

#if defined(_arm64_)
#error "macro (arm64) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (arm64) test FAILED!!"
#endif

#if defined(__arm64__)
#error "macro (arm64) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (arm64) test FAILED!!"
#endif

#if defined(arm)
#error "macro (arm) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (arm) test FAILED!!"
#endif

#if defined(_arm_)
#error "macro (arm) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (arm) test FAILED!!"
#endif

#if defined(__arm__)
#error "macro (arm) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (arm) test FAILED!!"
#endif

#if defined(neon)
#error "macro (neon) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (neon) test FAILED!!"
#endif

#if defined(_neon_)
#error "macro (neon) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (neon) test FAILED!!"
#endif

#if defined(__neon__)
#error "macro (neon) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (neon) test FAILED!!"
#endif

#if defined(sve)
#error "macro (sve) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (sve) test FAILED!!"
#endif

#if defined(_sve_)
#error "macro (sve) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (sve) test FAILED!!"
#endif

#if defined(__sve__)
#error "macro (sve) test PASSED!!" //expect: PreprocessorErrorIssue
#elif defined(sw64)
#error "macro (sw64) test FAILED!!"
#else
#error "macro (sve) test FAILED!!"
#endif

#if defined(alpha)
#error "macro (alpha) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (alpha) test FAILED!!"
#endif

#if defined(_alpha_)
#error "macro (alpha) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (alpha) test FAILED!!"
#endif

#if defined(__alpha__)
#error "macro (alpha) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (alpha) test FAILED!!"
#endif

#if defined(altivec)
#error "macro (altivec) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (altivec) test FAILED!!"
#endif

#if defined(_altivec_)
#error "macro (altivec) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (altivec) test FAILED!!"
#endif

#if defined(__altivec__)
#error "macro (altivec) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (altivec) test FAILED!!"
#endif

#if defined(amd64)
#error "macro (amd64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (amd64) test FAILED!!"
#endif

#if defined(_amd64_)
#error "macro (amd64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (amd64) test FAILED!!"
#endif

#if defined(__amd64__)
#error "macro (amd64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (amd64) test FAILED!!"
#endif

#if defined(avx)
#error "macro (avx) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (avx) test FAILED!!"
#endif

#if defined(_avx_)
#error "macro (avx) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (avx) test FAILED!!"
#endif

#if defined(__avx__)
#error "macro (avx) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (avx) test FAILED!!"
#endif

#if defined(avx512)
#error "macro (avx512) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (avx512) test FAILED!!"
#endif

#if defined(_avx512_)
#error "macro (avx512) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (avx512) test FAILED!!"
#endif

#if defined(__avx512__)
#error "macro (avx512) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (avx512) test FAILED!!"
#endif

#if defined(hppa)
#error "macro (hppa) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (hppa) test FAILED!!"
#endif

#if defined(_hppa_)
#error "macro (hppa) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (hppa) test FAILED!!"
#endif

#if defined(__hppa__)
#error "macro (hppa) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (hppa) test FAILED!!"
#endif

#if defined(i386)
#error "macro (i386) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i386) test FAILED!!"
#endif

#if defined(_i386_)
#error "macro (i386) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i386) test FAILED!!"
#endif

#if defined(__i386__)
#error "macro (i386) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i386) test FAILED!!"
#endif

#if defined(i586)
#error "macro (i586) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i586) test FAILED!!"
#endif

#if defined(_i586_)
#error "macro (i586) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i586) test FAILED!!"
#endif

#if defined(__i586__)
#error "macro (i586) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i586) test FAILED!!"
#endif

#if defined(i686)
#error "macro (i686) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i686) test FAILED!!"
#endif

#if defined(_i686_)
#error "macro (i686) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i686) test FAILED!!"
#endif

#if defined(__i686__)
#error "macro (i686) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i686) test FAILED!!"
#endif

#if defined(ia64)
#error "macro (ia64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ia64) test FAILED!!"
#endif

#if defined(_ia64_)
#error "macro (ia64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ia64) test FAILED!!"
#endif

#if defined(__ia64__)
#error "macro (ia64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ia64) test FAILED!!"
#endif

#if defined(intel)
#error "macro (intel) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue 
#else
#error "macro (intel) test FAILED!!"
#endif

#if defined(_intel_)
#error "macro (intel) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (intel) test FAILED!!"
#endif

#if defined(__intel__)
#error "macro (intel) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (intel) test FAILED!!"
#endif

#if defined(intel64)
#error "macro (intel64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (intel64) test FAILED!!"
#endif

#if defined(_intel64_)
#error "macro (intel64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (intel64) test FAILED!!"
#endif

#if defined(__intel64__)
#error "macro (intel64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (intel64) test FAILED!!"
#endif

#if defined(ix86)
#error "macro (ix86) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ix86) test FAILED!!"
#endif


#if defined(_ix86_)
#error "macro (ix86) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ix86) test FAILED!!"
#endif

#if defined(__ix86__)
#error "macro (ix86) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ix86) test FAILED!!"
#endif

#if defined(m68k)
#error "macro (m68k) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (m68k) test FAILED!!"
#endif

#if defined(_m68k_)
#error "macro (m68k) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (m68k) test FAILED!!"
#endif

#if defined(__m68k__)
#error "macro (m68k) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (m68k) test FAILED!!"
#endif

#if defined(microblaze)
#error "macro (microblaze) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (microblaze) test FAILED!!"
#endif

#if defined(_microblaze_)
#error "macro (microblaze) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (microblaze) test FAILED!!"
#endif

#if defined(__microblaze__)
#error "macro (microblaze) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (microblaze) test FAILED!!"
#endif

#if defined(mips)
#error "macro (mips) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (mips) test FAILED!!"
#endif

#if defined(_mips_)
#error "macro (mips) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (mips) test FAILED!!"
#endif

#if defined(__mips__)
#error "macro (mips) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (mips) test FAILED!!"
#endif

#if defined(nios2)
#error "macro (nios2) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (nios2) test FAILED!!"
#endif

#if defined(_nios2_)
#error "macro (nios2) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (nios2) test FAILED!!"
#endif

#if defined(__nios2__)
#error "macro (nios2) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (nios2) test FAILED!!"
#endif

#if defined(otherarch)
#error "macro (otherarch) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (otherarch) test FAILED!!"
#endif

#if defined(_otherarch_)
#error "macro (otherarch) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (otherarch) test FAILED!!"
#endif

#if defined(__otherarch__)
#error "macro (otherarch) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (otherarch) test FAILED!!"
#endif

#if defined(power)
#error "macro (power) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (power) test FAILED!!"
#endif

#if defined(_power_)
#error "macro (power) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (power) test FAILED!!"
#endif

#if defined(__power__)
#error "macro (power) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (power) test FAILED!!"
#endif

#if defined(powerpc)
#error "macro (powerpc) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (powerpc) test FAILED!!"
#endif

#if defined(_powerpc_)
#error "macro (powerpc) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (powerpc) test FAILED!!"
#endif

#if defined(__powerpc__)
#error "macro (powerpc) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (powerpc) test FAILED!!"
#endif

#if defined(powerpc32)
#error "macro (powerpc32) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (powerpc32) test FAILED!!"
#endif

#if defined(_powerpc32_)
#error "macro (powerpc32) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (powerpc32) test FAILED!!"
#endif

#if defined(__powerpc32__)
#error "macro (powerpc32) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (powerpc32) test FAILED!!"
#endif

#if defined(powerpc64)
#error "macro (powerpc64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (powerpc64) test FAILED!!"
#endif

#if defined(_powerpc64_)
#error "macro (powerpc64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else 
#error "macro (powerpc64) test FAILED!!"
#endif

#if defined(__powerpc64__)
#error "macro (powerpc64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (powerpc64) test FAILED!!"
#endif

#if defined(ppc64le)
#error "macro (ppc64le) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc64le) test FAILED!!"
#endif

#if defined(_ppc64le_)
#error "macro (ppc64le) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc64le) test FAILED!!"
#endif

#if defined(__ppc64le__)
#error "macro (ppc64le) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc64le) test FAILED!!"
#endif

#if defined(ppc64)
#error "macro (ppc64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc64) test FAILED!!"
#endif

#if defined(_ppc64_)
#error "macro (ppc64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc64) test FAILED!!"
#endif

#if defined(__ppc64__)
#error "macro (ppc64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc64) test FAILED!!"
#endif

#if defined(ppc)
#error "macro (ppc) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc) test FAILED!!"
#endif

#if defined(_ppc_)
#error "macro (ppc) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc) test FAILED!!"
#endif

#if defined(__ppc__)
#error "macro (ppc) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc) test FAILED!!"
#endif

#if defined(s390)
#error "macro (s390) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (s390) test FAILED!!"
#endif

#if defined(_s390_)
#error "macro (s390) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (s390) test FAILED!!"
#endif

#if defined(__s390__)
#error "macro (s390) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (s390) test FAILED!!"
#endif

#if defined(sh)
#error "macro (sh) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sh) test FAILED!!"
#endif

#if defined(_sh_)
#error "macro (sh) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sh) test FAILED!!"
#endif

#if defined(__sh__)
#error "macro (sh) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sh) test FAILED!!"
#endif

#if defined(sparc)
#error "macro (sparc) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!"  //expect: PreprocessorErrorIssue
#else
#error "macro (sparc) test FAILED!!"
#endif

#if defined(_sparc_)
#error "macro (sparc) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sparc) test FAILED!!"
#endif

#if defined(__sparc__)
#error "macro (sparc) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sparc) test FAILED!!"
#endif

#if defined(sse3)
#error "macro (sse3) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse3) test FAILED!!"
#endif

#if defined(_sse3_)
#error "macro (sse3) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse3) test FAILED!!"
#endif

#if defined(__sse3__)
#error "macro (sse3) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse3) test FAILED!!"
#endif

#if defined(sse2)
#error "macro (sse2) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse2) test FAILED!!"
#endif

#if defined(_sse2_)
#error "macro (sse2) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse2) test FAILED!!"
#endif

#if defined(__sse2__)
#error "macro (sse2) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse2) test FAILED!!"
#endif

#if defined(sse)
#error "macro (sse) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse) test FAILED!!"
#endif

#if defined(_sse_)
#error "macro (sse) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse) test FAILED!!"
#endif

#if defined(__sse__)
#error "macro (sse) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse) test FAILED!!"
#endif

#if defined(tile)
#error "macro (tile) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (tile) test FAILED!!"
#endif

#if defined(_tile_)
#error "macro (tile) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (tile) test FAILED!!"
#endif

#if defined(__tile__)
#error "macro (tile) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (tile) test FAILED!!"
#endif

#if defined(x64)
#error "macro (x64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (x64) test FAILED!!"
#endif

#if defined(_x64_)
#error "macro (x64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (x64) test FAILED!!"
#endif

#if defined(__x64__)
#error "macro (x64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (x64) test FAILED!!"
#endif

#if defined(x86)
#error "macro (x86) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (x86) test FAILED!!"
#endif

#if defined(_x86_)
#error "macro (x86) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (x86) test FAILED!!"
#endif

#if defined(__x86__)
#error "macro (x86) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (x86) test FAILED!!"
#endif

#if defined(x86_64)
#error "macro (x86_64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (x86_64) test FAILED!!"
#endif

#if defined(_x86_64_)
#error "macro (x86_64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (x86_64) test FAILED!!"
#endif

#if defined(__x86_64__)
#error "macro (x86_64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (x86_64) test FAILED!!"
#endif

#if defined(sw_64)
#error "macro (sw_64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw_64) test FAILED!!"
#endif

#if defined(_sw_64_)
#error "macro (sw_64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw_64) test FAILED!!"
#endif

#if defined(__sw_64__)
#error "macro (sw_64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw_64) test FAILED!!"
#endif

#if defined(sw64)
#error "macro (sw64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw64) test FAILED!!"
#endif

#if defined(_sw64_)
#error "macro (sw64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw64) test FAILED!!"
#endif

#if defined(__sw64__)
#error "macro (sw64) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw64) test FAILED!!"
#endif

#if defined(sw)
#error "macro (sw) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw) test FAILED!!"
#endif

#if defined(_sw_)
#error "macro (sw) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw) test FAILED!!"
#endif

#if defined(__sw__)
#error "macro (sw) test FAILED!!"
#elif defined(aarch64)
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw) test FAILED!!"
#endif


#ifdef aarch64
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (aarch64) test FAILED!!"
#endif

#ifdef arm64
#error "macro (arm64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (arm64) test FAILED!!"
#endif

#ifdef arm
#error "macro (arm) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (arm) test FAILED!!"
#endif

#ifdef neon
#error "macro (neon) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (neon) test FAILED!!"
#endif

#ifdef sve
#error "macro (sve) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sve) test FAILED!!"
#endif

#ifdef sw_64
#error "macro (sw_64) test FAILED!!"
#else
#error "macro (sw_64) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef sw64
#error "macro (sw64) test FAILED!!"
#else
#error "macro (sw64) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef sw
#error "macro (sw) test FAILED!!"
#else
#error "macro (sw) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef alpha
#error "macro (alpha) test FAILED!!"
#else
#error "macro (alpha) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef altivec
#error "macro (altivec) test FAILED!!"
#else
#error "macro (altivec) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef amd64
#error "macro (amd64) test FAILED!!"
#else
#error "macro (amd64) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef avx
#error "macro (avx) test FAILED!!"
#else
#error "macro (avx) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef avx512
#error "macro (avx512) test FAILED!!"
#else
#error "macro (avx512) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef hppa
#error "macro (hppa) test FAILED!!"
#else
#error "macro (hppa) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef i386
#error "macro (i386) test FAILED!!"
#else
#error "macro (i386) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef i586
#error "macro (i586) test FAILED!!"
#else
#error "macro (i586) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef i686
#error "macro (i686) test FAILED!!"
#else
#error "macro (i686) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef ia64
#error "macro (ia64) test FAILED!!"
#else
#error "macro (ia64) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef intel
#error "macro (intel) test FAILED!!" 
#else
#error "macro (intel) test PASSED!!" // expect: PreprocessorErrorIssue
#endif

#ifdef intel64
#error "macro (intel64) test FAILED!!"
#else
#error "macro (intel64) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef ix86
#error "macro (ix86) test FAILED!!"
#else
#error "macro (ix86) test PASSED!!" //expect: PreprocessorErrorIssue
#endif 

#ifdef m68k
#error "macro (m68k) test FAILED!!"
#else
#error "macro (m68k) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef microblaze
#error "macro (microblaze) test FAILED!!"
#else
#error "macro (microblaze) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef mips
#error "macro (mips) test FAILED!!"
#else
#error "macro (mips) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef nios2
#error "macro (nios2) test FAILED!!"
#else
#error "macro (nios2) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef otherarch
#error "macro (otherarch) test FAILED!!"
#else
#error "macro (otherarch) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef power
#error "macro (power) test FAILED!!"
#else
#error "macro (power) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef powerpc
#error "macro (powerpc) test FAILED!!"
#else
#error "macro (powerpc) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef powerpc32
#error "macro (powerpc32) test FAILED!!"
#else
#error "macro (powerpc32) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef powerpc64
#error "macro (powerpc64) test FAILED!!"
#else
#error "macro (powerpc64) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef ppc64le
#error "macro (ppc64le) test FAILED!!"
#else
#error "macro (ppc64le) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef ppc64
#error "macro (ppc64) test FAILED!!"
#else
#error "macro (ppc64) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef ppc
#error "macro (ppc) test FAILED!!"
#else
#error "macro (ppc) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef s390
#error "macro (s390) test FAILED!!"
#else
#error "macro (s390) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef sh
#error "macro (sh) test FAILED!!"
#else
#error "macro (sh) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef sparc
#error "macro (sparc) test FAILED!!"
#else
#error "macro (sparc) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef sse3
#error "macro (sse3) test FAILED!!"
#else
#error "macro (sse3) test PASSED!!"  //expect: PreprocessorErrorIssue
#endif

#ifdef sse2
#error "macro (sse2) test FAILED!!"
#else
#error "macro (sse2) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef sse
#error "macro (sse) test FAILED!!"
#else
#error "macro (sse) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef tile
#error "macro (tile) test FAILED!!"
#else
#error "macro (tile) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef x64
#error "macro (x64) test FAILED!!"
#else
#error "macro (x64) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef x86
#error "macro (x86) test FAILED!!"
#else
#error "macro (x86) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifdef x86_64
#error "macro (x86_64) test FAILED!!"
#else
#error "macro x86_64) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifndef aarch64
#error "macro (aarch64) test FAILED!!"
#else
#error "macro (aarch64) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifndef arm64
#error "macro (arm64) test FAILED!!"
#else
#error "macro (arm64) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifndef arm
#error "macro (arm) test FAILED!!"
#else
#error "macro (arm) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifndef neon
#error "macro (neon) test FAILED!!"
#else
#error "macro (neon) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifndef sve
#error "macro (sve) test FAILED!!"
#else
#error "macro (sve) test PASSED!!" //expect: PreprocessorErrorIssue
#endif

#ifndef sw_64
#error "macro (sw_64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw_64) test FAILED!!"
#endif

#ifndef sw64
#error "macro (sw64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw64) test FAILED!!"
#endif

#ifndef sw
#error "macro (sw) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sw) test FAILED!!"
#endif

#ifndef alpha
#error "macro (alpha) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (alpha) test FAILED!!"
#endif

#ifndef altivec
#error "macro (altivec) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (altivec) test FAILED!!"
#endif

#ifndef amd64
#error "macro (amd64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (amd64) test FAILED!!"
#endif

#ifndef avx
#error "macro (avx) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (avx) test FAILED!!"
#endif

#ifndef avx512
#error "macro (avx512) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (avx512) test FAILED!!"
#endif

#ifndef hppa
#error "macro (hppa) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (hppa) test FAILED!!"
#endif

#ifndef i386
#error "macro (i386) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i386) test FAILED!!"
#endif

#ifndef i586
#error "macro (i586) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i586) test FAILED!!"
#endif

#ifndef i686
#error "macro (i686) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (i686) test FAILED!!"
#endif

#ifndef ia64
#error "macro (ia64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ia64) test FAILED!!"
#endif

#ifndef intel
#error "macro (intel) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (intel) test FAILED!!"
#endif

#ifndef intel64
#error "macro (intel64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (intel64) test FAILED!!"
#endif

#ifndef ix86
#error "macro (ix86) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ix86) test FAILED!!"
#endif

#ifndef m68k
#error "macro (m68k) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (m68k) test FAILED!!"
#endif

#ifndef microblaze
#error "macro (microblaze) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (microblaze) test FAILED!!"
#endif

#ifndef mips
#error "macro (mips) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (mips) test FAILED!!"
#endif

#ifndef nios2
#error "macro (nios2) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (nios2) test FAILED!!"
#endif

#ifndef otherarch
#error "macro (otherarch) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (otherarch) test FAILED!!"
#endif

#ifndef power
#error "macro (power) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (power) test FAILED!!"
#endif

#ifndef powerpc
#error "macro (powerpc) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (powerpc) test FAILED!!"
#endif

#ifndef powerpc32
#error "macro (powerpc32) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (powerpc32) test FAILED!!"
#endif

#ifndef powerpc64
#error "macro (powerpc64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (powerpc64) test FAILED!!"
#endif

#ifndef ppc64le
#error "macro (ppc64le) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc64le) test FAILED!!"
#endif

#ifndef ppc64
#error "macro (ppc64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc64) test FAILED!!"
#endif

#ifndef ppc
#error "macro (ppc) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (ppc) test FAILED!!"
#endif

#ifndef s390
#error "macro (s390) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (s390) test FAILED!!"
#endif

#ifndef sh
#error "macro (sh) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sh) test FAILED!!"
#endif

#ifndef sparc
#error "macro (sparc) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sparc) test FAILED!!"
#endif

#ifndef sse3
#error "macro (sse3) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse3) test FAILED!!"
#endif

#ifndef sse2
#error "macro (sse2) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse2) test FAILED!!"
#endif

#ifndef sse
#error "macro (sse) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (sse) test FAILED!!"
#endif

#ifndef tile
#error "macro (tile) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (tile) test FAILED!!"
#endif

#ifndef x64
#error "macro (x64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (x64) test FAILED!!"
#endif

#ifndef x86
#error "macro (x86) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro (x86) test FAILED!!"
#endif

#ifndef x86_64
#error "macro (x86_64) test PASSED!!" //expect: PreprocessorErrorIssue
#else
#error "macro x86_64) test FAILED!!"
#endif

