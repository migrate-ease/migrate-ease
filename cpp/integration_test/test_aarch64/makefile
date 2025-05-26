CC := gcc
CFLAGS := -Wl,-Bdynamic

# scanner: arch specifc libs
LIBS := 'mkl'  //expect: ArchSpecificLibraryIssue
LIBS += 'otherarch'  //expect: ArchSpecificLibraryIssue

	$(CC) -static -$(LIBS)
	$(CC) -static -mkl //expect: ArchSpecificLibraryIssue
	$(CC) $(LIBS).a
	$(CC) mkl.a //expect: ArchSpecificLibraryIssue
	$(CC) -Wl,-Bstatic -$(LIBS)
	$(CC) -Wl,-Bstatic -mkl //expect: ArchSpecificLibraryIssue
	$(CC) -Wl,-Bdynamic -$(LIBS)
	$(CC) -Wl,-Bdynamic -mkl //expect: ArchSpecificLibraryIssue
	$(CC) $(CFLAGS) -$(LIBS)
	$(CC) $(CFLAGS) -mkl //expect: ArchSpecificLibraryIssue

	$(CC) -static -$(LIBS)
	$(CC) -static -otherarch //expect: ArchSpecificLibraryIssue
	$(CC) $(LIBS).a
	$(CC) otherarch.a //expect: ArchSpecificLibraryIssue
	$(CC) -Wl,-Bstatic -$(LIBS)
	$(CC) -Wl,-Bstatic -otherarch //expect: ArchSpecificLibraryIssue
	$(CC) -Wl,-Bdynamic -$(LIBS)
	$(CC) -Wl,-Bdynamic -otherarch //expect: ArchSpecificLibraryIssue
	$(CC) $(CFLAGS) -$(LIBS)
	$(CC) $(CFLAGS) -otherarch //expect: ArchSpecificLibraryIssue


# scanner: C Runtime Lib
LIBS=libfoo.lib
LIBS=libcmt.lib // works only when --target-os: windows
LIBS=libcmtd.lib // works only when --target-os: windows

# scanner: other PROCESSOR_ARCHITECTURE archs related lines
	$(CPU) == "amd64"  //expect: HostCpuDetectionIssue
	$(CPU) == "x86_64"  //expect: HostCpuDetectionIssue
	$(CPU) == "x86-64"  //expect: HostCpuDetectionIssue
	$(CPU) == "x86"  //expect: HostCpuDetectionIssue
	$(CPU) == "x64"  //expect: HostCpuDetectionIssue
	$(CPU) == "amd64"  //expect: HostCpuDetectionIssue
	$(CPU) == "avx"  //expect: HostCpuDetectionIssue
	$(CPU) == "avx2"  //expect: HostCpuDetectionIssue
	$(CPU) == "avx512"  //expect: HostCpuDetectionIssue
	$(CPU) == "i386"  //expect: HostCpuDetectionIssue
	$(CPU) == "i586"  //expect: HostCpuDetectionIssue
	$(CPU) == "i686"  //expect: HostCpuDetectionIssue
	$(CPU) == "ia32"  //expect: HostCpuDetectionIssue
	$(CPU) == "ia64"  //expect: HostCpuDetectionIssue
	$(CPU) == "intel"  //expect: HostCpuDetectionIssue
	$(CPU) == "intel64"  //expect: HostCpuDetectionIssue
	$(CPU) == "m68k"  //expect: HostCpuDetectionIssue
	$(CPU) == "sse5"  //expect: HostCpuDetectionIssue
	$(CPU) == "sse4.2"  //expect: HostCpuDetectionIssue
	$(CPU) == "sse4.1"  //expect: HostCpuDetectionIssue
	$(CPU) == "sse4"  //expect: HostCpuDetectionIssue
	$(CPU) == "sse3"  //expect: HostCpuDetectionIssue
	$(CPU) == "sse2"  //expect: HostCpuDetectionIssue
	$(CPU) == "sse"  //expect: HostCpuDetectionIssue
	$(CPU) == "alpha"  //expect: HostCpuDetectionIssue
	$(CPU) == "altivec"  //expect: HostCpuDetectionIssue
	$(CPU) == "hppa"  //expect: HostCpuDetectionIssue
	$(CPU) == "ix86"  //expect: HostCpuDetectionIssue
	$(CPU) == "microblaze"  //expect: HostCpuDetectionIssue
	$(CPU) == "mips"  //expect: HostCpuDetectionIssue
	$(CPU) == "nios2"  //expect: HostCpuDetectionIssue
	$(CPU) == "power"  //expect: HostCpuDetectionIssue
	$(CPU) == "powerpc"  //expect: HostCpuDetectionIssue
	$(CPU) == "powerpc32"  //expect: HostCpuDetectionIssue
	$(CPU) == "powerpc64"  //expect: HostCpuDetectionIssue
	$(CPU) == "ppc64le"  //expect: HostCpuDetectionIssue
	$(CPU) == "ppc64"  //expect: HostCpuDetectionIssue
	$(CPU) == "ppc"  //expect: HostCpuDetectionIssue
	$(CPU) == "s390"  //expect: HostCpuDetectionIssue
	$(CPU) == "sh"  //expect: HostCpuDetectionIssue
	$(CPU) == "sparc"  //expect: HostCpuDetectionIssue
	$(CPU) == "tile"  //expect: HostCpuDetectionIssue

	$(PROCESSOR_ARCHITECTURE) == "amd64"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "x86_64"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "x86-64"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "x86"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "x64"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "amd64"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "avx"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "avx2"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "avx512"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "i386"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "i586"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "i686"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "ia32"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "ia64"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "intel"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "intel64"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "m68k"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "sse5"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "sse4.2"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "sse4.1"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "sse4"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "sse3"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "sse2"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "sse"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "x86_6"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "alpha"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "altivec"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "hppa"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "ix86"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "microblaze"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "mips"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "nios2"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "power"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "powerpc"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "powerpc32"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "powerpc64"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "ppc64le"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "ppc64"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "ppc"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "s390"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "sh"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "sparc"  //expect: HostCpuDetectionIssue
	$(PROCESSOR_ARCHITECTURE) == "tile"  //expect: HostCpuDetectionIssue

# scanner: non-ARM/ARM64 architecture macro definition
	-Damd64  //expect: DefineOtherArchIssue
	-Dx86_64  //expect: DefineOtherArchIssue
	-Dx86-64  //expect: DefineOtherArchIssue
	-Dx86  //expect: DefineOtherArchIssue
	-Dx64  //expect: DefineOtherArchIssue
	-Damd64  //expect: DefineOtherArchIssue
	-Davx  //expect: DefineOtherArchIssue
	-Davx2  //expect: DefineOtherArchIssue
	-Davx512  //expect: DefineOtherArchIssue
	-Di386  //expect: DefineOtherArchIssue
	-Di586  //expect: DefineOtherArchIssue
	-Di686  //expect: DefineOtherArchIssue
	-Dia32  //expect: DefineOtherArchIssue
	-Dia64  //expect: DefineOtherArchIssue
	-Dintel  //expect: DefineOtherArchIssue
	-Dintel64  //expect: DefineOtherArchIssue
	-Dm68k  //expect: DefineOtherArchIssue
	-Dsse5  //expect: DefineOtherArchIssue
	-Dsse4.2  //expect: DefineOtherArchIssue
	-Dsse4.1  //expect: DefineOtherArchIssue
	-Dsse4  //expect: DefineOtherArchIssue
	-Dsse3  //expect: DefineOtherArchIssue
	-Dsse2  //expect: DefineOtherArchIssue
	-Dsse  //expect: DefineOtherArchIssue
	-Dalpha  //expect: DefineOtherArchIssue
	-Daltivec  //expect: DefineOtherArchIssue
	-Dhppa  //expect: DefineOtherArchIssue
	-Dix86  //expect: DefineOtherArchIssue
	-Dmicroblaze  //expect: DefineOtherArchIssue
	-Dmips  //expect: DefineOtherArchIssue
	-Dnios2  //expect: DefineOtherArchIssue
	-Dpower  //expect: DefineOtherArchIssue
	-Dpowerpc  //expect: DefineOtherArchIssue
	-Dpowerpc32  //expect: DefineOtherArchIssue
	-Dpowerpc64  //expect: DefineOtherArchIssue
	-Dppc64le  //expect: DefineOtherArchIssue
	-Dppc64  //expect: DefineOtherArchIssue
	-Dppc  //expect: DefineOtherArchIssue
	-Ds390  //expect: DefineOtherArchIssue
	-Dsh  //expect: DefineOtherArchIssue
	-Dsparc  //expect: DefineOtherArchIssue
	-Dtile  //expect: DefineOtherArchIssue

	-DAMD64  //expect: DefineOtherArchIssue
	-Dx86_64  //expect: DefineOtherArchIssue
	-Dx86-64  //expect: DefineOtherArchIssue
	-Dx86  //expect: DefineOtherArchIssue
	-Dx64  //expect: DefineOtherArchIssue
	-DAMD64  //expect: DefineOtherArchIssue
	-DAVX  //expect: DefineOtherArchIssue
	-DAVX2  //expect: DefineOtherArchIssue
	-DAVX512  //expect: DefineOtherArchIssue
	-DI386  //expect: DefineOtherArchIssue
	-DI586  //expect: DefineOtherArchIssue
	-DI686  //expect: DefineOtherArchIssue
	-DIA32  //expect: DefineOtherArchIssue
	-DIA64  //expect: DefineOtherArchIssue
	-DINTEL  //expect: DefineOtherArchIssue
	-DINTEL64  //expect: DefineOtherArchIssue
	-DM68K  //expect: DefineOtherArchIssue
	-DSSE5  //expect: DefineOtherArchIssue
	-DSSE4.2  //expect: DefineOtherArchIssue
	-DSSE4.1  //expect: DefineOtherArchIssue
	-DSSE4  //expect: DefineOtherArchIssue
	-DSSE3  //expect: DefineOtherArchIssue
	-DSSE2  //expect: DefineOtherArchIssue
	-DSSE  //expect: DefineOtherArchIssue
	-DALPHA  //expect: DefineOtherArchIssue
	-DALTIVEC  //expect: DefineOtherArchIssue
	-DHPPA  //expect: DefineOtherArchIssue
	-DIX86  //expect: DefineOtherArchIssue
	-DMICROBLAZE  //expect: DefineOtherArchIssue
	-DMIPS  //expect: DefineOtherArchIssue
	-DNIOS2  //expect: DefineOtherArchIssue
	-DPOWER  //expect: DefineOtherArchIssue
	-DPOWERPC  //expect: DefineOtherArchIssue
	-DPOWERPC32  //expect: DefineOtherArchIssue
	-DPOWERPC64  //expect: DefineOtherArchIssue
	-DPPC64LE  //expect: DefineOtherArchIssue
	-DPPC64  //expect: DefineOtherArchIssue
	-DPPC  //expect: DefineOtherArchIssue
	-DS390  //expect: DefineOtherArchIssue
	-DSH  //expect: DefineOtherArchIssue
	-DSPARC  //expect: DefineOtherArchIssue
	-DTILE  //expect: DefineOtherArchIssue

	-D_amd64_  //expect: DefineOtherArchIssue
	-D_x86_64_  //expect: DefineOtherArchIssue
	-D_x86-64_  //expect: DefineOtherArchIssue
	-D_x86_  //expect: DefineOtherArchIssue
	-D_x64_  //expect: DefineOtherArchIssue
	-D_amd64_  //expect: DefineOtherArchIssue
	-D_avx_  //expect: DefineOtherArchIssue
	-D_avx2_  //expect: DefineOtherArchIssue
	-D_avx512_  //expect: DefineOtherArchIssue
	-D_i386_  //expect: DefineOtherArchIssue
	-D_i586_  //expect: DefineOtherArchIssue
	-D_i686_  //expect: DefineOtherArchIssue
	-D_ia32_  //expect: DefineOtherArchIssue
	-D_ia64_  //expect: DefineOtherArchIssue
	-D_intel_  //expect: DefineOtherArchIssue
	-D_intel64_  //expect: DefineOtherArchIssue
	-D_m68k_  //expect: DefineOtherArchIssue
	-D_sse5_  //expect: DefineOtherArchIssue
	-D_sse4.2_  //expect: DefineOtherArchIssue
	-D_sse4.1_  //expect: DefineOtherArchIssue
	-D_sse4_  //expect: DefineOtherArchIssue
	-D_sse3_  //expect: DefineOtherArchIssue
	-D_sse2_  //expect: DefineOtherArchIssue
	-D_sse_  //expect: DefineOtherArchIssue
	-D_alpha_  //expect: DefineOtherArchIssue
	-D_altivec_  //expect: DefineOtherArchIssue
	-D_hppa_  //expect: DefineOtherArchIssue
	-D_ix86_  //expect: DefineOtherArchIssue
	-D_microblaze_  //expect: DefineOtherArchIssue
	-D_mips_  //expect: DefineOtherArchIssue
	-D_nios2_  //expect: DefineOtherArchIssue
	-D_power_  //expect: DefineOtherArchIssue
	-D_powerpc_  //expect: DefineOtherArchIssue
	-D_powerpc32_  //expect: DefineOtherArchIssue
	-D_powerpc64_  //expect: DefineOtherArchIssue
	-D_ppc64le_  //expect: DefineOtherArchIssue
	-D_ppc64_  //expect: DefineOtherArchIssue
	-D_ppc_  //expect: DefineOtherArchIssue
	-D_s390_  //expect: DefineOtherArchIssue
	-D_sh_  //expect: DefineOtherArchIssue
	-D_sparc_  //expect: DefineOtherArchIssue
	-D_tile_  //expect: DefineOtherArchIssue

	-D_AMD64_  //expect: DefineOtherArchIssue
	-D_x86_64_  //expect: DefineOtherArchIssue
	-D_x86-64_  //expect: DefineOtherArchIssue
	-D_x86_  //expect: DefineOtherArchIssue
	-D_x64_  //expect: DefineOtherArchIssue
	-D_AMD64_  //expect: DefineOtherArchIssue
	-D_AVX_  //expect: DefineOtherArchIssue
	-D_AVX2_  //expect: DefineOtherArchIssue
	-D_AVX512_  //expect: DefineOtherArchIssue
	-D_I386_  //expect: DefineOtherArchIssue
	-D_I586_  //expect: DefineOtherArchIssue
	-D_I686_  //expect: DefineOtherArchIssue
	-D_IA32_  //expect: DefineOtherArchIssue
	-D_IA64_  //expect: DefineOtherArchIssue
	-D_INTEL_  //expect: DefineOtherArchIssue
	-D_INTEL64_  //expect: DefineOtherArchIssue
	-D_M68K_  //expect: DefineOtherArchIssue
	-D_SSE5_  //expect: DefineOtherArchIssue
	-D_SSE4.2_  //expect: DefineOtherArchIssue
	-D_SSE4.1_  //expect: DefineOtherArchIssue
	-D_SSE4_  //expect: DefineOtherArchIssue
	-D_SSE3_  //expect: DefineOtherArchIssue
	-D_SSE2_  //expect: DefineOtherArchIssue
	-D_SSE_  //expect: DefineOtherArchIssue
	-D_ALPHA_  //expect: DefineOtherArchIssue
	-D_ALTIVEC_  //expect: DefineOtherArchIssue
	-D_HPPA_  //expect: DefineOtherArchIssue
	-D_IX86_  //expect: DefineOtherArchIssue
	-D_MICROBLAZE_  //expect: DefineOtherArchIssue
	-D_MIPS_  //expect: DefineOtherArchIssue
	-D_NIOS2_  //expect: DefineOtherArchIssue
	-D_POWER_  //expect: DefineOtherArchIssue
	-D_POWERPC_  //expect: DefineOtherArchIssue
	-D_POWERPC32_  //expect: DefineOtherArchIssue
	-D_POWERPC64_  //expect: DefineOtherArchIssue
	-D_PPC64LE_  //expect: DefineOtherArchIssue
	-D_PPC64_  //expect: DefineOtherArchIssue
	-D_PPC_  //expect: DefineOtherArchIssue
	-D_S390_  //expect: DefineOtherArchIssue
	-D_SH_  //expect: DefineOtherArchIssue
	-D_SPARC_  //expect: DefineOtherArchIssue
	-D_TILE_  //expect: DefineOtherArchIssue

	-D__amd64__  //expect: DefineOtherArchIssue
	-D__x86_64__  //expect: DefineOtherArchIssue
	-D__x86-64__  //expect: DefineOtherArchIssue
	-D__x86__  //expect: DefineOtherArchIssue
	-D__x64__  //expect: DefineOtherArchIssue
	-D__amd64__  //expect: DefineOtherArchIssue
	-D__avx__  //expect: DefineOtherArchIssue
	-D__avx2__  //expect: DefineOtherArchIssue
	-D__avx512__  //expect: DefineOtherArchIssue
	-D__i386__  //expect: DefineOtherArchIssue
	-D__i586__  //expect: DefineOtherArchIssue
	-D__i686__  //expect: DefineOtherArchIssue
	-D__ia32__  //expect: DefineOtherArchIssue
	-D__ia64__  //expect: DefineOtherArchIssue
	-D__intel__  //expect: DefineOtherArchIssue
	-D__intel64__  //expect: DefineOtherArchIssue
	-D__m68k__  //expect: DefineOtherArchIssue
	-D__sse5__  //expect: DefineOtherArchIssue
	-D__sse4.2__  //expect: DefineOtherArchIssue
	-D__sse4.1__  //expect: DefineOtherArchIssue
	-D__sse4__  //expect: DefineOtherArchIssue
	-D__sse3__  //expect: DefineOtherArchIssue
	-D__sse2__  //expect: DefineOtherArchIssue
	-D__sse__  //expect: DefineOtherArchIssue
	-D__alpha__  //expect: DefineOtherArchIssue
	-D__altivec__  //expect: DefineOtherArchIssue
	-D__hppa__  //expect: DefineOtherArchIssue
	-D__ix86__  //expect: DefineOtherArchIssue
	-D__microblaze__  //expect: DefineOtherArchIssue
	-D__mips__  //expect: DefineOtherArchIssue
	-D__nios2__  //expect: DefineOtherArchIssue
	-D__power__  //expect: DefineOtherArchIssue
	-D__powerpc__  //expect: DefineOtherArchIssue
	-D__powerpc32__  //expect: DefineOtherArchIssue
	-D__powerpc64__  //expect: DefineOtherArchIssue
	-D__ppc64le__  //expect: DefineOtherArchIssue
	-D__ppc64__  //expect: DefineOtherArchIssue
	-D__ppc__  //expect: DefineOtherArchIssue
	-D__s390__  //expect: DefineOtherArchIssue
	-D__sh__  //expect: DefineOtherArchIssue
	-D__sparc__  //expect: DefineOtherArchIssue
	-D__tile__  //expect: DefineOtherArchIssue

	-D__AMD64__  //expect: DefineOtherArchIssue
	-D__x86_64__  //expect: DefineOtherArchIssue
	-D__x86-64__  //expect: DefineOtherArchIssue
	-D__x86__  //expect: DefineOtherArchIssue
	-D__x64__  //expect: DefineOtherArchIssue
	-D__AMD64__  //expect: DefineOtherArchIssue
	-D__AVX__  //expect: DefineOtherArchIssue
	-D__AVX2__  //expect: DefineOtherArchIssue
	-D__AVX512__  //expect: DefineOtherArchIssue
	-D__I386__  //expect: DefineOtherArchIssue
	-D__I586__  //expect: DefineOtherArchIssue
	-D__I686__  //expect: DefineOtherArchIssue
	-D__IA32__  //expect: DefineOtherArchIssue
	-D__IA64__  //expect: DefineOtherArchIssue
	-D__INTEL__  //expect: DefineOtherArchIssue
	-D__INTEL64__  //expect: DefineOtherArchIssue
	-D__M68K__  //expect: DefineOtherArchIssue
	-D__SSE5__  //expect: DefineOtherArchIssue
	-D__SSE4.2__  //expect: DefineOtherArchIssue
	-D__SSE4.1__  //expect: DefineOtherArchIssue
	-D__SSE4__  //expect: DefineOtherArchIssue
	-D__SSE3__  //expect: DefineOtherArchIssue
	-D__SSE2__  //expect: DefineOtherArchIssue
	-D__SSE__  //expect: DefineOtherArchIssue
	-D__ALPHA__  //expect: DefineOtherArchIssue
	-D__ALTIVEC__  //expect: DefineOtherArchIssue
	-D__HPPA__  //expect: DefineOtherArchIssue
	-D__IX86__  //expect: DefineOtherArchIssue
	-D__MICROBLAZE__  //expect: DefineOtherArchIssue
	-D__MIPS__  //expect: DefineOtherArchIssue
	-D__NIOS2__  //expect: DefineOtherArchIssue
	-D__POWER__  //expect: DefineOtherArchIssue
	-D__POWERPC__  //expect: DefineOtherArchIssue
	-D__POWERPC32__  //expect: DefineOtherArchIssue
	-D__POWERPC64__  //expect: DefineOtherArchIssue
	-D__PPC64LE__  //expect: DefineOtherArchIssue
	-D__PPC64__  //expect: DefineOtherArchIssue
	-D__PPC__  //expect: DefineOtherArchIssue
	-D__S390__  //expect: DefineOtherArchIssue
	-D__SH__  //expect: DefineOtherArchIssue
	-D__SPARC__  //expect: DefineOtherArchIssue
	-D__TILE__  //expect: DefineOtherArchIssue

	/Damd64  //expect: DefineOtherArchIssue
	/Dx86_64  //expect: DefineOtherArchIssue
	/Dx86-64  //expect: DefineOtherArchIssue
	/Dx86  //expect: DefineOtherArchIssue
	/Dx64  //expect: DefineOtherArchIssue
	/Damd64  //expect: DefineOtherArchIssue
	/Davx  //expect: DefineOtherArchIssue
	/Davx2  //expect: DefineOtherArchIssue
	/Davx512  //expect: DefineOtherArchIssue
	/Di386  //expect: DefineOtherArchIssue
	/Di586  //expect: DefineOtherArchIssue
	/Di686  //expect: DefineOtherArchIssue
	/Dia32  //expect: DefineOtherArchIssue
	/Dia64  //expect: DefineOtherArchIssue
	/Dintel  //expect: DefineOtherArchIssue
	/Dintel64  //expect: DefineOtherArchIssue
	/Dm68k  //expect: DefineOtherArchIssue
	/Dsse5  //expect: DefineOtherArchIssue
	/Dsse4.2  //expect: DefineOtherArchIssue
	/Dsse4.1  //expect: DefineOtherArchIssue
	/Dsse4  //expect: DefineOtherArchIssue
	/Dsse3  //expect: DefineOtherArchIssue
	/Dsse2  //expect: DefineOtherArchIssue
	/Dsse  //expect: DefineOtherArchIssue
	/Dx86_6  //expect: DefineOtherArchIssue
	/Dalpha  //expect: DefineOtherArchIssue
	/Daltivec  //expect: DefineOtherArchIssue
	/Dhppa  //expect: DefineOtherArchIssue
	/Dix86  //expect: DefineOtherArchIssue
	/Dmicroblaze  //expect: DefineOtherArchIssue
	/Dmips  //expect: DefineOtherArchIssue
	/Dnios2  //expect: DefineOtherArchIssue
	/Dpower  //expect: DefineOtherArchIssue
	/Dpowerpc  //expect: DefineOtherArchIssue
	/Dpowerpc32  //expect: DefineOtherArchIssue
	/Dpowerpc64  //expect: DefineOtherArchIssue
	/Dppc64le  //expect: DefineOtherArchIssue
	/Dppc64  //expect: DefineOtherArchIssue
	/Dppc  //expect: DefineOtherArchIssue
	/Ds390  //expect: DefineOtherArchIssue
	/Dsh  //expect: DefineOtherArchIssue
	/Dsparc  //expect: DefineOtherArchIssue
	/Dtile  //expect: DefineOtherArchIssue

	/DAMD64  //expect: DefineOtherArchIssue
	/Dx86_64  //expect: DefineOtherArchIssue
	/Dx86-64  //expect: DefineOtherArchIssue
	/Dx86  //expect: DefineOtherArchIssue
	/Dx64  //expect: DefineOtherArchIssue
	/DAMD64  //expect: DefineOtherArchIssue
	/DAVX  //expect: DefineOtherArchIssue
	/DAVX2  //expect: DefineOtherArchIssue
	/DAVX512  //expect: DefineOtherArchIssue
	/DI386  //expect: DefineOtherArchIssue
	/DI586  //expect: DefineOtherArchIssue
	/DI686  //expect: DefineOtherArchIssue
	/DIA32  //expect: DefineOtherArchIssue
	/DIA64  //expect: DefineOtherArchIssue
	/DINTEL  //expect: DefineOtherArchIssue
	/DINTEL64  //expect: DefineOtherArchIssue
	/DM68K  //expect: DefineOtherArchIssue
	/DSSE5  //expect: DefineOtherArchIssue
	/DSSE4.2  //expect: DefineOtherArchIssue
	/DSSE4.1  //expect: DefineOtherArchIssue
	/DSSE4  //expect: DefineOtherArchIssue
	/DSSE3  //expect: DefineOtherArchIssue
	/DSSE2  //expect: DefineOtherArchIssue
	/DSSE  //expect: DefineOtherArchIssue
	/DALPHA  //expect: DefineOtherArchIssue
	/DALTIVEC  //expect: DefineOtherArchIssue
	/DHPPA  //expect: DefineOtherArchIssue
	/DIX86  //expect: DefineOtherArchIssue
	/DMICROBLAZE  //expect: DefineOtherArchIssue
	/DMIPS  //expect: DefineOtherArchIssue
	/DNIOS2  //expect: DefineOtherArchIssue
	/DPOWER  //expect: DefineOtherArchIssue
	/DPOWERPC  //expect: DefineOtherArchIssue
	/DPOWERPC32  //expect: DefineOtherArchIssue
	/DPOWERPC64  //expect: DefineOtherArchIssue
	/DPPC64LE  //expect: DefineOtherArchIssue
	/DPPC64  //expect: DefineOtherArchIssue
	/DPPC  //expect: DefineOtherArchIssue
	/DS390  //expect: DefineOtherArchIssue
	/DSH  //expect: DefineOtherArchIssue
	/DSPARC  //expect: DefineOtherArchIssue
	/DTILE  //expect: DefineOtherArchIssue

	/D_amd64_  //expect: DefineOtherArchIssue
	/D_x86_64_  //expect: DefineOtherArchIssue
	/D_x86-64_  //expect: DefineOtherArchIssue
	/D_x86_  //expect: DefineOtherArchIssue
	/D_x64_  //expect: DefineOtherArchIssue
	/D_amd64_  //expect: DefineOtherArchIssue
	/D_avx_  //expect: DefineOtherArchIssue
	/D_avx2_  //expect: DefineOtherArchIssue
	/D_avx512_  //expect: DefineOtherArchIssue
	/D_i386_  //expect: DefineOtherArchIssue
	/D_i586_  //expect: DefineOtherArchIssue
	/D_i686_  //expect: DefineOtherArchIssue
	/D_ia32_  //expect: DefineOtherArchIssue
	/D_ia64_  //expect: DefineOtherArchIssue
	/D_intel_  //expect: DefineOtherArchIssue
	/D_intel64_  //expect: DefineOtherArchIssue
	/D_m68k_  //expect: DefineOtherArchIssue
	/D_sse5_  //expect: DefineOtherArchIssue
	/D_sse4.2_  //expect: DefineOtherArchIssue
	/D_sse4.1_  //expect: DefineOtherArchIssue
	/D_sse4_  //expect: DefineOtherArchIssue
	/D_sse3_  //expect: DefineOtherArchIssue
	/D_sse2_  //expect: DefineOtherArchIssue
	/D_sse_  //expect: DefineOtherArchIssue
	/D_alpha_  //expect: DefineOtherArchIssue
	/D_altivec_  //expect: DefineOtherArchIssue
	/D_hppa_  //expect: DefineOtherArchIssue
	/D_ix86_  //expect: DefineOtherArchIssue
	/D_microblaze_  //expect: DefineOtherArchIssue
	/D_mips_  //expect: DefineOtherArchIssue
	/D_nios2_  //expect: DefineOtherArchIssue
	/D_power_  //expect: DefineOtherArchIssue
	/D_powerpc_  //expect: DefineOtherArchIssue
	/D_powerpc32_  //expect: DefineOtherArchIssue
	/D_powerpc64_  //expect: DefineOtherArchIssue
	/D_ppc64le_  //expect: DefineOtherArchIssue
	/D_ppc64_  //expect: DefineOtherArchIssue
	/D_ppc_  //expect: DefineOtherArchIssue
	/D_s390_  //expect: DefineOtherArchIssue
	/D_sh_  //expect: DefineOtherArchIssue
	/D_sparc_  //expect: DefineOtherArchIssue
	/D_tile_  //expect: DefineOtherArchIssue

	/D_AMD64_  //expect: DefineOtherArchIssue
	/D_x86_64_  //expect: DefineOtherArchIssue
	/D_x86-64_  //expect: DefineOtherArchIssue
	/D_x86_  //expect: DefineOtherArchIssue
	/D_x64_  //expect: DefineOtherArchIssue
	/D_AMD64_  //expect: DefineOtherArchIssue
	/D_AVX_  //expect: DefineOtherArchIssue
	/D_AVX2_  //expect: DefineOtherArchIssue
	/D_AVX512_  //expect: DefineOtherArchIssue
	/D_I386_  //expect: DefineOtherArchIssue
	/D_I586_  //expect: DefineOtherArchIssue
	/D_I686_  //expect: DefineOtherArchIssue
	/D_IA32_  //expect: DefineOtherArchIssue
	/D_IA64_  //expect: DefineOtherArchIssue
	/D_INTEL_  //expect: DefineOtherArchIssue
	/D_INTEL64_  //expect: DefineOtherArchIssue
	/D_M68K_  //expect: DefineOtherArchIssue
	/D_SSE5_  //expect: DefineOtherArchIssue
	/D_SSE4.2_  //expect: DefineOtherArchIssue
	/D_SSE4.1_  //expect: DefineOtherArchIssue
	/D_SSE4_  //expect: DefineOtherArchIssue
	/D_SSE3_  //expect: DefineOtherArchIssue
	/D_SSE2_  //expect: DefineOtherArchIssue
	/D_SSE_  //expect: DefineOtherArchIssue
	/D_ALPHA_  //expect: DefineOtherArchIssue
	/D_ALTIVEC_  //expect: DefineOtherArchIssue
	/D_HPPA_  //expect: DefineOtherArchIssue
	/D_IX86_  //expect: DefineOtherArchIssue
	/D_MICROBLAZE_  //expect: DefineOtherArchIssue
	/D_MIPS_  //expect: DefineOtherArchIssue
	/D_NIOS2_  //expect: DefineOtherArchIssue
	/D_POWER_  //expect: DefineOtherArchIssue
	/D_POWERPC_  //expect: DefineOtherArchIssue
	/D_POWERPC32_  //expect: DefineOtherArchIssue
	/D_POWERPC64_  //expect: DefineOtherArchIssue
	/D_PPC64LE_  //expect: DefineOtherArchIssue
	/D_PPC64_  //expect: DefineOtherArchIssue
	/D_PPC_  //expect: DefineOtherArchIssue
	/D_S390_  //expect: DefineOtherArchIssue
	/D_SH_  //expect: DefineOtherArchIssue
	/D_SPARC_  //expect: DefineOtherArchIssue
	/D_TILE_  //expect: DefineOtherArchIssue

	/D__amd64__  //expect: DefineOtherArchIssue
	/D__x86_64__  //expect: DefineOtherArchIssue
	/D__x86-64__  //expect: DefineOtherArchIssue
	/D__x86__  //expect: DefineOtherArchIssue
	/D__x64__  //expect: DefineOtherArchIssue
	/D__amd64__  //expect: DefineOtherArchIssue
	/D__avx__  //expect: DefineOtherArchIssue
	/D__avx2__  //expect: DefineOtherArchIssue
	/D__avx512__  //expect: DefineOtherArchIssue
	/D__i386__  //expect: DefineOtherArchIssue
	/D__i586__  //expect: DefineOtherArchIssue
	/D__i686__  //expect: DefineOtherArchIssue
	/D__ia32__  //expect: DefineOtherArchIssue
	/D__ia64__  //expect: DefineOtherArchIssue
	/D__intel__  //expect: DefineOtherArchIssue
	/D__intel64__  //expect: DefineOtherArchIssue
	/D__m68k__  //expect: DefineOtherArchIssue
	/D__sse5__  //expect: DefineOtherArchIssue
	/D__sse4.2__  //expect: DefineOtherArchIssue
	/D__sse4.1__  //expect: DefineOtherArchIssue
	/D__sse4__  //expect: DefineOtherArchIssue
	/D__sse3__  //expect: DefineOtherArchIssue
	/D__sse2__  //expect: DefineOtherArchIssue
	/D__sse__  //expect: DefineOtherArchIssue
	/D__alpha__  //expect: DefineOtherArchIssue
	/D__altivec__  //expect: DefineOtherArchIssue
	/D__hppa__  //expect: DefineOtherArchIssue
	/D__ix86__  //expect: DefineOtherArchIssue
	/D__microblaze__  //expect: DefineOtherArchIssue
	/D__mips__  //expect: DefineOtherArchIssue
	/D__nios2__  //expect: DefineOtherArchIssue
	/D__power__  //expect: DefineOtherArchIssue
	/D__powerpc__  //expect: DefineOtherArchIssue
	/D__powerpc32__  //expect: DefineOtherArchIssue
	/D__powerpc64__  //expect: DefineOtherArchIssue
	/D__ppc64le__  //expect: DefineOtherArchIssue
	/D__ppc64__  //expect: DefineOtherArchIssue
	/D__ppc__  //expect: DefineOtherArchIssue
	/D__s390__  //expect: DefineOtherArchIssue
	/D__sh__  //expect: DefineOtherArchIssue
	/D__sparc__  //expect: DefineOtherArchIssue
	/D__tile__  //expect: DefineOtherArchIssue

	/D__AMD64__  //expect: DefineOtherArchIssue
	/D__x86_64__  //expect: DefineOtherArchIssue
	/D__x86-64__  //expect: DefineOtherArchIssue
	/D__x86__  //expect: DefineOtherArchIssue
	/D__x64__  //expect: DefineOtherArchIssue
	/D__AMD64__  //expect: DefineOtherArchIssue
	/D__AVX__  //expect: DefineOtherArchIssue
	/D__AVX2__  //expect: DefineOtherArchIssue
	/D__AVX512__  //expect: DefineOtherArchIssue
	/D__I386__  //expect: DefineOtherArchIssue
	/D__I586__  //expect: DefineOtherArchIssue
	/D__I686__  //expect: DefineOtherArchIssue
	/D__IA32__  //expect: DefineOtherArchIssue
	/D__IA64__  //expect: DefineOtherArchIssue
	/D__INTEL__  //expect: DefineOtherArchIssue
	/D__INTEL64__  //expect: DefineOtherArchIssue
	/D__M68K__  //expect: DefineOtherArchIssue
	/D__SSE5__  //expect: DefineOtherArchIssue
	/D__SSE4.2__  //expect: DefineOtherArchIssue
	/D__SSE4.1__  //expect: DefineOtherArchIssue
	/D__SSE4__  //expect: DefineOtherArchIssue
	/D__SSE3__  //expect: DefineOtherArchIssue
	/D__SSE2__  //expect: DefineOtherArchIssue
	/D__SSE__  //expect: DefineOtherArchIssue
	/D__ALPHA__  //expect: DefineOtherArchIssue
	/D__ALTIVEC__  //expect: DefineOtherArchIssue
	/D__HPPA__  //expect: DefineOtherArchIssue
	/D__IX86__  //expect: DefineOtherArchIssue
	/D__MICROBLAZE__  //expect: DefineOtherArchIssue
	/D__MIPS__  //expect: DefineOtherArchIssue
	/D__NIOS2__  //expect: DefineOtherArchIssue
	/D__POWER__  //expect: DefineOtherArchIssue
	/D__POWERPC__  //expect: DefineOtherArchIssue
	/D__POWERPC32__  //expect: DefineOtherArchIssue
	/D__POWERPC64__  //expect: DefineOtherArchIssue
	/D__PPC64LE__  //expect: DefineOtherArchIssue
	/D__PPC64__  //expect: DefineOtherArchIssue
	/D__PPC__  //expect: DefineOtherArchIssue
	/D__S390__  //expect: DefineOtherArchIssue
	/D__SH__  //expect: DefineOtherArchIssue
	/D__SPARC__  //expect: DefineOtherArchIssue
	/D__TILE__  //expect: DefineOtherArchIssue

# scanner: the same name issue of build command and makefile target
void build_command()
{
	abc 
	ABC 
	_abc 
	./qwe1 
	.\qwe2 
	$(qwe3) 
}

void ASSIGNMENT_RE()
{
abc = text
ABC = text
_abc = text
qwe1 = text
qwe2 = text
$(qwe3) = text
}

void target()
{
abc := text //expect: BuildCommandIssue
ABC := text //expect: BuildCommandIssue
_abc := text //expect: BuildCommandIssue
./abc := text //expect: BuildCommandIssue
.\abc := text //expect: BuildCommandIssue
qwe1 := text //expect: BuildCommandIssue
qwe2 := text //expect: BuildCommandIssue
$(qwe3) := text //expect: BuildCommandIssue
}

void check_of_build_command()
{
	abc //expect: BuildCommandIssue
	ABC //expect: BuildCommandIssue
	_abc //expect: BuildCommandIssue
	./qwe1 //expect: BuildCommandIssue
	.\qwe2 //expect: BuildCommandIssue
	$(qwe3) //expect: BuildCommandIssue
}

# scanner: ARM GCC compiler option check
void GCC_compiler_option_check()
{
	=-m64 //expect: BuildCommandIssue
	 -m64  //expect: BuildCommandIssue
	"-m64" //expect: BuildCommandIssue
	=-O2  //expect: BuildCommandIssue
	 -O2  //expect: BuildCommandIssue
	"-O2" //expect: BuildCommandIssue
	=-msse2  //expect: BuildCommandIssue
	 -msse2  //expect: BuildCommandIssue
	"-msse2" //expect: BuildCommandIssue
	=-msse4.1  //expect: BuildCommandIssue
	 -msse4.1  //expect: BuildCommandIssue
	"-msse4.1" //expect: BuildCommandIssue
	=-mpclmul  //expect: BuildCommandIssue
	 -mpclmul  //expect: BuildCommandIssue
	"-mpclmul" //expect: BuildCommandIssue
	=-maes  //expect: BuildCommandIssue
	 -maes  //expect: BuildCommandIssue
	"-maes" //expect: BuildCommandIssue
}

