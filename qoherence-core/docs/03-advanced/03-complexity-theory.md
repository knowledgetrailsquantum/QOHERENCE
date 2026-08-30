# Quantum Complexity Theory (Advanced)

## Complexity classes
- **BQP** (Bounded-error Quantum Polynomial time): problems efficiently
  solvable by a quantum computer with bounded error probability.
- **P / NP**: classical complexity classes. BQP is believed to contain
  problems outside P (e.g. factoring) but is not believed to contain
  NP-complete problems in general.

## Where quantum speedups come from
- **Exponential speedup**: Shor's algorithm (factoring) — BQP vs believed
  classical hardness.
- **Quadratic speedup**: Grover's algorithm (search) — provably optimal;
  no quantum algorithm can do better than O(sqrt(N)) for unstructured search.
- **Heuristic/unproven speedup**: VQE, QAOA — empirically promising on
  near-term hardware, without proven asymptotic advantage.

## Why this matters for algorithm design
Understanding which complexity class a problem sits in tells you whether to
expect a quantum algorithm to help at all, and how to talk precisely about
what "quantum advantage" or "quantum supremacy" claims actually mean.

## Further reading
Aaronson, "Quantum Computing Since Democritus."
