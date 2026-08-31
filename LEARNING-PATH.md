# Qoherence Learning Path

Qoherence is an educational-first quantum computing repo set. Follow this
order, reading each repo's docs tiers (01-beginner -> 04-expert) in sequence:

1. **qoherence-core** — start here always. Qubits, superposition,
   entanglement, gates, circuits, linear algebra, QFT, fault tolerance.
2. **qoherence-sim** — run circuits without hardware; understand simulation
   limits and tensor-network methods.
3. **qoherence-algorithms** — Grover, Shor, VQE, QAOA — from basic
   intuition to implementing quantum subroutines.
4. **qoherence-hardware** — real device concepts, connectivity, backend
   adapters.
5. **qoherence-mitigate** — why/how noise is handled, from basic mitigation
   to stabilizer codes and decoders.
6. **qoherence-bench** — measuring and comparing everything above rigorously.
7. **qoherence-docs** — architecture reference tying all repos together.

Each repo's docs/ folder is split into:
- `01-beginner/` — no prior quantum knowledge assumed
- `02-intermediate/` — comfortable with beginner material
- `03-advanced/` — comfortable with linear algebra / complexity theory
- `04-expert/` — research-level / contribution-oriented

## Industry context
Once you've read `qoherence-core`'s beginner tier, `qoherence-docs/docs/industry-landscape.md` gives real-world grounding — how IBM, Google, Microsoft, IonQ, Quantinuum, Rigetti, Amazon, PsiQuantum and others' hardware, roadmaps, and public milestones connect to the concepts in these repos. Read it early for motivation, and revisit it after `qoherence-hardware` and `qoherence-mitigate` for full technical context.

## What changed in this expansion
Every tiered doc across all six repos was substantially expanded from short reference notes into in-depth explanations with worked analogies (and each analogy's limits), step-by-step mechanisms, concrete numbers, and grounding in real IBM/Google/Microsoft/IonQ/Quantinuum/Rigetti/Amazon/PsiQuantum hardware and roadmaps as of 2025-2026. A new `qoherence-docs/docs/industry-landscape.md` ties the whole set together industry-wide.

## Explanation style
Every doc with real mathematical notation now follows a two-part structure, styled after *Quantum Computing For Dummies* (Hurley & Smith): an "In Plain English" section first — analogies (spinning coins, foggy mountain hikes, tuning a radio, whispered messages down a line) with no symbols at all — followed by a "Now With the Math" section that walks through the actual notation (kets, amplitudes, matrices, Greek letters) symbol by symbol, always tying each one back to the plain-English picture that came before it. Docs that were already narrative and light on notation (most of `qoherence-hardware` and parts of `qoherence-sim`/`qoherence-mitigate`) were left as-is since they already match this approach.
