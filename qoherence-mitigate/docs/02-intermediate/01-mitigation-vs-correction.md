# Mitigation vs. Correction (Intermediate)

## Error mitigation techniques (used today, on NISQ hardware)

**Readout error correction** (`src/readout_correction.py`): the final measurement step itself has errors (a qubit truly in |0⟩ sometimes reads out as 1, and vice versa) — this is characterized separately from gate errors because it's often the single largest error source and, unlike gate errors, can be characterized and corrected *after the fact* via classical post-processing: run calibration circuits with known expected outputs, build a "confusion matrix" of true-vs-measured outcomes, and invert it to correct raw measurement counts.

**Zero-noise extrapolation (ZNE)** (`src/zne.py`): deliberately amplify a circuit's noise (e.g., by repeating gate pairs that should cancel in an ideal circuit but each add a "dose" of real noise), run the circuit at several noise levels, then extrapolate the resulting measurements back to what they'd be at zero noise — a technique borrowed conceptually from experimental physics (similar to extrapolation techniques used in analog measurement calibration). ZNE trades extra circuit executions (more cost, more time) for reduced bias in the final answer, without needing any extra qubits.

**Probabilistic error cancellation, dynamical decoupling, and other techniques** (not all implemented in this repo, but part of the same family): further statistical and pulse-level techniques that trade classical post-processing or extra runs for reduced effective noise.

The unifying theme: mitigation techniques reduce the *bias* in your final answer using classical cleverness and repeated runs, but they don't reduce the underlying physical error rate, and the number of extra runs needed generally grows with circuit size — meaning mitigation alone doesn't scale to the long, deep circuits fault-tolerant algorithms like Shor's need.

## Error correction (the path to fault tolerance)

**Quantum error correction** (`src/surface_code.py` and `03-advanced/01-stabilizer-codes.md`) takes a fundamentally different approach: encode one **logical qubit** redundantly across many **physical qubits**, and periodically measure special "syndrome" observables that reveal *what kind* of error occurred (bit-flip, phase-flip, or both) without directly measuring — and thus without collapsing — the encoded logical information itself. A classical decoder algorithm interprets these syndrome measurements and applies a corrective operation, actively removing the error rather than just statistically compensating for its effect on the final answer.

This is fundamentally more powerful (the threshold theorem, `qoherence-core/docs/04-expert/01-fault-tolerant-computation.md`, guarantees error correction can suppress noise arbitrarily given enough physical qubits per logical qubit and physical error rates below threshold) but requires substantially more physical qubits than the algorithm's logical qubit count would suggest — current estimates suggest hundreds to over a thousand physical qubits per logical qubit at today's physical fidelities.

## Why both exist simultaneously in industry roadmaps
Mitigation is what makes today's 50–1,000 physical-qubit devices useful *right now* for NISQ algorithms (VQE, QAOA), while error correction is the multi-year engineering project needed before fault-tolerant algorithms (Shor's, large-scale quantum chemistry beyond NISQ's reach) become practical. IBM's public roadmap explicitly frames this as a staged transition — "quantum-centric supercomputing" using heavy mitigation today, moving toward error-corrected systems later this decade — rather than treating mitigation and correction as competing approaches. Google's research has focused more heavily and earlier on demonstrating correction (Willow's below-threshold result), betting that near-term commercial value from mitigation-only NISQ algorithms is more limited than IBM's roadmap implies.

## A useful rule of thumb
If your circuit is shallow enough that mitigation's extra-run overhead is affordable and the answer only needs modest precision (many VQE/QAOA use cases), mitigation is the practical near-term tool. If your circuit is deep and needs near-perfect fidelity over millions to billions of gates (Shor's algorithm at cryptographically relevant scale), only full error correction can plausibly get you there — mitigation's overhead grows too fast to compensate for that much accumulated noise.

## Next
Read `03-advanced/01-stabilizer-codes.md` for how the surface code — the leading practical error-correcting code — actually works.

## A Bit of History
Zero-noise extrapolation has origins outside quantum computing entirely — a similar extrapolate-to-zero technique (Richardson extrapolation) was devised by Lewis Fry Richardson in 1911 for an entirely different problem: improving numerical weather-prediction calculations done, at the time, entirely by hand. It took over a century for quantum error mitigation researchers, facing their own version of "how do I get a cleaner answer out of an imperfect calculation," to rediscover essentially the same mathematical idea.

---
**[◀ Why Quantum Computers Need Error Handling](../01-beginner/01-why-quantum-computers-need-error-handling.md)**  |  [Index](../../../README.md)  |  **[Stabilizer Codes ▶](../03-advanced/01-stabilizer-codes.md)**
