# Grover's and Shor's Algorithms Explained (Intermediate)

## Grover's algorithm: amplitude amplification
Suppose you have N=2ⁿ items (indexed by n qubits) and a "black box" oracle function that can recognize the correct answer (flips the sign of its amplitude) but you have no other structure to exploit — a classical search needs, on average, N/2 checks. Grover's algorithm needs only ~(π/4)√N applications of the oracle.

The mechanism, step by step:
1. Put all n qubits into equal superposition with Hadamard gates — every possible index now has equal amplitude 1/√N.
2. Apply the **oracle**: flips the sign of the amplitude on the correct answer's basis state, leaving all others unchanged. (This doesn't change any measurement probability yet — sign flips are invisible to |amplitude|² — but it sets up the next step.)
3. Apply the **diffusion operator** (a reflection about the average amplitude): this converts that lone sign flip into a genuine boost in the correct answer's probability, while slightly reducing every other amplitude.
4. Repeat steps 2–3 approximately (π/4)√N times — each repetition amplifies the correct amplitude further, like a pendulum swinging closer to vertical.
5. Measure — the correct answer now appears with high probability.

Crucially: too *few* iterations under-amplifies the answer, but too *many* iterations overshoots and starts *decreasing* the correct probability again (the amplitude "rotates past" the target) — Grover's algorithm needs to know how many iterations to run, unlike classical search which can simply stop as soon as it finds the answer.

## Shor's algorithm: from factoring to period-finding
Shor's insight was a reduction: factoring a large number N can be converted into finding the **period** r of the function f(x) = aˣ mod N for a cleverly chosen a. Once you know r, basic number theory (computing a greatest common divisor) usually recovers a nontrivial factor of N directly. Classically, finding this period requires checking exponentially many values of x for large N. Quantumly:

1. Prepare a superposition over all values of x.
2. Compute f(x) = aˣ mod N *in superposition* (this modular exponentiation circuit is itself a substantial engineering challenge — it's the most gate-expensive part of Shor's algorithm in practice).
3. Apply the inverse Quantum Fourier Transform (`qoherence-core/docs/03-advanced/01-quantum-fourier-transform.md`) to the x-register — this converts the periodicity in f(x) into a directly measurable spike in the frequency domain.
4. Measure, and use classical post-processing (continued fractions) to extract r from the measured value with high probability.

The exponential speedup comes entirely from step 3 — the QFT lets you extract global periodicity information in O(n²) gates rather than the exponentially many function evaluations a classical approach would need.

## Analogy: Grover's is a smarter game of Battleship; Shor's is tuning a resonance
Grover's algorithm is like playing Battleship where each "shot" (oracle call) doesn't just say hit/miss on one square — it subtly reshapes your beliefs about the *whole board* toward the true ship location, so you converge in √N shots rather than N. Shor's algorithm is closer to the resonance-tuning analogy from the QFT doc: rather than checking candidate periods one at a time, it sets up the quantum state so the true period "rings out" via interference when you finally measure.

## Concrete resource comparisons
- Grover's algorithm searching a database of 1 million items: classically up to 1,000,000 checks; Grover's needs roughly 785 oracle calls (√1,000,000 × π/4). Real, but modest — and each "oracle call" on real hardware is itself a nontrivial circuit, so the quadratic speedup can be eaten up by per-call overhead for smaller N.
- Shor's algorithm factoring a 2048-bit RSA key: estimated to require on the order of 20 million physical qubits running for about 8 hours on a fault-tolerant device, per widely cited 2021 estimates (Gidney & Ekerå) — versus today's largest processors at roughly 1,000–1,200 physical qubits (IBM Condor-class, Google's latest generation). This gap is exactly why post-quantum cryptography migration (see `qoherence-core/docs/03-advanced/01-quantum-fourier-transform.md`) is a today problem despite Shor's algorithm being a future-hardware problem.

## Next
Read `03-advanced/01-vqe-and-qaoa-theory.md` for the NISQ-era algorithms that are actually being piloted on today's hardware.
