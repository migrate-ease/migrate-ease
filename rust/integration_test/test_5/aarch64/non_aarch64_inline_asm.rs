#![feature(asm)]

#[cfg(any(target_arch = "x86", target_arch = "x86_64"))]
fn bswap(mut val: u32) -> u32
{
    unsafe {
        // case1:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*memory.*
        asm!("" : : : "memory");// expect: RustInlineAsmIssue
        global_asm!("" : : : "memory"); // expect: RustInlineAsmIssue

        // case2:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*sfence.*
        asm!("" : : : "sfence");// expect: RustInlineAsmIssue
        global_asm!("" : : : "sfence"); // expect: RustInlineAsmIssue

        // case3:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*lfence.*
        asm!("" : : : "lfence");// expect: RustInlineAsmIssue
        global_asm!("" : : : "lfence"); // expect: RustInlineAsmIssue

        // case4:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*mfence.*
        asm!("" : : : "mfence");// expect: RustInlineAsmIssue
        global_asm!("" : : : "mfence"); // expect: RustInlineAsmIssue

        // case5:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*crc32b.*
        asm!("crc32b %1, %0" : "+r"(crc) : "rm"(v));// expect: RustInlineAsmIssue
        global_asm!("crc32b %1, %0" : "+r"(crc) : "rm"(v));// expect: RustInlineAsmIssue

        // case6:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*crc32w.*
        asm!("crc32w %1, %0" : "+r"(crc) : "rm"(v));// expect: RustInlineAsmIssue
        global_asm!("crc32w %1, %0" : "+r"(crc) : "rm"(v));// expect: RustInlineAsmIssue

        // case7:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*crc32l.*
        asm!("crc32l %1, %0" : "+r"(crc) : "rm"(v));// expect: RustInlineAsmIssue

        // case8:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*crc32q.*
        asm!("crc32q %1, %0" : "+r"(result) : "rm"(v));// expect: RustInlineAsmIssue

        // case9:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*bswap.*
        asm!("bswap %0" : "=r" (val) : "0" (val)); // expect: RustInlineAsmIssue

        // case10:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*rep.*
        asm!("rep;nop" ::: "memory");// expect: RustInlineAsmIssue

        // case11:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*pause.*
        asm!("pause" ::: "memory"); // expect: RustInlineAsmIssue

        // case12:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*rdtsc.*
        asm!("rdtsc" : "=a" (lo), "=d" (hi)); // expect: RustInlineAsmIssue

        // case13:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*popcntq.*
        asm!("popcntq %1, %0" : "=r"(result) : "mr"(a) : "cc"); // expect: RustInlineAsmIssue

        // case14:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*addl.*
        asm!(LOCK_PREFIX "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: RustInlineAsmIssue

        // case15:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*subl.*
        asm!(LOCK_PREFIX "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: RustInlineAsmIssue

        // case16:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*decl.*
        asm!(LOCK_PREFIX "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: RustInlineAsmIssue

        // case17:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*incl.*
        asm!(LOCK_PREFIX "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: RustInlineAsmIssue

        // case18:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*xaddq.*
        asm!("lock ; " "xaddq %0, %1;" :"=r"(i)  :"m"(v->counter), "0"(i)); // expect: RustInlineAsmIssue

        // case19:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*pcmpestrm.*
        asm!("pcmpestrm %5, %2, %1": "=Yz"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc"); // expect: RustInlineAsmIssue

        // case20:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*pcmpestri.*
        asm!("pcmpestri %5, %2, %1": "=c"(result) : "x"(str1), "xm"(str2), "a"(len1), "d"(len2), "i"(MODE) : "cc");// expect: RustInlineAsmIssue

        // case21:.*MOVDQU .*
        asm!( // expect: RustInlineAsmIssue
                "MOVDQU %1, %%xmm0\n\t"
                "MOVDQU %%xmm0, %0"
                :"=g"(sArrayB)
                :"x"(sArrayA)
                :"%xmm0"
                );

        // case22:.* PAND .*
        asm!("pand %0, s3, s4" : "=w"(sum) : :);   // expect: RustInlineAsmIssue
        global_asm!("pand %0, s3, s4" : "=w"(sum) : :);   // expect: RustInlineAsmIssue

        // case23:.*Pxor .*,.*
        asm!("PXOR %xmm0, %xmm0\n"                // expect: RustInlineAsmIssue
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
        asm!( // expect: RustInlineAsmIssue
                        "movdqu     (%0),%%xmm1\n"
                        "pshufb     %2,%%xmm1\n"
                        "movdqu     %%xmm1,(%1)\n"
                        :   "+r" (src),
                        "+r" (dst),
                        "+r" (map)
                        :
                        :   "memory", "cc", "xmm0", "xmm1", "xmm2", "xmm3", "xmm4"
                );
    }
    return;
}




