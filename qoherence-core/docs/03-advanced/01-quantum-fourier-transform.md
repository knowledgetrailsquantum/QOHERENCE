# Quantum Fourier Transform (Advanced)

## In Plain English

Think about tuning an old analog radio. You don't scan through every possible station one frequency at a time and painstakingly listen for a signal — a well-tuned receiver locks onto the station that's *resonating*, ringing out clearly, while everything off-frequency fades into static. The Quantum Fourier Transform (QFT) is the quantum-computing version of that resonance trick: instead of a signal, it works on a **pattern** — a repeating pattern hidden inside a quantum state's amplitudes — and instead of checking every possible repeat-length one at a time, it sets up the qubits so that the *true* repeat-length "rings out" clearly when you finally measure, while every wrong guess fades into near-silence via the interference ideas from `01-beginner/02-superposition-and-entanglement.md`.

There's a catch that trips up almost everyone learning this for the first time, so it's worth stating plainly: the QFT does **not** hand you a complete, readable answer sheet. Measurement still only ever gives you one sample — one "which station is this radio tuned to right now" reading — not a printout of every frequency's strength. The QFT's entire value is in making sure that single sample is overwhelmingly likely to be the *right* frequency, not that it somehow lets you read out everything at once.

The headline reason this matters: the QFT is the engine inside Shor's algorithm, the famous method for cracking the mathematical problem (factoring large numbers) that today's internet security depends on being hard. Because of that, the QFT is arguably the single most consequential piece of quantum algorithm design from a security standpoint — see `qoherence-algorithms/docs/02-intermediate/01-grover-and-shor-explained.md` for exactly how it's used there, and why "post-quantum cryptography" has become a real, funded, urgent priority years before the hardware that would need it actually exists.

## Now With the Math

**What "finding a hidden repeat" means, precisely.** Suppose a function `f(x)` repeats with some period `r` — meaning `f(x) = f(x+r)` for every `x`. Classically, discovering `r` for a large, complicated `f` generally requires sampling many values of `x` one at a time — expensive. The QFT lets you find `r` using exponentially fewer steps, by first encoding the periodicity into the *phase* of a quantum state (the sign/complex-angle information carried by each amplitude — the same phase information from `01-beginner/02-superposition-and-entanglement.md` that's invisible in isolation but decisive in combination), and then applying the QFT to convert that hidden phase pattern into something you can actually read off with a measurement.

**Gate count: `O(n²)` vs. `O(N log N)`.** The classical Fast Fourier Transform (FFT) needs roughly `N log N` arithmetic steps to transform `N` data points. The QFT achieves the *same underlying transform*, on `n` qubits representing `N = 2ⁿ` amplitudes, using only about `n²` quantum gates — exponentially fewer gates than the classical FFT needs arithmetic operations for the same `N`. This gate-count gap is the entire source of the QFT's fame; it's also exactly why the caveat above (you can't read out the full transformed array) matters so much — a free exponential speedup on paper, with a real, load-bearing asterisk attached.

**Circuit structure, briefly.** The QFT circuit alternates Hadamard gates (from `01-beginner/03-gates-and-circuits.md`, the "start spinning evenly" gate) with **controlled phase-rotation gates** — gates that nudge one qubit's phase by an amount that depends on another qubit's value, tying the qubits' phases together in exactly the pattern needed for the periodicity to show up later — followed by a reversal of qubit order (a chain of SWAP gates) at the end. For `n` qubits: `n` Hadamards, `n(n-1)/2` controlled rotations, up to `n/2` swaps — arithmetic that works out to the `O(n²)` gate count above.

## Real-world stakes
Because Shor's algorithm depends on the QFT, and Shor's algorithm threatens RSA/ECC cryptography, NIST finalized post-quantum cryptographic standards in 2024, and Microsoft, Google, IBM, Cloudflare, and Signal have all begun migrating production systems to post-quantum-safe algorithms years ahead of the hardware actually existing — current fault-tolerant hardware is nowhere near able to factor cryptographically relevant key sizes (see `qoherence-algorithms/docs/04-expert/01-implementing-shors-period-finding.md` for the resource numbers).

## Next
Read `02-density-matrices-and-mixed-states.md` for the formalism needed to describe real, noisy qubits — everything above assumed perfectly clean qubits, an idealization that breaks down the moment noise and decoherence enter the picture.

## A Bit of History
Peter Shor developed the algorithm that made the QFT famous in 1994, while working at Bell Labs — reportedly after a colleague, Umesh Vazirani, challenged him over a dinner conversation about whether quantum computers could do anything a classical computer provably couldn't. Shor's factoring algorithm, built on the QFT, is often cited as the single result that took quantum computing from an obscure academic curiosity to a topic of serious government and industry funding almost overnight, precisely because of what it implied for cryptography.

---
**[◀ Circuit Composition](../02-intermediate/03-circuit-composition.md)**  |  [Index](../../../README.md)  |  **[Density Matrices and Mixed States ▶](02-density-matrices-and-mixed-states.md)**
