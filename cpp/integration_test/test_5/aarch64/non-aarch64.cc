// case1:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*memory.*
#if defined(__aarch64__)
__asm__ __volatile__("" : : : "memory"); // expect: InlineAsmIssue
   __asm__ __volatile__("" : : : "memory");// expect: InlineAsmIssue
asm__ __volatile__("" : : : "memory"); // expect: InlineAsmIssue
_asm_ __volatile__("" : : : "memory");// expect: InlineAsmIssue
__asm __volatile__("" : : : "memory");// expect: InlineAsmIssue
__asm__      __volatile__("" : : : "memory");// expect: InlineAsmIssue
__asm__ volatile__("" : : : "memory");// expect: InlineAsmIssue
__asm__ __volatile("" : : : "memory");// expect: InlineAsmIssue
__asm__("" : : : "memory");// expect: InlineAsmIssue
__asm__ __volatile__ goto("" : : : "memory");// expect: InlineAsmIssue
__asm__ __volatile__("" // expect: InlineAsmIssue
: : : "memory");
#endif

// case2:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*sfence.*
#if defined(__aarch64__)
__asm__ __volatile__("" : : : "sfence"); // expect: InlineAsmIssue
   __asm__ __volatile__("" : : : "sfence");// expect: InlineAsmIssue
asm__ __volatile__("" : : : "sfence"); // expect: InlineAsmIssue
_asm_ __volatile__("" : : : "sfence");// expect: InlineAsmIssue
__asm __volatile__("" : : : "sfence");// expect: InlineAsmIssue
__asm__      __volatile__("" : : : "sfence");// expect: InlineAsmIssue
__asm__ volatile__("" : : : "sfence");// expect: InlineAsmIssue
__asm__ __volatile("" : : : "sfence");// expect: InlineAsmIssue
__asm__("" : : : "sfence");// expect: InlineAsmIssue
__asm__ __volatile__ goto("" : : : "sfence");// expect: InlineAsmIssue
__asm__ __volatile__("" : : : // expect: InlineAsmIssue
                                "sfence");
#endif

// case3:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*lfence.*
#if defined(__aarch64__)
__asm__ __volatile__("" : : : "lfence"); // expect: InlineAsmIssue
   __asm__ __volatile__("" : : : "lfence");// expect: InlineAsmIssue
asm__ __volatile__("" : : : "lfence"); // expect: InlineAsmIssue
_asm_ __volatile__("" : : : "lfence");// expect: InlineAsmIssue
__asm __volatile__("" : : : "lfence");// expect: InlineAsmIssue
__asm__      __volatile__("" : : : "lfence");// expect: InlineAsmIssue
__asm__ volatile__("" : : : "lfence");// expect: InlineAsmIssue
__asm__ __volatile("" : : : "lfence");// expect: InlineAsmIssue
__asm__("" : : : "lfence");// expect: InlineAsmIssue
__asm__ __volatile__ goto("" : : : "lfence");// expect: InlineAsmIssue
__asm__ __volatile__("" : : : "lfence");// expect: InlineAsmIssue
__asm__ __volatile__("" : : : // expect: InlineAsmIssue
                                "lfence");
#endif

// case4:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*mfence.*
#if defined(__aarch64__)
__asm__ __volatile__("" : : : "mfence"); // expect: InlineAsmIssue
   __asm__ __volatile__("" : : : "mfence");// expect: InlineAsmIssue
asm__ __volatile__("" : : : "mfence"); // expect: InlineAsmIssue
_asm_ __volatile__("" : : : "mfence");// expect: InlineAsmIssue
__asm __volatile__("" : : : "mfence");// expect: InlineAsmIssue
__asm__      __volatile__("" : : : "mfence");// expect: InlineAsmIssue
__asm__ volatile__("" : : : "mfence");// expect: InlineAsmIssue
__asm__ __volatile("" : : : "mfence");// expect: InlineAsmIssue
__asm__("" : : : "mfence");// expect: InlineAsmIssue
__asm__ __volatile__ goto("" : : : "mfence");// expect: InlineAsmIssue
__asm__ __volatile__("" : : : // expect: InlineAsmIssue
                                "mfence");
#endif

// case5:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*crc32l.*
#if defined(__aarch64__)
__asm__ __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: InlineAsmIssue
    __asm__ __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: InlineAsmIssue
asm__ __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v)); // expect: InlineAsmIssue
_asm_ __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: InlineAsmIssue
asm__ __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: InlineAsmIssue
__asm__      __volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: InlineAsmIssue
__asm__ volatile__("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: InlineAsmIssue
__asm__ __volatile("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: InlineAsmIssue
__asm__("crc32l %1, %0" : "+r"(crc) : "rm"(v)); // expect: InlineAsmIssue
__asm__ __volatile__ goto("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue
                        "crc32l %1, %0" : "+r"(crc) : "rm"(v));
#endif

// case6:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*crc32q.*
#if defined(__aarch64__)
__asm__ __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: InlineAsmIssue
    __asm__ __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: InlineAsmIssue
asm__ __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v)); // expect: InlineAsmIssue
_asm_ __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: InlineAsmIssue
asm__ __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: InlineAsmIssue
__asm__      __volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: InlineAsmIssue
__asm__ volatile__("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: InlineAsmIssue
__asm__ __volatile("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: InlineAsmIssue
__asm__("crc32q %1, %0" : "+r"(result) : "rm"(v)); // expect: InlineAsmIssue
__asm__ __volatile__ goto("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue
                        "crc32q %1, %0" : "+r"(result) : "rm"(v));
#endif

// case7:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*bswap.*
#if defined(__aarch64__)
__asm__ __volatile__("bswap %0" : "=r" (val) : "0" (val)); // expect: InlineAsmIssue
    __asm__ __volatile__("bswap %0" : "=r" (val) : "0" (val)); // expect: InlineAsmIssue
asm__ __volatile__("bswap %0" : "=r" (val) : "0" (val)); // expect: InlineAsmIssue
_asm_ __volatile__("bswap %0" : "=r" (val) : "0" (val));// expect: InlineAsmIssue
asm__ __volatile__("bswap %0" : "=r" (val) : "0" (val));// expect: InlineAsmIssue
__asm__      __volatile__("bswap %0" : "=r" (val) : "0" (val)); // expect: InlineAsmIssue
__asm__ volatile__("bswap %0" : "=r" (val) : "0" (val));// expect: InlineAsmIssue
__asm__ __volatile("bswap %0" : "=r" (val) : "0" (val));// expect: InlineAsmIssue
__asm__("bswap %0" : "=r" (val) : "0" (val)); // expect: InlineAsmIssue
__asm__ __volatile__ goto("bswap %0" : "=r" (val) : "0" (val));// expect: InlineAsmIssue
__asm__ __volatile__ // expect: InlineAsmIssue
    ("bswap %0" : "=r" (val) : "0" (val));
#endif

#if defined(__aarch64__) // case8:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*rep.*
__asm__ __volatile__ // expect: InlineAsmIssue
("rep;nop"
    ::: "memory");
#define nop __asm__ __volatile__("rep;nop" ::: "memory"); // expect: InlineAsmIssue
asm__ __volatile__("rep;nop" ::: "memory");// expect: InlineAsmIssue
_asm_ __volatile__("rep;nop" ::: "memory");// expect: InlineAsmIssue
asm__ __volatile__("rep;nop" ::: "memory");// expect: InlineAsmIssue
__asm__      __volatile__("rep;nop" ::: "memory");// expect: InlineAsmIssue
__asm__ volatile__("rep;nop" ::: "memory");// expect: InlineAsmIssue
__asm__ __volatile("rep;nop" ::: "memory");// expect: InlineAsmIssue
__asm__("rep;nop" ::: "memory"); // expect: InlineAsmIssue
__asm__ __volatile__ goto("rep;nop" ::: "memory");// expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue
                        "rep;nop" ::: "memory");
int main()
{
    unsigned int var_1 = 0;
    unsigned int var_2 = 999;
    unsigned int var_3 = 0;

    __asm__ __volatile__ // expect: InlineAsmIssue
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
__asm__ __volatile__( // expect: InlineAsmIssue
"pause" ::: "memory");
            __asm__ __volatile__("pause" ::: "memory"); // expect: InlineAsmIssue
asm__ __volatile__("pause" ::: "memory"); // expect: InlineAsmIssue
_asm_ __volatile__("pause" ::: "memory");// expect: InlineAsmIssue
asm__ __volatile__("pause" ::: "memory");// expect: InlineAsmIssue
__asm__      __volatile__("pause" ::: "memory");// expect: InlineAsmIssue
__asm__ volatile__("pause" ::: "memory");// expect: InlineAsmIssue
__asm__ __volatile("pause" ::: "memory");// expect: InlineAsmIssue
__asm__("pause" ::: "memory"); // expect: InlineAsmIssue
__asm__ __volatile__ goto("pause" ::: "memory");// expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue
                        "pause" ::: "memory");
#endif

// case10:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*rdtsc.*
#if defined(__aarch64__)
__asm__ __volatile__("rdtsc" : "=a" (lo), "=d" (hi)); // expect: InlineAsmIssue
            __asm__ __volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: InlineAsmIssue
asm__ __volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: InlineAsmIssue
_asm_ __volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: InlineAsmIssue
asm__ __volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: InlineAsmIssue
__asm__      __volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: InlineAsmIssue
__asm__ volatile__("rdtsc" : "=a" (lo), "=d" (hi));// expect: InlineAsmIssue
__asm__ __volatile("rdtsc" : "=a" (lo), "=d" (hi));// expect: InlineAsmIssue
__asm__("rdtsc" : "=a" (lo), "=d" (hi)); // expect: InlineAsmIssue
__asm__ __volatile__ goto("rdtsc" : "=a" (lo), "=d" (hi));// expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue
                        "rdtsc" : "=a" (lo), "=d" (hi));
#endif

 // case11:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*popcntq.*
#if defined(__aarch64__)
__asm__ __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: InlineAsmIssue
            __asm__ __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: InlineAsmIssue
asm__ __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: InlineAsmIssue
_asm_ __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: InlineAsmIssue
asm__ __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: InlineAsmIssue
__asm__      __volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: InlineAsmIssue
__asm__ volatile__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: InlineAsmIssue
__asm__ __volatile("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: InlineAsmIssue
__asm__("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: InlineAsmIssue
__asm__ __volatile__ goto("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue
                        "popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); 
#endif

// case12:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*addl.*
#if defined(__aarch64__)
__asm__ __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
            __asm__ __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
_asm_ __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__      __volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__ volatile__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__ __volatile(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__ __volatile__ goto(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue
                        LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i));            
asm volatile(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
#endif

// case13:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*subl.*
#if defined(__aarch64__)
__asm__ __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
            __asm__ __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
_asm_ __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__      __volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__ volatile__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__ __volatile(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__ __volatile__ goto(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue
                        LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i));                   
asm volatile(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: InlineAsmIssue
#endif

// case14:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*decl.*
#if defined(__aarch64__)
__asm__ __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
            __asm__ __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
_asm_ __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue 
asm__ __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__      __volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__ volatile__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__ __volatile(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__ __volatile__ goto(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue 
                        LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); 
asm volatile(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
#endif

// case15:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*incl.*
#if defined(__aarch64__)
__asm__ __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
            __asm__ __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
_asm_ __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
asm__ __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__      __volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__ volatile__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__ __volatile(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__ __volatile__ goto(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
__asm__ __volatile__( // expect: InlineAsmIssue
                        LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory");  
asm volatile(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: InlineAsmIssue
#endif

// case16:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*xaddq.*
#if defined(__aarch64__)
__asm__ __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: InlineAsmIssue
            __asm__ __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: InlineAsmIssue
asm__ __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: InlineAsmIssue
_asm_ __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: InlineAsmIssue
asm__ __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: InlineAsmIssue
__asm__      __volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: InlineAsmIssue
__asm__ volatile__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: InlineAsmIssue
__asm__ __volatile("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: InlineAsmIssue
__asm__("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: InlineAsmIssue
__asm__ __volatile__ goto("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue
                        "lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i));   
asm _volatile_("lock ; " "xaddq %0, %1;" // expect: InlineAsmIssue
:"=r"(i)  
:"m"(v->counter), "0"(i));
#endif

// case17:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*pcmpestrm.*
#if defined(__aarch64__)
__asm__ __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
            __asm__ __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
asm__ __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
_asm_ __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
asm__ __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
__asm__      __volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
__asm__ volatile__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
__asm__ __volatile("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
__asm__("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
__asm__ __volatile__ goto("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue
                        "pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); 
#endif

// case18:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*pcmpestri.*
#if defined(__aarch64__)
__asm__ __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc");// expect: InlineAsmIssue
            __asm__ __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
asm__ __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
_asm_ __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
asm__ __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
__asm__      __volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc");// expect: InlineAsmIssue
__asm__ volatile__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
__asm__ __volatile("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
__asm__("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: InlineAsmIssue
__asm__ __volatile__ goto("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc");// expect: InlineAsmIssue
__asm__ __volatile__(// expect: InlineAsmIssue
                        "pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc");  
#endif

// case19:.*MOVDQU .*
#if defined(__aarch64__)
    __asm__ __volatile__( // expect: InlineAsmIssue
       "MOVDQU %1, %%xmm0\n\t"
       "MOVDQU %%xmm0, %0"
       :"=g"(sArrayB)
       :"x"(sArrayA)
       :"%xmm0"
    );
#endif

// case20:.* PAND .*
#if defined(__aarch64__)
    asm volatile("pand %0, s3, s4" : "=w"(sum) : :);   // expect: InlineAsmIssue
#endif

// case21:.*Pxor .*,.*
#if defined(__aarch64__)
    asm volatile("PXOR %xmm0, %xmm0\n"                // expect: InlineAsmIssue
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
    asm volatile ( // expect: InlineAsmIssue
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