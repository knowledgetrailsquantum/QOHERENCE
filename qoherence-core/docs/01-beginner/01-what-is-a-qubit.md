# What Is a Qubit? (Beginner)

## Classical bits vs qubits
A classical computer bit is either 0 or 1. A quantum bit (qubit) can be 0,
1, or a blend of both at once — called **superposition**. Think of a coin:
a classical bit is like a coin lying flat (heads or tails, decided). A
qubit is like a coin spinning in the air — it doesn't "decide" heads or
tails until you look at it (measure it).

## Notation
Physicists write qubit states using "ket" notation:
- |0> means "definitely 0"
- |1> means "definitely 1"
- alpha|0> + beta|1> means "a mix of both", where alpha and beta are
  numbers (can be complex) that say how much of each is present.

## The one rule you must know
|alpha|^2 + |beta|^2 = 1

This just means: the probabilities of measuring 0 or 1 must add up to 100%.

## Measuring a qubit
When you measure a qubit in superposition, it randomly collapses to 0 or 1.
- Probability of getting 0 = |alpha|^2
- Probability of getting 1 = |beta|^2

Once measured, the superposition is gone — it's now a plain classical 0 or 1.

## Try it yourself
```python
from src.qubit import Qubit
q = Qubit(alpha=1.0, beta=0.0)  # definitely |0>
print(q)
```

## Next
Read `02-superposition-and-entanglement.md`.
