# Fidelity Metrics (Intermediate)

## In Plain English

If you bake a cake from a recipe, "fidelity" is a way of asking: how close did the actual cake come out to the recipe's ideal photo? A perfect match scores 100%; a burnt, lopsided disaster scores much lower. Quantum fidelity asks the exact same question about a quantum circuit's output — how close did the real, noisy result come to what a perfect, noise-free version of the same circuit would have produced?

This sounds simple, but measuring it honestly on real hardware is trickier than it first appears, for a reason worth understanding in plain terms before touching any formula: the very act of reading out a qubit's final answer (measurement) is *itself* imperfect on real hardware — a qubit that's truly 0 sometimes gets misread as 1, independent of anything that went wrong earlier in the circuit. If you're not careful, this "the scale itself is slightly broken" measurement error gets mixed up with "the cake itself came out wrong" circuit error, and you end up blaming the wrong culprit. Untangling these two — did the *circuit* go wrong, or did the *readout* go wrong — is most of what rigorous fidelity benchmarking is actually about.

The industry-standard trick for measuring gate quality fairly, called **randomized benchmarking**, sidesteps this tangle cleverly: run a long, randomly-chosen sequence of gates that mathematically must cancel back to "do nothing" if performed perfectly, so you always know in advance exactly what the "correct" answer should be. Then watch how often the real result matches that known-correct answer as the sequence gets longer and longer — the way success probability decays with sequence length tells you, cleanly, how good each individual gate is on average, without needing to separately untangle readout error from gate error by hand.

## Now With the Math

**State fidelity, `F`.** Given an ideal target state `|ψ_ideal⟩` and an actual, possibly-noisy output `ρ_actual` (a density matrix, from `qoherence-core/docs/03-advanced/02-density-matrices-and-mixed-states.md`, since real output is generally mixed, not clean):

  `F(ψ_ideal, ρ_actual) = ⟨ψ_ideal|ρ_actual|ψ_ideal⟩`

Read this as "sandwich the actual, messy output between the ideal target's bra and ket" — the result is a single number from 0 (completely wrong) to 1 (a perfect match), generalizing the simple overlap formula `|⟨φ|ψ⟩|²` from `qoherence-core/docs/02-intermediate/02-linear-algebra-foundations.md` to the real-world case where the output isn't a clean state at all.

**Process fidelity — grading the whole operation, not one output.** State fidelity grades a single run's output. **Process fidelity** grades an entire gate or circuit's behavior, averaged fairly over every possible input it might receive — this is what vendor-published "two-qubit gate fidelity 99.5%" numbers actually mean, and it's specifically what randomized benchmarking (plain-English section above) is designed to estimate cleanly, robust to exactly the readout-error confusion described there.

**Cross-entropy benchmarking (XEB).** Google's supremacy and advantage claims use a related but distinct tool: instead of comparing full quantum states directly (which becomes computationally infeasible to even *check* at large qubit counts), XEB compares the statistical *distribution* of measured outcomes against the theoretically predicted distribution for a specific circuit — a check that scales to larger circuits precisely because it never needs to reconstruct or store a full state to compare against.

**Composite metrics: quantum volume and algorithmic qubits.** IBM's **quantum volume** rolls qubit count, connectivity, gate fidelity, and circuit depth into one number via a standardized benchmark specifically designed to resist being gamed by improving just one dimension (you can't inflate it just by bolting on more noisy qubits). IonQ's **algorithmic qubits** pursues a similar goal via a different, vendor-specific methodology. Both are useful for tracking one vendor's own progress over time, but — because the underlying benchmark circuits and methods differ — they are not directly, numerically comparable across vendors, a genuinely important caveat when reading competing marketing claims.

## Next
Read `03-advanced/01-benchmarking-across-backends.md` for how to make these fidelity comparisons fair when comparing genuinely different hardware platforms.
