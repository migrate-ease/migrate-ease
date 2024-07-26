from cffi import FFI
ffi = FFI()
#cdef用来定义结构体,变量,或者方法的声明
#sw64 intrinsics:
ffi.cdef("""
    long __builtin_alpha_implver (void); //expect: PythonIntrinsicIssue
    long __builtin_alpha_rpcc (void); //expect: PythonIntrinsicIssue
    long __builtin_alpha_amask (long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_cmpbge (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_extbl (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_extwl (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_extll (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_extql (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_extwh (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_extlh (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_extqh (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_insbl (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_inswl (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_insll (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_insql (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_inswh (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_inslh (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_insqh (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_mskbl (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_mskwl (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_mskll (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_mskql (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_mskwh (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_msklh (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_mskqh (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_umulh (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_zap (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_zapnot (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_pklb (long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_pkwb (long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_unpkbl (long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_unpkbw (long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_minub8 (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_minsb8 (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_minuw4 (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_minsw4 (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_maxub8 (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_maxsb8 (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_maxuw4 (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_maxsw4 (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_perr (long, long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_cttz (long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_ctlz (long); //expect: PythonIntrinsicIssue
    long __builtin_alpha_ctpop (long); //expect: PythonIntrinsicIssue
    void * __builtin_thread_pointer (void); //expect: PythonIntrinsicIssue
    void __builtin_set_thread_pointer (void *); //expect: PythonIntrinsicIssue

    int printf(const char *format, ...);
""")
#dlopen是ABI模式的的基本读取方式
C = ffi.dlopen(None) # 加载整个C命名空间
arg = ffi.new("char[]", b"dsklfsd") # 等于C代码: char arg[] = "world"; 
C.printf(b"hello %s!\n", arg)