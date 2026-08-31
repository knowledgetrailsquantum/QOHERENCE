# State-Vector Simulation Limits (Intermediate)

## The precise memory math
An n-qubit state vector holds 2ⁿ complex amplitudes. Each complex number, stored as double-precision floating point (real + imaginary parts, 8 bytes each), takes 16 bytes. Total memory: 16 × 2ⁿ bytes.

| Qubits | Amplitudes | Memory |
|---|---|---|
| 10 | 1,024 | 16 KB |
| 20 | ~1.05 million | 16 MB |
| 30 | ~1.07 billion | 16 GB |
| 40 | ~1.1 trillion | 16 TB |
| 50 | ~1.1 quadrillion | 16 PB |
| 60 | ~1.15×10¹⁸ | 16 exabytes |

30 qubits is roughly the practical ceiling for a well-equipped single workstation; 40–50 qubits requires distributed supercomputing (many nodes, aggregating memory across a cluster) and has, in fact, been demonstrated by IBM, Google, and national labs specifically to establish credible classical baselines against which to judge "quantum advantage" claims — a 50-qubit exact state-vector simulation has been done, but it required some of the world's largest supercomputers and is close to the practical wall. Beyond roughly 50 qubits, exact general state-vector simulation is considered infeasible with any currently conceivable classical hardware.

## Why this specific number, and why it keeps shifting
This ceiling isn't fixed forever — better hardware (more RAM, GPU acceleration via tools like Nvidia's cuQuantum, distributed multi-node techniques) pushes it upward over time, and that's exactly why the field distinguishes "quantum supremacy at the time of the claim" from "quantum supremacy that stays classically infeasible" — several early supremacy claims (including aspects of Google's original 2019 Sycamore result) were later matched or closely approached by improved classical algorithms and hardware, prompting some public disagreement between Google and IBM researchers over how firmly "supremacy" had actually been established. This is a healthy, ongoing scientific back-and-forth, not an embarrassment for the field — it's precisely how the boundary between classical and quantum capability gets pinned down rigorously.

## Time complexity, not just memory
Beyond memory, applying a single-qubit gate to an n-qubit state vector requires touching all 2ⁿ amplitudes (each gate application is O(2ⁿ) time); a circuit with many gate layers multiplies this further. Even if memory weren't the binding constraint, simulation *time* would independently become prohibitive well before extremely large qubit counts for circuits with significant depth.

## Analogy: a spreadsheet that doubles every row
Imagine a spreadsheet that starts with 2 rows and doubles in size every time you add one more "qubit column" of information to track. After 10 columns, 1,024 rows — manageable. After 50 columns, more rows than there are grains of sand on Earth (roughly 10¹⁸, in the same ballpark as the 50-qubit amplitude count). This is exactly the exponential blowup that makes exact classical simulation infeasible past a certain point, and precisely the same exponential that (per `qoherence-core/docs/02-intermediate/01-multi-qubit-systems.md`) is the *source* of quantum computing's theoretical power — the wall for classical simulation and the promise of quantum computing are two faces of the same exponential.

## When you don't need the full state vector
Many real use cases don't need the *entire* state vector — only specific expectation values (as in VQE, `qoherence-algorithms/docs/03-advanced/01-vqe-and-qaoa-theory.md`) or samples from the output distribution. Sampling-based and expectation-value-based simulation strategies can sometimes be more efficient than materializing the full state vector, and tensor-network methods (next doc) exploit a different structural shortcut entirely — limited entanglement — to push the practical qubit-count ceiling much higher for certain circuit types.

## Next
Read `03-advanced/01-tensor-network-methods.md` for how circuits with limited entanglement can be simulated far beyond the ~30-50 qubit state-vector wall.
