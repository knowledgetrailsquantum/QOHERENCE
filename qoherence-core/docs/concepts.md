# Core Concepts

## Qubit
The fundamental unit of quantum information. Unlike a classical bit (0 or 1),
a qubit exists in a superposition: |psi> = alpha|0> + beta|1>, where alpha and
beta are complex amplitudes with |alpha|^2 + |beta|^2 = 1.

## Superposition
A qubit can be in a combination of |0> and |1> simultaneously. Measurement
collapses this superposition into one definite classical outcome, with
probability given by the squared amplitude.

## Entanglement
Two or more qubits can be correlated such that the state of one cannot be
described independently of the other, even at a distance. Entanglement is
the resource behind quantum speedups in algorithms like Grover's and Shor's.

## Gates
Quantum gates are unitary matrices that transform qubit states while
preserving total probability. Common gates:
- **X (NOT)**: flips |0> and |1>
- **H (Hadamard)**: creates superposition from a basis state
- **CNOT**: two-qubit gate that creates entanglement

## Circuits
A quantum circuit is an ordered sequence of gates applied to a register of
qubits, ending in measurement. qoherence-core's `Circuit` class models this
as a list of (gate, qubit_index) operations applied to a state vector.

## Measurement
Reading a qubit forces its superposition to collapse to a classical value
(0 or 1), with probability equal to the squared magnitude of its amplitude.
Measurement is irreversible and destroys superposition/entanglement.

## Why This Matters for qoherence-core
This repo provides the foundational data structures (Qubit, Gate, Circuit)
that every other Qoherence repo builds on:
- qoherence-algorithms uses these to build algorithm circuits
- qoherence-sim executes these circuits classically
- qoherence-hardware submits these circuits to real devices
- qoherence-mitigate operates on the results returned from execution
