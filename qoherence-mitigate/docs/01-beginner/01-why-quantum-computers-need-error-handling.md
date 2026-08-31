# Why Quantum Computers Need Error Handling (Beginner)

## Noise is the central obstacle, not qubit count
It's tempting to think "more qubits = more powerful quantum computer," and headlines often frame it that way. In practice, the harder and more important problem is noise: every physical qubit is imperfect, gates are applied with small errors, and qubits slowly lose their quantum state to the environment (decoherence — see `qoherence-core/docs/03-advanced/02-density-matrices-and-mixed-states.md`). A 1,000-qubit chip with high error rates can be *less* useful for a real algorithm than a 50-qubit chip with very low error rates, because errors compound multiplicatively across a circuit's gates — this is precisely why the industry increasingly reports **quantum volume**, **error per layered gate**, and logical qubit counts alongside raw physical qubit counts.

## Two different strategies: mitigation vs. correction
This repo's name split reflects an important distinction covered fully in `02-intermediate/01-mitigation-vs-correction.md`, but the headline version:
- **Error mitigation** (`src/zne.py`, `src/readout_correction.py`): statistical and post-processing techniques that reduce the *impact* of noise on your final answer, without needing extra qubits — practical on today's hardware, but doesn't scale to arbitrarily long computations.
- **Error correction** (`src/surface_code.py`): physically encoding one logical qubit across many physical qubits so errors can be detected and actively corrected during the computation — the path to fault tolerance, but requires substantial qubit overhead (see `qoherence-core/docs/04-expert/01-fault-tolerant-computation.md`).

## Analogy: cleaning up a noisy photograph vs. using a better camera
Error mitigation is like applying noise-reduction software to a photo taken with a noisy camera sensor — it genuinely improves the result, cheaply, but can't recover detail that was never captured, and works best when the noise isn't too severe to begin with. Error correction is like using a fundamentally better camera system (or many redundant sensors combined) that actively detects and compensates for sensor defects as the photo is taken — much more powerful, but requires more hardware (more physical qubits per useful "logical" qubit) and more complex engineering.

## Why this is the most actively funded problem in the field
Every major quantum computing organization — IBM's error-mitigation-focused "quantum-centric supercomputing" near-term strategy, Google's below-threshold surface-code demonstration with Willow, Microsoft's topological-qubit bet aimed at reducing error-correction overhead at the hardware level, and Quantinuum/IonQ's high-native-fidelity approach aimed at needing less correction overhead per logical qubit — is, underneath its specific technical strategy, fundamentally answering the same question: how do we get useful, reliable computation out of inherently noisy physical qubits? This is arguably a more central question to the field's near-term progress than algorithm design or even raw qubit-count scaling.

## What noise looks like in a real result
Ideally, running the Bell-pair circuit from `qoherence-core/docs/01-beginner/02-superposition-and-entanglement.md` on 1,000 shots would give ~500 |00⟩ and ~500 |11⟩, with zero |01⟩ or |10⟩ outcomes. On real hardware today, you typically see a small but nonzero fraction of "wrong" outcomes (a few percent) — this leakage is a direct, measurable signature of gate error, decoherence, and readout error combined, and is exactly the kind of signal `qoherence-bench`'s fidelity metrics (see `qoherence-bench/docs/02-intermediate/01-fidelity-metrics.md`) are designed to quantify precisely.

## Next
Read `02-intermediate/01-mitigation-vs-correction.md` for a deeper technical comparison of these two strategies and when each is used in practice.
