# Density Matrices and Mixed States (Advanced)

## The limitation of state vectors
Everything in `01-beginner` and `02-intermediate` describes **pure states** — a qubit whose state is precisely known as a vector |ψ⟩. Real qubits are never perfectly isolated: they interact with their environment (stray electromagnetic fields, thermal photons, imperfect control pulses), and this interaction introduces classical uncertainty on top of quantum uncertainty. A qubit that's "80% likely to be in state |ψ₁⟩ and 20% likely to be in state |ψ₂⟩" (due to noise, not measurement) cannot be written as any single state vector — it needs the **density matrix** formalism.

## The density matrix
A pure state |ψ⟩ corresponds to the density matrix ρ = |ψ⟩⟨ψ|. A **mixed state** — a genuine statistical mixture of several possible pure states |ψᵢ⟩, each with classical probability pᵢ — is ρ = Σᵢ pᵢ|ψᵢ⟩⟨ψᵢ⟩. Density matrices generalize state vectors: every quantum state, pure or mixed, has a density matrix, but not every density matrix corresponds to a single state vector.

Key facts used throughout `qoherence-mitigate`:
- **Trace**: Tr(ρ) = 1 always (total probability is conserved).
- **Purity**: Tr(ρ²) = 1 for a pure state, and < 1 for a mixed state — this single number is a standard way to quantify "how noisy" a qubit currently is.
- **Measurement probabilities**: the probability of outcome corresponding to projector P is Tr(Pρ), generalizing |⟨φ|ψ⟩|².

## Why this matters: decoherence is a mixed-state phenomenon
"Decoherence" — the loss of quantum information to the environment — is precisely the process by which a pure state's density matrix evolves toward a mixed one. Two standard noise processes, both directly measured and reported on real hardware datasheets from IBM, Google, IonQ, and Rigetti:

- **T1 (amplitude damping / relaxation time)**: how long it takes, on average, for an excited qubit (|1⟩) to spontaneously decay to |0⟩, losing energy to the environment.
- **T2 (dephasing time)**: how long it takes for the *phase relationship* between α and β to randomize, destroying superposition information even without necessarily flipping the qubit's measured value.

T1 and T2 are reported in microseconds and are among the first numbers any quantum hardware team publishes about a new chip — they directly bound how deep a circuit can be before results become noise-dominated. Superconducting qubits (IBM, Google, Rigetti) typically report T1/T2 in the tens to low hundreds of microseconds range; trapped-ion qubits (IonQ, Quantinuum) can have coherence times of seconds or more, a major reason they achieve higher-fidelity two-qubit gates despite slower gate speeds.

## Analogy: a clean photograph vs. a double exposure
A pure state is like a single, sharp photograph — perfectly determined, even though you can't fully "see" it without measuring (destructively). A mixed state is like a double- or triple-exposed photograph — a genuine blend of several possible sharp photographs, where you've lost track of which one is "really" underneath. No amount of staring at the blended photo alone can un-blend it; you'd need outside information (like knowing the mixing probabilities) that the photo itself doesn't fully encode.

## Partial trace: describing part of an entangled system
If two qubits are entangled and you only care about qubit A, you compute the **partial trace** over qubit B to get qubit A's **reduced density matrix**. A striking and important fact: for a maximally entangled pair (like the Bell pair from earlier docs), each individual qubit's reduced density matrix is *maximally mixed* — it looks completely random on its own, even though the pair together is in a perfectly well-defined pure state. This is the formal statement of "entanglement information lives in the correlations, not in either qubit individually," referenced informally in `01-beginner/02-superposition-and-entanglement.md`.

## In code (conceptually)
```python
import numpy as np
# Maximally mixed single qubit: 50% |0>, 50% |1>, classically
rho = 0.5 * np.array([[1, 0], [0, 0]]) + 0.5 * np.array([[0, 0], [0, 1]])
print(rho)          # [[0.5, 0], [0, 0.5]]
print(np.trace(rho @ rho))  # 0.5 -- less than 1, confirming it's mixed
```

## Next
Read `03-complexity-theory.md` to see how these physical realities connect to the theoretical question of *what* quantum computers can and can't speed up — and why "quantum computers solve NP-complete problems instantly" is a popular myth this doc will debunk.
