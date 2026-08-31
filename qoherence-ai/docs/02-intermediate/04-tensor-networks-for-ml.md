# Tensor Networks for Machine Learning

## In Plain English

Tensor networks were originally invented so physicists could simulate quantum systems on classical computers without running out of memory (see `qoherence-sim/docs/03-advanced/01-tensor-network-methods.md`). The trick: instead of storing one gigantic table of numbers describing a whole system at once, break it into a chain of smaller, connected pieces — like describing a long train not by memorizing every passenger's seat, but by describing car-by-car how each car connects to the next.

That same "break a huge thing into connected small pieces" trick turns out to be useful for classical machine learning too. Large neural network layers can be replaced with tensor-network structures that use dramatically fewer numbers, while still capturing most of the useful patterns — useful for compressing huge models to run on smaller devices, or for building models that are naturally suited to structured data.

This is a purely classical technique (no quantum hardware involved) — it's "quantum-inspired" in the sense that it was born from quantum physics simulation, then adopted by classical AI once people noticed how well it compressed information.

## Now With the Math

- **Tensor** — a generalization of a matrix to more dimensions. A single number is a 0-dimensional tensor, a list of numbers is 1-dimensional, a grid is 2-dimensional (a normal matrix), and tensor networks work with higher-dimensional versions.
- **Tensor network** — a collection of smaller tensors connected together (like train cars linked by couplings), whose combined structure represents a much larger tensor without ever having to store that larger tensor directly.
- **MPS (Matrix Product State)** — the simplest, most common tensor network shape: a straight chain, like train cars in a line. Used both in quantum simulation and, increasingly, in ML layers.
- **Bond dimension** — a number controlling how much information can flow between neighboring pieces of the tensor network; a bigger bond dimension means more accuracy but more computation, exactly mirroring the accuracy/cost trade-off in `qoherence-sim`'s discussion of simulating more entangled quantum states.

## A Bit of History

Tensor networks trace to physicist Steven White's 1992 DMRG (Density Matrix Renormalization Group) method, built to simulate one-dimensional quantum spin chains — a genuinely different motivation than machine learning. Their crossover into ML picked up around 2016, when researchers including Google's Miles Stoudenmire and David Schwab showed MPS-style tensor networks could classify handwritten digits (the classic MNIST dataset) competitively with far fewer parameters than a standard neural network layer. Since then, tensor-network layers have found real industrial use in model compression — shrinking huge neural networks so they fit on phones or edge devices — an unglamorous but genuinely useful export from quantum physics into everyday classical AI engineering.

---
**[◀ Quantum-Inspired Optimization](03-quantum-inspired-optimization.md)**  |  [Index](../../../README.md)  |  **[Quantum Neural Networks ▶](../03-advanced/01-quantum-neural-networks.md)**
