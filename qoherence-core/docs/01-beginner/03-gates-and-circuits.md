# Gates and Circuits (Beginner)

## In Plain English

If a qubit is a spinning coin, a **gate** is a precise, physical nudge you give the coin while it's still in the air — a flick that changes how it's spinning, without ever letting it land. You can flick it so it flips its lean entirely (mostly-heads becomes mostly-tails), or so it starts spinning evenly when it wasn't before, or so two coins, previously independent, start behaving as a linked pair (see the last chapter). A **circuit** is just an ordered recipe of these flicks — flick this coin this way, then that coin that way, then link these two — ending with everyone landing at once (measurement).

There's one rule every one of these flicks must obey, and it's worth understanding *why* it exists rather than just memorizing it: every gate must be **reversible**. You must always be able to, in principle, un-flick it — apply an "undo" nudge that brings the coin back to exactly how it was spinning before. A classical AND gate, by contrast, is *not* reversible: if you're told the output is 0, you can't tell whether the inputs were (0,0), (0,1), or (1,0) — that information is thrown away. Quantum gates are never allowed to throw information away like that, because the deep physical law that governs how quantum states evolve over time (the Schrödinger equation, if you want the name) is itself always reversible. This isn't a design choice engineers made for elegance; it's a hard constraint imposed by physics, and every quantum gate you'll ever encounter respects it.

The single most important flick in the entire field is the one that takes a qubit from "definitely 0" to "spinning evenly, 50/50" — this move, called the **Hadamard**, is how almost every quantum algorithm begins: "start everything spinning, then use the interference tricks from the last chapter to shape the answer." If gates are notes, a circuit is the whole musical score — and nearly every quantum score opens with the same first note.

Two-qubit flicks are where entanglement gets created. The classic one says "flick the second coin's spin, but only if the first coin is currently leaning toward 1." Apply that to a first coin that's already spinning evenly, and you get exactly the linked Bell pair from the previous chapter — this is, quite literally, the two-line recipe for creating entanglement from scratch, and you'll see it appear constantly throughout this repo.

## Now With the Math

**The gate as a matrix.** A gate is a small grid of numbers (a matrix) that multiplies a qubit's amplitude pair `[α, β]`, producing a new amplitude pair. "Applying a gate" and "multiplying by its matrix" are the same operation — this is the payoff for having written qubit states as vectors of numbers back in the first chapter: it lets "what does this flick do" become an ordinary (if unfamiliar) piece of arithmetic.

**X — the quantum NOT.**
```
X = [[0, 1],
     [1, 0]]
```
Multiplying `[α, β]` by this matrix swaps the two entries, giving `[β, α]`. In plain terms: it flips `|0⟩` into `|1⟩` and vice versa — the flick that fully reverses a coin's lean.

**H — the Hadamard, the "start spinning evenly" gate.**
```
H = (1/√2) [[1,  1],
            [1, -1]]
```
Applied to `[1, 0]` (a qubit definitely in `|0⟩`), this produces `[1/√2, 1/√2]` — equal-sized amplitudes for 0 and 1, meaning a perfect 50/50 spin. The `1/√2` out front is, again, just there to keep `|α|²+|β|²=1` true.

**Z — the invisible-until-combined gate.**
```
Z = [[1,  0],
     [0, -1]]
```
This leaves `|0⟩` completely alone and flips the *sign* of `|1⟩`'s amplitude (from `β` to `-β`). Squaring a negative number gives the same result as squaring a positive one, so `|−β|² = |β|²` — meaning Z changes nothing about what you'd measure on this qubit by itself. Why bother, then? Because that sign flip matters enormously later, when this qubit's amplitude gets combined with others during interference (from the last chapter) — a sign is invisible in isolation but decisive in combination, the same way a single negative ripple looks unremarkable until it meets another wave and the two cancel out.

**CNOT — the entangling gate.** A 4×4 matrix acting on two qubits at once (four amplitudes in, four amplitudes out, mirroring the four two-qubit outcomes `|00⟩,|01⟩,|10⟩,|11⟩` from the last chapter), whose plain-English rule is "flip the second qubit's amplitude pattern, but only in the part of the superposition where the first qubit is 1." Feed it a first qubit that's already 50/50 (via H) and a second qubit starting at `|0⟩`, and the output is exactly the Bell pair `(|00⟩+|11⟩)/√2` from the previous chapter — this two-gate sequence, H then CNOT, is the standard, universally-used recipe for manufacturing entanglement, and it's worth memorizing as a unit.

**Circuit diagrams.** Circuits are drawn left-to-right, one horizontal line per qubit, with symbols marking where each gate is applied in sequence:
```
q0: ─H──●──────
         │
q1: ────X──────
```
This is precisely the Bell-pair recipe above — Hadamard on q0, then CNOT with q0 as the "only if 1" control and q1 as the qubit that gets flipped.

## qoherence-core's Circuit class
```python
from src.circuit import Circuit
from src.gate import H, X, CNOT

c = Circuit(num_qubits=3)
c.apply(H, 0)
c.apply(CNOT, 0, 1)
c.apply(X, 2)
print(c)          # inspect the gate sequence
result = c.run()  # execute against the internal state vector
```

## Depth, width, and why they matter
"Width" is the qubit count a circuit needs; "depth" is roughly the number of sequential gate layers. Real hardware qubits decohere within a fixed time window, so a circuit that's too *deep* simply won't finish before the qubits' information is corrupted, regardless of how many qubits are available — which is why "1,000 qubits" on its own is a far less meaningful headline than "1,000 qubits at this coherence time and this gate fidelity."

## Next
Read `02-intermediate/01-multi-qubit-systems.md` to see how these ideas scale beyond two or three qubits, and where the exponential state space starts to bite.

## A Bit of History
The Hadamard gate is named after French mathematician Jacques Hadamard, who died in 1963 — a decade before anyone was building quantum circuits. He never worked on quantum computing; the "Hadamard matrix" pattern he studied in 1893 for an entirely different problem (matrix determinants) turned out, nearly a century later, to be exactly the mathematical shape needed to put a qubit into perfect superposition. It's one of quantum computing's odder debts to 19th-century pure mathematics that had no application in mind at all.

---
**[◀ Superposition and Entanglement](02-superposition-and-entanglement.md)**  |  [Index](../../../README.md)  |  **[Multi-Qubit Systems ▶](../02-intermediate/01-multi-qubit-systems.md)**
