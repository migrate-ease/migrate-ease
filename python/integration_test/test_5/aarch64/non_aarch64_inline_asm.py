import cffi

ffi = cffi.FFI()

ffi.set_source('_ext', r"""
    int add(int a, int b)
    {
        // case1:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*memory.*
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

        // case2:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*sfence.*
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
        __asm__ __volatile__("" : : : // expect: PythonInlineAsmIssue
                                        "sfence");

        // case3:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*lfence.*
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
        __asm__ __volatile__("" : : : // expect: PythonInlineAsmIssue
                                    "lfence");

        // case4:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*mfence.*
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
        __asm__ __volatile__("" : : : // expect: PythonInlineAsmIssue
                                        "mfence");

        // case5:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*crc32b.*
__asm__ __volatile__("crc32b %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        __asm__ __volatile__("crc32b %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        asm__ __volatile__("crc32b %1, %0" : "+r"(crc) : "rm"(v)); // expect: PythonInlineAsmIssue
        _asm_ __volatile__("crc32b %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        asm__ __volatile__("crc32b %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        __asm__      __volatile__("crc32b %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        __asm__ volatile__("crc32b %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        __asm__ __volatile("crc32b %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        __asm__("crc32b %1, %0" : "+r"(crc) : "rm"(v)); // expect: PythonInlineAsmIssue
        __asm__ __volatile__ goto("crc32b %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        __asm__ __volatile__(                              // expect: PythonInlineAsmIssue
                                "crc32b %1, %0" : "+r"(crc) : "rm"(v));

        // case6:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*crc32w.*
__asm__ __volatile__("crc32w %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        __asm__ __volatile__("crc32w %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        asm__ __volatile__("crc32w %1, %0" : "+r"(crc) : "rm"(v)); // expect: PythonInlineAsmIssue
        _asm_ __volatile__("crc32w %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        asm__ __volatile__("crc32w %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        __asm__      __volatile__("crc32w %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        __asm__ volatile__("crc32w %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        __asm__ __volatile("crc32w %1, %0" : "+r"(crc) : "rm"(v));// expect: PythonInlineAsmIssue
        __asm__("crc32w %1, %0" : "+r"(crc) : "rm"(v)); // expect: PythonInlineAsmIssue
        __asm__ __volatile__ goto("crc32w %1, %0" : "+r"(crc) : "rm"(v)); // expect: PythonInlineAsmIssue
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                "crc32w %1, %0" : "+r"(crc) : "rm"(v));

        // case7:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*crc32l.*
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
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                "crc32l %1, %0" : "+r"(crc) : "rm"(v));

        // case8:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*crc32q.*
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
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                "crc32q %1, %0" : "+r"(result) : "rm"(v));

        // case9:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*bswap.*
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
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                "bswap %0" : "=r" (val) : "0" (val));

        // case10:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*rep.*
__asm__ __volatile__("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
        __asm__ __volatile__("rep;nop" ::: "memory"); // expect: PythonInlineAsmIssue
        asm__ __volatile__("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
        _asm_ __volatile__("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
        asm__ __volatile__("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
        __asm__      __volatile__("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
        __asm__ volatile__("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
        __asm__ __volatile("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
        __asm__("rep;nop" ::: "memory"); // expect: PythonInlineAsmIssue
        __asm__ __volatile__ goto("rep;nop" ::: "memory");// expect: PythonInlineAsmIssue
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                "rep;nop" ::: "memory");


        // case11:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*pause.*
__asm__ __volatile__("pause" ::: "memory"); // expect: PythonInlineAsmIssue
        __asm__ __volatile__("pause" ::: "memory"); // expect: PythonInlineAsmIssue
        asm__ __volatile__("pause" ::: "memory"); // expect: PythonInlineAsmIssue
        _asm_ __volatile__("pause" ::: "memory");// expect: PythonInlineAsmIssue
        asm__ __volatile__("pause" ::: "memory");// expect: PythonInlineAsmIssue
        __asm__      __volatile__("pause" ::: "memory");// expect: PythonInlineAsmIssue
        __asm__ volatile__("pause" ::: "memory");// expect: PythonInlineAsmIssue
        __asm__ __volatile("pause" ::: "memory");// expect: PythonInlineAsmIssue
        __asm__("pause" ::: "memory"); // expect: PythonInlineAsmIssue
        __asm__ __volatile__ goto("pause" ::: "memory");// expect: PythonInlineAsmIssue
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                "pause" ::: "memory");

        // case12:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*rdtsc.*
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
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                "rdtsc" : "=a" (lo), "=d" (hi));

        // case13:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*popcntq.*
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
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                "popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); 

        // case14:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*addl.*
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
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i));            
        asm volatile(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue

        // case15:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*subl.*
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
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i));                   
        asm volatile(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: PythonInlineAsmIssue  

        // case16:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*decl.*
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
        __asm__ __volatile__(// expect: PythonInlineAsmIssue 
                                LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); 
        asm volatile(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue

        // case17:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*incl.*
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
        __asm__ __volatile__( // expect: PythonInlineAsmIssue
                                LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory");  
        asm volatile(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: PythonInlineAsmIssue

        // case18:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*xaddq.*
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
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                "lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i));   
        asm _volatile_("lock ; " "xaddq %0, %1;" // expect: PythonInlineAsmIssue
        :"=r"(i)  
        :"m"(v->counter), "0"(i));

        // case19:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*pcmpestrm.*
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
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                "pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); 

        // case20:(^|\s)([_]*asm[_]*)(\s+[_]*volatile[_]*)?(\s+goto)?\(.*(?:\n|\r\n)*.*pcmpestri.*
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
        __asm__ __volatile__(// expect: PythonInlineAsmIssue
                                "pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc");  

        // case21:.*MOVDQU .*
        __asm__ __volatile__( // expect: PythonInlineAsmIssue
        "MOVDQU %1, %%xmm0\n\t"
        "MOVDQU %%xmm0, %0"
        :"=g"(sArrayB)
        :"x"(sArrayA)
        :"%xmm0"
        );

        // case22:.* PAND .*
        asm volatile("pand %0, s3, s4" : "=w"(sum) : :);   // expect: PythonInlineAsmIssue

        // case23:.*Pxor .*,.*
        asm volatile("PXOR %xmm0, %xmm0\n"                // expect: PythonInlineAsmIssue
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

        // case24:.*PSHUFB .*,.*
        asm volatile ( // expect: PythonInlineAsmIssue
                "movdqu     (%0),%%xmm1\n"
                "pshufb     %2,%%xmm1\n"
                "movdqu     %%xmm1,(%1)\n"
                :   "+r" (src),
                "+r" (dst),
                "+r" (map)
                :
                :   "memory", "cc", "xmm0", "xmm1", "xmm2", "xmm3", "xmm4"
        );

        return a + b;
        }
""")

ffi.cdef("""int add(int a, int b);""")

if __name__ == '__main__':
    ffi.compile(verbose=True)