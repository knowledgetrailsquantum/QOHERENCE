# Complexity Theory for Quantum Computing (Advanced)

## The myth to dismantle first
"Quantum computers try every possibility at once and instantly pick the right answer" is the most common misconception in popular coverage of the field, and it's wrong in a specific, important way: measurement only ever gives you *one* sample, randomly, from the final probability distribution — you cannot simply "read off" the answer among exponentially many superposed possibilities. Real quantum speedup comes from carefully engineered interference (see `01-quantum-fourier-transform.md`) that makes correct answers much more probable than wrong ones, not from parallel brute-force search with free readout. This is also why quantum computers are *not* believed to efficiently solve NP-complete problems (like general SAT or the traveling salesman problem) — there's no known way to engineer the necessary interference for those problems' rugged solution landscapes.

## The complexity classes that matter
- **P**: problems solvable efficiently (polynomial time) on a classical computer.
- **NP**: problems whose *solutions* can be verified efficiently, even if finding them might be hard.
- **BPP** (bounded-error probabilistic polynomial time): P's randomized cousin — classical computers with access to a random-number generator, allowed a small error probability.
- **BQP** (bounded-error quantum polynomial time): the quantum analogue — problems a quantum computer can solve efficiently with high probability of correctness.

The central, still-unproven belief in the field: BPP ⊊ BQP — quantum computers can efficiently solve some problems (like integer factoring, via Shor's algorithm) that classical computers, even with randomness, cannot. Nobody has *proven* this rigorously (proving it would resolve deep open questions related to P vs. NP), but factoring is strong circumstantial evidence: no classical algorithm faster than sub-exponential is known despite 50 years of cryptography research motivating people to look hard, while Shor's algorithm is provably polynomial-time on a quantum computer.

## Where quantum speedup is proven vs. believed vs. absent
- **Proven exponential speedup**: a handful of somewhat artificial "oracle problems" (Simon's problem, Bernstein–Vazirani) where the speedup can be mathematically proven relative to a black-box oracle.
- **Believed but not proven exponential speedup**: integer factoring (Shor's), discrete logarithm, some quantum simulation problems (simulating quantum chemistry and materials, which is arguably the most commercially promising near-term application, per Google, IBM, and Microsoft's own public research roadmaps).
- **Proven polynomial (quadratic) speedup**: unstructured search, via Grover's algorithm — this is a real, provable speedup, but a quadratic speedup is much less dramatic than an exponential one, and for many practical search problem sizes it isn't enough to overcome the overhead and error rates of current hardware.
- **No known speedup, or proven impossibility**: NP-complete problems in general are not believed to be in BQP; some cryptographic primitives (symmetric-key ciphers like AES, and hash functions) are considered "quantum-resistant" already, needing only larger key sizes (per Grover) rather than complete replacement, unlike RSA/ECC which Shor's algorithm breaks outright.

## Quantum supremacy / advantage claims — what they actually mean
Google's 2019 "quantum supremacy" claim (a Sycamore processor performing a specific random-circuit-sampling task believed intractable classically) and its 2024 Willow follow-up were about a *narrow, deliberately chosen benchmark task*, not general-purpose usefulness — random circuit sampling has essentially no direct commercial application. IBM has been publicly skeptical of some supremacy claims, arguing classical simulation techniques (better tensor-network methods, more compute) can sometimes catch up faster than expected — and indeed, several early "supremacy" claims were later matched or beaten by improved classical algorithms. The current, more careful industry term is **quantum advantage** or **quantum utility** — IBM's 2023 "utility-scale" experiments and framing emphasize *useful* computations beating classical methods, not just any classically-hard sampling task. Treat every supremacy/advantage headline with the question: "beating classical at what specific, and how commercially relevant, a task?"

## Analogy: a lock that only some keys fit
Quantum speedup is less like "a universal skeleton key for hard problems" and more like a specific, oddly-shaped key that happens to fit a small number of very particular locks (period-finding-structured problems, quantum simulation, unstructured search) extremely well, while doing nothing at all for most other locks. Knowing which locks a quantum computer's key fits — and which it doesn't — is the actual expertise this field requires, as opposed to the popular framing of quantum computers as generically "more powerful" computers.

## Next
Read `04-expert/01-fault-tolerant-computation.md` to see what has to be true, physically and architecturally, before any of BQP's theoretical promise becomes practically realizable on error-prone hardware.
