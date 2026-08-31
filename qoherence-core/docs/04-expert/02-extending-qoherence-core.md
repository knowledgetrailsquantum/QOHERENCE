# Extending qoherence-core (Expert)

## Design philosophy
qoherence-core deliberately keeps three concerns separate, mirroring how production quantum SDKs (Qiskit, Cirq, Q#) are structured:
- **`Qubit`** — single-qubit state representation (used mainly for pedagogy; multi-qubit circuits use a full state vector, not a list of `Qubit` objects, since general multi-qubit states are entangled and can't be decomposed into independent per-qubit objects — see `02-intermediate/01-multi-qubit-systems.md`).
- **`Gate`** — matrix definitions and metadata (name, arity, whether it's parameterized).
- **`Circuit`** — the ordered sequence of (gate, qubit-indices) operations, plus the state-vector simulation engine (`run()`).

Downstream repos depend on this separation: `qoherence-algorithms` builds `Circuit` objects using standard gates; `qoherence-sim` provides alternative, more scalable execution backends for the same `Circuit` representation; `qoherence-hardware` compiles `Circuit` objects down to real-device instructions; `qoherence-mitigate` post-processes `Circuit.run()` results.

## Adding a new gate
1. Define the gate's unitary matrix in `src/gate.py`, following the existing pattern (a NumPy array, or a function returning one if the gate is parameterized, e.g. a rotation gate `RZ(theta)`).
2. Register its arity (1-qubit, 2-qubit, etc.) so `Circuit.apply()` knows how many qubit indices to expect.
3. If the gate is not already expressible as a composition of existing gates, add a unit test asserting unitarity (`U† U == I`, within floating-point tolerance) — a non-unitary "gate" will silently produce nonsensical, non-normalized probabilities in `Circuit.run()`, which is one of the more insidious classes of bugs in quantum software, precisely because it may not throw an error, just quietly wrong numbers.

## Adding a new simulation backend
`Circuit.run()`'s default backend maintains a full 2ⁿ-length state vector and applies each gate as a matrix-vector product — correct, but memory-limited to roughly 25–30 qubits on commodity hardware (see `qoherence-sim/docs/02-intermediate/01-state-vector-limits.md` for the precise math). A new backend should implement the same `run(circuit) -> Result` interface so it's a drop-in replacement; `qoherence-sim`'s tensor-network backend is the reference example of this pattern, trading generality for the ability to simulate certain low-entanglement circuits with far more qubits.

## Extending toward hardware realism
If you're contributing noise-aware simulation (rather than pure error-free execution), don't bolt noise onto `Circuit` directly — follow the density-matrix approach from `03-advanced/02-density-matrices-and-mixed-states.md` and route it through `qoherence-mitigate`'s noise-model interfaces, so noise characterization stays decoupled from the core gate/circuit abstractions. This mirrors how Qiskit separates `qiskit` (circuit construction) from `qiskit_aer` (noisy simulation) from `qiskit_ibm_runtime` (real hardware execution) — a separation that exists precisely because these three concerns evolve at different rates and are maintained by different expertise areas.

## Testing conventions
- Every new gate: assert unitarity, assert correct action on computational basis states, assert correct action on at least one superposition state (verifying not just "does it produce *a* normalized output" but "does it produce the mathematically *correct* output").
- Every new circuit-composition helper (per `02-intermediate/03-circuit-composition.md`): assert it correctly uncomputes any ancilla qubits it introduces, by checking that those qubits' reduced density matrix is |0⟩⟨0| at the end.
- Every new backend: run it against a shared conformance test suite comparing outputs to the reference state-vector backend on small circuits (where both are tractable), before trusting it on circuits too large for the reference backend to check.

## Contributing
See `CONTRIBUTING.md` in this repo's root for process; conceptually, contributions that add physical realism (noise models, connectivity constraints) belong here or in `qoherence-hardware`/`qoherence-mitigate` depending on whether they're about *representing* physical constraints (core/hardware) or *compensating* for them (mitigate).
