# GPU-Accelerated Simulation (Expert)

## Why GPUs fit this problem well
Both state-vector gate application and many tensor-network contraction operations reduce to large, highly parallel linear-algebra operations (matrix-vector and matrix-matrix multiplication) — exactly the workload GPUs were originally designed to accelerate for graphics, and have since been generalized for via CUDA and similar frameworks. Applying a single-qubit gate to an n-qubit state vector touches all 2ⁿ amplitudes independently and identically (each amplitude pair transforms via the same small 2×2 matrix), which parallelizes almost perfectly across thousands of GPU cores.

## Nvidia's cuQuantum and the broader ecosystem
Nvidia's cuQuantum SDK is the most widely adopted GPU-acceleration library for quantum simulation, providing optimized state-vector (`cuStateVec`) and tensor-network (`cuTensorNet`) primitives that major quantum software stacks integrate with — IBM's Qiskit Aer, Google's qsim, and various independent research simulators all support cuQuantum backends. This reflects a broader industry pattern: rather than each quantum software vendor building GPU acceleration from scratch, the field has converged on shared, highly optimized GPU linear-algebra tooling as common infrastructure, similar to how classical machine learning converged on shared GPU-accelerated tensor libraries (cuDNN and similar) rather than every framework reimplementing low-level GPU kernels independently.

## Multi-GPU and distributed simulation
Beyond a single GPU's memory limits (a modern high-end GPU might have 40-80GB of memory, supporting roughly 31-32 qubits of exact state-vector simulation), simulators distribute the state vector across multiple GPUs or multiple machines, using high-bandwidth interconnects (NVLink within a node, InfiniBand across nodes) to handle the communication gate application requires when it touches amplitudes that live on different devices. This is precisely the kind of infrastructure national labs and cloud providers use to push exact state-vector simulation toward its practical ~50-qubit ceiling (see `02-intermediate/01-state-vector-limits.md`) — not a single machine, but coordinated clusters with carefully engineered data movement.

## Where GPU acceleration doesn't help as much
GPU acceleration primarily speeds up the *arithmetic* of simulation — it doesn't change the fundamental exponential memory scaling of state-vector methods, or the fundamental entanglement-dependent scaling of tensor-network methods (see `03-advanced/01-tensor-network-methods.md`). A GPU cluster with 10x the memory of a CPU workstation buys you roughly 3-4 more qubits of exact state-vector simulation (since memory needed doubles per qubit) — a meaningful but not transformative gain against an exponential wall. This is an important expectation-management point: GPU acceleration is genuinely valuable (often 10-100x speedup in wall-clock time for a given qubit count, and meaningfully extends the practical ceiling), but it is not a way to sidestep the exponential barrier that fundamentally separates classical and quantum computational resources for genuinely hard circuits.

## Implementation notes for extending `qoherence-sim`
- A GPU backend for `src/statevector.py` should keep the same external interface as the CPU implementation (mirroring the backend-adapter pattern from `qoherence-hardware/docs/04-expert/01-building-a-custom-backend.md`) so algorithm code in `qoherence-algorithms` doesn't need to know or care which backend executes it.
- Profile before optimizing: for small qubit counts (under ~15-18 qubits), GPU kernel-launch overhead can make GPU execution *slower* than a well-optimized CPU implementation — GPU acceleration's benefit grows with problem size, and naively defaulting to GPU for small test circuits is a common performance anti-pattern.
- When benchmarking GPU vs. CPU simulation performance (relevant to `qoherence-bench`), report both raw wall-clock time and the specific hardware/memory configuration used — simulation benchmarks are notoriously hardware-dependent and easy to present misleadingly without full disclosure of the setup.

## Next
See `qoherence-bench/docs` for how to rigorously and reproducibly benchmark simulator and real-hardware performance.

## A Bit of History
GPUs were designed in the 1990s purely to push pixels for video games — Nvidia coined the term "GPU" itself in 1999 for the GeForce 256. Their re-purposing for scientific and quantum computing decades later, via general-purpose GPU computing frameworks like CUDA (2007) and eventually cuQuantum (2021), is one of computing's odder success stories: a chip built to render Quake and Doom ended up accelerating the simulation of some of the strangest physics ever discovered.

---
**[◀ Tensor Network Methods](../03-advanced/01-tensor-network-methods.md)**  |  [Index](../../../README.md)  |  **[Why Algorithms Need Quantum ▶](../../../qoherence-algorithms/docs/01-beginner/01-why-algorithms-need-quantum.md)**
