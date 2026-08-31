# Implementing Shor's Period-Finding (Expert)

## Scope of this doc
`02-intermediate/01-grover-and-shor-explained.md` gave the conceptual outline of Shor's algorithm. This doc goes one level deeper into the period-finding subroutine's circuit-level implementation — the part `src/shor.py` models — and why it's the dominant cost in any real implementation.

## The full period-finding circuit
Given N to factor and a chosen base a (coprime to N), we want the period r of f(x) = aˣ mod N.
1. **Register setup**: two registers — an "index" register of n₁ qubits (large enough that 2^n₁ ≥ N²  to guarantee enough resolution to recover r via continued fractions) and a "function value" register of n₂ qubits (large enough to hold values mod N).
2. **Superposition**: Hadamard every qubit in the index register, producing an equal superposition over all 2^n₁ values of x.
3. **Modular exponentiation**: apply a unitary that computes |x⟩|0⟩ → |x⟩|aˣ mod N⟩, entangling the two registers. This step is implemented as a sequence of controlled modular multiplications and is, empirically, the most gate-expensive part of the entire algorithm — modular arithmetic circuits require many more gates than the QFT step that follows, which is a common source of confusion since popular explanations emphasize the QFT as "the quantum part" while modular exponentiation quietly dominates real resource counts.
4. **Inverse QFT**: apply QFT⁻¹ to the index register only. Because the function-value register is entangled with the index register per the periodic structure of aˣ mod N, this converts the period information into a state sharply peaked around multiples of 2^n₁/r.
5. **Measure the index register**, getting some integer y that (with high probability) satisfies y/2^n₁ ≈ k/r for some integer k.
6. **Classical post-processing**: apply the continued-fractions algorithm to y/2^n₁ to recover a candidate r, then verify aʳ mod N = 1; if verification fails (which happens with bounded probability due to the k dependence), repeat the whole procedure with a different random a.

## Why resource estimates for real factoring are so large
The modular exponentiation step (3) needs to be repeated implicitly for every bit of the index register — implementing "compute aˣ mod N in superposition" decomposes into a sequence of controlled modular multiplications, each of which itself decomposes into many elementary (and, under error correction, expensive) gates like Toffoli and T gates. This compounding is why widely cited estimates (Gidney & Ekerå, 2021) put factoring RSA-2048 at roughly 20 million physical qubits for about 8 hours, even though the *logical* algorithm structure above looks compact on paper — nearly all of that resource cost is the error-corrected implementation of step 3, not the conceptually elegant QFT in step 4.

## Verification and probabilistic failure
Shor's algorithm is a **probabilistic** algorithm — a given run may fail to yield a useful factor (e.g., if the measured y happens to correspond to k=0, or if r turns out to be odd, which prevents extracting a nontrivial factor via the standard GCD step). The standard mitigation is simply retrying with a freshly chosen random a; the expected number of retries needed is small (a small constant on average), but any real implementation must include this classical retry loop, not just the "happy path" quantum circuit.

## Implementation notes for `src/shor.py`
- The modular exponentiation subroutine should be built compositionally per `qoherence-core/docs/02-intermediate/03-circuit-composition.md`, with explicit ancilla uncomputation — leftover garbage qubits here are a common source of subtly wrong probability distributions.
- Testing should use small, classically-checkable N (e.g., N=15, N=21) where the true factors and period are known in advance, before trusting the implementation on larger N via `qoherence-sim`.
- This implementation targets ideal (noise-free) simulation. Running period-finding on real noisy hardware (`qoherence-hardware`) at any nontrivial N is, as of 2025–2026, still a research demonstration rather than a practical capability, due to the circuit depth required by step 3.

## Next
See `qoherence-hardware/docs` for how circuits like this one get compiled down to real device constraints, and `qoherence-mitigate/docs` for the error-handling techniques that partially compensate for noise on today's hardware.

## A Bit of History
The first-ever hardware demonstration of Shor's algorithm ran in 2001 at IBM, factoring the number 15 (into 3 and 5) using a 7-qubit nuclear magnetic resonance system — a genuine milestone, though later criticized because the circuit had effectively been simplified using foreknowledge of the answer. More than two decades later, factoring numbers that small remains largely a demonstration exercise; the resource estimates in this doc for factoring a real 2048-bit RSA key show just how far that 2001 proof-of-concept still sits from a cryptographically meaningful result.

---
**[◀ VQE and QAOA Theory](../03-advanced/01-vqe-and-qaoa-theory.md)**  |  [Index](../../../README.md)  |  **[What Is Real Quantum Hardware? ▶](../../../qoherence-hardware/docs/01-beginner/01-what-is-real-quantum-hardware.md)**
