# Linear Algebra Foundations (Intermediate)

## In Plain English

Every idea so far in this repo — spinning coins, links between coins, flicks that change how they spin — has a precise mathematical backbone, and that backbone is a branch of math called linear algebra: the study of arrows (vectors), grids of numbers that rotate and stretch those arrows (matrices), and how to combine multiple arrows into one bigger picture. You don't need to have taken a linear algebra course to follow the ideas in this doc set, but it helps enormously to know *why* physicists reach for this particular branch of math rather than some other one.

The reason is almost philosophical: the fundamental law governing how quantum states change over time (the Schrödinger equation) is *linear*, meaning that if two different quantum states are each individually possible, then any blend of them is also a possible state. That single mathematical fact — linearity — is *why* superposition is allowed to exist at all. A non-linear theory of nature wouldn't permit "a bit of this state plus a bit of that state" to be meaningful; ours does, and linear algebra is simply the mathematical language built to describe exactly that kind of blending.

Think of a qubit's state as an arrow. Not an arrow on a flat page, but an arrow in an abstract space with as many directions as there are possible outcomes — for one qubit, that's a 2-directional space (one direction for "leans toward 0," one for "leans toward 1"); for `n` qubits, it's a `2ⁿ`-directional space, per the exponential from the last chapter. A gate is then just an instruction for rotating (and sometimes reflecting) that arrow within its space, without ever stretching or shrinking it — length-preserving, because the arrow's length is tied directly to "the total probability adds up to 100%," and that must never change no matter how you flick the coin.

## Now With the Math

**Vectors: qubit states as columns of numbers.** The state `|ψ⟩ = α|0⟩+β|1⟩` is literally the column `[α, β]`, stacked vertically. `n` qubits give a column with `2ⁿ` entries, one amplitude for each possible outcome combination (see `01-multi-qubit-systems.md`). This space of possible columns is called a Hilbert space — a fancy name for "the full menu of directions this arrow could point."

**Inner products, `⟨φ|ψ⟩` — measuring overlap.** Given two states `|φ⟩` and `|ψ⟩`, their "bra-ket" `⟨φ|ψ⟩` (the "bra" `⟨φ|` is `|φ⟩` written backward and complex-conjugated — don't worry about the mechanics, just that it's a well-defined way to compare two arrows) is a single number measuring how much the two states overlap, similar to how two arrows pointing the same way "overlap" a lot and two perpendicular arrows overlap zero. The probability of measuring outcome `φ` when the system is actually in state `ψ` is `|⟨φ|ψ⟩|²` — this is the multi-outcome generalization of the `|α|²` rule from the very first chapter of this repo.

**Matrices: gates, written out.** A gate on `n` qubits is a `2ⁿ×2ⁿ` grid of numbers (matrix) that multiplies the state column, producing a new state column. It must be **unitary**, written `U†U = I`: `U†` (read "U dagger") is the matrix's conjugate transpose — flip it across its diagonal and conjugate every entry — and `I` is the identity matrix (the "do nothing" matrix, all 1s on the diagonal, 0s elsewhere). The equation `U†U = I` says "undoing U by applying its dagger gets you back to exactly where you started," which is the symbol-level statement of the plain-English "gates must be reversible" rule from `01-beginner/03-gates-and-circuits.md`.

**Tensor products for gates, `⊗`.** Just as states combine via `⊗` (last chapter), gates acting on different qubits combine the same way: applying gate `A` to qubit 0 and gate `B` to qubit 1 at the same time is the combined matrix `A⊗B`. Applying a gate to *only some* qubits in a larger register means tensoring it with the identity matrix `I` on every untouched qubit — "leave those alone" written in the same mathematical language as "do this" — which is exactly what happens under the hood every time you call `c.apply(H, 0)` on a multi-qubit circuit.

**Eigenvalues — a preview for later chapters.** Some matrices have special directions they don't rotate at all — they only stretch or shrink along those directions, by an amount called the eigenvalue. Several important quantum algorithms (VQE, phase estimation underlying Shor's) are fundamentally about *finding* these special stretch amounts for a matrix representing a real physical system's energy — see `qoherence-algorithms/docs/03-advanced/01-vqe-and-qaoa-theory.md`.

## In code
```python
import numpy as np
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])
zero = np.array([1, 0])
print(H @ zero)   # [0.707, 0.707] -- equal superposition

# check unitarity: does undoing H with its own dagger get back to "do nothing"?
print(np.allclose(H.conj().T @ H, np.eye(2)))  # True
```

## Next
Read `03-circuit-composition.md` to see how these matrix operations combine into larger, reusable circuit building blocks.
