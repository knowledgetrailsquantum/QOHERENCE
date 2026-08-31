# Tensor Network Methods (Advanced)

## The key insight: not all states are equally hard to represent
A full state vector treats every possible n-qubit state as equally complex to store — 2ⁿ numbers regardless of structure. But many real, practically interesting circuits — especially ones with limited or geometrically local entanglement (e.g., circuits that mostly entangle nearby qubits, common in simulating physical systems like 1D or 2D materials) — have states that can be represented far more compactly using **tensor networks**, which factor the full state into a network of smaller, connected tensors rather than one enormous flat array.

## Matrix Product States (MPS): the simplest useful case
The most widely used tensor network for 1D-like qubit chains is the **Matrix Product State (MPS)** representation, implemented conceptually in `src/tensor_network.py`. Instead of storing 2ⁿ amplitudes directly, an MPS stores n smaller tensors chained together, with a "bond dimension" χ controlling how much entanglement can be represented between any cut point in the chain. Memory scales roughly as O(n·χ²) rather than O(2ⁿ) — for circuits where entanglement stays modest (low required χ), this is a dramatic improvement, enabling simulation of hundreds or even thousands of qubits for suitably structured, low-entanglement circuits.

## The catch: entanglement is the enemy again
The bond dimension χ needed to represent a state *exactly* grows with how entangled the state is — in the worst case (a highly, globally entangled state, such as those many genuinely hard quantum algorithms produce), χ must grow exponentially with system size, and MPS/tensor-network methods degrade back toward state-vector-level cost. This means tensor-network methods are not a universal replacement for state-vector simulation — they're a specialized tool that works extremely well for *some* circuits (low-entanglement, geometrically local ones) and poorly for others (highly entangled, all-to-all circuits like Grover's or Shor's on many qubits, or deep random circuits like Google's supremacy benchmark). Knowing which regime your circuit falls into is itself an important skill.

## Real-world use: this is exactly how classical researchers challenge "quantum advantage" claims
When researchers respond to a quantum advantage claim with an improved classical simulation, tensor-network methods (often combined with clever approximations that trade small, controlled accuracy loss for large speedups) are usually the tool used. This was central to the back-and-forth following Google's 2019 supremacy claim — subsequent classical tensor-network-based simulations narrowed the claimed classical/quantum gap substantially, which is precisely why later claims (including Google's Willow-era work) have emphasized tasks and metrics more specifically chosen to resist known classical tensor-network attacks, and why credible advantage claims now typically include explicit discussion of the best known classical simulation approach as a baseline, rather than treating "classically hard" as self-evident.

## Truncation: the practical trade-off
Real tensor-network simulators typically cap the bond dimension χ at some practical maximum and **truncate** (discard the least significant components of the representation) when a circuit's true entanglement would require more — trading a small, often well-controlled amount of simulation accuracy for tractability. This is directly analogous to lossy compression: JPEG images discard visually-insignificant detail to shrink file size; truncated tensor-network simulation discards computationally-insignificant entanglement structure to shrink memory and time cost. Well-designed truncation, with error tracked and bounded, can make otherwise-infeasible large simulations useful with quantified accuracy loss.

## Analogy: folding a large map along its natural creases
A state vector is like storing every point on a large, fully unfolded map individually. A tensor network is like storing the map *folded* along its natural creases — regions that don't interact much (low entanglement) can be compressed efficiently by the folding, but a map with complex, all-over creasing (high entanglement) resists compact folding and eventually needs to be stored close to fully unfolded again.

## Next
Read `04-expert/01-gpu-accelerated-simulation.md` for how both state-vector and tensor-network methods are accelerated using GPU hardware in practice.

## A Bit of History
Tensor networks didn't originate in quantum computing at all — they trace to condensed-matter physics in the 1990s-2000s, particularly work by Guifré Vidal and Steven White on efficiently describing 1D quantum materials (an idea called the Density Matrix Renormalization Group, developed by White in 1992). Quantum computing adopted the machinery wholesale roughly a decade later, once researchers realized the same compact representation that worked for describing real materials also worked for simulating quantum circuits classically — a rare case of one physics subfield's toolkit quietly rescuing another's.

---
**[◀ State-Vector Simulation Limits](../02-intermediate/01-state-vector-limits.md)**  |  [Index](../../../README.md)  |  **[GPU-Accelerated Simulation ▶](../04-expert/01-gpu-accelerated-simulation.md)**
