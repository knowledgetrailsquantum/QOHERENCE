# Statistical Rigor in Quantum Benchmarks (Expert)

## In Plain English

Flip a fair coin 10 times and you might well get 7 heads — that's not evidence the coin is rigged, it's just the ordinary wobble you'd expect from a small sample. Flip it 10,000 times and get 7,000 heads, and now something is clearly, statistically wrong. The exact same logic applies to quantum benchmarking, and it's easy to forget because quantum results already *sound* mysterious and probabilistic, which can make people too quick to shrug off a genuinely suspicious pattern as "oh, that's just quantum randomness." Sometimes it is. Sometimes it's too few measurement shots creating an illusion of a real effect that isn't there, or a genuine bug, or a real hardware problem — and telling these apart requires exactly the same statistical discipline any careful experimental scientist uses when comparing two coins, two drugs, or two manufacturing processes.

This matters especially in this field because quantum outcomes are inherently probabilistic even under perfect, noise-free conditions (the Born rule, from the very first chapter of this repo set) — so *every* quantum benchmark number is fundamentally a statistical estimate from a finite number of runs, never an exact reading. Treating a benchmark result as if it were exact — or comparing two such noisy estimates without proper statistical care — is one of the most common ways both academic papers and vendor marketing end up overstating a claim.

## Now With the Math

**Shot noise, `√(p(1-p)/N)`.** If the true probability of some outcome is `p`, and you run `N` measurement shots, your *estimate* of `p` wobbles around the true value with a typical size of roughly `√(p(1-p)/N)` — read this as "take p times (1 minus p), divide by the number of shots, then take the square root." The key practical takeaway, without needing to memorize the formula: this wobble shrinks as `N` grows, but only slowly — to cut the wobble in half, you need *four times* as many shots, not twice as many, because of the square root. Running too few shots and then comparing two nearly-identical numbers is a recipe for mistaking ordinary wobble for a real effect.

**Confidence intervals.** Rather than reporting a single bare number ("this backend scored 94% fidelity"), a rigorous benchmark reports a range that's very likely to contain the true value ("94% ± 2%"), computed from the shot count and observed outcome using standard statistical methods (the Wilson score interval is a commonly recommended choice here, because it behaves better than simpler approximations when the true probability is close to 0% or 100%, a common situation in high-fidelity quantum hardware reporting).

**Hypothesis testing — is A really better than B?** Simply comparing two point estimates and declaring the bigger one "the winner" is exactly the "7 heads out of 10" trap from the plain-English section. A statistically sound comparison uses a proper test (a two-proportion z-test is a standard, straightforward choice) that accounts for both estimates' uncertainty and only calls a difference "real" if it clears an appropriate statistical bar — not just "one number happened to be bigger this time."

## Practical discipline this repo's benchmarks should follow
- Report confidence intervals, not bare point estimates.
- Compute the shot count needed to reliably detect an effect of a given size *before* running an expensive real-hardware benchmark campaign, not after.
- **Interleave** conditions being compared (alternate shots between backend A and backend B) rather than running all of A first and all of B second — hardware calibration drifts over time, and interleaving keeps that drift from systematically favoring whichever condition happened to run first.
- Apply a correction for multiple comparisons (such as the Bonferroni correction) when testing many algorithm variants or backend configurations at once and reporting only the best-looking result — otherwise, pure chance guarantees *something* will look significant purely by luck, the more comparisons you run.

## Next
This is the final tier of qoherence-bench's docs. See `qoherence-docs/docs/architecture.md` for how all six qoherence repos fit together, and `qoherence-docs/docs/industry-landscape.md` for the broader industry context these benchmarking practices sit within.

## A Bit of History
The statistical methods this doc leans on — confidence intervals, hypothesis testing, corrections for running many comparisons at once — mostly predate quantum computing by a century; the two-proportion z-test and Bonferroni-style corrections trace to statisticians like Karl Pearson and Carlo Bonferroni working in the early-to-mid 1900s on entirely unrelated problems, from genetics to actuarial tables. Quantum benchmarking didn't need to invent new statistics; it needed to remember to actually use the old ones rigorously, which — as several retracted or revised early quantum-advantage claims have shown — isn't automatic even among trained physicists.

---
**[◀ Benchmarking Across Backends](../03-advanced/01-benchmarking-across-backends.md)**  |  [Index](../../../README.md)  |  **[Qoherence Architecture ▶](../../../qoherence-docs/docs/architecture.md)**
