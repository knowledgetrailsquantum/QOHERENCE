# Hardware Backends Overview

qoherence-hardware ships adapters for three representative vendor platforms, chosen to span the major physical qubit technologies compared in `02-intermediate/01-qubit-technologies.md`:

| Adapter | Vendor | Platform | Native connectivity |
|---|---|---|---|
| `src/ibm_backend.py` | IBM | Superconducting | Fixed heavy-hex lattice |
| `src/ionq_backend.py` | IonQ | Trapped ion | All-to-all |
| `src/rigetti_backend.py` | Rigetti | Superconducting | Fixed, chip-dependent grid |

All three implement the common interface defined in `src/base_backend.py` — see `04-expert/01-building-a-custom-backend.md` for the design rationale and what a well-built adapter must handle (auth, transpilation, result normalization, calibration awareness).

## Deep dives
- What real quantum hardware physically is, and why it needs extreme cooling/isolation: `01-beginner/01-what-is-real-quantum-hardware.md`
- Full platform comparison (superconducting, trapped-ion, neutral-atom, topological, photonic) and which companies build each: `02-intermediate/01-qubit-technologies.md`
- How logical circuits get compiled onto physical connectivity constraints: `03-advanced/01-connectivity-and-transpilation.md`
- How to build a new vendor backend adapter: `04-expert/01-building-a-custom-backend.md`

## Broader industry context
See `qoherence-docs/docs/industry-landscape.md` for how IBM, Google, Microsoft, IonQ, Quantinuum, Rigetti, Amazon, and others' hardware roadmaps and public milestones relate to one another and to fault tolerance timelines.
