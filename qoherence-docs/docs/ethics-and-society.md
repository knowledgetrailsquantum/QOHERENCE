# Ethical, Societal, and Economic Implications

## In Plain English

Every technology this consequential eventually raises questions bigger than "does it work." This page is a short, honest look at the ones that come up most for quantum computing — not to give final answers, but so this repo's "end-to-end expertise" includes them at all.

## Jobs and Workforce

Quantum computing is creating an entirely new job category — quantum software engineers, error-correction specialists, hardware physicists working at cryogenic temperatures — while today's supply of trained people is far smaller than demand. Universities and companies (IBM, Microsoft's Quantum Katas project, and others) have built free educational programs specifically to close this gap. The flip side, further out, is less certain: if quantum computers eventually outperform classical ones at specific optimization or simulation tasks, that could reshape which classical-computing skills stay valuable in those specific niches — though, as `applications-by-industry.md` makes clear, that shift is not close to happening broadly yet, so predictions about job displacement remain speculative rather than observed.

## Security Policy: The "Harvest Now, Decrypt Later" Problem

This is the field's most concrete, already-acted-upon societal implication. Because Shor's algorithm would eventually break today's standard encryption (`qoherence-algorithms/docs/02-intermediate/01-grover-and-shor-explained.md`), adversaries can record encrypted data *today* and simply wait for quantum computers capable of decrypting it later. This isn't hypothetical policy caution — it's why NIST finalized post-quantum cryptography standards in 2024, and why governments and companies handling long-lived sensitive data (health records, state secrets, financial history) are migrating encryption now, even though the hardware that would exploit the old encryption doesn't exist yet. It's a rare case of a future technology's risk already reshaping present-day infrastructure decisions.

## Access and Inequality

Quantum computers are extraordinarily expensive to build and run. Cloud access (IBM Quantum, Amazon Braket, Microsoft Azure Quantum) has lowered the barrier to *experimenting* with quantum programming to effectively zero — a striking contrast to earlier eras of computing, where hardware access itself was the barrier (see the history of IBM opening its first public quantum computer in 2016, `qoherence-hardware/docs/04-expert/01-building-a-custom-backend.md`). But building and owning frontier hardware remains concentrated among a small number of well-funded companies and governments, raising ordinary questions about who benefits first from any future quantum advantage, similar to earlier debates about access to supercomputing and, before that, mainframe computing.

## Scientific Trust and Overclaiming

This field has a genuine, recurring credibility problem: "quantum supremacy" and "quantum advantage" claims have repeatedly been announced, publicly debated, and in some cases partially walked back as classical techniques caught up (`qoherence-core/docs/03-advanced/03-complexity-theory.md`). Microsoft's 2025 "Majorana 1" topological qubit claim drew significant scientific scrutiny over the strength of its evidence (`qoherence-hardware/docs/02-intermediate/01-qubit-technologies.md`). None of this means the field is fraudulent — genuine, hard-won progress is real and documented throughout this repo — but it does mean healthy skepticism toward any single headline claim is warranted, and is exactly the discipline `qoherence-bench/docs/04-expert/01-statistical-rigor-in-quantum-benchmarks.md` argues for applying rigorously.

## A Grounded Closing Thought

The physicists who built quantum mechanics a century ago (`qoherence-core/docs/00-history-of-quantum-mechanics.md`) were resolving a scientific crisis about the nature of light and atoms — they had no way to know it would eventually raise questions about jobs, encryption, and public trust in scientific claims. That's a useful closing perspective for this whole repo: quantum computing is simultaneously some of the deepest, most abstract physics ever done, and an increasingly concrete matter of public policy — and taking it seriously means holding both of those at once.

## Next
The trail continues into `qoherence-ai/` — quantum machine learning and quantum-inspired classical AI. Or return to the [Index](../../README.md) to revisit any part of the journey.

---
**[◀ Applications by Industry](applications-by-industry.md)**  |  [Index](../../README.md)  |  **[What Is Quantum AI? ▶](../../qoherence-ai/docs/01-beginner/01-what-is-quantum-ai.md)**
