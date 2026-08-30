# Extending qoherence-core (Expert)

## Design philosophy
qoherence-core intentionally stays minimal — `Qubit`, `Gate`, `Circuit` —
so it can serve as a shared foundation without opinionated assumptions
about simulation backend, hardware target, or algorithm structure.

## Extension points for contributors
1. **Multi-qubit gate support**: extend `Gate`/`Circuit` to cleanly express
   controlled operations (CNOT, Toffoli, controlled-phase) across arbitrary
   qubit pairs, using tensor product embedding into the full Hilbert space.
2. **Density matrix representation**: add a `DensityMatrix` class alongside
   `Qubit` for representing and evolving mixed/noisy states (see
   `03-advanced/02-density-matrices-and-mixed-states.md`).
3. **Circuit optimization passes**: gate cancellation, commutation-based
   reordering, and depth reduction — useful before submitting circuits to
   qoherence-hardware backends with limited coherence time.
4. **QFT and phase estimation primitives**: reusable `Circuit` builders
   that qoherence-algorithms can import directly.

## Contribution workflow
See `../CONTRIBUTING.md`. New primitives should include:
- Unit tests validating unitarity (U†U = I) for any new gate
- A doc entry in the appropriate tier (beginner/intermediate/advanced/expert)
- An example in `/examples` demonstrating the primitive in a small circuit
