# Connectivity & Transpilation (Advanced)

Real devices don't have all-to-all qubit connectivity — two-qubit gates
only work between physically coupled qubits. **Transpilation** rewrites a
logical circuit to fit hardware topology, inserting SWAP gates as needed,
which adds depth and noise. Backend adapters in qoherence-hardware should
eventually integrate provider-specific transpilers (Qiskit, pyQuil) before
submission.
