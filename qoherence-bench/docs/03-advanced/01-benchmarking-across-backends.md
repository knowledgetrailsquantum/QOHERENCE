# Benchmarking Across Backends (Advanced)

## Why cross-vendor comparison is genuinely hard
Comparing IBM's superconducting hardware against IonQ's or Quantinuum's trapped-ion hardware, or Rigetti's superconducting chips, isn't a matter of running "the same circuit" and comparing raw numbers — the platforms differ in native gate sets, connectivity (fixed grid vs. all-to-all, see `qoherence-hardware/docs/02-intermediate/01-qubit-technologies.md`), gate speeds, and error characteristics in ways that make naive comparison misleading. A circuit that transpiles efficiently on IonQ's all-to-all connectivity might require substantial SWAP overhead on IBM's fixed heavy-hex lattice (see `qoherence-hardware/docs/03-advanced/01-connectivity-and-transpilation.md`) purely due to connectivity, independent of either platform's intrinsic qubit quality — so a naive "run this circuit on both, compare success rate" comparison partly measures transpilation overhead, not fundamental hardware quality.

## Application-oriented benchmarking
The field has increasingly moved toward **application-oriented** or **volumetric** benchmarking — rather than comparing an abstract, hardware-agnostic circuit, compare how well each platform solves a realistic, application-representative problem (e.g., a specific VQE molecule, a specific QAOA graph instance), letting each platform use its own best transpilation and, where allowed, its own best mitigation techniques. This is fairer in the sense of measuring "how useful is this platform for this real task" rather than "how does this platform handle one specific abstract circuit shape it may or may not be well-suited to" — but it requires being explicit and careful about exactly what's being held fixed (the problem) versus what's allowed to vary (the implementation) between platforms being compared.

## Normalizing for cost and access model
A fair benchmark also needs to account for factors beyond raw technical performance: cloud queue times, per-shot costs, and access tiers differ substantially across IBM Quantum, Amazon Braket (which resells IonQ, Rigetti, and others), Microsoft Azure Quantum (which similarly resells multiple hardware vendors), and Google's more limited external access model. A platform that's technically excellent but has multi-hour queue times or high per-shot costs may be practically inferior for a real workflow despite winning on pure fidelity metrics — `src/runtime_bench.py`'s runtime benchmarks should ideally capture full wall-clock time including queueing, not just quantum execution time, to reflect this.

## Common pitfalls in cross-backend benchmarking
- **Cherry-picking favorable circuit structures**: reporting only results from circuit shapes that happen to transpile efficiently on your preferred platform's connectivity.
- **Ignoring calibration drift**: hardware calibration changes over time (sometimes significantly within a single day); a benchmark run once, without repeated trials across different calibration windows, can be an unrepresentative snapshot rather than a stable characterization.
- **Comparing mitigated results on one platform against unmitigated results on another**: error mitigation (`qoherence-mitigate`) can substantially improve apparent results — a fair comparison should either apply comparable mitigation on all platforms being compared, or explicitly and clearly report which results are mitigated and which aren't.
- **Small sample sizes**: statistical noise in a small number of shots or trials can easily be mistaken for a genuine performance difference between platforms — see `04-expert/01-statistical-rigor-in-quantum-benchmarks.md` for how to guard against this.

## Analogy: comparing cars on different tracks
Comparing raw quantum hardware fidelity numbers across vendors without accounting for connectivity, native gate sets, and access model differences is a bit like comparing two race cars' lap times when they raced on different tracks with different weather — you need to normalize for the track (application-oriented benchmarking) and be explicit about what conditions applied (mitigation, calibration window, cost/access) before the comparison means much.

## Next
Read `04-expert/01-statistical-rigor-in-quantum-benchmarks.md` for the statistical methodology (confidence intervals, sample size, hypothesis testing) that makes any of these comparisons trustworthy rather than anecdotal.

## A Bit of History
Cross-vendor quantum benchmarking got a very public real-world test in 2021 when IonQ became the first pure-play quantum hardware company to go public via a SPAC merger, forcing its performance claims — including its "algorithmic qubits" metric — into the kind of public, investor-facing scrutiny that academic benchmarking papers rarely attract. It marked a shift for the whole field: benchmarking disputes stopped being purely a conference-hallway argument between physicists and started having real stock-price consequences.

---
**[◀ Fidelity Metrics](../02-intermediate/01-fidelity-metrics.md)**  |  [Index](../../../README.md)  |  **[Statistical Rigor in Quantum Benchmarks ▶](../04-expert/01-statistical-rigor-in-quantum-benchmarks.md)**
