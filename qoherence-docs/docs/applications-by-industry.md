# Applications by Industry

## In Plain English

Most of this repo answers "how does quantum computing work." This page answers a more practical question: "who is actually using it, for what, right now?" The honest answer today is a mix of real, narrow, working use cases and a lot of speculative future promise — this page tries to keep those two things clearly separated.

## Cybersecurity and Cryptography

This is the field's oldest and clearest application, for a slightly backwards reason: quantum computing's biggest near-term cybersecurity impact isn't something a quantum computer does *for* you — it's a threat it poses. Shor's algorithm (`qoherence-algorithms/docs/02-intermediate/01-grover-and-shor-explained.md`) would break the encryption (RSA, ECC) that protects most of today's internet traffic, if it were ever run at large enough scale. That's why "post-quantum cryptography" — new encryption methods immune to Shor's algorithm — is being deployed today, years ahead of the hardware that would need it, following NIST's 2024 finalized standards.

The flip side is **quantum key distribution (QKD)**, a genuinely working near-term technology: using entangled or single-photon quantum states to detect whether an eavesdropper tampered with a communication channel, because measuring a quantum state disturbs it (see `qoherence-core/docs/01-beginner/01-what-is-a-qubit.md`'s discussion of measurement collapse). QKD networks already exist in limited, real deployments — mostly government and financial-sector links — though it needs dedicated hardware (typically fiber-optic links) and doesn't replace ordinary internet infrastructure the way post-quantum cryptography does.

## Finance

Banks and hedge funds have been early, well-funded testers of NISQ-era algorithms (`qoherence-algorithms/docs/03-advanced/01-vqe-and-qaoa-theory.md`), particularly QAOA, for portfolio optimization (choosing a mix of investments to balance risk and return) and options pricing. As of 2025-2026 these remain pilot projects and research collaborations (JPMorgan, Goldman Sachs, and others have published joint work with IBM, IonQ, and others) rather than production systems replacing classical financial models — today's quantum hardware isn't yet reliably beating classical optimization methods on real trading-scale problems, but the finance sector's tolerance for expensive, exploratory research makes it a natural early adopter.

## Chemistry, Materials, and Healthcare

This is where the field's most credible near-term promise lives. VQE-style algorithms (`qoherence-algorithms/docs/03-advanced/01-vqe-and-qaoa-theory.md`) are built to find a molecule's lowest-energy configuration — directly useful for drug discovery, battery electrolyte design, and catalyst design, all problems where classical simulation cost explodes exponentially with molecule size. Microsoft's Azure Quantum Elements, IBM's collaborations with pharmaceutical and materials companies, and Google's chemistry research groups are all active here. Genuinely useful results at commercially meaningful molecule sizes are still ahead of us, but this is widely considered the most likely place quantum computing delivers real value before full fault tolerance arrives.

## Logistics and Supply Chains

Route optimization, scheduling, and resource allocation are natural QAOA-shaped problems (`qoherence-algorithms/docs/03-advanced/01-vqe-and-qaoa-theory.md`) — airlines, shipping companies, and logistics firms have run pilot projects with IBM, D-Wave (a quantum annealing specialist, a related but different approach not covered in depth elsewhere in this repo), and others. As with finance, these remain pilots rather than production replacements for classical solvers, which remain highly optimized and hard to beat at today's problem sizes.

## The Honest Summary

Across every industry above, the pattern repeats: real pilot projects, real published research, real corporate investment — and, so far, no widely-deployed production system where a quantum computer is reliably beating the best classical alternative on a commercially important problem at meaningful scale. `qoherence-bench/docs/03-advanced/02-resource-estimation.md` is the tool for checking, honestly, whether a specific claimed use case has actually crossed that line yet.

## Next
Read `ethics-and-society.md` for the broader implications beyond "does it work" — what happens to jobs, security policy, and public trust as this technology matures.

---
**[◀ The Quantum Computing Industry Landscape](industry-landscape.md)**  |  [Index](../../README.md)  |  **[Ethical, Societal, and Economic Implications ▶](ethics-and-society.md)**
