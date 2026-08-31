# Phase Estimation (Advanced)

## In Plain English

Back in `01-quantum-fourier-transform.md`, we said the QFT is like tuning a radio to find a hidden repeating pattern. **Phase estimation** is the specific recipe that uses the QFT to answer one very useful question: "if I apply this gate over and over, what secret number is it quietly encoding?"

Here's the setup. Every quantum gate, applied to the right input state, doesn't just move the state around — it can also multiply it by an invisible spinning factor called a **phase**. You can't see this phase directly by measuring once (it doesn't change any single probability), but if you apply the gate *many times*, that phase builds up in a way that becomes measurable. Phase estimation is the trick that reads out that hidden number precisely, using the QFT to convert "an invisible spin rate" into "an ordinary number you can read off."

Why bother? Because an enormous number of useful quantum results boil down to finding a hidden number this way — the period in Shor's algorithm, the energy of a molecule in more advanced chemistry algorithms, all sorts of things. Phase estimation is the general-purpose tool; the specific applications are what use it.

## The Recipe, Step by Step

1. Prepare a set of "counting" qubits in superposition (Hadamard gates on all of them).
2. Apply the mystery gate, repeatedly, controlled by the counting qubits — each counting qubit triggers a different number of repetitions, doubling each time (1, 2, 4, 8...). This is what builds the invisible phase up into something detectable.
3. Apply the inverse QFT to the counting qubits.
4. Measure the counting qubits. The result, read as a binary number, is your estimate of the hidden phase.

More counting qubits means more decimal places of precision in your answer — the same trade-off as adding more digits to a ruler.

## Now With the Math

**Eigenvalues and phases.** If a gate `U` has a special input `|ψ⟩` that it doesn't rotate away from itself — only multiplies by a number — that number is called an eigenvalue (see `02-intermediate/02-linear-algebra-foundations.md` for the preview). For a quantum gate, that eigenvalue always has the form `e^(2πiθ)` — a phase factor, where `θ` (theta) is a number between 0 and 1 that phase estimation is built to find. `e^(2πiθ)` is just "a point spinning around a circle, θ of the way around" — you don't need to compute with it directly, just know it packages up the hidden number `θ`.

**Why repetition helps.** Applying `U` twice multiplies the phase by itself: `e^(2πiθ) × e^(2πiθ) = e^(2πi·2θ)`. Applying it `2^k` times gives `e^(2πi·2^k θ)`. This doubling trick is what lets a modest number of counting qubits pin down `θ` to high precision — each extra counting qubit effectively doubles your resolving power, the same exponential-doubling idea that shows up everywhere else in this repo, here working in your favor instead of against you.

## A Bit of History

Phase estimation was formalized in 1995 by Alexei Kitaev — the same physicist who, a couple of years later, proposed the surface code (`qoherence-mitigate/docs/03-advanced/01-stabilizer-codes.md`). It's a good example of how a handful of researchers in the mid-1990s kept independently building the exact tools the field would need decades later, well before hardware existed to run any of it.

## Next
Read `02-density-matrices-and-mixed-states.md` — the tool for describing what happens when the "mystery gate" above isn't running on a perfectly clean qubit.

---
**[◀ Quantum Fourier Transform](01-quantum-fourier-transform.md)**  |  [Index](../../../README.md)  |  **[Density Matrices and Mixed States ▶](02-density-matrices-and-mixed-states.md)**
