# Building a Custom Backend (Expert)

## The adapter pattern
`qoherence-hardware`'s `src/base_backend.py` defines a common interface that `src/ibm_backend.py`, `src/ionq_backend.py`, and `src/rigetti_backend.py` all implement — mirroring how real cross-vendor SDKs (Qiskit's provider system, Amazon Braket's device abstraction, Microsoft's Azure Quantum multi-provider model) let the same circuit-construction code target different physical hardware with minimal changes. This decoupling matters practically: a research team benchmarking VQE across IBM and IonQ hardware (a common real-world workflow, since the two platforms have very different connectivity and noise profiles — see `02-intermediate/01-qubit-technologies.md`) should be able to swap backends without rewriting the algorithm.

## What a backend adapter must handle
1. **Authentication and job submission**: translating a local `Circuit` object into the vendor's API request format (IBM's Qiskit Runtime primitives, IonQ's native API or Qiskit/Cirq provider plugins, Rigetti's pyQuil/Quil format) and submitting it to a queue — real quantum hardware is a shared, scheduled resource, not something you get exclusive, on-demand access to, so job submission is inherently asynchronous.
2. **Transpilation to the target's native gate set and connectivity** (see `03-advanced/01-connectivity-and-transpilation.md`) — each vendor's native gate set differs (IBM's basis includes CX/ECR plus single-qubit rotations; Rigetti's gate set differs slightly; IonQ exposes a more abstract gate set to users while compiling internally to native Mølmer–Sørensen-based operations).
3. **Result format normalization**: vendors return results differently (raw bitstring counts, error-mitigated expectation values, varying metadata about job status and calibration data) — a good adapter normalizes these into a consistent `Result` object so downstream code (like `qoherence-mitigate` and `qoherence-bench`) doesn't need per-vendor branching logic.
4. **Calibration-aware compilation (advanced)**: the best real-world adapters pull each device's live calibration data (per-qubit and per-gate error rates, which drift over time and are recalibrated regularly) and use it to inform qubit mapping — preferring the currently-best-calibrated qubits and gates rather than a static, calibration-blind layout.

## Simulator-as-backend
A useful design detail: a noise-free or noise-modeled simulator (see `qoherence-sim`) should also implement the same `base_backend` interface. This lets test suites and CI pipelines validate algorithm code against a fast, free, deterministic simulator backend before ever submitting a paid, queued job to real hardware — standard practice across the industry, and directly mirrored in how Qiskit's `AerSimulator` and Amazon Braket's local simulator both implement the same device interface as their respective real-hardware backends.

## Handling hardware-specific realities
- **Queue times**: real cloud quantum hardware often has job queues ranging from seconds to hours depending on device popularity and your access tier — a robust backend adapter needs async job polling, not a blocking call.
- **Shot limits and cost**: cloud quantum providers typically charge per shot or per task, and enforce maximum shots per job — a production backend adapter should expose these limits rather than let them fail silently mid-experiment.
- **Native gate mismatches causing silent inefficiency**: a naive adapter that transpiles correctly but not *efficiently* (see optimization passes in `03-advanced/01-connectivity-and-transpilation.md`) will still produce correct results on real hardware, just with much worse fidelity than necessary — this is one of the most common gaps between a functionally-correct student implementation and a production-grade one.

## Testing a new backend adapter
Before trusting a new adapter's results, validate it against small circuits with known outcomes (a Bell pair should show ~50/50 |00⟩/|11⟩ correlation; a GHZ state should show similar behavior across more qubits) run first on the reference simulator backend, then on real hardware, comparing agreement within expected noise bounds — significant deviation from expected correlation patterns on real hardware is often a transpilation or qubit-mapping bug in the adapter, not "just noise," and should be diagnosed rather than assumed.

## Next
See `qoherence-bench/docs` for the rigorous, statistically sound methodology for comparing backend performance once your adapter is validated.
