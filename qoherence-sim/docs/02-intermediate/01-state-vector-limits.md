# State-Vector Simulation Limits (Intermediate)

Memory needed grows as 2^n complex numbers for n qubits. At 16 bytes per
complex128 number: 20 qubits ≈ 16MB, 30 qubits ≈ 16GB, 40 qubits ≈ 16TB.
This exponential wall is exactly the reason quantum hardware exists at all.
