# What Is Quantum AI?

## In Plain English

"Quantum AI" is actually two different things people lump together, and separating them makes everything else in this repo easier to follow.

**Branch one: real quantum machine learning (QML).** This means running some part of an AI system — usually the part that does pattern-matching — on an actual quantum computer or a simulator of one. Think of it like swapping out one gear in a car engine for a new experimental gear, and seeing if the car goes faster on certain roads. It might, on some roads. On most roads today, it doesn't yet, because the "engine" (real quantum hardware) is still small and noisy.

**Branch two: quantum-inspired classical AI.** This means taking *ideas* from quantum physics — like how nature explores many possibilities at once, or how particles settle into low-energy states — and building purely classical (regular, non-quantum) algorithms that mimic that behavior. No quantum computer needed at all. It's like designing a running shoe inspired by how a cheetah's legs move, without needing an actual cheetah.

Both branches are legitimate and both show up constantly in industry reporting, so this repo covers both, and always tells you which one a given page is about.

## Now With the Math

You don't need new math to understand the split, but here's the vocabulary you'll see repeatedly:

- **QML (Quantum Machine Learning)** — branch one. A quantum circuit (see `qoherence-core`) is used somewhere in the learning pipeline, usually as a "feature map" (turning data into quantum states) or as a trainable model itself.
- **Quantum-inspired** — branch two. Terms like "simulated annealing," "tensor networks," or "quantum-inspired optimization" describe classical algorithms borrowing quantum *math structures* (like how annealing borrows the physics idea of a system settling into its lowest-energy state) without borrowing quantum *hardware*.
- **Hybrid** — a system using both a classical computer and a quantum computer together, with results passed back and forth. Nearly all real QML today is hybrid, because quantum computers currently aren't large enough to run a whole AI pipeline alone.

## A Bit of History

The idea of using quantum effects for computation goes back to Richard Feynman's 1981 observation that simulating quantum systems is naturally suited to quantum hardware (see `qoherence-core/docs/00-history-of-quantum-mechanics.md`). Quantum machine learning as its own research area took off later — Lloyd, Mohseni, and Rebentrost's 2013 paper on quantum algorithms for supervised and unsupervised learning is often cited as a founding moment. IBM launched its cloud quantum access in 2016, and by 2018-2019 "quantum machine learning" had become one of the most cited subfields of quantum computing research, partly because ML was already the hottest area of classical computing, and partly because early theoretical results (like the "HHL" algorithm for linear systems) suggested speedups that later research showed were more nuanced than first thought — a caution this repo returns to often, especially in `04-expert/03-hype-check-and-limitations.md`.

Meanwhile, quantum-*inspired* classical algorithms have an even longer, quieter history: simulated annealing itself dates to 1983 (Kirkpatrick, Gelatt, and Vecchi), decades before "quantum-inspired" was a marketing term, and it was directly inspired by the physical process of annealing metal — heating it, then cooling it slowly so atoms settle into a low-energy, low-defect arrangement.

---
**[◀ Ethics, Society & Economics](../../../qoherence-docs/docs/ethics-and-society.md)**  |  [Index](../../../README.md)  |  **[How Classical ML Works (Recap) ▶](02-how-classical-ml-works-recap.md)**
