# Complexity Theory for Quantum Computing (Advanced)

## In Plain English

Here's the single most common misconception about quantum computers, and it's worth dismantling carefully because it shows up in nearly every popular-science headline: "a quantum computer tries every possible answer at once and instantly knows the right one." That is not how any of this works. Measurement, as covered all the way back in the very first chapter of this repo, only ever gives you *one* sample, chosen randomly according to the probabilities baked into the amplitudes — you never get to peek at all the "parallel possibilities" and simply pick the best one. Real quantum speedup comes entirely from the interference trick (constructive and destructive combination of amplitudes, from `01-beginner/02-superposition-and-entanglement.md`) being carefully engineered so the right answer's probability gets boosted and the wrong answers' probabilities get suppressed, before that one, final, random-seeming sample is drawn.

This is also exactly why quantum computers are *not* expected to instantly solve every hard problem — famously, problems like "find the shortest possible delivery route through 500 cities" (the traveling salesman problem) or general logic-puzzle satisfiability are believed to stay hard even for quantum computers, because nobody has found a way to engineer the necessary interference pattern for their rugged, bumpy solution landscapes. Quantum speedup isn't a general-purpose power-up; it's a narrow, specific tool that fits a narrow, specific set of locks.

Which problems *does* it fit? Three buckets, roughly, worth knowing by name because you'll see these terms used loosely (and often incorrectly) in press coverage:

- **Genuinely proven, big speedups** exist only for a handful of somewhat artificial textbook problems, chosen specifically because the speedup can be mathematically proven rather than just strongly suspected.
- **Strongly believed but not mathematically proven** speedups cover the famous, practically important cases — factoring large numbers (Shor's algorithm) and simulating quantum chemistry and materials. Nobody has *proven* no classical algorithm could ever match them; the evidence is that decades of extremely motivated searching (particularly by the cryptography community, who would very much like factoring to stay easy classically) has turned up nothing better.
- **A real, but modest, provable speedup** exists for unstructured search (Grover's algorithm) — real and useful, but "faster," not "instant," and for many realistic problem sizes today's hardware overhead eats up much of the advantage anyway.

## Now With the Math

**The complexity classes, decoded.** Computer scientists sort problems into named buckets by how their solving-time scales with problem size:
- **P** — solvable efficiently (in a time that scales as a polynomial, like `n²` or `n³`, rather than exploding) on an ordinary computer.
- **NP** — a solution, once found, can be *checked* efficiently, even if finding it in the first place might be hard.
- **BPP** — P's randomized cousin: an ordinary computer that's allowed to flip coins and accept a small chance of a wrong answer.
- **BQP** — the quantum version of BPP: what a quantum computer can solve efficiently, with high (though not certain) probability of a correct answer.

**The central open question, in symbols: `BPP ⊊ BQP`.** The `⊊` symbol means "is a strict subset of" — everything BPP can do, BQP can also do, but BQP can do at least one thing BPP provably cannot. This is *believed* true (factoring is the headline supporting evidence — no faster-than-quantum classical factoring algorithm has ever been found despite immense financial incentive to find one) but has never been formally proven; proving it would resolve some of the deepest open questions in all of computer science, closely related to the famous unsolved P-vs-NP problem.

**Quantum supremacy vs. quantum advantage — reading the fine print.** Google's 2019 "quantum supremacy" claim, and its 2024 Willow follow-up, were about beating classical computers at one specific, deliberately chosen benchmark task (random circuit sampling) that has essentially no direct real-world use on its own. IBM has publicly pushed back on some supremacy claims, showing that improved *classical* techniques (particularly tensor-network methods, see `qoherence-sim/docs/03-advanced/01-tensor-network-methods.md`) sometimes catch up faster than expected. The more careful, current industry term is **quantum advantage** or **quantum utility** — always worth asking, of any headline: "beating classical computers at exactly *what* task, and how commercially relevant is that task?"

## Next
Read `04-expert/01-fault-tolerant-computation.md` to see what has to be true, physically and architecturally, before any of BQP's theoretical promise becomes practically realizable on error-prone hardware.

## A Bit of History
The complexity class BQP wasn't formally defined until 1993, by Ethan Bernstein and Umesh Vazirani — nearly two decades after Feynman's 1981 spark. Before that, nobody had a rigorous way to even ask "how much more powerful, precisely, is a quantum computer?" Bernstein and Vazirani's paper, along with a problem they invented specifically to have a provable quantum speedup, gave the field its first solid theoretical foothold — a reminder that quantum computing spent its first decade as much a question in mathematical logic as in physics or engineering.

---
**[◀ Density Matrices and Mixed States](02-density-matrices-and-mixed-states.md)**  |  [Index](../../../README.md)  |  **[Fault-Tolerant Computation ▶](../04-expert/01-fault-tolerant-computation.md)**
