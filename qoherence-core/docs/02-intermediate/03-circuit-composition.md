# Circuit Composition (Intermediate)

## Building blocks, not one-off circuits
Real quantum programs are rarely written gate-by-gate from scratch. Just as classical software is built from functions and libraries, quantum circuits are built from reusable **subcircuits**: a Bell-pair preparation, a "diffusion" operator (used repeatedly in Grover's algorithm), a quantum Fourier transform block (used in Shor's and phase estimation), or an "ansatz" block (a parameterized subcircuit used in VQE — see `qoherence-algorithms`). qoherence-core's `Circuit` class is designed so these blocks can be composed: build a subcircuit, then splice it into a larger circuit at a chosen set of qubit indices.

## Composition patterns
- **Sequential composition**: apply circuit A's gates, then circuit B's gates, to the same qubits — the combined unitary is U_B · U_A (matrix multiplication in reverse order of application, a common source of bugs when translating circuit diagrams to code).
- **Parallel composition**: apply circuit A to qubits {0,1} and circuit B to qubits {2,3} simultaneously — the combined unitary is the tensor product U_A ⊗ U_B.
- **Controlled subcircuits**: apply an entire subcircuit only if some other qubit is |1⟩ — this generalizes the single-gate CNOT idea to whole blocks, and is essential for algorithms like quantum phase estimation.

## Barriers, ancillas, and uncomputation
Real circuits often need **ancilla qubits** — temporary "scratch space" qubits used mid-circuit and then returned to |0⟩ before the end, a process called **uncomputation** (running part of the circuit in reverse to erase intermediate results, since gates are reversible). Forgetting to uncompute ancillas is one of the most common correctness bugs in quantum programming: leftover entanglement between ancillas and your "answer" qubits will bias or randomize the final measurement in subtle ways, because a lingering entangled ancilla acts like an unwanted measurement that partially collapses your result.

## Analogy: composing circuits is like composing functions, with a twist
In classical programming, `f(g(x))` composes cleanly because functions can discard information. In quantum circuit composition, every block must be reversible, so "composing" is closer to composing bijections (one-to-one, invertible mappings) than composing arbitrary functions — you can always ask "what mapped to this state?" and get a unique answer. This reversibility constraint is why quantum programming languages (Qiskit from IBM, Cirq from Google, Q# from Microsoft) all bake "no implicit information loss" into their circuit-building APIs, even though it feels restrictive coming from classical software design.

## Transpilation preview
A circuit you compose logically (in terms of "ideal" gates like arbitrary rotations or all-to-all CNOT) usually cannot run directly on real hardware, which supports only a specific native gate set and only allows two-qubit gates between physically adjacent qubits. Converting your composed circuit into the hardware's native gates and connectivity is called **transpilation**, covered in depth in `qoherence-hardware/docs/03-advanced/01-connectivity-and-transpilation.md`. Composition and transpilation are related but distinct concerns: composition is about circuit *design*, transpilation is about circuit *compilation* for a specific target.

## In code
```python
from src.circuit import Circuit
from src.gate import H, CNOT, X

def bell_pair_block(circuit, q0, q1):
    circuit.apply(H, q0)
    circuit.apply(CNOT, q0, q1)

c = Circuit(num_qubits=4)
bell_pair_block(c, 0, 1)   # first entangled pair
bell_pair_block(c, 2, 3)   # second, independent entangled pair
result = c.run()
```

## Next
Read `03-advanced/01-quantum-fourier-transform.md` — the QFT is the most important reusable subcircuit block in quantum computing, underlying Shor's algorithm, phase estimation, and much of quantum signal processing.
