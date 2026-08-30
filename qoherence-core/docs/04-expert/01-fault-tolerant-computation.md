# Fault-Tolerant Quantum Computation (Expert)

## The threshold theorem
If physical error rates are below a certain threshold (roughly ~1% for
surface codes, depending on architecture), arbitrarily long quantum
computations become possible by encoding logical qubits redundantly and
correcting errors faster than they accumulate. This is the theoretical
basis that makes large-scale quantum computing plausible at all.

## Logical vs physical qubits
Current NISQ (Noisy Intermediate-Scale Quantum) devices manipulate physical
qubits directly, with no error correction — hence the heavy reliance on
mitigation techniques (see qoherence-mitigate). Fault-tolerant computation
requires encoding one logical qubit across many (often 100s-1000s of)
physical qubits, depending on the code and target error rate.

## Magic state distillation
Certain gates (like the T gate) needed for universal computation cannot be
implemented "for free" within many stabilizer error-correcting codes and
require expensive resource states called magic states, purified via
distillation protocols — a major overhead driver in fault-tolerant designs.

## Where this connects across Qoherence
- qoherence-mitigate implements NISQ-era mitigation (ZNE, readout
  correction) and toy surface-code logic — a stepping stone toward
  full fault tolerance.
- qoherence-hardware's backend abstraction is designed to be extensible
  toward future fault-tolerant hardware backends as they mature.

## Further reading
Fowler et al., "Surface codes: Towards practical large-scale quantum
computation" (2012).
