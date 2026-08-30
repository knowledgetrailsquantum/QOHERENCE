# What Is Real Quantum Hardware? (Beginner)

Simulators (qoherence-sim) run "perfect" quantum math on a classical
computer. Real hardware uses actual physical qubits — superconducting
circuits (IBM, Rigetti), trapped ions (IonQ), or other technologies — and
is noisy, imperfect, and limited in qubit count and connectivity today.

## Why an abstraction layer?
Every provider has a different API. qoherence-hardware's `Backend` class
lets algorithm code stay provider-agnostic.
