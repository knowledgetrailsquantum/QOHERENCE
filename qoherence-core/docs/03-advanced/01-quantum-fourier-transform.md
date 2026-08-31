# Quantum Fourier Transform (Advanced)

## What the classical Fourier transform does
The classical discrete Fourier transform (DFT) converts a signal from the "time domain" (a sequence of values) into the "frequency domain" (how much of each periodic frequency is present). It's the mathematical foundation of audio compression, image processing (JPEG), and much of signal processing. The Fast Fourier Transform (FFT) computes it in O(N log N) time for N data points classically.

## What the Quantum Fourier Transform does differently
The QFT performs the *same mathematical transform*, but on the amplitudes of a quantum state rather than on classical array values, and it does so using only O(n²) quantum gates for n qubits — exponentially fewer gate operations than classical FFT needs arithmetic operations, since n qubits represent N=2ⁿ amplitudes. This sounds like a free exponential speedup for signal processing, but there's a catch that trips up nearly everyone learning this for the first time: **you cannot read out all N transformed amplitudes** — measurement gives you only one sample from the resulting probability distribution. The QFT's power comes from setting up interference so that the *right* frequency shows up with high measurement probability, not from letting you extract an entire transformed array.

## The real payoff: period-finding
The QFT's headline application is finding the *period* of a function — the core subroutine that makes Shor's algorithm work. If a function f(x) repeats with period r (f(x)=f(x+r) for all x), a classical computer generally needs to sample many values of x to find r for large numbers. Quantum phase estimation, built on the QFT, can find r using exponentially fewer operations by encoding period information into the phase of a quantum state and then using the QFT to convert that phase information into a directly measurable value. This is precisely the mathematical mechanism that lets Shor's algorithm factor large integers efficiently (see `qoherence-algorithms/docs/02-intermediate/01-grover-and-shor-explained.md`), which is why RSA encryption — used for HTTPS and most of today's internet security — is considered broken by a sufficiently large fault-tolerant quantum computer, and why "post-quantum cryptography" has become a priority for NIST, and for Microsoft, Google, IBM, and Amazon's cloud security roadmaps, even though no such large fault-tolerant machine exists yet.

## Circuit structure
The QFT circuit alternates Hadamard gates with controlled phase-rotation gates, in a specific pattern that depends on qubit index, followed by a qubit-order reversal (a series of SWAP gates) at the end. For n qubits it uses:
- n Hadamard gates
- n(n-1)/2 controlled phase rotations
- up to n/2 SWAP gates

This O(n²) gate count, versus the O(N log N) = O(2ⁿ · n) classical FFT gate count, is where the exponential advantage comes from.

## Analogy: tuning many instruments at once via resonance, not measurement
Classically finding a signal's frequency content means sampling it repeatedly and computing. The QFT is more like tuning a set of resonant instruments simultaneously so that only the "correct" frequency rings out loudly when you finally listen — the computation happens through interference during the process, not through repeated classical sampling afterward. This is a genuinely different computational paradigm, not merely a faster version of the classical one.

## Real-world stakes
Because Shor's algorithm depends on the QFT, and Shor's algorithm threatens RSA/ECC cryptography, the QFT is arguably the single most consequential piece of quantum algorithm design from a security-policy perspective. Current fault-tolerant hardware is nowhere near able to factor cryptographically relevant key sizes (that would require thousands of clean, error-corrected logical qubits — current devices have at most a handful of demonstrated logical qubits), but the "harvest now, decrypt later" threat model (adversaries storing encrypted data today to decrypt once quantum computers mature) is why NIST finalized post-quantum cryptographic standards in 2024, and why Microsoft, Google, IBM, Cloudflare, and Signal have all begun migrating production systems to post-quantum-safe algorithms years ahead of the hardware actually existing.

## Next
Read `02-density-matrices-and-mixed-states.md` for the formalism needed to describe real, noisy qubits — pure-state vectors (used everywhere in this doc set so far) are an idealization that breaks down the moment noise and decoherence enter the picture.
