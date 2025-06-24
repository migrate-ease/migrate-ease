    # Python extension packages available for aarch64 and x86
    -engine

    from keystone-engine import
    from fibers import
    
    # Python extension packages only available for aarch64 
    -arm-linux
    -arm-linux

    from pycuda-arm-linux import
    from HTSeq-arm-linux import
    from wlauto import

    # Python extension packages only available for x86
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