# Qoherence Architecture

## The six repos and how they depend on each other

```
qoherence-core        <- foundational: Qubit, Gate, Circuit, state-vector math
      ^  ^  ^  ^
      |  |  |  |
qoherence-algorithms  <- builds Circuits for Grover, Shor, VQE, QAOA
qoherence-sim         <- alternative execution backends for Circuits (state-vector, tensor-network)
qoherence-hardware    <- real-device backend adapters (IBM, IonQ, Rigetti) + transpilation
qoherence-mitigate    <- post-processes results from sim/hardware execution (mitigation + correction)
      ^
      |
qoherence-bench       <- benchmarks fidelity/noise/runtime across sim and hardware backends
```

Everything depends on `qoherence-core`'s `Circuit`/`Gate`/`Qubit` abstractions as the shared representation. `qoherence-algorithms` produces circuits; `qoherence-sim` and `qoherence-hardware` are two alternative ways to *execute* those circuits (one classical-exact-or-approximate, one on real physical qubits); `qoherence-mitigate` improves the results coming out of either execution path; `qoherence-bench` measures and compares everything.

## Why this separation mirrors real industry SDK design
This layered structure deliberately mirrors how production quantum software stacks are organized — IBM's Qiskit separates circuit construction (`qiskit`) from simulation (`qiskit_aer`) from real hardware execution (`qiskit_ibm_runtime`) from error mitigation utilities; Google's Cirq and OpenFermion separate similarly; Microsoft's Q#/QDK separates language/compilation from the Azure Quantum resource-estimation and execution layer. The pattern holds because the concerns genuinely are separable and evolve at different rates: circuit *design* (algorithms), circuit *execution fidelity* (simulation and hardware), and result *quality improvement* (mitigation) are different engineering and research problems with different specialists working on them.

## Data flow example: running VQE end to end
1. `qoherence-algorithms/src/vqe.py` builds a parameterized ansatz `Circuit` using `qoherence-core` primitives.
2. The circuit is executed via either `qoherence-sim` (for development/testing) or `qoherence-hardware` (for real results) — both implement the same backend interface (see `qoherence-hardware/docs/04-expert/01-building-a-custom-backend.md`), so the algorithm code doesn't need to change based on which is used.
3. Raw results pass through `qoherence-mitigate` (readout correction, possibly ZNE) before the energy expectation value is computed.
4. The mitigated expectation value feeds back into VQE's classical optimization loop, which produces updated ansatz parameters for the next `Circuit`.
5. Throughout, `qoherence-bench` can measure fidelity, noise resilience, and runtime at any stage of this pipeline for comparison and reporting.

## Next
See `getting-started.md` for how to set up and run your first circuit across this stack, `LEARNING-PATH.md` (repo root) for the recommended reading order through all the docs tiers, and `industry-landscape.md` for how this maps onto the real-world quantum computing industry.

## A Bit of History
Layered software architecture — keeping circuit construction, execution, and post-processing in separate, swappable pieces — is a design lesson the whole software industry learned the hard way, well before quantum computing existed: the ARPANET's 1970s designers split networking into layers for exactly this reason, a decision that let the internet's lower layers (cables, then fiber, then wireless) evolve for fifty years without breaking the applications running on top. This repo's six-part split is a very direct descendant of that decades-old networking lesson.

---
**[◀ Statistical Rigor in Quantum Benchmarks](../../qoherence-bench/docs/04-expert/01-statistical-rigor-in-quantum-benchmarks.md)**  |  [Index](../../README.md)  |  **[Getting Started ▶](getting-started.md)**
