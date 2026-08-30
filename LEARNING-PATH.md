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
