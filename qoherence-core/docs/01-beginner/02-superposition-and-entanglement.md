# Superposition and Entanglement (Beginner)

## Superposition, recapped
A single qubit in superposition is a blend of |0⟩ and |1⟩. That alone gives you *possibility*, but not yet *power* — a classical random-number generator also produces unpredictable outcomes. What makes quantum computing different is what happens when superposed qubits are combined: **interference** and **entanglement**.

## Interference: the actual engine of quantum speedup
Amplitudes (α and β) can be negative or even complex, which means when you combine paths through a circuit, they can *cancel each other out* or *reinforce each other* — just like ripples on a pond. A well-designed quantum algorithm doesn't "try all answers at once and pick the best" (a common but misleading description). It arranges the circuit so that amplitudes leading to *wrong* answers destructively interfere (cancel toward zero) and amplitudes leading to the *right* answer constructively interfere (reinforce toward one). Grover's algorithm (see `qoherence-algorithms`) is essentially interference engineered step by step. This is the single most important thing to understand about why quantum computers are not just "fast classical computers with a magic coin."

## Entanglement: correlation stronger than classical
Two qubits are entangled when their combined state cannot be written as a simple product of two independent single-qubit states. The canonical example is a **Bell pair**:

  |Φ⁺⟩ = (|00⟩ + |11⟩) / √2

Measure the first qubit and you get 0 or 1 with 50/50 probability — nothing special there. But the *instant* you measure it, the second qubit's outcome is now fixed: if the first came out 0, the second will always come out 0 too, and likewise for 1. Neither qubit "decided" its value in advance (this has been experimentally confirmed via Bell-inequality tests, ruling out hidden local variables) — the correlation is a property of the pair, not of either qubit individually.

## Analogy: the magic coin pair (and where it breaks)
Imagine two coins that are magically linked: flip one in Tokyo and one in New York, and no matter how the Tokyo coin lands, the New York coin will match it. That's the surface-level intuition. It breaks down in an important way: this is *not* a communication channel. You cannot use entanglement to send a message faster than light, because the person in New York just sees random 50/50 outcomes on their end — they only learn about the correlation once someone compares notes classically (e.g., over a phone call). Entanglement gives you shared randomness with guaranteed correlation, not a signal.

## Why entanglement matters for computation, not just physics trivia
Entanglement is what lets a quantum computer represent correlations between qubits that no classical bit-string, and no classical probability distribution over bit-strings, can represent efficiently. This is the formal reason an n-qubit system needs 2ⁿ complex numbers to describe fully — those numbers encode not just each qubit's individual state, but every possible correlation between every subset of qubits. Simulating this on a classical computer is why `qoherence-sim` runs out of memory around ~30–50 qubits even on a supercomputer (see `qoherence-sim/docs`), and it's the reason genuinely useful quantum algorithms (Shor's factoring, quantum chemistry simulation) are believed to be exponentially hard classically but efficient quantumly.

## A concrete real-world anchor
IBM's, Google's, and Microsoft's quantum roadmaps are all, underneath the marketing, roadmaps for *sustaining high-fidelity entanglement across more qubits for longer*. Every "qubit count" headline is meaningless without accompanying numbers for **coherence time** (how long superposition/entanglement survives before noise destroys it) and **two-qubit gate fidelity** (how accurately an entangling operation like CNOT can be performed). IonQ and Quantinuum, using trapped-ion qubits, currently lead on two-qubit gate fidelity (often above 99.9%) but have slower gate speeds than superconducting qubits (IBM, Google); superconducting qubits are faster but noisier and need to run at near absolute-zero temperatures in dilution refrigerators. `qoherence-hardware/docs/02-intermediate/01-qubit-technologies.md` compares these platforms in depth.

## Try it yourself
```python
from src.circuit import Circuit
from src.gate import H, CNOT

c = Circuit(num_qubits=2)
c.apply(H, 0)          # put qubit 0 in superposition
c.apply(CNOT, 0, 1)    # entangle qubit 1 with qubit 0
result = c.run()
print(result)           # roughly 50% |00>, 50% |11>, never |01> or |10>
```

## Next
Read `03-gates-and-circuits.md` to see the actual operations (H, X, CNOT, and friends) that create and manipulate superposition and entanglement.
