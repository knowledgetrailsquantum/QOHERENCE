# Implementing a Decoder (Expert)

## The decoder's job
Given a stream of syndrome measurements from a surface code (see `03-advanced/01-stabilizer-codes.md`), a **decoder** is the classical algorithm that infers the most likely physical error pattern and outputs the correction to apply. This is a genuinely hard combinatorial inference problem — and, critically, it must run *fast enough* to keep up with the physical qubits' error rate in real time, or errors will accumulate faster than they can be corrected, defeating the entire purpose.

## Minimum-weight perfect matching (MWPM)
The classic and still widely-used decoding approach for the surface code treats syndrome defects as "particles" that must be paired up (matched) via the most likely error chains connecting them, formulated as a **minimum-weight perfect matching** problem on a graph — a well-studied problem in classical computer science with efficient (polynomial-time) algorithms. Each edge in the matching graph is weighted by the estimated probability of that particular error chain, informed by the device's actual calibrated per-qubit and per-gate error rates (not a uniform assumption — real decoders are calibration-aware for better accuracy, mirroring the calibration-aware compilation point in `qoherence-hardware/docs/04-expert/01-building-a-custom-backend.md`).

## Why decoder speed is a hard systems problem, not just an algorithms problem
Superconducting qubits' error-correction cycles run on the order of roughly 1 microsecond; a decoder that can't keep pace with syndrome measurements arriving at that rate creates a growing backlog, which means by the time a correction is finally computed and applied, additional errors have already occurred, degrading the effective threshold. This has driven real hardware-decoder co-design work: Google has published specialized, highly optimized/parallelized MWPM decoder implementations; Riverlane (a decoder-focused quantum software company) and others have explored decoders implemented directly in FPGA hardware for the lowest possible latency, because a software decoder running on a conventional CPU is often too slow for real-time operation at scale.

## Beyond MWPM: neural-network and other decoders
MWPM assumes independent, relatively simple error models and can be suboptimal for more complex, correlated real-hardware noise (e.g., crosstalk between neighboring qubits causing correlated errors that violate MWPM's independence assumptions). Research has explored neural-network-based decoders that can, in principle, learn more accurate noise models directly from data — trading interpretability and worst-case guarantees for potentially better average-case accuracy on real, messy hardware noise. As of 2025–2026 this remains an active research area rather than a deployed industry standard, with MWPM-family decoders still the practical default in most published real-device error-correction demonstrations, including Google's Willow results.

## Implementation notes for `qoherence-mitigate`
- `src/surface_code.py` should expose syndrome extraction as a clearly separated step from decoding, so different decoder implementations (MWPM, or experimental alternatives) can be swapped in and benchmarked against each other — mirroring the backend-adapter separation pattern in `qoherence-hardware/docs/04-expert/01-building-a-custom-backend.md`.
- Decoder correctness testing should include both idealized, independent-error-model synthetic syndrome data (where the "correct" decode is analytically known) and, where possible, noise models informed by real device calibration data, since decoder performance can differ meaningfully between the two.
- Decoder *latency*, not just accuracy, should be tracked as a first-class benchmark metric (see `qoherence-bench/docs/04-expert/01-statistical-rigor-in-quantum-benchmarks.md`) — a highly accurate but too-slow decoder is not practically usable for real-time error correction.

## Next
See `qoherence-bench/docs` for how to rigorously benchmark decoder accuracy, latency, and overall system fidelity.
