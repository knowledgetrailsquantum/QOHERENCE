# Algorithms Overview

qoherence-algorithms implements four algorithms spanning the field's two eras — fault-tolerant-era (Grover, Shor) and NISQ-era (VQE, QAOA). Full depth, analogies, and industry context live in the tiered docs:

| Algorithm | Tier | Doc | Speedup type | Era |
|---|---|---|---|---|
| Why quantum algorithms exist at all | Beginner | `01-beginner/01-why-algorithms-need-quantum.md` | — | — |
| Grover's search | Intermediate | `02-intermediate/01-grover-and-shor-explained.md` | Proven quadratic | Fault-tolerant |
| Shor's factoring | Intermediate | `02-intermediate/01-grover-and-shor-explained.md` | Believed exponential | Fault-tolerant |
| VQE (ground-state energy) | Advanced | `03-advanced/01-vqe-and-qaoa-theory.md` | Problem-dependent | NISQ |
| QAOA (combinatorial optimization) | Advanced | `03-advanced/01-vqe-and-qaoa-theory.md` | Problem-dependent | NISQ |
| Shor's period-finding, implementation detail | Expert | `04-expert/01-implementing-shors-period-finding.md` | — | Fault-tolerant |

## Source-to-doc map
- `src/grover.py` ↔ `02-intermediate/01-grover-and-shor-explained.md`
- `src/shor.py` ↔ `02-intermediate/01-grover-and-shor-explained.md` + `04-expert/01-implementing-shors-period-finding.md`
- `src/vqe.py`, `src/qaoa.py` ↔ `03-advanced/01-vqe-and-qaoa-theory.md`

## Who's using what, in practice (2025–2026)
VQE- and QAOA-family algorithms dominate real pilot deployments (IBM Quantum Network partners, Google's chemistry research collaborations, Microsoft Azure Quantum Elements customers, IonQ and Quantinuum enterprise pilots in finance and logistics) because they tolerate current noise levels. Grover's and Shor's remain primarily research and roadmap-planning topics — see `04-expert/01-implementing-shors-period-finding.md` for why the resource gap to practical Shor's is still enormous.

## Next
See `qoherence-hardware/docs` for how these algorithms map onto specific physical qubit technologies, and `qoherence-bench/docs` for how to rigorously measure and compare their performance.
