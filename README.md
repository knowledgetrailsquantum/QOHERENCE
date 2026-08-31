# Qoherence

An educational-first, end-to-end quantum computing repo set: from "what is a qubit" through algorithms, real hardware, simulation, error handling, and rigorous benchmarking — with real-world grounding in IBM, Google, Microsoft, IonQ, Quantinuum, Rigetti, Amazon, and PsiQuantum's actual hardware and roadmaps.

Start with `LEARNING-PATH.md` for the full recommended reading order. This README is the navigation hub — every link below goes to a real doc in this repo set.

## Start here
1. [`qoherence-core/docs/00-history-of-quantum-mechanics.md`](qoherence-core/docs/00-history-of-quantum-mechanics.md) — **start here.** Planck's reluctant 1900 "act of despair" through Einstein, Bohr, Heisenberg, Feynman's 1981 spark, Shor's 1994 algorithm, and how qubits are physically built today
2. [`qoherence-core/docs/01-beginner/01-what-is-a-qubit.md`](qoherence-core/docs/01-beginner/01-what-is-a-qubit.md) — what a qubit actually is, with analogies and their limits
3. [`qoherence-core/docs/01-beginner/02-superposition-and-entanglement.md`](qoherence-core/docs/01-beginner/02-superposition-and-entanglement.md)
4. [`qoherence-core/docs/01-beginner/03-gates-and-circuits.md`](qoherence-core/docs/01-beginner/03-gates-and-circuits.md)
5. [`qoherence-docs/docs/industry-landscape.md`](qoherence-docs/docs/industry-landscape.md) — real-world grounding: who's building what, and what's actually true vs. hype
6. [`qoherence-docs/docs/getting-started.md`](qoherence-docs/docs/getting-started.md) — run your first circuit

## The six repos, in dependency order

| # | Repo | What it's for | Start doc |
|---|---|---|---|
| 1 | [`qoherence-core`](qoherence-core/) | Qubits, gates, circuits — the shared foundation every other repo builds on | [beginner tier](qoherence-core/docs/01-beginner/01-what-is-a-qubit.md) |
| 2 | [`qoherence-algorithms`](qoherence-algorithms/) | Grover, Shor, VQE, QAOA | [why algorithms need quantum](qoherence-algorithms/docs/01-beginner/01-why-algorithms-need-quantum.md) |
| 3 | [`qoherence-sim`](qoherence-sim/) | Classical simulation backends (state-vector, tensor-network) | [why simulate](qoherence-sim/docs/01-beginner/01-why-simulate-quantum-computers.md) |
| 4 | [`qoherence-hardware`](qoherence-hardware/) | Real device backends (IBM, IonQ, Rigetti), connectivity, transpilation | [what is real hardware](qoherence-hardware/docs/01-beginner/01-what-is-real-quantum-hardware.md) |
| 5 | [`qoherence-mitigate`](qoherence-mitigate/) | Error mitigation and error correction | [why error handling](qoherence-mitigate/docs/01-beginner/01-why-quantum-computers-need-error-handling.md) |
| 6 | [`qoherence-bench`](qoherence-bench/) | Rigorous, statistically sound benchmarking across all of the above | [what is benchmarking](qoherence-bench/docs/01-beginner/01-what-is-benchmarking.md) |
| — | [`qoherence-docs`](qoherence-docs/) | Cross-repo architecture and industry context | [architecture](qoherence-docs/docs/architecture.md) · [industry landscape](qoherence-docs/docs/industry-landscape.md) |

See [`qoherence-docs/docs/architecture.md`](qoherence-docs/docs/architecture.md) for exactly how these six repos depend on and feed into each other (a diagram + data-flow walkthrough).

## Per-repo tier navigation (beginner → expert)

Every repo's docs follow the same four-tier structure: `01-beginner/` (no prior knowledge assumed) → `02-intermediate/` → `03-advanced/` (comfortable with linear algebra / complexity theory) → `04-expert/` (research/contribution-level).

### qoherence-core — qubits, gates, circuits, the math underneath
- **History (start here):** [a history of quantum mechanics — and how it became a computer](qoherence-core/docs/00-history-of-quantum-mechanics.md)
- Beginner: [what is a qubit](qoherence-core/docs/01-beginner/01-what-is-a-qubit.md) → [superposition & entanglement](qoherence-core/docs/01-beginner/02-superposition-and-entanglement.md) → [gates & circuits](qoherence-core/docs/01-beginner/03-gates-and-circuits.md)
- Intermediate: [multi-qubit systems](qoherence-core/docs/02-intermediate/01-multi-qubit-systems.md) → [linear algebra foundations](qoherence-core/docs/02-intermediate/02-linear-algebra-foundations.md) → [circuit composition](qoherence-core/docs/02-intermediate/03-circuit-composition.md) → [reversible computing](qoherence-core/docs/02-intermediate/04-reversible-computing.md)
- Advanced: [quantum Fourier transform](qoherence-core/docs/03-advanced/01-quantum-fourier-transform.md) → [phase estimation](qoherence-core/docs/03-advanced/04-phase-estimation.md) → [density matrices & mixed states](qoherence-core/docs/03-advanced/02-density-matrices-and-mixed-states.md) → [complexity theory](qoherence-core/docs/03-advanced/03-complexity-theory.md)
- Expert: [fault-tolerant computation](qoherence-core/docs/04-expert/01-fault-tolerant-computation.md) → [extending qoherence-core](qoherence-core/docs/04-expert/02-extending-qoherence-core.md)
- Reference: [concepts](qoherence-core/docs/concepts.md) · [API reference](qoherence-core/docs/api-reference.md)

### qoherence-algorithms — Grover, Shor, VQE, QAOA
- Beginner: [why algorithms need quantum](qoherence-algorithms/docs/01-beginner/01-why-algorithms-need-quantum.md)
- Intermediate: [Grover's & Shor's explained](qoherence-algorithms/docs/02-intermediate/01-grover-and-shor-explained.md)
- Advanced: [VQE & QAOA theory](qoherence-algorithms/docs/03-advanced/01-vqe-and-qaoa-theory.md)
- Expert: [implementing Shor's period-finding](qoherence-algorithms/docs/04-expert/01-implementing-shors-period-finding.md) → [worked example: Grover's on N-Queens](qoherence-algorithms/docs/04-expert/02-worked-example-grover-n-queens.md)
- Reference: [algorithms overview](qoherence-algorithms/docs/algorithms-overview.md)

### qoherence-hardware — real devices, IBM/IonQ/Rigetti, transpilation
- Beginner: [what is real quantum hardware](qoherence-hardware/docs/01-beginner/01-what-is-real-quantum-hardware.md)
- Intermediate: [qubit technologies compared](qoherence-hardware/docs/02-intermediate/01-qubit-technologies.md)
- Advanced: [connectivity & transpilation](qoherence-hardware/docs/03-advanced/01-connectivity-and-transpilation.md)
- Expert: [building a custom backend](qoherence-hardware/docs/04-expert/01-building-a-custom-backend.md)
- Reference: [backends overview](qoherence-hardware/docs/backends.md)

### qoherence-mitigate — noise, mitigation, error correction
- Beginner: [why error handling](qoherence-mitigate/docs/01-beginner/01-why-quantum-computers-need-error-handling.md)
- Intermediate: [mitigation vs. correction](qoherence-mitigate/docs/02-intermediate/01-mitigation-vs-correction.md)
- Advanced: [stabilizer codes](qoherence-mitigate/docs/03-advanced/01-stabilizer-codes.md)
- Expert: [implementing a decoder](qoherence-mitigate/docs/04-expert/01-implementing-a-decoder.md)
- Reference: [error mitigation overview](qoherence-mitigate/docs/error-mitigation.md)

### qoherence-sim — classical simulation
- Beginner: [why simulate quantum computers](qoherence-sim/docs/01-beginner/01-why-simulate-quantum-computers.md)
- Intermediate: [state-vector limits](qoherence-sim/docs/02-intermediate/01-state-vector-limits.md)
- Advanced: [tensor network methods](qoherence-sim/docs/03-advanced/01-tensor-network-methods.md)
- Expert: [GPU-accelerated simulation](qoherence-sim/docs/04-expert/01-gpu-accelerated-simulation.md)
- Reference: [simulators overview](qoherence-sim/docs/simulators.md)

### qoherence-bench — benchmarking methodology
- Beginner: [what is benchmarking](qoherence-bench/docs/01-beginner/01-what-is-benchmarking.md)
- Intermediate: [fidelity metrics](qoherence-bench/docs/02-intermediate/01-fidelity-metrics.md)
- Advanced: [benchmarking across backends](qoherence-bench/docs/03-advanced/01-benchmarking-across-backends.md) → [resource estimation](qoherence-bench/docs/03-advanced/02-resource-estimation.md)
- Expert: [statistical rigor in quantum benchmarks](qoherence-bench/docs/04-expert/01-statistical-rigor-in-quantum-benchmarks.md)
- Reference: [benchmarking overview](qoherence-bench/docs/benchmarking.md)

### qoherence-docs — cross-cutting
- [Architecture](qoherence-docs/docs/architecture.md) — how all six repos fit together, with a data-flow walkthrough
- [Getting started](qoherence-docs/docs/getting-started.md) — environment setup and your first circuit
- [Industry landscape](qoherence-docs/docs/industry-landscape.md) — IBM, Google, Microsoft, IonQ, Quantinuum, Rigetti, Amazon, PsiQuantum: real roadmaps, real milestones, and how to tell progress from hype
- [Applications by industry](qoherence-docs/docs/applications-by-industry.md) — cybersecurity/QKD, finance, chemistry & healthcare, logistics: what's real today vs. still a pilot
- [Ethics, society & economics](qoherence-docs/docs/ethics-and-society.md) — jobs, post-quantum cryptography policy, access & inequality, scientific overclaiming — the final page of the trail

## Full reading order
See [`LEARNING-PATH.md`](LEARNING-PATH.md) for the complete tier-by-tier plan across all six repos, and what changed in the most recent expansion of this doc set.
