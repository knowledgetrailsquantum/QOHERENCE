# Circuit Composition (Intermediate)

## In Plain English

Nobody writes real software by describing every single CPU instruction from scratch each time — they write functions, and call them, and build bigger functions out of smaller ones. Quantum circuits work the same way. Instead of listing every gate for a 50-qubit algorithm one by one, you build small, reusable *blocks* — "make a Bell pair," "shuffle these four qubits' amplitudes around" — and stitch them together into bigger circuits, the same way you'd assemble a recipe from smaller sub-recipes ("make the dough," "make the filling," "assemble and bake").

There's a wrinkle unique to the quantum case, though, that doesn't show up in ordinary programming: because every gate must be reversible (from `01-beginner/03-gates-and-circuits.md`), you sometimes need temporary "scratch space" qubits — borrow a qubit, use it partway through a calculation, and then very deliberately run part of the circuit *backward* to erase whatever mess you made in that scratch qubit before you finish, a process called **uncomputation**. If you forget to clean up, that leftover scratch qubit stays tangled up with your real answer qubits, and — because it's entangled — that lingering link quietly corrupts your final measurement, like a forgotten variable in a spreadsheet that keeps throwing off totals you can't quite trace back.

## Composition patterns, in plain terms

- **Sequential composition** — do block A, then do block B, to the same qubits, one after the other. Order matters: doing your left shoe then your right sock is not the same as doing your right sock then your left shoe.
- **Parallel composition** — do block A on one set of qubits and block B on a completely different set, at the same time — like two people cooking different dishes on separate stovetops simultaneously.
- **Controlled subcircuits** — run an entire block, but only in the branch of the superposition where some other qubit happens to be 1 — the block-sized version of the single-gate CNOT idea from `01-beginner/03-gates-and-circuits.md`.

## Now With the Math

**Sequential composition as matrix multiplication.** If block A's overall effect is the matrix `U_A` and block B's is `U_B`, doing A then B is the matrix `U_B · U_A` — note block B's matrix goes on the *left* even though it happens second. This ordering (right-to-left, matching "the thing that acts on the state first is written closest to the state") is a very common source of bugs when translating a left-to-right circuit diagram into matrix algebra, so it's worth internalizing early.

**Parallel composition as tensor product.** Doing block A on one group of qubits and block B on a disjoint group at the same time is the matrix `U_A ⊗ U_B` — the same `⊗` combining operation from `02-linear-algebra-foundations.md`, now applied to whole blocks instead of single gates.

**Uncomputation, precisely.** If a subcircuit's matrix is `U`, running it "backward" means applying `U†` (its dagger, from the last chapter) — and because every gate is unitary, `U†U = I` guarantees this backward-run genuinely restores the scratch qubits to exactly `|0⟩`, with no residual entanglement to the rest of the circuit. Checking this in code means verifying an ancilla qubit's reduced state (see `03-advanced/02-density-matrices-and-mixed-states.md`) really is `|0⟩⟨0|` at the end, not just "probably close to it."

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

## A real-world grounding
This reversibility-first, no-implicit-information-loss design philosophy is baked directly into IBM's Qiskit, Google's Cirq, and Microsoft's Q# — none of them let you "just discard" a qubit's information mid-circuit the way a classical language lets you overwrite a variable, precisely because the underlying physics doesn't allow it either.

## Next
Read `03-advanced/01-quantum-fourier-transform.md` — the QFT is the most important reusable subcircuit block in quantum computing, underlying Shor's algorithm, phase estimation, and much of quantum signal processing.
