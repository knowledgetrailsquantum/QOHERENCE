# Hybrid Quantum-Classical Training Loops

## In Plain English

Almost no real QML system today runs entirely on a quantum computer. Instead, it's a partnership: the quantum computer does one specific job (running a parameterized circuit and producing measurements), and an ordinary classical computer does everything else (deciding how to adjust the circuit's parameters, tracking training progress, handling data). This partnership, repeated many times, is a **hybrid training loop** — and it's the actual, practical shape of essentially all near-term QML.

Think of it like a chef (classical computer) directing a very specialized, very literal sous-chef (quantum computer) who can only do one exact task — taste a specific dish and report back a number — over and over, while the chef adjusts the recipe based on those reports.

## Now With the Math

The loop, step by step:
1. **Classical computer** picks initial parameter values θ.
2. **Quantum computer** runs the parameterized circuit with those θ values on real data, many times (many "shots"), and reports measurement statistics.
3. **Classical computer** computes the cost function value from those statistics, and estimates the gradient — often via the parameter-shift rule (`02-intermediate/01-variational-quantum-classifiers.md`), which itself requires the quantum computer to run several more circuit variations.
4. **Classical computer** updates θ using a classical optimizer (like Adam, the same optimizer used throughout ordinary deep learning) and loops back to step 2.

- **Shots** — the number of times a circuit is run and measured per parameter estimate. More shots reduce statistical noise in the result but cost more time/money on real hardware — a direct, practical trade-off unique to this hybrid setting (classical neural networks don't have an analogous "shot count").
- **Classical optimizer** — nearly always a standard, off-the-shelf classical algorithm (Adam, COBYLA, SPSA) — QML rarely invents new optimizers; it reuses the classical AI toolbox and only swaps in quantum-computed gradients.

## A Bit of History

The hybrid loop pattern was formalized for chemistry problems first — the Variational Quantum Eigensolver (VQE), introduced by Peruzzo et al. in 2014 (see `qoherence-algorithms/docs/03-advanced/01-vqe-and-qaoa-theory.md`) — and QML researchers directly adapted that same loop shape for classification and regression tasks a few years later. This shared structure is why VQE, QAOA, VQCs, and QNNs are often described together as "variational algorithms": they're really the same training pattern, applied to different problems (energy minimization, combinatorial optimization, classification). IBM's Qiskit Runtime, launched in 2021, was built specifically to make this back-and-forth loop faster by keeping the classical and quantum parts closer together (reducing network round-trip delay between them) — a purely engineering fix that turned out to matter enormously for how practical these loops are on real cloud-accessed hardware.

---
**[◀ Quantum Neural Networks](01-quantum-neural-networks.md)**  |  [Index](../../../README.md)  |  **[The Barren Plateaus Problem ▶](03-barren-plateaus.md)**
