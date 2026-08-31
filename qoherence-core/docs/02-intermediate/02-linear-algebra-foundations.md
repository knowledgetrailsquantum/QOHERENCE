# Linear Algebra Foundations (Intermediate)

## Why linear algebra, specifically
Quantum mechanics is, mathematically, linear algebra over complex vector spaces. This isn't an approximation or a teaching simplification — the Schrödinger equation is linear, meaning if |ψ₁⟩ and |ψ₂⟩ are both valid states, so is any combination a|ψ₁⟩+b|ψ₂⟩ (suitably normalized). That linearity is *why* superposition exists at all: it's what a linear theory of nature permits that a nonlinear one wouldn't.

## Vectors: qubit states
A single qubit state |ψ⟩ = α|0⟩+β|1⟩ is literally the column vector [α, β]ᵀ. n qubits give a vector in a 2ⁿ-dimensional complex vector space (a "Hilbert space"). The basis vectors |0⟩=[1,0]ᵀ and |1⟩=[0,1]ᵀ are the computational basis; multi-qubit basis states like |01⟩ are tensor products of these.

## Inner products: measurement probabilities
The inner product ⟨φ|ψ⟩ (bra-ket notation — ⟨φ| is the conjugate transpose of |φ⟩) measures the overlap between two states. The probability of measuring outcome φ when the qubit is in state ψ is |⟨φ|ψ⟩|². This single formula (the Born rule) is how every probability in this repo's `Circuit.run()` output is computed.

## Matrices: gates
A quantum gate on n qubits is a 2ⁿ×2ⁿ unitary matrix U, meaning U†U = I (its conjugate transpose is its inverse). Unitarity is what guarantees the gate preserves the normalization Σ|amplitude|²=1 — a non-unitary matrix would let probabilities leak away or exceed 1, which isn't physically meaningful. Some familiar gates as matrices:

```
X = [[0, 1],      H = (1/√2)[[1,  1],     Z = [[1,  0],
     [1, 0]]                 [1, -1]]          [0, -1]]
```

CNOT, acting on 2 qubits, is a 4×4 matrix that swaps the |10⟩ and |11⟩ basis-vector rows relative to the identity, encoding "flip the target when the control is 1."

## Tensor products: composing systems
Combining independent qubit states uses the tensor (Kronecker) product ⊗, described in `01-multi-qubit-systems.md`. Combining *gates* that act on different qubits works the same way: applying gate A to qubit 0 and gate B to qubit 1 simultaneously is the matrix A⊗B. Applying a gate to only *some* qubits in a larger register means tensoring it with identity matrices on the untouched qubits — this is exactly what `src/circuit.py`'s gate-application logic does under the hood when you call `c.apply(H, 0)` on a multi-qubit circuit.

## Eigenvalues and eigenvectors: why they matter here
Several important quantum algorithms — including VQE and quantum phase estimation, which underlies Shor's algorithm — are fundamentally about finding eigenvalues of a matrix (often representing a molecule's or system's energy, the Hamiltonian). A quantum computer can prepare states, apply unitary evolution related to the Hamiltonian, and extract eigenvalue information via measurement statistics in ways that are exponentially hard to do classically for large systems. This is the mathematical basis for the excitement around quantum computers accelerating materials science, drug discovery, and battery chemistry — Microsoft's Azure Quantum Elements platform, IBM's collaboration with Cleveland Clinic on molecular simulation, and Google's chemistry-focused algorithm research all point back to this same eigenvalue-finding structure.

## Analogy: matrices as instructions for rotating and reflecting a shape
If a state vector is an arrow, a unitary matrix is an instruction for rotating and/or reflecting that arrow without stretching or shrinking it (unitary transformations preserve vector length). This maps cleanly onto the Bloch sphere picture from `01-what-is-a-qubit.md`: every single-qubit gate is literally a rotation of the compass-needle arrow on that sphere. Multi-qubit gates are harder to visualize this simply (there's no single "Bloch sphere" for entangled multi-qubit states), which is part of why entanglement resists easy intuition.

## In code
```python
import numpy as np
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])
zero = np.array([1, 0])
print(H @ zero)   # [0.707, 0.707] — equal superposition

# check unitarity
print(np.allclose(H.conj().T @ H, np.eye(2)))  # True
```

## Next
Read `03-circuit-composition.md` to see how these matrix operations combine into larger, reusable circuit building blocks.
