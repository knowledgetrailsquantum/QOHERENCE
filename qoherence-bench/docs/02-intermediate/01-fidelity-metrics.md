# Fidelity Metrics (Intermediate)

## State fidelity: comparing quantum states
Given an ideal target state |ψ_ideal⟩ and an actual (possibly mixed, per `qoherence-core/docs/03-advanced/02-density-matrices-and-mixed-states.md`) output state ρ_actual, the standard **state fidelity** metric is:

  F(ψ_ideal, ρ_actual) = ⟨ψ_ideal|ρ_actual|ψ_ideal⟩

This ranges from 0 (completely orthogonal, maximally wrong) to 1 (perfect match). It generalizes the simple overlap |⟨φ|ψ⟩|² from `qoherence-core/docs/02-intermediate/02-linear-algebra-foundations.md` to the mixed-state case that real noisy hardware actually produces.

## Process fidelity: comparing operations, not just states
State fidelity tells you how close *one output* was to ideal. **Process fidelity** (also called gate fidelity when applied to a single gate) characterizes how close an entire *operation* (a gate, or a full circuit) is to its ideal unitary, averaged appropriately over all possible input states — this is what vendor-published "two-qubit gate fidelity" numbers (commonly 99.5%-99.9%+ depending on platform, see `qoherence-hardware/docs/02-intermediate/01-qubit-technologies.md`) actually refer to, typically measured via a standardized protocol called **randomized benchmarking**.

## Randomized benchmarking: why it's the industry standard
Directly measuring process fidelity naively would require characterizing a gate's effect on every possible input state — infeasible. **Randomized benchmarking** sidesteps this: run long sequences of randomly chosen gates from a group (often the Clifford group) that compose to the identity operation, so the ideal final result is always a known, fixed state; measure how the success probability decays as sequence length grows, and fit an exponential decay curve to extract an average per-gate error rate. This approach is specifically designed to be robust to state-preparation and measurement (SPAM) errors confounding the gate-error estimate — a subtlety that makes randomized benchmarking numbers more trustworthy and comparable across platforms than naive fidelity measurements, and is why it's the near-universal standard vendors use to report gate fidelity (IBM, Google, IonQ, Rigetti, Quantinuum all publish randomized-benchmarking-derived numbers).

## Cross-entropy benchmarking (XEB): a different tool for a different job
Google's supremacy and advantage claims have specifically used **cross-entropy benchmarking**, which compares the statistical distribution of measured bitstring outcomes against the theoretically predicted distribution for a specific random circuit, without needing to reconstruct or compare full quantum states directly — useful precisely because it scales to larger qubit counts where full state or process tomography becomes computationally infeasible even as a benchmarking exercise. XEB and randomized benchmarking answer related but distinct questions and aren't directly interchangeable numbers.

## Quantum volume and algorithmic qubits: composite, vendor-specific metrics
IBM's **quantum volume** metric combines qubit count, connectivity, gate fidelity, and circuit depth into a single number via a standardized random-circuit benchmark, specifically designed to resist gaming by any single dimension (you can't inflate quantum volume just by adding noisy qubits). IonQ's **algorithmic qubits** metric is a similarly composite, vendor-defined measure aimed at a similar goal via a different specific methodology. Both are useful within their own vendor's reporting but are not perfectly apples-to-apples comparable across vendors, precisely because the underlying benchmark circuits and methodologies differ — a genuinely important caveat when reading competing vendor marketing claims.

## Practical guidance for `src/fidelity_bench.py`
- Always report *both* the fidelity number and the specific circuit/state used to measure it — a fidelity number without its measurement context is close to meaningless for comparison purposes.
- Prefer randomized-benchmarking-style protocols over naive direct fidelity estimation when SPAM errors could confound results, which is essentially always true on real hardware.
- When comparing across backends (`qoherence-hardware`), hold circuit structure and shot count fixed, and report confidence intervals, not just point estimates — see `04-expert/01-statistical-rigor-in-quantum-benchmarks.md`.

## Next
Read `03-advanced/01-benchmarking-across-backends.md` for how to make these fidelity comparisons fair when comparing genuinely different hardware platforms.
