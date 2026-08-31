# What Is Benchmarking? (Beginner)

## Why benchmarking is its own discipline here
It's tempting to think "run the circuit, see if the answer is right" is enough evaluation for a quantum algorithm or device. In practice, quantum results are inherently probabilistic (even a perfect, noise-free quantum computer gives you a probability distribution, not a single deterministic answer for superposition-based circuits), and real hardware adds noise on top of that inherent randomness. Distinguishing "this result looks wrong because of expected quantum randomness" from "this result looks wrong because of hardware error" from "this result looks wrong because of an actual bug" requires rigorous, statistically grounded benchmarking — which is exactly what qoherence-bench provides tooling for.

## The three benchmark types this repo covers
- **Fidelity** (`src/fidelity_bench.py`, `02-intermediate/01-fidelity-metrics.md`): how close is the actual output distribution to the ideal, noise-free expected distribution?
- **Noise resilience** (`src/noise_resilience.py`): how does a given algorithm's accuracy degrade as noise increases — some algorithms (like QAOA with shallow depth) are much more noise-tolerant than others (like Shor's, which needs near-perfect fidelity over long circuits).
- **Runtime** (`src/runtime_bench.py`): how long does a circuit take to execute, including queue time, transpilation time, and actual quantum execution time — a full picture, not just the theoretical gate count.

## Analogy: benchmarking a race car, not just checking it starts
Confirming a quantum circuit "runs" is like confirming a race car's engine starts — necessary, but far from sufficient. Real benchmarking is closer to a full performance evaluation: lap times under various conditions (runtime benchmarks), how much the car deviates from the ideal racing line under stress (fidelity benchmarks), and how performance degrades as track conditions worsen (noise resilience benchmarks) — all measured with proper statistical rigor across multiple runs, not a single anecdotal lap.

## Why this matters for comparing hardware vendors fairly
Every major vendor (IBM, Google, IonQ, Quantinuum, Rigetti) publishes benchmark numbers, but these numbers are measured differently enough across vendors that naive comparison is misleading — IBM's "quantum volume" metric, IonQ's "algorithmic qubits" metric, and various vendors' quoted gate fidelities are not directly interchangeable, because they're measured on different benchmark tasks with different statistical methodologies. Understanding benchmarking rigor (this module) is a prerequisite for interpreting any vendor's published performance claims critically rather than taking marketing numbers at face value — a genuinely important skill given how much hype surrounds this field.

## Next
Read `02-intermediate/01-fidelity-metrics.md` for the specific mathematical definitions of fidelity used to quantify "how close to ideal" a real result is.
