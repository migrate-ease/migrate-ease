    # Python extension packages only available for x86/x86-64
    //expect: PythonPackageIssue
    -cpu-iomp //expect: PythonPackageIssue
    -cpu-vcomp //expect: PythonPackageIssue
    -cpu-tbb //expect: PythonPackageIssue
    -devel-cpu-tbb //expect: PythonPackageIssue
    -devel-cpu-iomp //expect: PythonPackageIssue
    -cpu-dpcpp-gpu-dpcpp //expect: PythonPackageIssue
    -devel-cpu-dpcpp-gpu-dpcpp //expect: PythonPackageIssue
    //expect: PythonPackageIssue
    -static //expect: PythonPackageIssue
    -include //expect: PythonPackageIssue
    //expect: PythonPackageIssue
    -devel //expect: PythonPackageIssue
    -learn-intelex //expect: PythonPackageIssue
    -openmp //expect: PythonPackageIssue
    -opencl-rt //expect: PythonPackageIssue
    -fortran-rt //expect: PythonPackageIssue
    -devel //expect: PythonPackageIssue
    -dpcpp //expect: PythonPackageIssue
    -include //expect: PythonPackageIssue
    -static //expect: PythonPackageIssue
    //expect: PythonPackageIssue
    -devel-dpcpp //expect: PythonPackageIssue
    import dpcpp-cpp-rt //expect: PythonPackageIssue
    -x86 //expect: PythonPackageIssue
    
    from pyqbdi import //expect: PythonPackageIssue
    from onednn-cpu-iomp import //expect: PythonPackageIssue
    from onednn-cpu-vcomp import //expect: PythonPackageIssue
    from onednn-cpu-tbb import //expect: PythonPackageIssue
    from onednn-devel-cpu-tbb import //expect: PythonPackageIssue
    from onednn-devel-cpu-iomp import //expect: PythonPackageIssue
    from onednn-cpu-dpcpp-gpu-dpcpp import //expect: PythonPackageIssue
    from onednn-devel-cpu-dpcpp-gpu-dpcpp import //expect: PythonPackageIssue
    from daal4py import //expect: PythonPackageIssue
    from daal-static import //expect: PythonPackageIssue
    from daal-include import //expect: PythonPackageIssue
    from daal import //expect: PythonPackageIssue
    from daal-devel import //expect: PythonPackageIssue
    from scikit-learn-intelex import //expect: PythonPackageIssue
    from intel-openmp import //expect: PythonPackageIssue
    from intel-opencl-rt import //expect: PythonPackageIssue
    from intel-fortran-rt import //expect: PythonPackageIssue
    from mkl-devel import //expect: PythonPackageIssue
    from mkl-dpcpp import //expect: PythonPackageIssue
    from mkl-include import //expect: PythonPackageIssue
    from mkl-static import //expect: PythonPackageIssue
    from mkl import //expect: PythonPackageIssue
    from mkl-devel-dpcpp import //expect: PythonPackageIssue
    from dpcpp-cpp-rt import //expect: PythonPackageIssue
    from iced-x86 import //expect: PythonPackageIssue
