# Implementing Shor's Period-Finding (Expert)

To complete `shor.py`, implement the quantum subroutine:
1. Prepare a superposition over all inputs x in register 1.
2. Compute a^x mod N into register 2 (modular exponentiation circuit).
3. Apply inverse QFT to register 1 (see qoherence-core advanced docs).
4. Measure register 1 — result is related to the period r via continued
   fractions.
5. Classically verify r and recover factors via gcd(a^(r/2) ± 1, N).

Modular exponentiation circuits are the most gate-expensive part — a good
research/contribution area for optimizing qoherence-algorithms further.
