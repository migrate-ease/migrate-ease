// Set the warning level to L1, the tool will check branches in SUPPORTED state.
// start of common test for gcc.
#if defined(__x86__) || defined(__ATOMIC_RELEASE)
#include <emmintrin.h>       //expect: IncompatibleHeaderFileIssue
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val)); //expect: InlineAsmIssue
#error not implement    //expect: PreprocessorErrorIssue
#pragma simd    //expect: PragmaIssue
#endif

#if defined(__x86__) && defined(__ATOMIC_RELEASE)
#include <emmintrin.h>
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#error not implement
#pragma simd
#endif

#ifdef __ATOMIC_RELEASE
#if __ARM_FP > 10
#include <emmintrin.h>  //expect: IncompatibleHeaderFileIssue
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));  //expect: InlineAsmIssue
#error not implement //expect: PreprocessorErrorIssue
#pragma simd //expect: PragmaIssue
#else
#include <emmintrin.h>
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#error not implement
#pragma simd
#endif
#endif

#if A || defined(__aarch64__)
#include <emmintrin.h>       //expect: IncompatibleHeaderFileIssue
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));  //expect: InlineAsmIssue
#error not implement  //expect: PreprocessorErrorIssue
#pragma simd  //expect: PragmaIssue
#endif

#if A && defined(__aarch64__)
#include <emmintrin.h>
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#error not implement
#pragma simd
#endif

#ifdef A
#if __ARM_FP > 10
#include <emmintrin.h>
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#error not implement
#pragma simd
#else
#include <emmintrin.h>
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#error not implement
#pragma simd
#endif
#endif
// end of common test for gcc.

// start of gcc specific tests.
#ifdef __ARM_ALIGN_MAX_PWR
#ifdef __ARM_ARCH_8A
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val)); //expect: InlineAsmIssue
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif

#ifdef __ARM_NEON_FP
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));  //expect: InlineAsmIssue
#endif

#ifdef A
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val)); //expect: InlineAsmIssue
#endif

#ifdef _WIN32
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));  //expect: InlineAsmIssue
#endif
#endif

#ifdef __CLANG_ATOMIC_BOOL_LOCK_FREE
#ifdef __ARM_ARCH_8A
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif

#ifdef __ARM_NEON_FP
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif

#ifdef A
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif

#ifdef _WIN32
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif
#endif

// ABC is an unknown macro.
#ifdef ABC
#ifdef __ARM_ARCH_8A
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif

#ifdef __ARM_NEON_FP
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif

#ifdef A
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif

#ifdef _WIN32
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif
#endif

// _MSC_VER_ is not supported by gcc.
#ifdef _MSC_VER_
#ifdef __ARM_ARCH_8A
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif

#ifdef __ARM_NEON_FP
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif

#ifdef A
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif

#ifdef _WIN32
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#else
__asm__ volatile("crc32l %w0, %w0, %w1" : "+r"(crc) : "r"(val));
#endif
#endif
//end of gcc specific tests.