# Qubit Technologies Compared (Intermediate)

## Superconducting qubits — IBM, Google, Rigetti
A tiny loop of superconducting metal (usually niobium or aluminum on silicon/sapphire) cooled to near absolute zero forms a "transmon" — an artificial atom whose two lowest energy levels serve as |0⟩ and |1⟩. Control and readout use microwave pulses.
- **Strengths**: fast gate times (tens of nanoseconds), lithographically fabricated using techniques adapted from the classical semiconductor industry (favorable for scaling qubit count), mature software/control stack.
- **Weaknesses**: relatively short coherence times (tens to low hundreds of microseconds T1/T2), requires bulky dilution-refrigerator cooling, qubit-to-qubit variability from manufacturing imperfections (no two transmons are perfectly identical, unlike atoms).
- **Who**: IBM (Eagle, Osprey, Condor, Heron processor families; over 1,000 qubits on Condor), Google Quantum AI (Sycamore, Willow), Rigetti Computing, AWS's in-house superconducting research.

## Trapped-ion qubits — IonQ, Quantinuum
Individual charged atoms (commonly ytterbium or calcium ions) are suspended in a vacuum using electromagnetic fields, with qubit states encoded in the ions' internal electronic energy levels. Lasers perform gates and readout.
- **Strengths**: very long coherence times (seconds or more), all ions of a given species are physically identical (no manufacturing variability), typically the highest reported two-qubit gate fidelities (often >99.9%), and any ion can in principle be entangled with any other in the same trap ("all-to-all connectivity") without the fixed-neighbor limitation superconducting chips have.
- **Weaknesses**: slower gate times (microseconds, roughly 100-1000x slower than superconducting), historically harder to scale ion count in a single trap, though modular/networked-trap architectures are addressing this.
- **Who**: IonQ (publicly traded, cloud-accessible via AWS Braket, Azure Quantum, Google Cloud), Quantinuum (Honeywell-spinout plus Cambridge Quantum, H-series systems), Alpine Quantum Technologies.

## Neutral-atom qubits — QuEra, Pasqal, Atom Computing
Individual neutral atoms are trapped and arranged in custom patterns using focused laser beams ("optical tweezers"), with qubit states encoded in atomic energy levels, including highly excited "Rydberg states" used to mediate entangling interactions.
- **Strengths**: highly flexible, reconfigurable qubit layouts (tweezers can be rearranged between circuit runs), rapid recent qubit-count scaling (thousands of atoms demonstrated), atoms are naturally identical.
- **Weaknesses**: a comparatively newer approach with less mature error-correction and control-software ecosystems than superconducting or trapped-ion platforms, though progressing quickly — Harvard/QuEra/MIT collaborations have demonstrated some of the largest logical-qubit-count error-correction experiments to date on this platform.
- **Who**: QuEra Computing, Pasqal, Atom Computing (partnered with Microsoft on logical-qubit demonstrations).

## Topological qubits — Microsoft
A more speculative, longer-horizon bet: encode qubit information in the braiding properties of exotic quasiparticles (Majorana zero modes) in specially engineered semiconductor-superconductor nanowires, so that quantum information is protected by topology itself rather than requiring as much external error-correction overhead.
- **Strengths (if realized)**: theoretically dramatically lower physical-to-logical qubit overhead than other approaches, potentially a faster path to large logical qubit counts.
- **Weaknesses**: still largely unproven at scale; Microsoft's 2025 "Majorana 1" chip announcement claimed evidence of topological qubit behavior but drew significant scrutiny and debate within the physics community over the strength of the experimental evidence, illustrating how much harder this approach's basic physics validation has been compared to the other platforms above.
- **Who**: Microsoft (Azure Quantum), in a research effort distinct from Microsoft's separate strategy of offering third-party hardware (IonQ, Quantinuum, Rigetti, Pasqal) through Azure Quantum's cloud marketplace.

## Photonic qubits — PsiQuantum, Xanadu
Qubits encoded in properties of individual photons (e.g., which of several paths a photon takes).
- **Strengths**: no need for extreme cryogenic cooling of the qubits themselves (though supporting detector electronics often still need cooling), photons don't interact with their environment as readily as matter-based qubits, potentially leverages existing semiconductor photonics fabrication for manufacturing scale.
- **Weaknesses**: photons are hard to make interact with each other on demand (needed for two-qubit gates), historically requiring complex and lossy optical setups; this is an active, well-funded, but not-yet-dominant approach.
- **Who**: PsiQuantum (large, well-funded, pursuing a fault-tolerant-from-the-start strategy rather than incremental NISQ devices), Xanadu.

## Choosing a platform: the trade-off in one table

| Platform | Gate speed | Coherence | Connectivity | Cooling needs | Maturity |
|---|---|---|---|---|---|
| Superconducting | Fast | Short | Fixed, local | Dilution fridge | High |
| Trapped ion | Slow | Long | All-to-all | Vacuum + lasers | High |
| Neutral atom | Medium | Medium | Reconfigurable | Vacuum + lasers | Medium |
| Topological | Unproven | Theoretically robust | Unproven | Dilution fridge | Low |
| Photonic | Fast (in principle) | High (photons don't decohere like matter) | Complex to engineer | Minimal for qubits | Medium |

No platform is strictly better than the others across every dimension — this is precisely why the field currently supports many competing approaches rather than having converged on one, unlike classical computing's early convergence on silicon transistors.

## Next
Read `03-advanced/01-connectivity-and-transpilation.md` for how a circuit's *logical* qubit connectivity gets mapped onto a real chip's *physical* connectivity constraints.
