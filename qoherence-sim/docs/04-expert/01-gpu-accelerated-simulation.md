# GPU-Accelerated Simulation (Expert)

State-vector operations are large matrix-vector products — well suited to
GPU acceleration via CUDA-backed numpy alternatives (e.g. CuPy) or
dedicated simulators (qsim, cuQuantum). Contributors extending
`statevector.py` for GPU support should benchmark against `qoherence-bench`
to quantify real speedups per qubit count.
