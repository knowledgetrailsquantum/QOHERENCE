# Benchmarking QML vs. Classical AI

## In Plain English

If someone claims "our quantum model beats classical models on this task," the honest next question is always: compared to what, exactly? A weak or badly-tuned classical baseline can make almost anything look impressive. Rigorous QML benchmarking means comparing a quantum or quantum-inspired approach against the *best* classical approach available for the same task, on the same data, under the same resource budget (time, energy, dollars) — not against a strawman.

This mirrors exactly the discipline `qoherence-bench` argues for across quantum computing generally (see `qoherence-bench/docs/04-expert/01-statistical-rigor-in-quantum-benchmarks.md`) — QML is simply one more place that discipline needs to be applied, and arguably one where it's needed most, because QML claims get outsized media attention.

## Now With the Math

Fair QML benchmarking typically has to control for:
- **Dataset size and dimensionality** — a quantum kernel showing an "advantage" on a tiny, synthetic, deliberately quantum-friendly dataset says little about performance on messy, real-world data with millions of examples.
- **Resource-normalized comparison** — comparing accuracy alone isn't enough; a fair benchmark reports accuracy *per unit of compute time, per dollar, or per shot count*, since quantum hardware access has very different cost structure than classical GPU time.
- **Classical baseline strength** — the comparison classical model should itself be well-tuned (not a deliberately weak version), often meaning the same or a comparably-optimized architecture, trained with equal care.
- **Noise and shot-count sensitivity** — because real quantum hardware is noisy (`qoherence-mitigate`), a fair report includes results across multiple noise levels and shot counts, not just a single cherry-picked best run.

## A Bit of History

Concern over unfair or overstated QML benchmarks grew directly out of the broader "dequantization" wave discussed in `01-beginner/03-why-quantum-might-help-ai.md` — once researchers showed several supposed quantum speedups could be matched classically, the field's culture shifted meaningfully toward more careful, adversarial benchmarking. Google's TensorFlow Quantum and IBM's Qiskit both later added tooling specifically for apples-to-apples classical/quantum comparisons rather than leaving it to individual papers to self-police. As of 2026, the most credible published QML results are the ones explicit about exactly which narrow condition (specific dataset structure, specific noise level, specific resource budget) their claimed advantage holds under — and equally explicit about where it doesn't.

---
**[◀ The Barren Plateaus Problem](03-barren-plateaus.md)**  |  [Index](../../../README.md)  |  **[Industry Case Studies ▶](../04-expert/01-industry-case-studies.md)**
