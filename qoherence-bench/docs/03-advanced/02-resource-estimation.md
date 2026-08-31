# Resource Estimation (Advanced)

## In Plain English

Earlier docs said things like "Grover's algorithm is quadratically faster" or "Shor's algorithm needs 20 million physical qubits." Where do numbers like that actually come from? They come from **resource estimation** — a step that takes an algorithm's design and works out, concretely, how many qubits it needs, how deep the circuit is, and how long it would actually take to run, on a specific (real or hypothetical) piece of hardware.

This matters because "asymptotically faster" and "actually faster today" are two very different claims. Grover's algorithm needs `√N` oracle calls instead of `N` — true, and provable. But if building the oracle itself (see `qoherence-algorithms/docs/04-expert/02-worked-example-grover-n-queens.md`) takes a lot of extra qubits and gates, the real, practical crossover point where Grover's algorithm actually beats a classical computer might be at a much larger `N` than the simple headline speedup suggests. Resource estimation is how you find that crossover point honestly, instead of guessing.

## What a Resource Estimate Reports

A serious resource estimate answers, at minimum:
- **Physical qubit count** — including error-correction overhead, not just the "logical" qubit count the algorithm's textbook description uses (see `qoherence-core/docs/04-expert/01-fault-tolerant-computation.md`).
- **Circuit depth / runtime** — how long the algorithm takes given a specific gate speed and error-correction cycle time.
- **T-gate count** — a specific, expensive-to-error-correct gate type (see `qoherence-core/docs/01-beginner/03-gates-and-circuits.md`) that's often the dominant cost driver for fault-tolerant algorithms, more than raw qubit count.

## Microsoft's Azure Quantum Resource Estimator

Microsoft built a tool, the Azure Quantum Resource Estimator, specifically to make this calculation accessible without needing to be an error-correction specialist: you describe your algorithm (as a circuit or a high-level operation count), pick target hardware assumptions (gate speed, error rate, choice of error-correcting code), and it reports the physical qubit count and runtime you'd need. This is exactly the kind of tool that produced the widely-cited "20 million physical qubits, 8 hours" estimate for factoring RSA-2048 (`qoherence-algorithms/docs/04-expert/01-implementing-shors-period-finding.md`) — a number that would be nearly impossible to sanity-check by hand.

## A Simple Worked Comparison

Take the N-queens Grover oracle from the previous doc. A resource estimate for it would report something like: "for 4 queens, 14 qubits, oracle depth X, needing Y total gate operations." Compare that to a classical brute-force search over the same 4-queens puzzle (256 candidate boards, checked in a fraction of a second on a laptop) and the honest answer is: classical wins easily at this tiny size. The estimate only starts favoring Grover's algorithm once the board size — and therefore `N` — grows large enough that `√N`'s advantage outweighs the oracle's real, non-trivial hardware cost. Reporting that crossover point, with real numbers, is what separates a resource estimate from a marketing claim.

## Why This Belongs in Benchmarking

Resource estimation and the fidelity/statistical work covered elsewhere in `qoherence-bench` answer two different but related questions: fidelity metrics (`02-intermediate/01-fidelity-metrics.md`) ask "how good is this specific piece of hardware, today?" Resource estimation asks "how big would hardware need to get before this specific algorithm becomes practically worth running?" Both are needed for an honest answer to "is quantum computing useful for my problem yet?"

## Next
Read `04-expert/01-statistical-rigor-in-quantum-benchmarks.md` for how to compare any of these numbers rigorously once you actually have hardware to test on.

---
**[◀ Benchmarking Across Backends](01-benchmarking-across-backends.md)**  |  [Index](../../../README.md)  |  **[Statistical Rigor in Quantum Benchmarks ▶](../04-expert/01-statistical-rigor-in-quantum-benchmarks.md)**
