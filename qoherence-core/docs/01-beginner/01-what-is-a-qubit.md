# What Is a Qubit? (Beginner)

## In Plain English

Picture an ordinary light switch. It's either off or on — nothing in between, no ambiguity, no mystery. That's a classical bit: a 0 or a 1, full stop. Every computer you've ever touched, from a calculator to a supercomputer, is built from billions of these switches.

Now picture a coin, not lying flat on a table, but spinning in the air. While it's spinning, it isn't heads and it isn't tails — it's genuinely, physically undecided. It's not that the coin secretly "knows" which way it will land and is just hiding it from you; the outcome doesn't exist yet. Only the instant it hits the table and you look does it become one or the other. That spinning coin is a much better mental picture of a **qubit** than a dimmer switch or a percentage ever will be, because a dimmer switch is still secretly "decided" at 73% brightness — it's just a number you haven't looked up. A spinning coin isn't secretly decided. Neither is a qubit.

So a qubit is the quantum version of a bit: instead of being locked to 0 or 1 like a light switch, it can be in a genuine blend of both — spinning — right up until the moment you measure it, at which point it "lands" on a definite 0 or 1 and stays that way. This in-between condition is called **superposition**, and it's the first of two ideas (the second, entanglement, comes in the next chapter of this doc set) that everything else in quantum computing is built on top of.

Here's the part that trips people up: a spinning coin isn't 50/50 by necessity. You can spin it in a way that makes it more likely to land heads, or more likely to land tails, while it's still genuinely unresolved in the air. A qubit works the same way — its superposition can lean toward 0, lean toward 1, or sit exactly in between, and *how* it leans is precisely what a quantum engineer controls when designing a circuit.

When you finally measure a qubit, something irreversible happens: the "spinning" stops and it becomes an ordinary, classical 0 or 1. You cannot un-measure it and get the superposition back. This is fundamentally different from reading a classical bit, which you can check as many times as you like without disturbing it. A quantum computation is therefore a one-shot affair — you set the qubits spinning in a carefully engineered way, and then you look, once, at the end.

## Now With the Math

Everything above is true and it's the right way to *think* about a qubit day to day. But to actually build circuits, quantum engineers need a precise, symbol-based way to describe "how a qubit is spinning" — something more exact than "leaning a bit toward heads." That's what this section gives you, symbol by symbol.

**The ket, `|...⟩`.** Physicists write a qubit's state inside this odd-looking bracket, called a "ket." `|0⟩` just means "the qubit is definitely, purely in the 0 state" — the spinning coin has already landed heads-up and stopped. `|1⟩` means the same thing for 1. Don't overthink the bracket notation itself; it's just a labeled box for "the state of the system," chosen by physicists (Paul Dirac, specifically) so that quantum states could be written and manipulated like algebra.

**The general state, `|ψ⟩ = α|0⟩ + β|1⟩`.** This is the "spinning coin in the air" written as an equation. `ψ` (the Greek letter psi) is just a name — "call this particular qubit state ψ," the way you'd write `x = 5` in ordinary algebra. The right-hand side says the qubit's state is a mix of "some amount of `|0⟩`" plus "some amount of `|1⟩`." The "some amount" is what `α` and `β` (alpha and beta) capture.

**The amplitudes, `α` and `β`.** These are numbers (technically, they're allowed to be *complex* numbers, meaning they can involve `i = √-1`, though you can build good intuition while pretending they're ordinary numbers that can also be negative) that say how much of `|0⟩` and how much of `|1⟩` is in the mix. Crucially, `α` and `β` are **not** the probabilities themselves — they're one mathematical step removed from probability, the way a wave's height isn't the same thing as the energy it carries.

**Turning amplitudes into probability: `|α|²`.** To get an actual probability — a real percentage you could bet money on — you square the amplitude's size. The probability of measuring 0 is `|α|²`, and the probability of measuring 1 is `|β|²`. The vertical bars mean "take the magnitude" (for an ordinary real number this is just "ignore the sign"; for a complex number it's a slightly more involved calculation, but the idea is the same — turn it into a plain, non-negative size). This squaring step is called the **Born rule**, and it's one of the strangest and most experimentally battle-tested facts in all of physics: nobody has a deeper explanation for *why* nature uses the square of the amplitude rather than the amplitude itself, it's simply what every experiment confirms.

**The one rule that keeps this from being nonsense: `|α|² + |β|² = 1`.** This equation just says: the probability of getting 0, plus the probability of getting 1, must add up to 100%. That has to be true of any honest probability, quantum or not — you can't have a 60% chance of heads and a 60% chance of tails, because that's 120%, which is nonsense. This single constraint is the mathematical fence that keeps superposition from being "magic" — whatever blend a qubit is in, the numbers always land on a legitimate 100% total once you measure.

**Measurement.** In the math, "measuring" means: roll a weighted die where the weights are `|α|²` and `|β|²`, get an outcome of 0 or 1, and then the qubit's state instantly *becomes* `|0⟩` or `|1⟩` — the α and β information beyond that single bit is gone. This is what "the coin lands and stops spinning" means in symbols.

## Try it yourself
```python
from src.qubit import Qubit
q = Qubit(alpha=1.0, beta=0.0)   # definitely |0> -- the coin isn't spinning, it's already heads
print(q)

import math
q2 = Qubit(alpha=1/math.sqrt(2), beta=1/math.sqrt(2))  # equal superposition -- a fairly-spun coin
print(q2)   # 50/50 chance of 0 or 1 on measurement, because (1/sqrt(2))**2 = 0.5 for both
```

## What's happening in the world right now
As of 2025–2026, qubit counts on the flashiest chips (IBM's Condor-class and Heron-class processors, Google's Willow, Atom Computing/Quantinuum's neutral-atom and trapped-ion systems) range from roughly 100 to over 1,000 physical qubits, but the industry's real benchmark has shifted to **logical qubits** — error-corrected qubits built by combining many physical ones (see `qoherence-mitigate`). Google's Willow chip made headlines in late 2024 for demonstrating that error rates *drop* as more physical qubits are added per logical qubit — the first hard evidence that the error-correction math actually works below the "surface code threshold" in a real device.

## Next
Read `02-superposition-and-entanglement.md` — superposition on its own is interesting, but it's what happens when *multiple* qubits interact that gives quantum computers their power.

## A Bit of History
The word "qubit" was coined in 1995 by physicist Benjamin Schumacher, who needed a short name for "quantum bit" while writing a paper on quantum data compression — reportedly suggested to him in conversation by William Wootters. It stuck instantly, the way "bit" (itself coined by statistician John Tukey in 1947, popularized by Claude Shannon) had decades earlier. Both words did the same job: giving an entire field a one-syllable unit to build sentences around.

---
**[◀ A History of Quantum Mechanics](../00-history-of-quantum-mechanics.md)**  |  [Index](../../../README.md)  |  **[Superposition and Entanglement ▶](02-superposition-and-entanglement.md)**
