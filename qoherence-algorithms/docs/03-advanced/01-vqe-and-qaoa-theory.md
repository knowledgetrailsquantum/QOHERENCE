# VQE and QAOA Theory (Advanced)

## The hybrid quantum-classical pattern
VQE and QAOA share a design pattern that defines essentially all practical near-term ("NISQ") quantum algorithms: a **parameterized quantum circuit** (called an "ansatz") is run on quantum hardware, its measurement statistics are fed into a **classical optimizer**, which adjusts the circuit's parameters and re-runs it — iterating this loop until the parameters converge. The quantum computer's job is narrow and short (evaluate a function's value for given parameters); the classical computer does the harder job of deciding *which* parameters to try next. This division of labor is deliberate: it keeps quantum circuits shallow enough to survive today's noise levels while still leveraging the quantum computer for the one piece of the problem it does better.

## VQE: finding ground-state energies
VQE targets the lowest eigenvalue (ground-state energy) of a Hamiltonian — the matrix describing a physical system's energy, most commonly a molecule for quantum chemistry applications. This connects directly to the eigenvalue discussion in `qoherence-core/docs/02-intermediate/02-linear-algebra-foundations.md`.
1. Choose an ansatz circuit with tunable parameters θ that can represent candidate quantum states |ψ(θ)⟩.
2. Run the circuit, measure, and compute the expectation value ⟨ψ(θ)|H|ψ(θ)⟩ — the estimated energy for that parameter choice (this itself requires many repeated circuit executions, since expectation values are estimated statistically from measurement shots).
3. Feed this energy value to a classical optimizer (gradient descent, COBYLA, SPSA, and other methods suited to noisy, expensive-to-evaluate functions).
4. Update θ, repeat, until the energy estimate stops improving — by the variational principle, this converged value is guaranteed to be an *upper bound* on the true ground-state energy, so lower is always better.

This is the algorithmic basis for essentially every quantum-chemistry and materials-science pilot from IBM, Google, and Microsoft's Azure Quantum Elements platform — modeling molecules for battery electrolytes, drug candidates, and catalysts, all areas where classical simulation cost grows exponentially with the number of interacting electrons.

## QAOA: approximate combinatorial optimization
QAOA targets combinatorial optimization problems expressible as minimizing a "cost Hamiltonian" — the canonical teaching example is Max-Cut (partition a graph's nodes into two groups to maximize the number of edges crossing between them, an NP-hard problem in general).
1. Alternate between applying a "cost" unitary (encoding the problem to be optimized) and a "mixer" unitary (encoding exploration across candidate solutions), each with a tunable parameter, for p rounds (the "QAOA depth").
2. Measure, and use the resulting bitstring as a candidate solution, scored by the classical cost function.
3. Feed the score back to a classical optimizer that adjusts the 2p parameters, repeat.
4. As depth p increases, QAOA provably approaches the optimal solution — but each added round adds more noise-vulnerable circuit depth, so real hardware caps how large p can practically be.

## Why "variational" — and its known weaknesses
Both algorithms are called "variational" because they search over a family of quantum states parameterized by θ rather than directly computing an answer. This makes them noise-tolerant (small errors mostly perturb θ rather than catastrophically corrupting the answer) but introduces real, actively-researched problems:
- **Barren plateaus**: for many ansatz designs, the optimization landscape becomes exponentially flat as qubit count grows, making gradient-based optimization stall — a major open research problem limiting how far VQE/QAOA can scale.
- **Ansatz expressibility vs. trainability trade-off**: a more expressive ansatz (able to represent more candidate states) is often *harder* to optimize; a more trainable ansatz may not be able to represent the true ground state at all.
- **Shot noise**: because expectation values are estimated statistically, each optimization step's "measurement" of the energy is itself noisy, on top of hardware noise — a genuinely double-noisy optimization problem.

## Analogy: hiking a foggy, noisy mountain
Classical optimization on a known landscape is like hiking with a full map. VQE/QAOA is like hiking in thick fog (you can only sense the slope right where you stand — one parameter evaluation at a time) with an unreliable altimeter (noisy hardware and finite measurement shots blur each reading). The classical optimizer is the hiking strategy; the quantum circuit is the noisy altimeter reading at each step. Barren plateaus are the fog becoming so thick that the ground reads as perfectly flat everywhere, leaving no direction to walk.

## Next
Read `04-expert/01-implementing-shors-period-finding.md` for a detailed circuit-level walkthrough of Shor's algorithm's most technically demanding subroutine.
