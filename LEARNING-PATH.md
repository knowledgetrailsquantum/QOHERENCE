# Qoherence Learning Path

Qoherence is an educational-first quantum computing repo set. Follow this
order, reading each repo's docs tiers (01-beginner -> 04-expert) in sequence:

0. **`qoherence-core/docs/00-history-of-quantum-mechanics.md`** — read this literal first page before anything else: a century of physics history (Planck, Einstein, Bohr, Heisenberg, Feynman, Deutsch, Shor) and how it led to real, physically-built qubits today.
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

## Second expansion: sourced from three additional books
Reviewed against *Quantum for Everyone* (Alan H. Patrick), *Quantum Programming in Depth* (Mariia Mykhailova), and *Why Nobody Understands Quantum Physics* (Frank Verstraete & Céline Broeckaert), six new pages were added to fill real gaps:
- `qoherence-core/docs/02-intermediate/04-reversible-computing.md` and `qoherence-core/docs/03-advanced/04-phase-estimation.md` — foundational tools used by Shor's algorithm and quantum chemistry that were previously only mentioned in passing.
- `qoherence-algorithms/docs/04-expert/02-worked-example-grover-n-queens.md` — a real, runnable Qiskit worked example, showing the oracle-construction work an abstract algorithm description skips over.
- `qoherence-bench/docs/03-advanced/02-resource-estimation.md` — how tools like Microsoft's Azure Quantum Resource Estimator turn algorithm designs into honest qubit-count and runtime numbers.
- `qoherence-docs/docs/applications-by-industry.md` and `qoherence-docs/docs/ethics-and-society.md` — real-world use cases by sector, and the jobs/policy/access/trust questions the technology raises. `ethics-and-society.md` is now the last page of the trail.
The history page also gained the double-slit experiment and Heisenberg's microscope thought experiment; the hardware qubit-technologies page gained an explanation of BCS superconductivity theory (why cooling a superconducting loop actually switches on the physics a qubit depends on, not just "slows noise down"); and the linear-algebra page gained the Hilbert's Hotel analogy for Hilbert spaces.

## Third expansion: qoherence-ai (new repo)
A new sibling repo, `qoherence-ai/`, was added covering both real quantum machine learning (variational quantum classifiers, quantum kernels, quantum neural networks, hybrid training loops, barren plateaus) and quantum-inspired classical AI (annealing, tensor networks) — grounded in three additional books: *Quantum AI* (Aiden Cooper), *Quantum Computing and Artificial Intelligence in Logistics and Supply Chain Management*, and *Quantum Computing and Artificial Intelligence: The Industry Use Cases* (Raj). It follows the same four-tier structure and In Plain English / Now With the Math / A Bit of History page format as the other six repos, with expert-tier industry case studies (healthcare, fintech, logistics, cybersecurity, manufacturing, NLP) and an honest hype-check page on QML's real vs. overstated capabilities.

`qoherence-ai` is now the eighth and final leg of the trail: read it after `qoherence-docs` (whose `ethics-and-society.md` now links forward into it instead of ending the trail). Its own final page, `qoherence-ai/docs/04-expert/04-future-outlook.md`, is now the literal end of the whole trail.

8. **qoherence-ai** — quantum machine learning and quantum-inspired classical AI, read last: variational classifiers, quantum kernels, quantum neural networks, barren plateaus, and real industry case studies in healthcare, fintech, logistics, and cybersecurity.
