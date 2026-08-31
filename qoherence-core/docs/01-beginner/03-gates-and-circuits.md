# Gates and Circuits (Beginner)

## Gates are how you steer a qubit
A classical logic gate (AND, OR, NOT) takes bits in and produces bits out, often irreversibly (an AND gate throws away information — you can't reconstruct both inputs from the output alone). A quantum gate is different in a crucial way: it must be **reversible** and **unitary**, meaning it preserves the total probability of the state (the amplitudes still sum-square to 1 after the gate) and, mathematically, you could always apply the "reverse" gate to undo it. This isn't a design choice quantum engineers made for elegance — it's a consequence of the Schrödinger equation, which governs how quantum states evolve, always being reversible.

Practically, a gate is a small matrix that multiplies the qubit's amplitude vector.

## The essential single-qubit gates
- **X gate (quantum NOT)**: flips |0⟩ ↔ |1⟩. On the Bloch-sphere-compass analogy from `01-what-is-a-qubit.md`, this is a 180° rotation around the x-axis.
- **H gate (Hadamard)**: the workhorse of quantum computing. Applied to |0⟩, it produces the equal superposition (|0⟩+|1⟩)/√2. It's how nearly every quantum algorithm starts — "put everything into superposition, then use interference to shape the answer."
- **Z gate**: leaves |0⟩ alone but flips the *sign* of |1⟩'s amplitude. You can't see this with a single measurement (probabilities are unaffected — |−β|² = |β|²), but it matters enormously once you combine it with other gates, because that sign flip changes how amplitudes interfere later.
- **S and T gates**: smaller phase rotations than Z. T in particular is important because, together with H and CNOT, it forms a "universal" gate set — any quantum computation can be built from just these three gate types (approximately, to arbitrary precision). T gates are also disproportionately expensive to implement with error correction, which is why algorithm designers count "T-gate depth" as a cost metric almost as important as qubit count.

## The essential two-qubit gate: CNOT
CNOT (controlled-NOT) flips a "target" qubit if and only if a "control" qubit is |1⟩. Applied to a superposed control qubit, CNOT is what actually *creates* entanglement (see `02-superposition-and-entanglement.md`'s Bell-pair example: H then CNOT). Every quantum computing platform's hardware roadmap ultimately reports its native two-qubit gate — CNOT for IBM's superconducting devices, a Mølmer–Sørensen gate for trapped ions (IonQ, Quantinuum) — because two-qubit gates are dramatically noisier and slower than single-qubit gates, and they're the resource that limits circuit depth in practice.

## Analogy: gates as sheet music, circuits as the performance
If a qubit is an instrument, a gate is a single note or chord instruction, and a **circuit** — an ordered sequence of gates applied to a register of qubits, ending in measurement — is the whole score. Just as a symphony's meaning comes from the sequence and combination of notes, not any single note, a quantum algorithm's power comes from how gates are sequenced to build up interference patterns, not from any individual gate.

## Circuit diagrams
Circuits are conventionally drawn left-to-right, one horizontal line per qubit, with gate symbols placed on the lines in the order they're applied:

```
q0: ─H──●──────
         │
q1: ────X──────
```

This is the Bell-pair circuit from the previous doc: Hadamard on q0, then CNOT with q0 as control and q1 as target.

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

Internally, `Circuit` maintains a state vector of length 2ⁿ and applies each gate as a matrix operation to the relevant qubit indices — this is the same approach `qoherence-sim` scales up (and eventually hits memory limits on), and it's conceptually what real hardware does physically rather than numerically (see `qoherence-hardware`).

## Depth, width, and why they matter
"Width" is the qubit count a circuit needs; "depth" is roughly the number of sequential gate layers. Real hardware qubits decohere (lose their quantum state to environmental noise) within a fixed time window — often microseconds for superconducting qubits, longer for trapped ions — so a circuit that's too *deep* simply won't finish before the qubits' information is corrupted, regardless of how many qubits are available. This is why "1000 qubits" is a much less meaningful number on its own than "1000 qubits at this coherence time and this gate fidelity, supporting a circuit of this depth" — a distinction IBM's own public roadmap explicitly moved toward emphasizing after 2023, shifting from a "qubit count race" framing to a "quantum volume" and "error-per-layered-gate" framing.

## Next
Read `02-intermediate/01-multi-qubit-systems.md` to see how these ideas scale beyond two or three qubits, and where the exponential state space starts to bite.
