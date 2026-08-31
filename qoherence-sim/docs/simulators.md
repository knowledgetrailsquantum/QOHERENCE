# Simulators Overview

qoherence-sim implements two complementary classical simulation strategies:

| Backend | File | Strategy | Best for | Practical qubit ceiling |
|---|---|---|---|---|
| State-vector | `src/statevector.py` | Exact, full 2^n amplitude tracking | Any circuit, exact results | ~30 (workstation), ~50 (supercomputer) |
| Tensor network | `src/tensor_network.py` | Compressed representation exploiting limited entanglement | Low-entanglement, geometrically local circuits | Hundreds to thousands, *if* entanglement stays low |

Full depth: `01-beginner/01-why-simulate-quantum-computers.md` → `02-intermediate/01-state-vector-limits.md` → `03-advanced/01-tensor-network-methods.md` → `04-expert/01-gpu-accelerated-simulation.md`.

## Choosing a backend
Use state-vector simulation by default for correctness testing and any circuit under ~25-30 qubits. Switch to tensor-network simulation only once you understand your circuit's entanglement structure well enough to expect it to stay tractable (see `03-advanced/01-tensor-network-methods.md`) — misapplying tensor-network methods to a highly entangled circuit will either be slow, memory-hungry, or silently inaccurate if truncation is applied without checking convergence.

## Industry parallels
This mirrors real-world tools: IBM's Qiskit Aer and Google's qsim both offer state-vector and (in some configurations) tensor-network or matrix-product-state backends; Nvidia's cuQuantum accelerates both approaches on GPUs (see `04-expert/01-gpu-accelerated-simulation.md`).
