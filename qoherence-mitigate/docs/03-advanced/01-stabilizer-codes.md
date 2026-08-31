# Stabilizer Codes (Advanced)

## The core idea: redundancy without cloning
`qoherence-core/docs/04-expert/01-fault-tolerant-computation.md` noted the no-cloning theorem prevents simply copying a qubit's state for redundancy. Stabilizer codes solve this by encoding logical information into the *joint, entangled* state of many physical qubits, such that no individual physical qubit's state alone reveals the logical information — errors on individual physical qubits can then be detected and corrected without ever directly measuring (and thus destroying) the encoded logical state.

## Stabilizers, syndromes, and why this works
A **stabilizer code** is defined by a set of operators (the "stabilizers," built from products of Pauli X and Z operations across several physical qubits) that all have eigenvalue +1 on the valid encoded logical states. Measuring a stabilizer doesn't reveal the logical qubit's actual value — but if a physical error has occurred, it flips the outcome of one or more stabilizer measurements to -1, called a **syndrome**. Different error types (X errors, Z errors, or both) produce distinguishable syndrome patterns, letting a classical **decoder** infer what error most likely occurred and which correction to apply — all without the measurement itself collapsing the logical information, because stabilizer measurements are carefully designed to be "logical-state-agnostic."

## The surface code: the field's leading practical candidate
The **surface code** (`src/surface_code.py`) arranges physical qubits on a 2D lattice, alternating "data" qubits (which hold the encoded information) with "ancilla" qubits used purely to measure local stabilizers — a pattern that only requires nearest-neighbor interactions, which is exactly why it's compatible with superconducting chips' fixed 2D connectivity (see `qoherence-hardware/docs/03-advanced/01-connectivity-and-transpilation.md`), and part of why IBM's heavy-hex lattice chip layout was chosen with surface-code compatibility in mind.

Key properties:
- **Code distance d**: roughly, the minimum number of physical errors needed to cause an undetectable logical error. Larger d means more physical qubits per logical qubit, but exponentially better logical error suppression (below the threshold error rate).
- **Threshold behavior**: below a critical physical error rate (~1% for the surface code, roughly), increasing d *decreases* logical error rate; above threshold, increasing d makes things *worse*. Google's Willow chip's December 2024 headline result was demonstrating clean below-threshold scaling — logical error rate dropping by roughly half with each increase in code distance — the first such clear demonstration in a real superconducting device at meaningful scale.
- **Overhead**: current practical estimates suggest on the order of 1,000+ physical qubits per logical qubit at today's physical error rates for the surface code specifically, which is why fault-tolerant algorithms needing many logical qubits (Shor's at cryptographic scale) require millions of physical qubits — a huge gap from today's hundreds to low-thousands-qubit devices.

## Beyond the surface code: quantum LDPC codes
The surface code's large overhead has motivated research into alternative codes — particularly **quantum low-density parity-check (LDPC) codes** — that promise substantially better encoding rates (fewer physical qubits needed per logical qubit) at the cost of requiring longer-range qubit connectivity than a simple 2D grid provides. IBM has published research (including its 2023–2024 work on "bivariate bicycle codes") suggesting LDPC-style codes could cut physical-qubit overhead by roughly an order of magnitude compared to the surface code, at the cost of needing more complex chip connectivity than today's heavy-hex layout — an active area of hardware-codesign research as of 2025–2026, illustrating that error-correcting code choice and physical chip architecture design are deeply intertwined decisions, not independent layers.

## Analogy: a lattice-wide checksum, not a single backup copy
A single classical backup copy (RAID-style redundancy) says "if the original is damaged, use the copy." A stabilizer code is closer to a distributed checksum system spread across the whole lattice — no single physical qubit is "the" backup, and the encoded information only exists meaningfully in the *pattern* of correlations across many qubits, checked continuously via non-destructive syndrome measurements, and corrected on the fly.

## Next
Read `04-expert/01-implementing-a-decoder.md` for how the classical algorithm that interprets syndrome measurements and decides what correction to apply actually works.
