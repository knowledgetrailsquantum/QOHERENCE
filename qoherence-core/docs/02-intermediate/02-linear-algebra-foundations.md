# Linear Algebra Foundations (Intermediate)

## State vectors
A qubit's state is a vector in a complex vector space (Hilbert space). For
n qubits, this vector has 2^n complex entries. Qoherence's `StateVectorSimulator`
represents this directly as a numpy array.

## Gates as unitary matrices
Every quantum gate is a unitary matrix U, meaning U† U = I (its conjugate
transpose is its inverse). This guarantees:
- Reversibility (you can always "undo" a gate)
- Preservation of total probability (no information is created or destroyed)

## Applying a gate
Applying a gate is matrix-vector multiplication: new_state = U @ state.
For multi-qubit circuits, gates on a subset of qubits are embedded into
the full 2^n x 2^n space using tensor (Kronecker) products with identity
matrices on the untouched qubits.

## Inner products and probabilities
The probability of measuring a particular basis state is the squared
magnitude of its amplitude: P(x) = |<x|psi>|^2, where <x|psi> is the inner
product (dot product with complex conjugation) between the basis state and
the current state vector.

## Why this matters for qoherence-core
`Gate.apply()` is literally this matrix multiplication. Understanding the
linear algebra underneath means you can extend qoherence-core with new
custom gates confidently.
