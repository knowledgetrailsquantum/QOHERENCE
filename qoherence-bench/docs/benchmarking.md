# Benchmarking Overview

qoherence-bench provides three benchmark families used throughout the other repos:

| Benchmark | File | Question answered |
|---|---|---|
| Fidelity | `src/fidelity_bench.py` | How close is the actual output to the ideal, noise-free result? |
| Noise resilience | `src/noise_resilience.py` | How does accuracy degrade as noise increases? |
| Runtime | `src/runtime_bench.py` | How long does execution actually take, end to end? |

Full depth: `01-beginner/01-what-is-benchmarking.md` → `02-intermediate/01-fidelity-metrics.md` → `03-advanced/01-benchmarking-across-backends.md` → `04-expert/01-statistical-rigor-in-quantum-benchmarks.md`.

## Why rigor matters here specifically
Quantum measurement is inherently probabilistic (Born rule), so every benchmark number is a statistical estimate, not an exact reading — see `04-expert/01-statistical-rigor-in-quantum-benchmarks.md` for the confidence-interval and hypothesis-testing discipline this repo's benchmarks should follow, and `03-advanced/01-benchmarking-across-backends.md` for why comparing across vendors (IBM, Google, IonQ, Rigetti, Quantinuum) fairly is harder than it looks.
