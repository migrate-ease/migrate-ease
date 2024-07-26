#![feature(asm)]
#[cfg(any(target_arch = "x86", target_arch = "x86_64"))]
fn bswap(mut val : u32) -> u32
{
    unsafe {
        // case1:(?mis)\A\s*(asm!|llvm_asm!)\(.*(LLDW|LLDL)
        asm!("" : : : "LLDW");// expect: RustInlineAsmIssue
       
        // case2:(?mis)\A\s*(asm!|llvm_asm!)\(.*(LSTW|LSTL)
        asm!("" : : : "LSTL"); // expect: RustInlineAsmIssue


        // case3:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*memory.*
        asm!("" : : : "memory");// expect: RustInlineAsmIssue

        // case4:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*pause.*
        asm!("pause" ::: "memory");// expect: RustInlineAsmIssue

        // case5:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*(LOCK|lock).*decl.*set.*
        asm!(lock_prefix "decl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: RustInlineAsmIssue

        // case6:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*(LOCK|lock).*subl.*set.*
        asm!(lock_prefix "subl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: RustInlineAsmIssue

        // case7:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*(LOCK|lock).*addl.*set.*
        asm!(lock_prefix "addl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: RustInlineAsmIssue

        // case8:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*(LOCK|lock).*incl.*set.*
        asm!(lock_prefix "incl %0; sete %1" : "+m" (v->counter), "=qm" (c) : : "memory"); // expect: RustInlineAsmIssue

        // case9:(?mis)\A\s*(asm!|llvm_asm!)\(.*(?:\n|\r\n)*.*(LOCK|lock).*xaddl.*
        asm!(lock_prefix "xaddl %1,%0" : "+m" (v->counter) : "ir" (i)); // expect: RustInlineAsmIssue

    }
    return;
}