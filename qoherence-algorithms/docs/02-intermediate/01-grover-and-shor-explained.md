# Grover's and Shor's Algorithms Explained (Intermediate)

## In Plain English

**Grover's algorithm: a smarter way to search.** Imagine a huge phone book with a million entries, listed in no particular order, and you're looking for the one entry matching a phone number you have. Classically, there's no shortcut — on average you'd have to check about half a million entries before finding it. Grover's algorithm doesn't magically skip to the answer, but it does something clever: each "check" doesn't just say yes-or-no about one entry, it subtly reshapes your belief about *every* entry at once, nudging the true answer's likelihood up and every wrong answer's likelihood down, a little at a time, using the interference tricks from `qoherence-core/docs/01-beginner/02-superposition-and-entanglement.md`. Do this nudge enough times — roughly the square root of a million, about 1,000 times, instead of half a million — and the true answer becomes overwhelmingly likely. That's a real, meaningful speedup, but notice it's *square-root* faster, not *exponentially* faster — genuinely useful, but not the sweeping "instant answer" popular science often implies.

**Shor's algorithm: finding a hidden rhythm.** Factoring a large number turns out to be secretly related to finding a repeating pattern (a period) in a related, much simpler-looking function — a mathematical sleight of hand discovered by Peter Shor. Classically, finding that hidden rhythm in a huge number requires checking an enormous number of candidates one at a time. Quantumly, the QFT (`qoherence-core/docs/03-advanced/01-quantum-fourier-transform.md`) lets you find the rhythm the way a well-tuned radio finds a station — by resonance, all at once, rather than by scanning frequency by frequency. Once you know the rhythm, ordinary grade-school-level number theory (finding a greatest common divisor) usually hands you a real factor of the original number directly.

Here's the plain-English version of why this matters so much: essentially all of today's secure internet traffic (HTTPS, banking, messaging apps) relies on factoring large numbers being classically hard. Shor's algorithm, if ever run on a large enough, reliable enough quantum computer, breaks that assumption completely. That's why "post-quantum cryptography" — new encryption methods that don't rely on factoring being hard — is being rolled out today, years before any computer capable of running Shor's algorithm at that scale actually exists; the concern is that encrypted data intercepted and stored *today* could be decrypted once such a machine arrives ("harvest now, decrypt later").

## Now With the Math

**Grover's algorithm, step by step.** For `N = 2ⁿ` items indexed by `n` qubits:
1. Apply Hadamard gates to every qubit (`01-beginner/03-gates-and-circuits.md`), putting all `N` indices into an equal superposition — every entry starts with amplitude `1/√N`.
2. Apply the **oracle** — a gate that flips the sign of the amplitude on the correct answer's index, leaving every other amplitude untouched. Squaring a flipped-sign amplitude gives the same probability as before (`|−α|²=|α|²`, from `qoherence-core/docs/01-beginner/03-gates-and-circuits.md`'s discussion of the Z gate), so this step alone changes *nothing* measurable yet — it just sets up the next step.
3. Apply the **diffusion operator** — a reflection of every amplitude about their average value. Because step 2 singled out one amplitude with a flipped sign, this reflection converts that lone sign flip into a genuine, measurable boost for the correct answer, at the expense of every other amplitude.
4. Repeat steps 2–3 about `(π/4)√N` times (`π` here is the familiar 3.14159..., and `√N` is the square root of the total item count) — each repetition nudges the correct amplitude a bit further, the way a pendulum swings closer to vertical with each push.
5. Measure. The correct answer now dominates the probability.

Run this loop *too many* times and you overshoot — the amplitude keeps rotating past the ideal point and starts *decreasing* again, so Grover's algorithm needs to know roughly how many repetitions to run, unlike a classical search that can just stop the moment it finds the answer.

**Shor's algorithm, the shape of it.** To factor a number `N`, pick a random number `a` and consider the function `f(x) = aˣ mod N` (read `mod N` as "remainder after dividing by N" — the same "clock arithmetic" idea as a 12-hour clock wrapping back to 1 after 12). This function repeats with some period `r`. Steps:
1. Prepare a superposition over many values of `x`.
2. Compute `f(x) = aˣ mod N` *in superposition* — entangling an "index" register with a "value" register (this step, called modular exponentiation, is the most gate-expensive part of the whole algorithm in practice, more expensive than the QFT itself).
3. Apply the inverse QFT to the index register, converting the hidden period `r` into a measurable spike.
4. Measure, then use a classical technique (continued fractions — a way of approximating a fraction using nested divisions) to extract a candidate `r` from the measured number.
5. Check whether `r` actually works (using it to compute a greatest common divisor with `N`); if not, retry with a different `a` — this is a probabilistic algorithm, not a guaranteed-first-try one.

## Concrete resource comparisons
Grover's algorithm searching 1 million items: classically up to 1,000,000 checks; Grover's needs roughly 785 (`√1,000,000 × π/4`). Shor's algorithm factoring a 2048-bit RSA key: estimated to need on the order of 20 million physical qubits running for about 8 hours on fault-tolerant hardware (Gidney & Ekerå, 2021) — versus today's largest processors at roughly 1,000–1,200 physical qubits.

## Next
Read `03-advanced/01-vqe-and-qaoa-theory.md` for the algorithms that are actually being piloted on today's hardware.

## A Bit of History
Lov Grover published his search algorithm in 1996, two years after Shor's factoring algorithm, and reportedly had to fight to get it taken seriously at first — a mere quadratic speedup seemed unglamorous next to Shor's exponential one. History proved Grover's contribution had a different kind of staying power: because it applies to *any* unstructured search problem rather than one specific number-theoretic trick, variants of Grover's algorithm show up as a subroutine inside a huge fraction of quantum algorithms devised since, making it arguably the more broadly influential of the two, even if it's less famous outside the field.

---
**[◀ Why Algorithms Need Quantum](../01-beginner/01-why-algorithms-need-quantum.md)**  |  [Index](../../../README.md)  |  **[VQE and QAOA Theory ▶](../03-advanced/01-vqe-and-qaoa-theory.md)**
