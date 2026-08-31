# A Worked Example: Grover's Algorithm on the N-Queens Puzzle (Expert)

## In Plain English

Every other doc about Grover's algorithm (`02-intermediate/01-grover-and-shor-explained.md`) describes it abstractly: "search N items, find the marked one." Real problems don't hand you a neat list of N items — you have to build the "oracle" (the part that recognizes a correct answer) yourself, out of the actual rules of your problem. This doc walks through that translation step, using a classic puzzle: place 4 queens on a 4×4 chessboard so that no two attack each other (share a row, column, or diagonal).

The translation has three parts:
1. **Encode candidate answers as qubits.** Each queen's column position (0-3) becomes a 2-qubit number, one queen per row. Four queens, one per row, need 8 qubits total.
2. **Build an oracle that checks the puzzle's rules.** The oracle compares every pair of queens and flags the state's amplitude if any pair conflicts (same column, or diagonal).
3. **Run ordinary Grover's algorithm** (Hadamards, then repeated oracle + diffusion) on top of that oracle.

The interesting engineering work is almost entirely in step 2 — encoding "no two queens share a diagonal" as a reversible quantum circuit is far more work than the neat, abstract "flip the sign of the right answer" description usually implies.

## Building the Oracle

For each pair of queens `(row_i, row_j)`, the oracle needs to detect three kinds of conflict: same column, same diagonal going one way, same diagonal going the other way. Each check is implemented as a small reversible sub-circuit (see `qoherence-core/docs/02-intermediate/04-reversible-computing.md`) that flips a shared "conflict" ancilla qubit if that particular pair conflicts. After checking every pair, a multi-controlled gate flips the overall answer's phase only if *no* conflict ancilla got set — exactly the "flip the sign of the correct answer" step from Grover's algorithm, just built from many smaller reversible pieces instead of one clean abstract gate.

## Runnable Qiskit Code

```python
from qiskit import QuantumCircuit
from qiskit.circuit.library import MCXGate
import numpy as np

def column_conflict_oracle(qc, q1, q2, ancilla):
    # Flags 'ancilla' if the two 2-qubit column registers q1, q2 are equal
    qc.cx(q1[0], q2[0])
    qc.cx(q1[1], q2[1])
    qc.x(q2[0])
    qc.x(q2[1])
    qc.mcx([q2[0], q2[1]], ancilla)
    qc.x(q2[0])
    qc.x(q2[1])
    qc.cx(q1[0], q2[0])
    qc.cx(q1[1], q2[1])

# 4 queens, 2 qubits each for column position (0-3), plus conflict ancillas
n_queens = 4
qc = QuantumCircuit(n_queens * 2 + 6, n_queens * 2)  # extra ancillas for conflict checks
queens = [qc.qubits[i*2:i*2+2] for i in range(n_queens)]

# Step 1: superposition over all column placements
for q in qc.qubits[:n_queens*2]:
    qc.h(q)

# Step 2 (sketch): pairwise conflict checks feed into a final phase flip.
# A full implementation checks columns and both diagonals for every pair
# and combines all conflict ancillas with a multi-controlled Z before uncomputing.

# Step 3: the diffusion operator (standard Grover step, same for every problem)
def diffusion(qc, qubits):
    for q in qubits:
        qc.h(q)
        qc.x(q)
    qc.h(qubits[-1])
    qc.mcx(qubits[:-1], qubits[-1])
    qc.h(qubits[-1])
    for q in qubits:
        qc.x(q)
        qc.h(q)
```

This is a sketch, not the full working solution — the complete version needs diagonal-conflict checks (a small modular-arithmetic-style comparison) and careful ancilla uncomputation (see `qoherence-core/docs/02-intermediate/03-circuit-composition.md`) so no leftover entanglement corrupts the final measurement. The full worked project, including tests, is the kind of thing covered end-to-end in Mariia Mykhailova's *Quantum Programming in Depth* — a good next stop for anyone who wants the complete, tested version.

## The Practical Lesson

Building this oracle takes far more circuit depth than the four rows of the puzzle might suggest — every pairwise check adds ancilla qubits and gates, and Grover's quadratic speedup (`√N` instead of `N`) has to be weighed against that real, non-trivial oracle cost. For small puzzles like 4-queens, a classical brute-force search is faster in practice once you count actual runtime, not just query count — Grover's algorithm only starts winning once `N` gets large enough that the quadratic gap outweighs the oracle-construction overhead. This gap between "asymptotically faster" and "actually faster today" is exactly what `qoherence-bench/docs/03-advanced/02-resource-estimation.md` is about.

## Next
Read `qoherence-hardware/docs/01-beginner/01-what-is-real-quantum-hardware.md` — from here, the trail moves from algorithm design to the physical machines these circuits actually run on.

---
**[◀ Implementing Shor's Period-Finding](01-implementing-shors-period-finding.md)**  |  [Index](../../../README.md)  |  **[What Is Real Quantum Hardware? ▶](../../../qoherence-hardware/docs/01-beginner/01-what-is-real-quantum-hardware.md)**
