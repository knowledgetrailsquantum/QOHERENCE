# Why Algorithms Need Quantum (Beginner)

## Not every problem benefits
A recurring surprise for newcomers: most everyday computing tasks (spreadsheets, web browsing, video playback, most databases) get *no* benefit from a quantum computer, and never will, even in principle. Quantum algorithms only help for a specific, narrow class of problems whose mathematical structure allows the interference tricks described in `qoherence-core/docs/01-beginner/02-superposition-and-entanglement.md` to concentrate probability onto the right answer. This repo focuses on the handful of problem classes where that structure exists and a real speedup is proven or strongly believed.

## The four flagship algorithms in this repo
- **Grover's algorithm** (`src/grover.py`) — unstructured search, quadratic speedup. If you're searching an unsorted list of N items for one that matches a condition, classically you need ~N checks on average; Grover's needs ~√N. Quadratic, not exponential — real but modest.
- **Shor's algorithm** (`src/shor.py`) — integer factoring, believed exponential speedup. This is the algorithm that threatens RSA encryption (see `qoherence-core/docs/03-advanced/01-quantum-fourier-transform.md`).
- **VQE** (Variational Quantum Eigensolver, `src/vqe.py`) — finding the lowest-energy state (ground state) of a quantum system, like a molecule — the flagship near-term application for quantum chemistry and materials science.
- **QAOA** (Quantum Approximate Optimization Algorithm, `src/qaoa.py`) — approximate solutions to combinatorial optimization problems (like max-cut on a graph), designed to work on today's noisy, non-fault-tolerant hardware.

## Analogy: specialized tools, not a universal upgrade
A quantum computer is less like a faster general-purpose CPU and more like a specialized coprocessor — the way a GPU dramatically accelerates matrix multiplication and graphics rendering but does nothing for, say, running a web server. The skill in quantum algorithm design is recognizing which real-world problems can be *reformulated* to match one of these narrow speedup patterns (search, period-finding, eigenvalue-finding, combinatorial optimization) — most practical applications require significant problem-specific translation work, not a drop-in replacement of a classical subroutine.

## NISQ vs. fault-tolerant algorithms
This repo's four algorithms split cleanly into two eras:
- Grover's and Shor's are **fault-tolerant-era** algorithms — they need deep, precise circuits and (for cryptographically relevant problem sizes) thousands of clean logical qubits (see `qoherence-core/docs/04-expert/01-fault-tolerant-computation.md`). They are not practically useful at meaningful scale on today's hardware.
- VQE and QAOA are **NISQ-era** algorithms (Noisy Intermediate-Scale Quantum — a term coined by physicist John Preskill in 2018) — deliberately designed with short, shallow circuits and a classical optimization loop that helps compensate for hardware noise, making them the realistic candidates for near-term commercial value on current IBM, Google, and IonQ hardware.

## What's happening in the world right now
As of 2025–2026, essentially all commercially-marketed "quantum advantage" pilots from pharmaceutical, finance, logistics, and materials companies (working with IBM, Google, Microsoft Azure Quantum, IonQ, and Quantinuum) use VQE-family or QAOA-family algorithms, or classical-quantum hybrid variants, precisely because they tolerate today's noise levels. Shor's algorithm remains a research and long-term-roadmap topic, not a deployed capability — running it on RSA-2048 would require millions of physical qubits at today's error-correction overhead, versus the hundreds to low thousands of physical qubits available on today's largest processors.

## Next
Read `02-intermediate/01-grover-and-shor-explained.md` for how Grover's and Shor's algorithms actually work step by step.
