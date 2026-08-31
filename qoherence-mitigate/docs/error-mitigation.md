# Error Mitigation & Correction Overview

qoherence-mitigate spans both near-term error mitigation (usable on today's noisy hardware, no extra qubits) and longer-term quantum error correction (needs many extra physical qubits per logical qubit, but scales to arbitrarily low error rates below threshold).

| Technique | File | Category | Extra qubits needed? |
|---|---|---|---|
| Readout error correction | `src/readout_correction.py` | Mitigation | No |
| Zero-noise extrapolation | `src/zne.py` | Mitigation | No |
| Surface code | `src/surface_code.py` | Correction | Yes, substantial (~1,000+ physical per logical) |

Full conceptual grounding: `01-beginner/01-why-quantum-computers-need-error-handling.md` → `02-intermediate/01-mitigation-vs-correction.md` → `03-advanced/01-stabilizer-codes.md` → `04-expert/01-implementing-a-decoder.md`.

## The one-paragraph mental model
Mitigation cleans up noisy results after the fact using statistics and classical post-processing; correction actively detects and fixes errors mid-computation using redundant encoding — and the field currently needs both, at different scales, because today's hardware can't yet support correction at the scale fault-tolerant algorithms require, while mitigation alone can't scale to those algorithms' circuit depths. See `qoherence-core/docs/04-expert/01-fault-tolerant-computation.md` for how this connects to the industry's fault-tolerance roadmaps (IBM, Google, Microsoft, IonQ/Quantinuum).
