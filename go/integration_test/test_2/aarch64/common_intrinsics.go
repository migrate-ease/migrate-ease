package main

/*
#include <stdio.h>

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


void printInt(int v) {
    printf("printint: %d\n", v);
}
*/
import "C"

func main() {
    v := 42
    C.printInt(C.int(v))
}