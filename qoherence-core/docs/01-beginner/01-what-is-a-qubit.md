# What Is a Qubit? (Beginner)

## The one-sentence answer
A qubit is the smallest unit of quantum information — like a bit, but instead of being locked to 0 or 1, it can hold a weighted, reversible blend of both until you measure it.

## Start with the classical bit
Every computer you have ever used — your phone, a laptop, the servers behind a website — represents information as bits: physical switches (transistors) that are either off (0) or on (1). A byte is 8 of these switches. A gigabyte is roughly 8 billion of them. Classical computing is, at bottom, the choreography of enormous numbers of two-state switches.

A qubit is also a two-state physical system, but the state it can be in is richer than "off or on." The two reference states are usually written |0⟩ and |1⟩ (the "ket" notation physicists use for quantum states), but a qubit can also be in a **superposition**:

  |ψ⟩ = α|0⟩ + β|1⟩

α and β are complex numbers called amplitudes. They are not probabilities themselves — the actual probability of measuring 0 is |α|², and of measuring 1 is |β|², and these two must sum to 1 (you can't measure "1.3" or "-0.2" of anything). This is the single rule that keeps quantum mechanics from being magic: whatever superposition a qubit is in, the probabilities of its possible outcomes always add up to 100%.

## Three analogies, and where each one breaks down
Analogies for qubits are popular because superposition has no everyday equivalent, but every analogy is imperfect — knowing where it fails is as useful as the analogy itself.

**The spinning coin.** A classical bit is a coin lying flat on a table: heads or tails, already decided, and you just haven't looked yet. A qubit is more like a coin spinning in the air — genuinely undetermined, not "secretly" heads or tails waiting to be revealed. This captures superposition well but fails to capture amplitude *phase* (the coin analogy has no notion of the negative or complex-valued relationships between α and β that make interference possible).

**The dimmer switch vs. the light switch.** A classical bit is an on/off light switch. A qubit is a dimmer, but that's misleading too, because a dimmer has one dial (brightness) while a qubit's state lives on the surface of a sphere (the Bloch sphere) — it has two degrees of freedom, not one. Still, this analogy is useful for building intuition that a qubit's state is continuous, not just "somewhere between 0 and 1" in a linear sense.

**The compass needle.** A qubit's state can be visualized as an arrow pointing somewhere on a 3D sphere (the Bloch sphere), where the North Pole is |0⟩ and the South Pole is |1⟩. Points on the equator are equal superpositions. This is the analogy practicing quantum engineers actually use daily, because it maps directly onto how gates rotate the qubit's state — but it requires accepting an abstract 3D picture rather than something you can touch.

## Measurement: the point of no return
When you measure a qubit, the superposition doesn't get "read out" — it collapses. The qubit picks a definite outcome (0 or 1) with probability |α|² or |β|², and after that instant, the qubit *is* that classical value; the information about α and β (beyond the one that was picked) is gone. This is fundamentally different from classical bit-reading, which is non-destructive. It's also why quantum algorithms are engineered so that the useful answer has high amplitude right before the final measurement — you generally get exactly one shot per run of the circuit.

## Why this is worth the trouble
A single qubit isn't more powerful than a single bit — the payoff comes from combining many qubits, where the size of the state space needed to describe them grows exponentially (2ⁿ complex amplitudes for n qubits) while a classical bit register only needs n bits to describe its state. That exponential is qoherence-core's entire reason for existing, and it's why companies like IBM, Google, and Microsoft measure progress in "how many *good* qubits" rather than qubit count alone — a noisy qubit that decoheres before your circuit finishes is nearly as useless as no qubit at all. `03-gates-and-circuits.md` and `qoherence-hardware` go into what "good" means physically.

## What's happening in the world right now
As of 2025–2026, qubit counts on the flashiest chips (IBM's Condor-class and Heron-class processors, Google's Willow, Atom Computing/Quantinuum's neutral-atom and trapped-ion systems) range from roughly 100 to over 1,000 physical qubits, but the industry's real benchmark has shifted to **logical qubits** — error-corrected qubits built by combining many physical ones (see `qoherence-mitigate`). Google's Willow chip made headlines in late 2024 for demonstrating that error rates *drop* as more physical qubits are added per logical qubit, which is the first hard evidence that the error-correction math actually works below the "surface code threshold" in a real device — a milestone the field had chased for over a decade.

## Try it yourself
```python
from src.qubit import Qubit
q = Qubit(alpha=1.0, beta=0.0)   # definitely |0>
print(q)

import math
q2 = Qubit(alpha=1/math.sqrt(2), beta=1/math.sqrt(2))  # equal superposition
print(q2)   # 50/50 chance of 0 or 1 on measurement
```

## Next
Read `02-superposition-and-entanglement.md` — superposition on its own is interesting, but it's what happens when *multiple* qubits interact that gives quantum computers their power.
