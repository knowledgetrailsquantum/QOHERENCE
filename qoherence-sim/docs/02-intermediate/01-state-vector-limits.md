# State-Vector Simulation Limits (Intermediate)

## In Plain English

Imagine trying to write down, on paper, every possible outcome of flipping 50 coins at once — not just "how many heads," but every single distinguishable combination (heads-heads-tails-heads-..., all the way through). There are over a quadrillion such combinations. No amount of paper, and no amount of computer memory that will ever plausibly exist, can hold a list that long written out explicitly. This is exactly the wall that "exact" quantum simulation runs into: to track a quantum state exactly, you need to keep a number for every possible outcome combination, and that count doubles with every qubit you add — the same exponential from `qoherence-core/docs/02-intermediate/01-multi-qubit-systems.md`, now showing up as a hard, physical memory limit rather than an abstract idea.

This wall moves around a specific number worth remembering: roughly 30 qubits is where a single, well-equipped computer runs out of room; roughly 50 qubits is where even the world's largest supercomputers, pooling memory across thousands of machines, hit their limit. Past that, exact simulation of a general quantum state is considered off the table for the foreseeable future, full stop — not "slow," but genuinely, physically impossible with any classical machine built from ordinary matter.

## Now With the Math

**The memory formula: `16 × 2ⁿ` bytes.** An `n`-qubit state needs `2ⁿ` amplitudes (from `qoherence-core/docs/02-intermediate/01-multi-qubit-systems.md`). Each amplitude, stored as a double-precision complex number (a real part plus an imaginary part, 8 bytes each), takes 16 bytes. Multiply those together and you get the total memory a full, exact simulation needs.

| Qubits | Amplitudes (`2ⁿ`) | Memory (`16 × 2ⁿ`) |
|---|---|---|
| 10 | 1,024 | 16 KB |
| 20 | ~1.05 million | 16 MB |
| 30 | ~1.07 billion | 16 GB |
| 40 | ~1.1 trillion | 16 TB |
| 50 | ~1.1 quadrillion | 16 PB |

**Time, not just memory.** Applying even one single-qubit gate touches every one of the `2ⁿ` amplitudes (the gate's small matrix has to multiply through the whole state vector), so gate application is `O(2ⁿ)` time — read `O(...)` as "scales roughly like ...". A circuit with many gate layers multiplies this cost further, meaning simulation *time* independently becomes prohibitive for deep circuits well before qubit count alone would be the limiting factor.

## A moving wall, and why the field cares
This ceiling shifts upward over time as hardware improves (more RAM, GPU acceleration — see `04-expert/01-gpu-accelerated-simulation.md`), and that's precisely why "quantum supremacy" claims are watched so carefully for classical rebuttals: several early claims (including aspects of Google's original 2019 Sycamore result) were later matched or closely approached by improved classical simulation techniques, prompting genuine, healthy scientific disagreement between Google and IBM researchers over exactly where the classical wall actually sits.

## Next
Read `03-advanced/01-tensor-network-methods.md` for how circuits with limited entanglement can be simulated far beyond this ~30-50 qubit wall, by exploiting structure rather than fighting the raw exponential head-on.
