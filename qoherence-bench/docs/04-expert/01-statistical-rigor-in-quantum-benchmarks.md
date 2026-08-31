# Statistical Rigor in Quantum Benchmarks (Expert)

## Why this deserves an expert-tier doc of its own
Quantum measurement outcomes are inherently probabilistic even under ideal, noise-free conditions (see `qoherence-core/docs/01-beginner/01-what-is-a-qubit.md` on the Born rule). This means every quantum benchmark result is fundamentally a statistical estimate from a finite number of shots, not a deterministic measurement — and treating it as if it were exact, or comparing two such estimates without proper statistical methodology, is one of the most common ways benchmark claims (in both academic papers and vendor marketing) end up overstated or simply wrong.

## Shot noise and confidence intervals
If the true probability of a given outcome is p, and you run N shots, the standard error of your estimate is approximately √(p(1-p)/N) — meaning a benchmark run with too few shots can easily show an apparent difference between two conditions (two backends, two mitigation techniques, two algorithm variants) that's actually just shot noise, not a real effect. `src/*_bench.py` implementations should always report confidence intervals (or, better, use methods like the Wilson score interval, which behaves better than the naive normal approximation at extreme probabilities near 0 or 1) alongside point estimates, and should explicitly compute the shot count needed to detect an effect of a given expected size before running an expensive real-hardware benchmark campaign, not after.

## Hypothesis testing for "is backend A really better than backend B?"
A statistically sound comparison between two backends' fidelity, given finite-shot estimates for each, requires a proper hypothesis test (e.g., a two-proportion z-test, or a permutation test for more complex derived metrics) rather than simply comparing two point estimates and declaring the larger one "better." A difference that isn't statistically significant given the sample size shouldn't be reported as a real performance difference, no matter how appealing the narrative — this is a standard rigor bar in most experimental sciences that quantum benchmarking, as a relatively young applied field, has sometimes been inconsistent about enforcing in published and marketed results.

## Calibration drift as a hidden confound
Real hardware calibration changes over time — sometimes meaningfully within hours, due to environmental drift and periodic recalibration cycles. A rigorous benchmark should either run comparison conditions within the same calibration window (interleaved, not sequentially block-run, to avoid drift biasing one condition), or explicitly model and report calibration-window variance as part of the uncertainty in the final result. Interleaving is the standard practical mitigation: alternate shots or circuit runs between the conditions being compared rather than running all of condition A first and all of condition B second, so any drift affects both conditions roughly equally rather than systematically favoring whichever ran first or second.

## Multiple-comparisons and publication-bias awareness
When benchmarking many algorithm variants, backends, or mitigation technique combinations simultaneously (a common real workflow), the chance of finding at least one "statistically significant" difference purely by chance grows with the number of comparisons made — standard multiple-hypothesis-testing corrections (e.g., Bonferroni correction, or controlling false discovery rate) should be applied when many comparisons are run and only the most favorable-looking ones are highlighted, a pattern that has appeared in some published quantum benchmark claims that were later hard to reproduce.

## Reproducibility checklist for `qoherence-bench` results
- Report exact circuit definitions, shot counts, and backend/calibration identifiers used, not just summary statistics.
- Report confidence intervals, not bare point estimates.
- Interleave conditions being compared rather than sequentially block-running them, when comparing across time or across backends.
- Apply appropriate multiple-comparison correction when reporting the best of many tested variants.
- Distinguish clearly between mitigated and unmitigated results (see `qoherence-bench/docs/03-advanced/01-benchmarking-across-backends.md`).

## Next
This is the final tier of qoherence-bench's docs. See `qoherence-docs/docs/architecture.md` for how all six qoherence repos fit together, and `qoherence-docs/docs/industry-landscape.md` for the broader industry context these benchmarking practices sit within.
