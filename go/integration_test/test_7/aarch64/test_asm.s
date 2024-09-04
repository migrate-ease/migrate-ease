

// PLAN9_GOLANG_COMMON
    MOVB
    MOVW
    ADDW
    SUBW
    MULW
    MULL
    FADDD
    FSUBD
    FMULD
    FDIVD
    WORD
    LAST

// PLAN9_GOLANG_X86_AND_AARCH64
    MULSD
    ADCW
    ANDW
    CMPW
    CRC32B
    CRC32W
    HLT
    LSLW
    NEGW
    RORW
    FMOVD
    VMOVQ
    VMOVD
    AESIMC

// PLAN9_GOLANG_X86
    AAA //expect: AsmIssue
    AAD //expect: AsmIssue
    AAM //expect: AsmIssue
    AAS //expect: AsmIssue
    ADCB //expect: AsmIssue
    ADCL //expect: AsmIssue
    ADCQ //expect: AsmIssue
    ADCXL //expect: AsmIssue
    ADCXQ //expect: AsmIssue
    ADDB //expect: AsmIssue
    ADDPD //expect: AsmIssue
    ADDPS //expect: AsmIssue
    ADDQ //expect: AsmIssue
    ADDSD //expect: AsmIssue
    ADDSS //expect: AsmIssue
    ADDSUBPD //expect: AsmIssue
    ADDSUBPS //expect: AsmIssue
    ADJSP //expect: AsmIssue
    ADOXL //expect: AsmIssue
    ADOXQ //expect: AsmIssue
    AESDEC //expect: AsmIssue
    AESDECLAST //expect: AsmIssue
    AESENC //expect: AsmIssue
    AESENCLAST //expect: AsmIssue
    AESKEYGENASSIST //expect: AsmIssue
    ANDB //expect: AsmIssue
    ANDL //expect: AsmIssue
    ANDNL //expect: AsmIssue
    ANDNPD //expect: AsmIssue
    ANDNPS //expect: AsmIssue
    ANDNQ //expect: AsmIssue
    ANDPD //expect: AsmIssue
    ANDPS //expect: AsmIssue
    ANDQ //expect: AsmIssue
    ADDL //expect: AsmIssue
    SUBL //expect: AsmIssue
    ARPL //expect: AsmIssue
    BEXTRL //expect: AsmIssue
    BEXTRQ //expect: AsmIssue
    BLENDPD //expect: AsmIssue
    BLENDPS //expect: AsmIssue
    BLENDVPD //expect: AsmIssue
    BLENDVPS //expect: AsmIssue
    BLSIL //expect: AsmIssue
    BLSIQ //expect: AsmIssue
    BLSMSKL //expect: AsmIssue
    BLSMSKQ //expect: AsmIssue
    BLSRL //expect: AsmIssue
    BLSRQ //expect: AsmIssue
    BOUNDL //expect: AsmIssue
    BOUNDW //expect: AsmIssue
    BSFL //expect: AsmIssue
    BSFQ //expect: AsmIssue
    BSFW //expect: AsmIssue
    BSRL //expect: AsmIssue
    BSRQ //expect: AsmIssue
    BSRW //expect: AsmIssue
    BSWAPL //expect: AsmIssue
    BSWAPQ //expect: AsmIssue
    BTCL //expect: AsmIssue
    BTCQ //expect: AsmIssue
    BTCW //expect: AsmIssue
    BTL //expect: AsmIssue
    BTQ //expect: AsmIssue
    BTRL //expect: AsmIssue
    BTRQ //expect: AsmIssue
    BTRW //expect: AsmIssue
    BTSL //expect: AsmIssue
    BTSQ //expect: AsmIssue
    BTSW //expect: AsmIssue
    BTW //expect: AsmIssue
    BYTE //expect: AsmIssue
    BZHIL //expect: AsmIssue
    BZHIQ //expect: AsmIssue
    CBW //expect: AsmIssue
    CDQ //expect: AsmIssue
    CDQE //expect: AsmIssue
    CLAC //expect: AsmIssue
    CLC //expect: AsmIssue
    CLD //expect: AsmIssue
    CLDEMOTE //expect: AsmIssue
    CLFLUSH //expect: AsmIssue
    CLFLUSHOPT //expect: AsmIssue
    CLI //expect: AsmIssue
    CLTS //expect: AsmIssue
    CLWB //expect: AsmIssue
    CMC //expect: AsmIssue
    CMOVLCC //expect: AsmIssue
    CMOVLCS //expect: AsmIssue
    CMOVLEQ //expect: AsmIssue
    CMOVLGE //expect: AsmIssue
    CMOVLGT //expect: AsmIssue
    CMOVLHI //expect: AsmIssue
    CMOVLLE //expect: AsmIssue
    CMOVLLS //expect: AsmIssue
    CMOVLLT //expect: AsmIssue
    CMOVLMI //expect: AsmIssue
    CMOVLNE //expect: AsmIssue
    CMOVLOC //expect: AsmIssue
    CMOVLOS //expect: AsmIssue
    CMOVLPC //expect: AsmIssue
    CMOVLPL //expect: AsmIssue
    CMOVLPS //expect: AsmIssue
    CMOVQCC //expect: AsmIssue
    CMOVQCS //expect: AsmIssue
    CMOVQEQ //expect: AsmIssue
    CMOVQGE //expect: AsmIssue
    CMOVQGT //expect: AsmIssue
    CMOVQHI //expect: AsmIssue
    CMOVQLE //expect: AsmIssue
    CMOVQLS //expect: AsmIssue
    CMOVQLT //expect: AsmIssue
    CMOVQMI //expect: AsmIssue
    CMOVQNE //expect: AsmIssue
    CMOVQOC //expect: AsmIssue
    CMOVQOS //expect: AsmIssue
    CMOVQPC //expect: AsmIssue
    CMOVQPL //expect: AsmIssue
    CMOVQPS //expect: AsmIssue
    CMOVWCC //expect: AsmIssue
    CMOVWCS //expect: AsmIssue
    CMOVWEQ //expect: AsmIssue
    CMOVWGE //expect: AsmIssue
    CMOVWGT //expect: AsmIssue
    CMOVWHI //expect: AsmIssue
    CMOVWLE //expect: AsmIssue
    CMOVWLS //expect: AsmIssue
    CMOVWLT //expect: AsmIssue
    CMOVWMI //expect: AsmIssue
    CMOVWNE //expect: AsmIssue
    CMOVWOC //expect: AsmIssue
    CMOVWOS //expect: AsmIssue
    CMOVWPC //expect: AsmIssue
    CMOVWPL //expect: AsmIssue
    CMOVWPS //expect: AsmIssue
    CMPB //expect: AsmIssue
    CMPL //expect: AsmIssue
    CMPPD //expect: AsmIssue
    CMPPS //expect: AsmIssue
    CMPQ //expect: AsmIssue
    CMPSB //expect: AsmIssue
    CMPSD //expect: AsmIssue
    CMPSL //expect: AsmIssue
    CMPSQ //expect: AsmIssue
    CMPSS //expect: AsmIssue
    CMPSW //expect: AsmIssue
    CMPXCHG16B //expect: AsmIssue
    CMPXCHG8B //expect: AsmIssue
    CMPXCHGB //expect: AsmIssue
    CMPXCHGL //expect: AsmIssue
    CMPXCHGQ //expect: AsmIssue
    CMPXCHGW //expect: AsmIssue
    COMISD //expect: AsmIssue
    COMISS //expect: AsmIssue
    CPUID //expect: AsmIssue
    CQO //expect: AsmIssue
    CRC32L //expect: AsmIssue
    CRC32Q //expect: AsmIssue
    CVTPD2PL //expect: AsmIssue
    CVTPD2PS //expect: AsmIssue
    CVTPL2PD //expect: AsmIssue
    CVTPL2PS //expect: AsmIssue
    CVTPS2PD //expect: AsmIssue
    CVTPS2PL //expect: AsmIssue
    CVTSD2SL //expect: AsmIssue
    CVTSD2SQ //expect: AsmIssue
    CVTSD2SS //expect: AsmIssue
    CVTSL2SD //expect: AsmIssue
    CVTSL2SS //expect: AsmIssue
    CVTSQ2SD //expect: AsmIssue
    CVTSQ2SS //expect: AsmIssue
    CVTSS2SD //expect: AsmIssue
    CVTSS2SL //expect: AsmIssue
    CVTSS2SQ //expect: AsmIssue
    CVTTPD2PL //expect: AsmIssue
    CVTTPS2PL //expect: AsmIssue
    CVTTSD2SL //expect: AsmIssue
    CVTTSD2SQ //expect: AsmIssue
    CVTTSS2SL //expect: AsmIssue
    CVTTSS2SQ //expect: AsmIssue
    CWD //expect: AsmIssue
    CWDE //expect: AsmIssue
    DAA //expect: AsmIssue
    DAS //expect: AsmIssue
    DECB //expect: AsmIssue
    DECL //expect: AsmIssue
    DECQ //expect: AsmIssue
    DECW //expect: AsmIssue
    DIVB //expect: AsmIssue
    DIVL //expect: AsmIssue
    DIVPD //expect: AsmIssue
    DIVPS //expect: AsmIssue
    DIVQ //expect: AsmIssue
    DIVSD //expect: AsmIssue
    DIVSS //expect: AsmIssue
    DIVW //expect: AsmIssue
    DPPD //expect: AsmIssue
    DPPS //expect: AsmIssue
    EMMS //expect: AsmIssue
    ENTER //expect: AsmIssue
    EXTRACTPS //expect: AsmIssue
    F2XM1 //expect: AsmIssue
    FABS //expect: AsmIssue
    FADDDP //expect: AsmIssue
    FADDF //expect: AsmIssue
    FADDL //expect: AsmIssue
    FADDW //expect: AsmIssue
    FBLD //expect: AsmIssue
    FBSTP //expect: AsmIssue
    FCHS //expect: AsmIssue
    FCLEX //expect: AsmIssue
    FCMOVB //expect: AsmIssue
    FCMOVBE //expect: AsmIssue
    FCMOVCC //expect: AsmIssue
    FCMOVCS //expect: AsmIssue
    FCMOVE //expect: AsmIssue
    FCMOVEQ //expect: AsmIssue
    FCMOVHI //expect: AsmIssue
    FCMOVLS //expect: AsmIssue
    FCMOVNB //expect: AsmIssue
    FCMOVNBE //expect: AsmIssue
    FCMOVNE //expect: AsmIssue
    FCMOVNU //expect: AsmIssue
    FCMOVU //expect: AsmIssue
    FCMOVUN //expect: AsmIssue
    FCOMD //expect: AsmIssue
    FCOMDP //expect: AsmIssue
    FCOMDPP //expect: AsmIssue
    FCOMF //expect: AsmIssue
    FCOMFP //expect: AsmIssue
    FCOMI //expect: AsmIssue
    FCOMIP //expect: AsmIssue
    FCOML //expect: AsmIssue
    FCOMLP //expect: AsmIssue
    FCOMW //expect: AsmIssue
    FCOMWP //expect: AsmIssue
    FCOS //expect: AsmIssue
    FDECSTP //expect: AsmIssue
    FDIVDP //expect: AsmIssue
    FDIVF //expect: AsmIssue
    FDIVL //expect: AsmIssue
    FDIVRD //expect: AsmIssue
    FDIVRDP //expect: AsmIssue
    FDIVRF //expect: AsmIssue
    FDIVRL //expect: AsmIssue
    FDIVRW //expect: AsmIssue
    FDIVW //expect: AsmIssue
    FFREE //expect: AsmIssue
    FINCSTP //expect: AsmIssue
    FINIT //expect: AsmIssue
    FLD1 //expect: AsmIssue
    FLDCW //expect: AsmIssue
    FLDENV //expect: AsmIssue
    FLDL2E //expect: AsmIssue
    FLDL2T //expect: AsmIssue
    FLDLG2 //expect: AsmIssue
    FLDLN2 //expect: AsmIssue
    FLDPI //expect: AsmIssue
    FLDZ //expect: AsmIssue
    FMOVB //expect: AsmIssue
    FMOVBP //expect: AsmIssue
    FMOVDP //expect: AsmIssue
    FMOVF //expect: AsmIssue
    FMOVFP //expect: AsmIssue
    FMOVL //expect: AsmIssue
    FMOVLP //expect: AsmIssue
    FMOVV //expect: AsmIssue
    FMOVVP //expect: AsmIssue
    FMOVW //expect: AsmIssue
    FMOVWP //expect: AsmIssue
    FMOVX //expect: AsmIssue
    FMOVXP //expect: AsmIssue
    FMULDP //expect: AsmIssue
    FMULF //expect: AsmIssue
    FMULL //expect: AsmIssue
    FMULW //expect: AsmIssue
    FNOP //expect: AsmIssue
    FPATAN //expect: AsmIssue
    FPREM //expect: AsmIssue
    FPREM1 //expect: AsmIssue
    FPTAN //expect: AsmIssue
    FRNDINT //expect: AsmIssue
    FRSTOR //expect: AsmIssue
    FSAVE //expect: AsmIssue
    FSCALE //expect: AsmIssue
    FSIN //expect: AsmIssue
    FSINCOS //expect: AsmIssue
    FSQRT //expect: AsmIssue
    FSTCW //expect: AsmIssue
    FSTENV //expect: AsmIssue
    FSTSW //expect: AsmIssue
    FSUBDP //expect: AsmIssue
    FSUBF //expect: AsmIssue
    FSUBL //expect: AsmIssue
    FSUBRD //expect: AsmIssue
    FSUBRDP //expect: AsmIssue
    FSUBRF //expect: AsmIssue
    FSUBRL //expect: AsmIssue
    FSUBRW //expect: AsmIssue
    FSUBW //expect: AsmIssue
    FTST //expect: AsmIssue
    FUCOM //expect: AsmIssue
    FUCOMI //expect: AsmIssue
    FUCOMIP //expect: AsmIssue
    FUCOMP //expect: AsmIssue
    FUCOMPP //expect: AsmIssue
    FXAM //expect: AsmIssue
    FXCHD //expect: AsmIssue
    FXRSTOR //expect: AsmIssue
    FXRSTOR64 //expect: AsmIssue
    FXSAVE //expect: AsmIssue
    FXSAVE64 //expect: AsmIssue
    FXTRACT //expect: AsmIssue
    FYL2X //expect: AsmIssue
    FYL2XP1 //expect: AsmIssue
    HADDPD //expect: AsmIssue
    HADDPS //expect: AsmIssue
    HSUBPD //expect: AsmIssue
    HSUBPS //expect: AsmIssue
    ICEBP //expect: AsmIssue
    IDIVB //expect: AsmIssue
    IDIVL //expect: AsmIssue
    IDIVQ //expect: AsmIssue
    IDIVW //expect: AsmIssue
    IMUL3L //expect: AsmIssue
    IMUL3Q //expect: AsmIssue
    IMUL3W //expect: AsmIssue
    IMULB //expect: AsmIssue
    IMULL //expect: AsmIssue
    IMULQ //expect: AsmIssue
    IMULW //expect: AsmIssue
    INB //expect: AsmIssue
    INCB //expect: AsmIssue
    INCL //expect: AsmIssue
    INCQ //expect: AsmIssue
    INCW //expect: AsmIssue
    INL //expect: AsmIssue
    INSB //expect: AsmIssue
    INSERTPS //expect: AsmIssue
    INSL //expect: AsmIssue
    INSW //expect: AsmIssue
    INT //expect: AsmIssue
    INTO //expect: AsmIssue
    INVD //expect: AsmIssue
    INVLPG //expect: AsmIssue
    INVPCID //expect: AsmIssue
    INW //expect: AsmIssue
    IRETL //expect: AsmIssue
    IRETQ //expect: AsmIssue
    IRETW //expect: AsmIssue
    JCC //expect: AsmIssue
    JCS //expect: AsmIssue
    JCXZL //expect: AsmIssue
    JCXZQ //expect: AsmIssue
    JCXZW //expect: AsmIssue
    JEQ //expect: AsmIssue
    JGE //expect: AsmIssue
    JGT //expect: AsmIssue
    JHI //expect: AsmIssue
    JLE //expect: AsmIssue
    JLS //expect: AsmIssue
    JLT //expect: AsmIssue
    JMI //expect: AsmIssue
    JNE //expect: AsmIssue
    JOC //expect: AsmIssue
    JOS //expect: AsmIssue
    JPC //expect: AsmIssue
    JPL //expect: AsmIssue
    JPS //expect: AsmIssue
    KADDB //expect: AsmIssue
    KADDD //expect: AsmIssue
    KADDQ //expect: AsmIssue
    KADDW //expect: AsmIssue
    KANDB //expect: AsmIssue
    KANDD //expect: AsmIssue
    KANDNB //expect: AsmIssue
    KANDND //expect: AsmIssue
    KANDNQ //expect: AsmIssue
    KANDNW //expect: AsmIssue
    KANDQ //expect: AsmIssue
    KANDW //expect: AsmIssue
    KMOVB //expect: AsmIssue
    KMOVD //expect: AsmIssue
    KMOVQ //expect: AsmIssue
    KMOVW //expect: AsmIssue
    KNOTB //expect: AsmIssue
    KNOTD //expect: AsmIssue
    KNOTQ //expect: AsmIssue
    KNOTW //expect: AsmIssue
    KORB //expect: AsmIssue
    KORD //expect: AsmIssue
    KORQ //expect: AsmIssue
    KORTESTB //expect: AsmIssue
    KORTESTD //expect: AsmIssue
    KORTESTQ //expect: AsmIssue
    KORTESTW //expect: AsmIssue
    KORW //expect: AsmIssue
    KSHIFTLB //expect: AsmIssue
    KSHIFTLD //expect: AsmIssue
    KSHIFTLQ //expect: AsmIssue
    KSHIFTLW //expect: AsmIssue
    KSHIFTRB //expect: AsmIssue
    KSHIFTRD //expect: AsmIssue
    KSHIFTRQ //expect: AsmIssue
    KSHIFTRW //expect: AsmIssue
    KTESTB //expect: AsmIssue
    KTESTD //expect: AsmIssue
    KTESTQ //expect: AsmIssue
    KTESTW //expect: AsmIssue
    KUNPCKBW //expect: AsmIssue
    KUNPCKDQ //expect: AsmIssue
    KUNPCKWD //expect: AsmIssue
    KXNORB //expect: AsmIssue
    KXNORD //expect: AsmIssue
    KXNORQ //expect: AsmIssue
    KXNORW //expect: AsmIssue
    KXORB //expect: AsmIssue
    KXORD //expect: AsmIssue
    KXORQ //expect: AsmIssue
    KXORW //expect: AsmIssue
    LAHF //expect: AsmIssue
    LARL //expect: AsmIssue
    LARQ //expect: AsmIssue
    LARW //expect: AsmIssue
    LDDQU //expect: AsmIssue
    LDMXCSR //expect: AsmIssue
    LEAL //expect: AsmIssue
    LEAQ //expect: AsmIssue
    LEAVEL //expect: AsmIssue
    LEAVEQ //expect: AsmIssue
    LEAVEW //expect: AsmIssue
    LEAW //expect: AsmIssue
    LFENCE //expect: AsmIssue
    LFSL //expect: AsmIssue
    LFSQ //expect: AsmIssue
    LFSW //expect: AsmIssue
    LGDT //expect: AsmIssue
    LGSL //expect: AsmIssue
    LGSQ //expect: AsmIssue
    LGSW //expect: AsmIssue
    LIDT //expect: AsmIssue
    LLDT //expect: AsmIssue
    LMSW //expect: AsmIssue
    LOCK //expect: AsmIssue
    LODSB //expect: AsmIssue
    LODSL //expect: AsmIssue
    LODSQ //expect: AsmIssue
    LODSW //expect: AsmIssue
    LONG //expect: AsmIssue
    LOOP //expect: AsmIssue
    LOOPEQ //expect: AsmIssue
    LOOPNE //expect: AsmIssue
    LSLL //expect: AsmIssue
    LSLQ //expect: AsmIssue
    LSSL //expect: AsmIssue
    LSSQ //expect: AsmIssue
    LSSW //expect: AsmIssue
    LTR //expect: AsmIssue
    LZCNTL //expect: AsmIssue
    LZCNTQ //expect: AsmIssue
    LZCNTW //expect: AsmIssue
    MASKMOVOU //expect: AsmIssue
    MASKMOVQ //expect: AsmIssue
    MAXPD //expect: AsmIssue
    MAXPS //expect: AsmIssue
    MAXSD //expect: AsmIssue
    MAXSS //expect: AsmIssue
    MFENCE //expect: AsmIssue
    MINPD //expect: AsmIssue
    MINPS //expect: AsmIssue
    MINSD //expect: AsmIssue
    MINSS //expect: AsmIssue
    MONITOR //expect: AsmIssue
    MOVAPD //expect: AsmIssue
    MOVAPS //expect: AsmIssue
    MOVBELL //expect: AsmIssue
    MOVBEQQ //expect: AsmIssue
    MOVBEWW //expect: AsmIssue
    MOVBLSX //expect: AsmIssue
    MOVBLZX //expect: AsmIssue
    MOVBQSX //expect: AsmIssue
    MOVBQZX //expect: AsmIssue
    MOVBWSX //expect: AsmIssue
    MOVBWZX //expect: AsmIssue
    MOVDDUP //expect: AsmIssue
    MOVHLPS //expect: AsmIssue
    MOVHPD //expect: AsmIssue
    MOVHPS //expect: AsmIssue
    MOVL //expect: AsmIssue
    MOVLHPS //expect: AsmIssue
    MOVLPD //expect: AsmIssue
    MOVLPS //expect: AsmIssue
    MOVLQSX //expect: AsmIssue
    MOVLQZX //expect: AsmIssue
    MOVMSKPD //expect: AsmIssue
    MOVMSKPS //expect: AsmIssue
    MOVNTDQA //expect: AsmIssue
    MOVNTIL //expect: AsmIssue
    MOVNTIQ //expect: AsmIssue
    MOVNTO //expect: AsmIssue
    MOVNTPD //expect: AsmIssue
    MOVNTPS //expect: AsmIssue
    MOVNTQ //expect: AsmIssue
    MOVO //expect: AsmIssue
    MOVOU //expect: AsmIssue
    MOVQ //expect: AsmIssue
    MOVQL //expect: AsmIssue
    MOVQOZX //expect: AsmIssue
    MOVSB //expect: AsmIssue
    MOVSD //expect: AsmIssue
    MOVSHDUP //expect: AsmIssue
    MOVSL //expect: AsmIssue
    MOVSLDUP //expect: AsmIssue
    MOVSQ //expect: AsmIssue
    MOVSS //expect: AsmIssue
    MOVSW //expect: AsmIssue
    MOVSWW //expect: AsmIssue
    MOVUPD //expect: AsmIssue
    MOVUPS //expect: AsmIssue
    MOVWLSX //expect: AsmIssue
    MOVWLZX //expect: AsmIssue
    MOVWQSX //expect: AsmIssue
    MOVWQZX //expect: AsmIssue
    MOVZWW //expect: AsmIssue
    MPSADBW //expect: AsmIssue
    MULB //expect: AsmIssue
    MULPD //expect: AsmIssue
    MULPS //expect: AsmIssue
    MULQ //expect: AsmIssue
    MULSS //expect: AsmIssue
    MULXL //expect: AsmIssue
    MULXQ //expect: AsmIssue
    MWAIT //expect: AsmIssue
    NEGB //expect: AsmIssue
    NEGL //expect: AsmIssue
    NEGQ //expect: AsmIssue
    NOPL //expect: AsmIssue
    NOPW //expect: AsmIssue
    NOTB //expect: AsmIssue
    NOTL //expect: AsmIssue
    NOTQ //expect: AsmIssue
    NOTW //expect: AsmIssue
    ORB //expect: AsmIssue
    ORL //expect: AsmIssue
    ORPD //expect: AsmIssue
    ORPS //expect: AsmIssue
    ORQ //expect: AsmIssue
    ORW //expect: AsmIssue
    OUTB //expect: AsmIssue
    OUTL //expect: AsmIssue
    OUTSB //expect: AsmIssue
    OUTSL //expect: AsmIssue
    OUTSW //expect: AsmIssue
    OUTW //expect: AsmIssue
    PABSB //expect: AsmIssue
    PABSD //expect: AsmIssue
    PABSW //expect: AsmIssue
    PACKSSLW //expect: AsmIssue
    PACKSSWB //expect: AsmIssue
    PACKUSDW //expect: AsmIssue
    PACKUSWB //expect: AsmIssue
    PADDB //expect: AsmIssue
    PADDL //expect: AsmIssue
    PADDQ //expect: AsmIssue
    PADDSB //expect: AsmIssue
    PADDSW //expect: AsmIssue
    PADDUSB //expect: AsmIssue
    PADDUSW //expect: AsmIssue
    PADDW //expect: AsmIssue
    PALIGNR //expect: AsmIssue
    PAND //expect: AsmIssue
    PANDN //expect: AsmIssue
    PAUSE //expect: AsmIssue
    PAVGB //expect: AsmIssue
    PAVGW //expect: AsmIssue
    PBLENDVB //expect: AsmIssue
    PBLENDW //expect: AsmIssue
    PCLMULQDQ //expect: AsmIssue
    PCMPEQB //expect: AsmIssue
    PCMPEQL //expect: AsmIssue
    PCMPEQQ //expect: AsmIssue
    PCMPEQW //expect: AsmIssue
    PCMPESTRI //expect: AsmIssue
    PCMPESTRM //expect: AsmIssue
    PCMPGTB //expect: AsmIssue
    PCMPGTL //expect: AsmIssue
    PCMPGTQ //expect: AsmIssue
    PCMPGTW //expect: AsmIssue
    PCMPISTRI //expect: AsmIssue
    PCMPISTRM //expect: AsmIssue
    PDEPL //expect: AsmIssue
    PDEPQ //expect: AsmIssue
    PEXTL //expect: AsmIssue
    PEXTQ //expect: AsmIssue
    PEXTRB //expect: AsmIssue
    PEXTRD //expect: AsmIssue
    PEXTRQ //expect: AsmIssue
    PEXTRW //expect: AsmIssue
    PHADDD //expect: AsmIssue
    PHADDSW //expect: AsmIssue
    PHADDW //expect: AsmIssue
    PHMINPOSUW //expect: AsmIssue
    PHSUBD //expect: AsmIssue
    PHSUBSW //expect: AsmIssue
    PHSUBW //expect: AsmIssue
    PINSRB //expect: AsmIssue
    PINSRD //expect: AsmIssue
    PINSRQ //expect: AsmIssue
    PINSRW //expect: AsmIssue
    PMADDUBSW //expect: AsmIssue
    PMADDWL //expect: AsmIssue
    PMAXSB //expect: AsmIssue
    PMAXSD //expect: AsmIssue
    PMAXSW //expect: AsmIssue
    PMAXUB //expect: AsmIssue
    PMAXUD //expect: AsmIssue
    PMAXUW //expect: AsmIssue
    PMINSB //expect: AsmIssue
    PMINSD //expect: AsmIssue
    PMINSW //expect: AsmIssue
    PMINUB //expect: AsmIssue
    PMINUD //expect: AsmIssue
    PMINUW //expect: AsmIssue
    PMOVMSKB //expect: AsmIssue
    PMOVSXBD //expect: AsmIssue
    PMOVSXBQ //expect: AsmIssue
    PMOVSXBW //expect: AsmIssue
    PMOVSXDQ //expect: AsmIssue
    PMOVSXWD //expect: AsmIssue
    PMOVSXWQ //expect: AsmIssue
    PMOVZXBD //expect: AsmIssue
    PMOVZXBQ //expect: AsmIssue
    PMOVZXBW //expect: AsmIssue
    PMOVZXDQ //expect: AsmIssue
    PMOVZXWD //expect: AsmIssue
    PMOVZXWQ //expect: AsmIssue
    PMULDQ //expect: AsmIssue
    PMULHRSW //expect: AsmIssue
    PMULHUW //expect: AsmIssue
    PMULHW //expect: AsmIssue
    PMULLD //expect: AsmIssue
    PMULLW //expect: AsmIssue
    PMULULQ //expect: AsmIssue
    POPAL //expect: AsmIssue
    POPAW //expect: AsmIssue
    POPCNTL //expect: AsmIssue
    POPCNTQ //expect: AsmIssue
    POPCNTW //expect: AsmIssue
    POPFL //expect: AsmIssue
    POPFQ //expect: AsmIssue
    POPFW //expect: AsmIssue
    POPL //expect: AsmIssue
    POPQ //expect: AsmIssue
    POPW //expect: AsmIssue
    POR //expect: AsmIssue
    PREFETCHNTA //expect: AsmIssue
    PREFETCHT0 //expect: AsmIssue
    PREFETCHT1 //expect: AsmIssue
    PREFETCHT2 //expect: AsmIssue
    PSADBW //expect: AsmIssue
    PSHUFB //expect: AsmIssue
    PSHUFD //expect: AsmIssue
    PSHUFHW //expect: AsmIssue
    PSHUFL //expect: AsmIssue
    PSHUFLW //expect: AsmIssue
    PSHUFW //expect: AsmIssue
    PSIGNB //expect: AsmIssue
    PSIGND //expect: AsmIssue
    PSIGNW //expect: AsmIssue
    PSLLL //expect: AsmIssue
    PSLLO //expect: AsmIssue
    PSLLQ //expect: AsmIssue
    PSLLW //expect: AsmIssue
    PSRAL //expect: AsmIssue
    PSRAW //expect: AsmIssue
    PSRLL //expect: AsmIssue
    PSRLO //expect: AsmIssue
    PSRLQ //expect: AsmIssue
    PSRLW //expect: AsmIssue
    PSUBB //expect: AsmIssue
    PSUBL //expect: AsmIssue
    PSUBQ //expect: AsmIssue
    PSUBSB //expect: AsmIssue
    PSUBSW //expect: AsmIssue
    PSUBUSB //expect: AsmIssue
    PSUBUSW //expect: AsmIssue
    PSUBW //expect: AsmIssue
    PTEST //expect: AsmIssue
    PUNPCKHBW //expect: AsmIssue
    PUNPCKHLQ //expect: AsmIssue
    PUNPCKHQDQ //expect: AsmIssue
    PUNPCKHWL //expect: AsmIssue
    PUNPCKLBW //expect: AsmIssue
    PUNPCKLLQ //expect: AsmIssue
    PUNPCKLQDQ //expect: AsmIssue
    PUNPCKLWL //expect: AsmIssue
    PUSHAL //expect: AsmIssue
    PUSHAW //expect: AsmIssue
    PUSHFL //expect: AsmIssue
    PUSHFQ //expect: AsmIssue
    PUSHFW //expect: AsmIssue
    PUSHL //expect: AsmIssue
    PUSHQ //expect: AsmIssue
    PUSHW //expect: AsmIssue
    PXOR //expect: AsmIssue
    QUAD //expect: AsmIssue
    RCLB //expect: AsmIssue
    RCLL //expect: AsmIssue
    RCLQ //expect: AsmIssue
    RCLW //expect: AsmIssue
    RCPPS //expect: AsmIssue
    RCPSS //expect: AsmIssue
    RCRB //expect: AsmIssue
    RCRL //expect: AsmIssue
    RCRQ //expect: AsmIssue
    RCRW //expect: AsmIssue
    RDFSBASEL //expect: AsmIssue
    RDFSBASEQ //expect: AsmIssue
    RDGSBASEL //expect: AsmIssue
    RDGSBASEQ //expect: AsmIssue
    RDMSR //expect: AsmIssue
    RDPKRU //expect: AsmIssue
    RDPMC //expect: AsmIssue
    RDRANDL //expect: AsmIssue
    RDRANDQ //expect: AsmIssue
    RDRANDW //expect: AsmIssue
    RDSEEDL //expect: AsmIssue
    RDSEEDQ //expect: AsmIssue
    RDSEEDW //expect: AsmIssue
    RDTSC //expect: AsmIssue
    RDTSCP //expect: AsmIssue
    REP //expect: AsmIssue
    REPN //expect: AsmIssue
    RETFL //expect: AsmIssue
    RETFQ //expect: AsmIssue
    RETFW //expect: AsmIssue
    ROLB //expect: AsmIssue
    ROLL //expect: AsmIssue
    ROLQ //expect: AsmIssue
    ROLW //expect: AsmIssue
    RORB //expect: AsmIssue
    RORL //expect: AsmIssue
    RORQ //expect: AsmIssue
    RORXL //expect: AsmIssue
    RORXQ //expect: AsmIssue
    ROUNDPD //expect: AsmIssue
    ROUNDPS //expect: AsmIssue
    ROUNDSD //expect: AsmIssue
    ROUNDSS //expect: AsmIssue
    RSM //expect: AsmIssue
    RSQRTPS //expect: AsmIssue
    RSQRTSS //expect: AsmIssue
    SAHF //expect: AsmIssue
    SALB //expect: AsmIssue
    SALL //expect: AsmIssue
    SALQ //expect: AsmIssue
    SALW //expect: AsmIssue
    SARB //expect: AsmIssue
    SARL //expect: AsmIssue
    SARQ //expect: AsmIssue
    SARW //expect: AsmIssue
    SARXL //expect: AsmIssue
    SARXQ //expect: AsmIssue
    SBBB //expect: AsmIssue
    SBBL //expect: AsmIssue
    SBBQ //expect: AsmIssue
    SBBW //expect: AsmIssue
    SCASB //expect: AsmIssue
    SCASL //expect: AsmIssue
    SCASQ //expect: AsmIssue
    SCASW //expect: AsmIssue
    SETCC //expect: AsmIssue
    SETCS //expect: AsmIssue
    SETEQ //expect: AsmIssue
    SETGE //expect: AsmIssue
    SETGT //expect: AsmIssue
    SETHI //expect: AsmIssue
    SETLE //expect: AsmIssue
    SETLS //expect: AsmIssue
    SETLT //expect: AsmIssue
    SETMI //expect: AsmIssue
    SETNE //expect: AsmIssue
    SETOC //expect: AsmIssue
    SETOS //expect: AsmIssue
    SETPC //expect: AsmIssue
    SETPL //expect: AsmIssue
    SETPS //expect: AsmIssue
    SFENCE //expect: AsmIssue
    SGDT //expect: AsmIssue
    SHA1MSG1 //expect: AsmIssue
    SHA1MSG2 //expect: AsmIssue
    SHA1NEXTE //expect: AsmIssue
    SHA1RNDS4 //expect: AsmIssue
    SHA256MSG1 //expect: AsmIssue
    SHA256MSG2 //expect: AsmIssue
    SHA256RNDS2 //expect: AsmIssue
    SHLB //expect: AsmIssue
    SHLL //expect: AsmIssue
    SHLQ //expect: AsmIssue
    SHLW //expect: AsmIssue
    SHLXL //expect: AsmIssue
    SHLXQ //expect: AsmIssue
    SHRB //expect: AsmIssue
    SHRL //expect: AsmIssue
    SHRQ //expect: AsmIssue
    SHRW //expect: AsmIssue
    SHRXL //expect: AsmIssue
    SHRXQ //expect: AsmIssue
    SHUFPD //expect: AsmIssue
    SHUFPS //expect: AsmIssue
    SIDT //expect: AsmIssue
    SLDTL //expect: AsmIssue
    SLDTQ //expect: AsmIssue
    SLDTW //expect: AsmIssue
    SMSWL //expect: AsmIssue
    SMSWQ //expect: AsmIssue
    SMSWW //expect: AsmIssue
    SQRTPD //expect: AsmIssue
    SQRTPS //expect: AsmIssue
    SQRTSD //expect: AsmIssue
    SQRTSS //expect: AsmIssue
    STAC //expect: AsmIssue
    STC //expect: AsmIssue
    STD //expect: AsmIssue
    STI //expect: AsmIssue
    STMXCSR //expect: AsmIssue
    STOSB //expect: AsmIssue
    STOSL //expect: AsmIssue
    STOSQ //expect: AsmIssue
    STOSW //expect: AsmIssue
    STRL //expect: AsmIssue
    STRQ //expect: AsmIssue
    STRW //expect: AsmIssue
    SUBB //expect: AsmIssue
    SUBPD //expect: AsmIssue
    SUBPS //expect: AsmIssue
    SUBQ //expect: AsmIssue
    SUBSD //expect: AsmIssue
    SUBSS //expect: AsmIssue
    SWAPGS //expect: AsmIssue
    SYSCALL //expect: AsmIssue
    SYSENTER //expect: AsmIssue
    SYSENTER64 //expect: AsmIssue
    SYSEXIT //expect: AsmIssue
    SYSEXIT64 //expect: AsmIssue
    SYSRET //expect: AsmIssue
    TESTB //expect: AsmIssue
    TESTL //expect: AsmIssue
    TESTQ //expect: AsmIssue
    TESTW //expect: AsmIssue
    TPAUSE //expect: AsmIssue
    TZCNTL //expect: AsmIssue
    TZCNTQ //expect: AsmIssue
    TZCNTW //expect: AsmIssue
    UCOMISD //expect: AsmIssue
    UCOMISS //expect: AsmIssue
    UD1 //expect: AsmIssue
    UD2 //expect: AsmIssue
    UMWAIT //expect: AsmIssue
    UNPCKHPD //expect: AsmIssue
    UNPCKHPS //expect: AsmIssue
    UNPCKLPD //expect: AsmIssue
    UNPCKLPS //expect: AsmIssue
    UMONITOR //expect: AsmIssue
    V4FMADDPS //expect: AsmIssue
    V4FMADDSS //expect: AsmIssue
    V4FNMADDPS //expect: AsmIssue
    V4FNMADDSS //expect: AsmIssue
    VADDPD //expect: AsmIssue
    VADDPS //expect: AsmIssue
    VADDSD //expect: AsmIssue
    VADDSS //expect: AsmIssue
    VADDSUBPD //expect: AsmIssue
    VADDSUBPS //expect: AsmIssue
    VAESDEC //expect: AsmIssue
    VAESDECLAST //expect: AsmIssue
    VAESENC //expect: AsmIssue
    VAESENCLAST //expect: AsmIssue
    VAESIMC //expect: AsmIssue
    VAESKEYGENASSIST //expect: AsmIssue
    VALIGND //expect: AsmIssue
    VALIGNQ //expect: AsmIssue
    VANDNPD //expect: AsmIssue
    VANDNPS //expect: AsmIssue
    VANDPD //expect: AsmIssue
    VANDPS //expect: AsmIssue
    VBLENDMPD //expect: AsmIssue
    VBLENDMPS //expect: AsmIssue
    VBLENDPD //expect: AsmIssue
    VBLENDPS //expect: AsmIssue
    VBLENDVPD //expect: AsmIssue
    VBLENDVPS //expect: AsmIssue
    VBROADCASTF128 //expect: AsmIssue
    VBROADCASTF32X2 //expect: AsmIssue
    VBROADCASTF32X4 //expect: AsmIssue
    VBROADCASTF32X8 //expect: AsmIssue
    VBROADCASTF64X2 //expect: AsmIssue
    VBROADCASTF64X4 //expect: AsmIssue
    VBROADCASTI128 //expect: AsmIssue
    VBROADCASTI32X2 //expect: AsmIssue
    VBROADCASTI32X4 //expect: AsmIssue
    VBROADCASTI32X8 //expect: AsmIssue
    VBROADCASTI64X2 //expect: AsmIssue
    VBROADCASTI64X4 //expect: AsmIssue
    VBROADCASTSD //expect: AsmIssue
    VBROADCASTSS //expect: AsmIssue
    VCMPPD //expect: AsmIssue
    VCMPPS //expect: AsmIssue
    VCMPSD //expect: AsmIssue
    VCMPSS //expect: AsmIssue
    VCOMISD //expect: AsmIssue
    VCOMISS //expect: AsmIssue
    VCOMPRESSPD //expect: AsmIssue
    VCOMPRESSPS //expect: AsmIssue
    VCVTDQ2PD //expect: AsmIssue
    VCVTDQ2PS //expect: AsmIssue
    VCVTPD2DQ //expect: AsmIssue
    VCVTPD2DQX //expect: AsmIssue
    VCVTPD2DQY //expect: AsmIssue
    VCVTPD2PS //expect: AsmIssue
    VCVTPD2PSX //expect: AsmIssue
    VCVTPD2PSY //expect: AsmIssue
    VCVTPD2QQ //expect: AsmIssue
    VCVTPD2UDQ //expect: AsmIssue
    VCVTPD2UDQX //expect: AsmIssue
    VCVTPD2UDQY //expect: AsmIssue
    VCVTPD2UQQ //expect: AsmIssue
    VCVTPH2PS //expect: AsmIssue
    VCVTPS2DQ //expect: AsmIssue
    VCVTPS2PD //expect: AsmIssue
    VCVTPS2PH //expect: AsmIssue
    VCVTPS2QQ //expect: AsmIssue
    VCVTPS2UDQ //expect: AsmIssue
    VCVTPS2UQQ //expect: AsmIssue
    VCVTQQ2PD //expect: AsmIssue
    VCVTQQ2PS //expect: AsmIssue
    VCVTQQ2PSX //expect: AsmIssue
    VCVTQQ2PSY //expect: AsmIssue
    VCVTSD2SI //expect: AsmIssue
    VCVTSD2SIQ //expect: AsmIssue
    VCVTSD2SS //expect: AsmIssue
    VCVTSD2USI //expect: AsmIssue
    VCVTSD2USIL //expect: AsmIssue
    VCVTSD2USIQ //expect: AsmIssue
    VCVTSI2SDL //expect: AsmIssue
    VCVTSI2SDQ //expect: AsmIssue
    VCVTSI2SSL //expect: AsmIssue
    VCVTSI2SSQ //expect: AsmIssue
    VCVTSS2SD //expect: AsmIssue
    VCVTSS2SI //expect: AsmIssue
    VCVTSS2SIQ //expect: AsmIssue
    VCVTSS2USI //expect: AsmIssue
    VCVTSS2USIL //expect: AsmIssue
    VCVTSS2USIQ //expect: AsmIssue
    VCVTTPD2DQ //expect: AsmIssue
    VCVTTPD2DQX //expect: AsmIssue
    VCVTTPD2DQY //expect: AsmIssue
    VCVTTPD2QQ //expect: AsmIssue
    VCVTTPD2UDQ //expect: AsmIssue
    VCVTTPD2UDQX //expect: AsmIssue
    VCVTTPD2UDQY //expect: AsmIssue
    VCVTTPD2UQQ //expect: AsmIssue
    VCVTTPS2DQ //expect: AsmIssue
    VCVTTPS2QQ //expect: AsmIssue
    VCVTTPS2UDQ //expect: AsmIssue
    VCVTTPS2UQQ //expect: AsmIssue
    VCVTTSD2SI //expect: AsmIssue
    VCVTTSD2SIQ //expect: AsmIssue
    VCVTTSD2USI //expect: AsmIssue
    VCVTTSD2USIL //expect: AsmIssue
    VCVTTSD2USIQ //expect: AsmIssue
    VCVTTSS2SI //expect: AsmIssue
    VCVTTSS2SIQ //expect: AsmIssue
    VCVTTSS2USI //expect: AsmIssue
    VCVTTSS2USIL //expect: AsmIssue
    VCVTTSS2USIQ //expect: AsmIssue
    VCVTUDQ2PD //expect: AsmIssue
    VCVTUDQ2PS //expect: AsmIssue
    VCVTUQQ2PD //expect: AsmIssue
    VCVTUQQ2PS //expect: AsmIssue
    VCVTUQQ2PSX //expect: AsmIssue
    VCVTUQQ2PSY //expect: AsmIssue
    VCVTUSI2SD //expect: AsmIssue
    VCVTUSI2SDL //expect: AsmIssue
    VCVTUSI2SDQ //expect: AsmIssue
    VCVTUSI2SS //expect: AsmIssue
    VCVTUSI2SSL //expect: AsmIssue
    VCVTUSI2SSQ //expect: AsmIssue
    VDBPSADBW //expect: AsmIssue
    VDIVPD //expect: AsmIssue
    VDIVPS //expect: AsmIssue
    VDIVSD //expect: AsmIssue
    VDIVSS //expect: AsmIssue
    VDPPD //expect: AsmIssue
    VDPPS //expect: AsmIssue
    VERR //expect: AsmIssue
    VERW //expect: AsmIssue
    VEXP2PD //expect: AsmIssue
    VEXP2PS //expect: AsmIssue
    VEXPANDPD //expect: AsmIssue
    VEXPANDPS //expect: AsmIssue
    VEXTRACTF128 //expect: AsmIssue
    VEXTRACTF32X4 //expect: AsmIssue
    VEXTRACTF32X8 //expect: AsmIssue
    VEXTRACTF64X2 //expect: AsmIssue
    VEXTRACTF64X4 //expect: AsmIssue
    VEXTRACTI128 //expect: AsmIssue
    VEXTRACTI32X4 //expect: AsmIssue
    VEXTRACTI32X8 //expect: AsmIssue
    VEXTRACTI64X2 //expect: AsmIssue
    VEXTRACTI64X4 //expect: AsmIssue
    VEXTRACTPS //expect: AsmIssue
    VFIXUPIMMPD //expect: AsmIssue
    VFIXUPIMMPS //expect: AsmIssue
    VFIXUPIMMSD //expect: AsmIssue
    VFIXUPIMMSS //expect: AsmIssue
    VFMADD132PD //expect: AsmIssue
    VFMADD132PS //expect: AsmIssue
    VFMADD132SD //expect: AsmIssue
    VFMADD132SS //expect: AsmIssue
    VFMADD213PD //expect: AsmIssue
    VFMADD213PS //expect: AsmIssue
    VFMADD213SD //expect: AsmIssue
    VFMADD213SS //expect: AsmIssue
    VFMADD231PD //expect: AsmIssue
    VFMADD231PS //expect: AsmIssue
    VFMADD231SD //expect: AsmIssue
    VFMADD231SS //expect: AsmIssue
    VFMADDSUB132PD //expect: AsmIssue
    VFMADDSUB132PS //expect: AsmIssue
    VFMADDSUB213PD //expect: AsmIssue
    VFMADDSUB213PS //expect: AsmIssue
    VFMADDSUB231PD //expect: AsmIssue
    VFMADDSUB231PS //expect: AsmIssue
    VFMSUB132PD //expect: AsmIssue
    VFMSUB132PS //expect: AsmIssue
    VFMSUB132SD //expect: AsmIssue
    VFMSUB132SS //expect: AsmIssue
    VFMSUB213PD //expect: AsmIssue
    VFMSUB213PS //expect: AsmIssue
    VFMSUB213SD //expect: AsmIssue
    VFMSUB213SS //expect: AsmIssue
    VFMSUB231PD //expect: AsmIssue
    VFMSUB231PS //expect: AsmIssue
    VFMSUB231SD //expect: AsmIssue
    VFMSUB231SS //expect: AsmIssue
    VFMSUBADD132PD //expect: AsmIssue
    VFMSUBADD132PS //expect: AsmIssue
    VFMSUBADD213PD //expect: AsmIssue
    VFMSUBADD213PS //expect: AsmIssue
    VFMSUBADD231PD //expect: AsmIssue
    VFMSUBADD231PS //expect: AsmIssue
    VFNMADD132PD //expect: AsmIssue
    VFNMADD132PS //expect: AsmIssue
    VFNMADD132SD //expect: AsmIssue
    VFNMADD132SS //expect: AsmIssue
    VFNMADD213PD //expect: AsmIssue
    VFNMADD213PS //expect: AsmIssue
    VFNMADD213SD //expect: AsmIssue
    VFNMADD213SS //expect: AsmIssue
    VFNMADD231PD //expect: AsmIssue
    VFNMADD231PS //expect: AsmIssue
    VFNMADD231SD //expect: AsmIssue
    VFNMADD231SS //expect: AsmIssue
    VFNMSUB132PD //expect: AsmIssue
    VFNMSUB132PS //expect: AsmIssue
    VFNMSUB132SD //expect: AsmIssue
    VFNMSUB132SS //expect: AsmIssue
    VFNMSUB213PD //expect: AsmIssue
    VFNMSUB213PS //expect: AsmIssue
    VFNMSUB213SD //expect: AsmIssue
    VFNMSUB213SS //expect: AsmIssue
    VFNMSUB231PD //expect: AsmIssue
    VFNMSUB231PS //expect: AsmIssue
    VFNMSUB231SD //expect: AsmIssue
    VFNMSUB231SS //expect: AsmIssue
    VFPCLASSPD //expect: AsmIssue
    VFPCLASSPDX //expect: AsmIssue
    VFPCLASSPDY //expect: AsmIssue
    VFPCLASSPDZ //expect: AsmIssue
    VFPCLASSPS //expect: AsmIssue
    VFPCLASSPSX //expect: AsmIssue
    VFPCLASSPSY //expect: AsmIssue
    VFPCLASSPSZ //expect: AsmIssue
    VFPCLASSSD //expect: AsmIssue
    VFPCLASSSS //expect: AsmIssue
    VGATHERDPD //expect: AsmIssue
    VGATHERDPS //expect: AsmIssue
    VGATHERPF0DPD //expect: AsmIssue
    VGATHERPF0DPS //expect: AsmIssue
    VGATHERPF0QPD //expect: AsmIssue
    VGATHERPF0QPS //expect: AsmIssue
    VGATHERPF1DPD //expect: AsmIssue
    VGATHERPF1DPS //expect: AsmIssue
    VGATHERPF1QPD //expect: AsmIssue
    VGATHERPF1QPS //expect: AsmIssue
    VGATHERQPD //expect: AsmIssue
    VGATHERQPS //expect: AsmIssue
    VGETEXPPD //expect: AsmIssue
    VGETEXPPS //expect: AsmIssue
    VGETEXPSD //expect: AsmIssue
    VGETEXPSS //expect: AsmIssue
    VGETMANTPD //expect: AsmIssue
    VGETMANTPS //expect: AsmIssue
    VGETMANTSD //expect: AsmIssue
    VGETMANTSS //expect: AsmIssue
    VGF2P8AFFINEINVQB //expect: AsmIssue
    VGF2P8AFFINEQB //expect: AsmIssue
    VGF2P8MULB //expect: AsmIssue
    VHADDPD //expect: AsmIssue
    VHADDPS //expect: AsmIssue
    VHSUBPD //expect: AsmIssue
    VHSUBPS //expect: AsmIssue
    VINSERTF128 //expect: AsmIssue
    VINSERTF32X4 //expect: AsmIssue
    VINSERTF32X8 //expect: AsmIssue
    VINSERTF64X2 //expect: AsmIssue
    VINSERTF64X4 //expect: AsmIssue
    VINSERTI128 //expect: AsmIssue
    VINSERTI32X4 //expect: AsmIssue
    VINSERTI32X8 //expect: AsmIssue
    VINSERTI64X2 //expect: AsmIssue
    VINSERTI64X4 //expect: AsmIssue
    VINSERTPS //expect: AsmIssue
    VLDDQU //expect: AsmIssue
    VLDMXCSR //expect: AsmIssue
    VMASKMOVDQU //expect: AsmIssue
    VMASKMOVPD //expect: AsmIssue
    VMASKMOVPS //expect: AsmIssue
    VMAXPD //expect: AsmIssue
    VMAXPS //expect: AsmIssue
    VMAXSD //expect: AsmIssue
    VMAXSS //expect: AsmIssue
    VMINPD //expect: AsmIssue
    VMINPS //expect: AsmIssue
    VMINSD //expect: AsmIssue
    VMINSS //expect: AsmIssue
    VMOVAPD //expect: AsmIssue
    VMOVAPS //expect: AsmIssue
    VMOVDDUP //expect: AsmIssue
    VMOVDQA //expect: AsmIssue
    VMOVDQA32 //expect: AsmIssue
    VMOVDQA64 //expect: AsmIssue
    VMOVDQU //expect: AsmIssue
    VMOVDQU16 //expect: AsmIssue
    VMOVDQU32 //expect: AsmIssue
    VMOVDQU64 //expect: AsmIssue
    VMOVDQU8 //expect: AsmIssue
    VMOVHLPS //expect: AsmIssue
    VMOVHPD //expect: AsmIssue
    VMOVHPS //expect: AsmIssue
    VMOVLHPS //expect: AsmIssue
    VMOVLPD //expect: AsmIssue
    VMOVLPS //expect: AsmIssue
    VMOVMSKPD //expect: AsmIssue
    VMOVMSKPS //expect: AsmIssue
    VMOVNTDQ //expect: AsmIssue
    VMOVNTDQA //expect: AsmIssue
    VMOVNTPD //expect: AsmIssue
    VMOVNTPS //expect: AsmIssue
    VMOVSD //expect: AsmIssue
    VMOVSHDUP //expect: AsmIssue
    VMOVSLDUP //expect: AsmIssue
    VMOVSS //expect: AsmIssue
    VMOVUPD //expect: AsmIssue
    VMOVUPS //expect: AsmIssue
    VMPSADBW //expect: AsmIssue
    VMULPD //expect: AsmIssue
    VMULPS //expect: AsmIssue
    VMULSD //expect: AsmIssue
    VMULSS //expect: AsmIssue
    VORPD //expect: AsmIssue
    VORPS //expect: AsmIssue
    VP4DPWSSD //expect: AsmIssue
    VP4DPWSSDS //expect: AsmIssue
    VPABSB //expect: AsmIssue
    VPABSD //expect: AsmIssue
    VPABSQ //expect: AsmIssue
    VPABSW //expect: AsmIssue
    VPACKSSDW //expect: AsmIssue
    VPACKSSWB //expect: AsmIssue
    VPACKUSDW //expect: AsmIssue
    VPACKUSWB //expect: AsmIssue
    VPADDB //expect: AsmIssue
    VPADDD //expect: AsmIssue
    VPADDQ //expect: AsmIssue
    VPADDSB //expect: AsmIssue
    VPADDSW //expect: AsmIssue
    VPADDUSB //expect: AsmIssue
    VPADDUSW //expect: AsmIssue
    VPADDW //expect: AsmIssue
    VPALIGNR //expect: AsmIssue
    VPAND //expect: AsmIssue
    VPANDD //expect: AsmIssue
    VPANDN //expect: AsmIssue
    VPANDND //expect: AsmIssue
    VPANDNQ //expect: AsmIssue
    VPANDQ //expect: AsmIssue
    VPAVGB //expect: AsmIssue
    VPAVGW //expect: AsmIssue
    VPBLENDD //expect: AsmIssue
    VPBLENDMB //expect: AsmIssue
    VPBLENDMD //expect: AsmIssue
    VPBLENDMQ //expect: AsmIssue
    VPBLENDMW //expect: AsmIssue
    VPBLENDVB //expect: AsmIssue
    VPBLENDW //expect: AsmIssue
    VPBROADCASTB //expect: AsmIssue
    VPBROADCASTD //expect: AsmIssue
    VPBROADCASTMB2Q //expect: AsmIssue
    VPBROADCASTMW2D //expect: AsmIssue
    VPBROADCASTQ //expect: AsmIssue
    VPBROADCASTW //expect: AsmIssue
    VPCLMULQDQ //expect: AsmIssue
    VPCMPB //expect: AsmIssue
    VPCMPD //expect: AsmIssue
    VPCMPEQB //expect: AsmIssue
    VPCMPEQD //expect: AsmIssue
    VPCMPEQQ //expect: AsmIssue
    VPCMPEQW //expect: AsmIssue
    VPCMPESTRI //expect: AsmIssue
    VPCMPESTRM //expect: AsmIssue
    VPCMPGTB //expect: AsmIssue
    VPCMPGTD //expect: AsmIssue
    VPCMPGTQ //expect: AsmIssue
    VPCMPGTW //expect: AsmIssue
    VPCMPISTRI //expect: AsmIssue
    VPCMPISTRM //expect: AsmIssue
    VPCMPQ //expect: AsmIssue
    VPCMPUB //expect: AsmIssue
    VPCMPUD //expect: AsmIssue
    VPCMPUQ //expect: AsmIssue
    VPCMPUW //expect: AsmIssue
    VPCMPW //expect: AsmIssue
    VPCOMPRESSB //expect: AsmIssue
    VPCOMPRESSD //expect: AsmIssue
    VPCOMPRESSQ //expect: AsmIssue
    VPCOMPRESSW //expect: AsmIssue
    VPCONFLICTD //expect: AsmIssue
    VPCONFLICTQ //expect: AsmIssue
    VPDPBUSD //expect: AsmIssue
    VPDPBUSDS //expect: AsmIssue
    VPDPWSSD //expect: AsmIssue
    VPDPWSSDS //expect: AsmIssue
    VPERM2F128 //expect: AsmIssue
    VPERM2I128 //expect: AsmIssue
    VPERMB //expect: AsmIssue
    VPERMD //expect: AsmIssue
    VPERMI2B //expect: AsmIssue
    VPERMI2D //expect: AsmIssue
    VPERMI2PD //expect: AsmIssue
    VPERMI2PS //expect: AsmIssue
    VPERMI2Q //expect: AsmIssue
    VPERMI2W //expect: AsmIssue
    VPERMILPD //expect: AsmIssue
    VPERMILPS //expect: AsmIssue
    VPERMPD //expect: AsmIssue
    VPERMPS //expect: AsmIssue
    VPERMQ //expect: AsmIssue
    VPERMT2B //expect: AsmIssue
    VPERMT2D //expect: AsmIssue
    VPERMT2PD //expect: AsmIssue
    VPERMT2PS //expect: AsmIssue
    VPERMT2Q //expect: AsmIssue
    VPERMT2W //expect: AsmIssue
    VPERMW //expect: AsmIssue
    VPEXPANDB //expect: AsmIssue
    VPEXPANDD //expect: AsmIssue
    VPEXPANDQ //expect: AsmIssue
    VPEXPANDW //expect: AsmIssue
    VPEXTRB //expect: AsmIssue
    VPEXTRD //expect: AsmIssue
    VPEXTRQ //expect: AsmIssue
    VPEXTRW //expect: AsmIssue
    VPGATHERDD //expect: AsmIssue
    VPGATHERDQ //expect: AsmIssue
    VPGATHERQD //expect: AsmIssue
    VPGATHERQQ //expect: AsmIssue
    VPHADDD //expect: AsmIssue
    VPHADDSW //expect: AsmIssue
    VPHADDW //expect: AsmIssue
    VPHMINPOSUW //expect: AsmIssue
    VPHSUBD //expect: AsmIssue
    VPHSUBSW //expect: AsmIssue
    VPHSUBW //expect: AsmIssue
    VPINSRB //expect: AsmIssue
    VPINSRD //expect: AsmIssue
    VPINSRQ //expect: AsmIssue
    VPINSRW //expect: AsmIssue
    VPLZCNTD //expect: AsmIssue
    VPLZCNTQ //expect: AsmIssue
    VPMADD52HUQ //expect: AsmIssue
    VPMADD52LUQ //expect: AsmIssue
    VPMADDUBSW //expect: AsmIssue
    VPMADDWD //expect: AsmIssue
    VPMASKMOVD //expect: AsmIssue
    VPMASKMOVQ //expect: AsmIssue
    VPMAXSB //expect: AsmIssue
    VPMAXSD //expect: AsmIssue
    VPMAXSQ //expect: AsmIssue
    VPMAXSW //expect: AsmIssue
    VPMAXUB //expect: AsmIssue
    VPMAXUD //expect: AsmIssue
    VPMAXUQ //expect: AsmIssue
    VPMAXUW //expect: AsmIssue
    VPMINSB //expect: AsmIssue
    VPMINSD //expect: AsmIssue
    VPMINSQ //expect: AsmIssue
    VPMINSW //expect: AsmIssue
    VPMINUB //expect: AsmIssue
    VPMINUD //expect: AsmIssue
    VPMINUQ //expect: AsmIssue
    VPMINUW //expect: AsmIssue
    VPMOVB2M //expect: AsmIssue
    VPMOVD2M //expect: AsmIssue
    VPMOVDB //expect: AsmIssue
    VPMOVDW //expect: AsmIssue
    VPMOVM2B //expect: AsmIssue
    VPMOVM2D //expect: AsmIssue
    VPMOVM2Q //expect: AsmIssue
    VPMOVM2W //expect: AsmIssue
    VPMOVMSKB //expect: AsmIssue
    VPMOVQ2M //expect: AsmIssue
    VPMOVQB //expect: AsmIssue
    VPMOVQD //expect: AsmIssue
    VPMOVQW //expect: AsmIssue
    VPMOVSDB //expect: AsmIssue
    VPMOVSDW //expect: AsmIssue
    VPMOVSQB //expect: AsmIssue
    VPMOVSQD //expect: AsmIssue
    VPMOVSQW //expect: AsmIssue
    VPMOVSWB //expect: AsmIssue
    VPMOVSXBD //expect: AsmIssue
    VPMOVSXBQ //expect: AsmIssue
    VPMOVSXBW //expect: AsmIssue
    VPMOVSXDQ //expect: AsmIssue
    VPMOVSXWD //expect: AsmIssue
    VPMOVSXWQ //expect: AsmIssue
    VPMOVUSDB //expect: AsmIssue
    VPMOVUSDW //expect: AsmIssue
    VPMOVUSQB //expect: AsmIssue
    VPMOVUSQD //expect: AsmIssue
    VPMOVUSQW //expect: AsmIssue
    VPMOVUSWB //expect: AsmIssue
    VPMOVW2M //expect: AsmIssue
    VPMOVWB //expect: AsmIssue
    VPMOVZXBD //expect: AsmIssue
    VPMOVZXBQ //expect: AsmIssue
    VPMOVZXBW //expect: AsmIssue
    VPMOVZXDQ //expect: AsmIssue
    VPMOVZXWD //expect: AsmIssue
    VPMOVZXWQ //expect: AsmIssue
    VPMULDQ //expect: AsmIssue
    VPMULHRSW //expect: AsmIssue
    VPMULHUW //expect: AsmIssue
    VPMULHW //expect: AsmIssue
    VPMULLD //expect: AsmIssue
    VPMULLQ //expect: AsmIssue
    VPMULLW //expect: AsmIssue
    VPMULTISHIFTQB //expect: AsmIssue
    VPMULUDQ //expect: AsmIssue
    VPOPCNTB //expect: AsmIssue
    VPOPCNTD //expect: AsmIssue
    VPOPCNTQ //expect: AsmIssue
    VPOPCNTW //expect: AsmIssue
    VPOR //expect: AsmIssue
    VPORD //expect: AsmIssue
    VPORQ //expect: AsmIssue
    VPROLD //expect: AsmIssue
    VPROLQ //expect: AsmIssue
    VPROLVD //expect: AsmIssue
    VPROLVQ //expect: AsmIssue
    VPRORD //expect: AsmIssue
    VPRORQ //expect: AsmIssue
    VPRORVD //expect: AsmIssue
    VPRORVQ //expect: AsmIssue
    VPSADBW //expect: AsmIssue
    VPSCATTERDD //expect: AsmIssue
    VPSCATTERDQ //expect: AsmIssue
    VPSCATTERQD //expect: AsmIssue
    VPSCATTERQQ //expect: AsmIssue
    VPSHLDD //expect: AsmIssue
    VPSHLDQ //expect: AsmIssue
    VPSHLDVD //expect: AsmIssue
    VPSHLDVQ //expect: AsmIssue
    VPSHLDVW //expect: AsmIssue
    VPSHLDW //expect: AsmIssue
    VPSHRDD //expect: AsmIssue
    VPSHRDQ //expect: AsmIssue
    VPSHRDVD //expect: AsmIssue
    VPSHRDVQ //expect: AsmIssue
    VPSHRDVW //expect: AsmIssue
    VPSHRDW //expect: AsmIssue
    VPSHUFB //expect: AsmIssue
    VPSHUFBITQMB //expect: AsmIssue
    VPSHUFD //expect: AsmIssue
    VPSHUFHW //expect: AsmIssue
    VPSHUFLW //expect: AsmIssue
    VPSIGNB //expect: AsmIssue
    VPSIGND //expect: AsmIssue
    VPSIGNW //expect: AsmIssue
    VPSLLD //expect: AsmIssue
    VPSLLDQ //expect: AsmIssue
    VPSLLQ //expect: AsmIssue
    VPSLLVD //expect: AsmIssue
    VPSLLVQ //expect: AsmIssue
    VPSLLVW //expect: AsmIssue
    VPSLLW //expect: AsmIssue
    VPSRAD //expect: AsmIssue
    VPSRAQ //expect: AsmIssue
    VPSRAVD //expect: AsmIssue
    VPSRAVQ //expect: AsmIssue
    VPSRAVW //expect: AsmIssue
    VPSRAW //expect: AsmIssue
    VPSRLD //expect: AsmIssue
    VPSRLDQ //expect: AsmIssue
    VPSRLQ //expect: AsmIssue
    VPSRLVD //expect: AsmIssue
    VPSRLVQ //expect: AsmIssue
    VPSRLVW //expect: AsmIssue
    VPSRLW //expect: AsmIssue
    VPSUBB //expect: AsmIssue
    VPSUBD //expect: AsmIssue
    VPSUBQ //expect: AsmIssue
    VPSUBSB //expect: AsmIssue
    VPSUBSW //expect: AsmIssue
    VPSUBUSB //expect: AsmIssue
    VPSUBUSW //expect: AsmIssue
    VPSUBW //expect: AsmIssue
    VPTERNLOGD //expect: AsmIssue
    VPTERNLOGQ //expect: AsmIssue
    VPTEST //expect: AsmIssue
    VPTESTMB //expect: AsmIssue
    VPTESTMD //expect: AsmIssue
    VPTESTMQ //expect: AsmIssue
    VPTESTMW //expect: AsmIssue
    VPTESTNMB //expect: AsmIssue
    VPTESTNMD //expect: AsmIssue
    VPTESTNMQ //expect: AsmIssue
    VPTESTNMW //expect: AsmIssue
    VPUNPCKHBW //expect: AsmIssue
    VPUNPCKHDQ //expect: AsmIssue
    VPUNPCKHQDQ //expect: AsmIssue
    VPUNPCKHWD //expect: AsmIssue
    VPUNPCKLBW //expect: AsmIssue
    VPUNPCKLDQ //expect: AsmIssue
    VPUNPCKLQDQ //expect: AsmIssue
    VPUNPCKLWD //expect: AsmIssue
    VPXOR //expect: AsmIssue
    VPXORD //expect: AsmIssue
    VPXORQ //expect: AsmIssue
    VRANGEPD //expect: AsmIssue
    VRANGEPS //expect: AsmIssue
    VRANGESD //expect: AsmIssue
    VRANGESS //expect: AsmIssue
    VRCP14PD //expect: AsmIssue
    VRCP14PS //expect: AsmIssue
    VRCP14SD //expect: AsmIssue
    VRCP14SS //expect: AsmIssue
    VRCP28PD //expect: AsmIssue
    VRCP28PS //expect: AsmIssue
    VRCP28SD //expect: AsmIssue
    VRCP28SS //expect: AsmIssue
    VRCPPS //expect: AsmIssue
    VRCPSS //expect: AsmIssue
    VREDUCEPD //expect: AsmIssue
    VREDUCEPS //expect: AsmIssue
    VREDUCESD //expect: AsmIssue
    VREDUCESS //expect: AsmIssue
    VRNDSCALEPD //expect: AsmIssue
    VRNDSCALEPS //expect: AsmIssue
    VRNDSCALESD //expect: AsmIssue
    VRNDSCALESS //expect: AsmIssue
    VROUNDPD //expect: AsmIssue
    VROUNDPS //expect: AsmIssue
    VROUNDSD //expect: AsmIssue
    VROUNDSS //expect: AsmIssue
    VRSQRT14PD //expect: AsmIssue
    VRSQRT14PS //expect: AsmIssue
    VRSQRT14SD //expect: AsmIssue
    VRSQRT14SS //expect: AsmIssue
    VRSQRT28PD //expect: AsmIssue
    VRSQRT28PS //expect: AsmIssue
    VRSQRT28SD //expect: AsmIssue
    VRSQRT28SS //expect: AsmIssue
    VRSQRTPS //expect: AsmIssue
    VRSQRTSS //expect: AsmIssue
    VSCALEFPD //expect: AsmIssue
    VSCALEFPS //expect: AsmIssue
    VSCALEFSD //expect: AsmIssue
    VSCALEFSS //expect: AsmIssue
    VSCATTERDPD //expect: AsmIssue
    VSCATTERDPS //expect: AsmIssue
    VSCATTERPF0DPD //expect: AsmIssue
    VSCATTERPF0DPS //expect: AsmIssue
    VSCATTERPF0QPD //expect: AsmIssue
    VSCATTERPF0QPS //expect: AsmIssue
    VSCATTERPF1DPD //expect: AsmIssue
    VSCATTERPF1DPS //expect: AsmIssue
    VSCATTERPF1QPD //expect: AsmIssue
    VSCATTERPF1QPS //expect: AsmIssue
    VSCATTERQPD //expect: AsmIssue
    VSCATTERQPS //expect: AsmIssue
    VSHUFF32X4 //expect: AsmIssue
    VSHUFF64X2 //expect: AsmIssue
    VSHUFI32X4 //expect: AsmIssue
    VSHUFI64X2 //expect: AsmIssue
    VSHUFPD //expect: AsmIssue
    VSHUFPS //expect: AsmIssue
    VSQRTPD //expect: AsmIssue
    VSQRTPS //expect: AsmIssue
    VSQRTSD //expect: AsmIssue
    VSQRTSS //expect: AsmIssue
    VSTMXCSR //expect: AsmIssue
    VSUBPD //expect: AsmIssue
    VSUBPS //expect: AsmIssue
    VSUBSD //expect: AsmIssue
    VSUBSS //expect: AsmIssue
    VTESTPD //expect: AsmIssue
    VTESTPS //expect: AsmIssue
    VUCOMISD //expect: AsmIssue
    VUCOMISS //expect: AsmIssue
    VUNPCKHPD //expect: AsmIssue
    VUNPCKHPS //expect: AsmIssue
    VUNPCKLPD //expect: AsmIssue
    VUNPCKLPS //expect: AsmIssue
    VXORPD //expect: AsmIssue
    VXORPS //expect: AsmIssue
    VZEROALL //expect: AsmIssue
    VZEROUPPER //expect: AsmIssue
    WAIT //expect: AsmIssue
    WBINVD //expect: AsmIssue
    WRFSBASEL //expect: AsmIssue
    WRFSBASEQ //expect: AsmIssue
    WRGSBASEL //expect: AsmIssue
    WRGSBASEQ //expect: AsmIssue
    WRMSR //expect: AsmIssue
    WRPKRU //expect: AsmIssue
    XABORT //expect: AsmIssue
    XACQUIRE //expect: AsmIssue
    XADDB //expect: AsmIssue
    XADDL //expect: AsmIssue
    XADDQ //expect: AsmIssue
    XADDW //expect: AsmIssue
    XBEGIN //expect: AsmIssue
    XCHGB //expect: AsmIssue
    XCHGL //expect: AsmIssue
    XCHGQ //expect: AsmIssue
    XCHGW //expect: AsmIssue
    XEND //expect: AsmIssue
    XGETBV //expect: AsmIssue
    XLAT //expect: AsmIssue
    XORB //expect: AsmIssue
    XORL //expect: AsmIssue
    XORPD //expect: AsmIssue
    XORPS //expect: AsmIssue
    XORQ //expect: AsmIssue
    XORW //expect: AsmIssue
    XRELEASE //expect: AsmIssue
    XRSTOR //expect: AsmIssue
    XRSTOR64 //expect: AsmIssue
    XRSTORS //expect: AsmIssue
    XRSTORS64 //expect: AsmIssue
    XSAVE //expect: AsmIssue
    XSAVE64 //expect: AsmIssue
    XSAVEC //expect: AsmIssue
    XSAVEC64 //expect: AsmIssue
    XSAVEOPT //expect: AsmIssue
    XSAVEOPT64 //expect: AsmIssue
    XSAVES //expect: AsmIssue
    XSAVES64 //expect: AsmIssue
    XSETBV //expect: AsmIssue
    XTEST //expect: AsmIssue

// PLAN9_GOLANG_AARCH64
    RSB
    RSC
    TEQ
    MOVWD
    MOVWF
    MOVDW
    MOVFW
    MOVFD
    MOVDF
    CMPF
    CMPD
    ADDF
    ADDD
    SUBF
    SUBD
    MULF
    MULD
    NMULF
    NMULD
    MULAF
    MULAD
    NMULAF
    NMULAD
    MULSF
    NMULSF
    NMULSD
    FMULAF
    FMULAD
    FNMULAF
    FNMULAD
    FMULSF
    FMULSD
    FNMULSF
    FNMULSD
    DIVF
    DIVD
    SQRTF
    SQRTD
    ABSF
    ABSD
    NEGF
    NEGD
    MULU
    DIVU
    MMUL
    DIV
    MOD
    MODU
    DIVHW
    DIVUHW
    MOVBS
    MOVHS
    MOVM
    SWPBU
    RFE
    SWI
    MULA
    MULS
    MMULA
    MMULS
    MULAL
    MULLU
    MULALU
    BX
    BXRET
    LDREX
    STREX
    LDREXD
    STREXD
    PLD
    REVSH
    XTAB
    XTAH
    XTABU
    XTAHU
    BFX
    BFXU
    BFC
    MULWT
    MULWB
    MULBB
    MULAWT
    MULAWB
    MULABB
    MRC
    ADC
    ADCS
    ADCSW
    ADD
    ADDS
    ADDSW
    ADR
    ADRP
    ANDS
    ANDSW
    ASR
    ASRW
    AT
    BFI
    BFIW
    BFM
    BFMW
    BFXIL
    BFXILW
    BICS
    BICSW
    BICW
    BRK
    CBNZ
    CBNZW
    CBZ
    CBZW
    CCMN
    CCMNW
    CCMP
    CCMPW
    CINC
    CINCW
    CINV
    CINVW
    CLREX
    CLS
    CLSW
    CLZ
    CLZW
    CMN
    CMNW
    CMP
    CNEG
    CNEGW
    CRC32CB
    CRC32CH
    CRC32CW
    CRC32CX
    CRC32H
    CRC32X
    CSEL
    CSELW
    CSET
    CSETM
    CSETMW
    CSETW
    CSINC
    CSINCW
    CSINV
    CSINVW
    CSNEG
    CSNEGW
    DC
    DCPS1
    DCPS2
    DCPS3
    DMB
    DRPS
    DSB
    EON
    EONW
    EOR
    EORW
    ERET
    EXTR
    EXTRW
    HINT
    HVC
    IC
    ISB
    LDADDAB
    LDADDAD
    LDADDAH
    LDADDAW
    LDADDALB
    LDADDALD
    LDADDALH
    LDADDALW
    LDADDB
    LDADDD
    LDADDH
    LDADDW
    LDADDLB
    LDADDLD
    LDADDLH
    LDADDLW
    LDAR
    LDARB
    LDARH
    LDARW
    LDAXP
    LDAXPW
    LDAXR
    LDAXRB
    LDAXRH
    LDAXRW
    LDCLRAB
    LDCLRAD
    LDCLRAH
    LDCLRAW
    LDCLRALB
    LDCLRALD
    LDCLRALH
    LDCLRALW
    LDCLRB
    LDCLRD
    LDCLRH
    LDCLRW
    LDCLRLB
    LDCLRLD
    LDCLRLH
    LDCLRLW
    LDEORAB
    LDEORAD
    LDEORAH
    LDEORAW
    LDEORALB
    LDEORALD
    LDEORALH
    LDEORALW
    LDEORB
    LDEORD
    LDEORH
    LDEORW
    LDEORLB
    LDEORLD
    LDEORLH
    LDEORLW
    LDORAB
    LDORAD
    LDORAH
    LDORAW
    LDORALB
    LDORALD
    LDORALH
    LDORALW
    LDORB
    LDORD
    LDORH
    LDORW
    LDORLB
    LDORLD
    LDORLH
    LDORLW
    LDP
    LDPW
    LDPSW
    LDXR
    LDXRB
    LDXRH
    LDXRW
    LDXP
    LDXPW
    LSL
    LSR
    LSRW
    MADD
    MADDW
    MNEG
    MNEGW
    MOVK
    MOVKW
    MOVN
    MOVNW
    MOVZ
    MOVZW
    MRS
    MSR
    MSUB
    MSUBW
    MUL
    MVN
    MVNW
    NEG
    NEGS
    NEGSW
    NGC
    NGCS
    NGCSW
    NGCW
    ORN
    ORNW
    ORR
    ORRW
    PRFM
    PRFUM
    RBIT
    RBITW
    REM
    REMW
    REV
    REV16
    REV16W
    REV32
    REVW
    ROR
    SBC
    SBCS
    SBCSW
    SBCW
    SBFIZ
    SBFIZW
    SBFM
    SBFMW
    SBFX
    SBFXW
    SDIV
    SDIVW
    SEV
    SEVL
    SMADDL
    SMC
    SMNEGL
    SMSUBL
    SMULH
    SMULL
    STXR
    STXRB
    STXRH
    STXP
    STXPW
    STXRW
    STLP
    STLPW
    STLR
    STLRB
    STLRH
    STLRW
    STLXP
    STLXPW
    STLXR
    STLXRB
    STLXRH
    STLXRW
    STP
    STPW
    SUB
    SUBS
    SUBSW
    SVC
    SXTB
    SXTBW
    SXTH
    SXTHW
    SXTW
    SYS
    SYSL
    TBNZ
    TBZ
    TLBI
    TST
    TSTW
    UBFIZ
    UBFIZW
    UBFM
    UBFMW
    UBFX
    UBFXW
    UDIV
    UDIVW
    UMADDL
    UMNEGL
    UMSUBL
    UMULL
    UREM
    UREMW
    UXTB
    UXTH
    UXTW
    UXTBW
    UXTHW
    WFE
    WFI
    YIELD
    MOVNP
    MOVNPW
    MOVP
    MOVPD
    MOVPQ
    MOVPS
    MOVPSW
    MOVPW
    SWPAD
    SWPAW
    SWPAH
    SWPAB
    SWPALD
    SWPALW
    SWPALH
    SWPALB
    SWPD
    SWPW
    SWPH
    SWPB
    SWPLD
    SWPLW
    SWPLH
    SWPLB
    CASD
    CASW
    CASH
    CASB
    CASAD
    CASAW
    CASLD
    CASLW
    CASALD
    CASALW
    CASALH
    CASALB
    CASPD
    CASPW
    BCS
    BHS
    BCC
    BLO
    BMI
    BPL
    BVS
    BVC
    BHI
    BLS
    FABSD
    FABSS
    FCCMPD
    FCCMPED
    FCCMPS
    FCCMPES
    FCMPD
    FCMPED
    FCMPES
    FCMPS
    FCVTZSD
    FCVTZSDW
    FCVTZSS
    FCVTZSSW
    FCVTZUD
    FCVTZUDW
    FCVTZUS
    FCVTZUSW
    FLDPD
    FLDPS
    FMOVQ
    FMOVS
    VMOVS
    FNEGD
    FNEGS
    FSTPD
    FSTPS
    SCVTFD
    SCVTFS
    SCVTFWD
    SCVTFWS
    UCVTFD
    UCVTFS
    UCVTFWD
    UCVTFWS
    DWORD
    FCSELS
    FCSELD
    FMAXS
    FMINS
    FMAXD
    FMIND
    FMAXNMS
    FMAXNMD
    FNMULS
    FNMULD
    FRINTNS
    FRINTND
    FRINTPS
    FRINTPD
    FRINTMS
    FRINTMD
    FRINTZS
    FRINTZD
    FRINTAS
    FRINTAD
    FRINTXS
    FRINTXD
    FRINTIS
    FRINTID
    FMADDS
    FMADDD
    FMSUBS
    FMSUBD
    FNMADDS
    FNMADDD
    FNMSUBS
    FNMSUBD
    FMINNMS
    FMINNMD
    FCVTDH
    FCVTHS
    FCVTHD
    FCVTSH
    AESD
    AESE
    AESMC
    SHA1C
    SHA1H
    SHA1M
    SHA1P
    SHA1SU0
    SHA1SU1
    SHA256H
    SHA256H2
    SHA256SU0
    SHA256SU1
    SHA512H
    SHA512H2
    SHA512SU0
    SHA512SU1
    VADD
    VADDP
    VAND
    VBIF
    VBCAX
    VCMEQ
    VCNT
    VEOR
    VEOR3
    VMOV
    VLD1
    VLD2
    VLD3
    VLD4
    VLD1R
    VLD2R
    VLD3R
    VLD4R
    VORR
    VREV16
    VREV32
    VREV64
    VST1
    VST2
    VST3
    VST4
    VDUP
    VADDV
    VMOVI
    VUADDLV
    VSUB
    VFMLA
    VFMLS
    VPMULL
    VPMULL2
    VEXT
    VRBIT
    VRAX1
    VUSHR
    VUSHLL
    VUSHLL2
    VUXTL
    VUXTL2
    VUZP1
    VUZP2
    VSHL
    VSRI
    VSLI
    VBSL
    VBIT
    VTBL
    VXAR
    VZIP1
    VZIP2
    VCMTST
    VUADDW2
    VUADDW
    VUSRA
    BEQ
    BNE
    BLT
    BLE
    BGT
    BGE
    MOVBU
    MOVH
    MOVHU
    MOVWU
    MOVF
    MOVD
    UMULH
    FADDS
    FSUBS
    FMULS
    FDIVS
    FCVTSD
    FCVTDS
    FSQRTS
    FSQRTD
    AND
    BIC
    SLL
    SRL
    SRA
    NOOP
