# Multi-Qubit Systems (Intermediate)

## Tensor products
A single qubit lives in a 2-dimensional space (amplitudes for |0>, |1>).
n qubits together live in a 2^n-dimensional space, built via the tensor
product of individual qubit spaces. Two qubits have 4 basis states:
|00>, |01>, |10>, |11>, each with its own complex amplitude.

## Why exponential scaling matters
This is the core source of both quantum computing's power and its
simulation difficulty: 20 qubits need a state vector of size 2^20 (~1M)
complex numbers; 50 qubits need 2^50 (~1 quadrillion) — infeasible
classically. This is why real quantum hardware matters for scale.

## Entangled vs separable states
A two-qubit state is **separable** if it can be written as (qubit A) ⊗
(qubit B) independently. It's **entangled** if it cannot — e.g. the Bell
state (|00> + |11>)/sqrt(2) cannot be factored into independent qubits.

## Multi-qubit gates
- **CNOT (controlled-NOT)**: flips the target qubit only if the control
  qubit is |1>. This is the standard way to create entanglement.
- **Toffoli (CCNOT)**: three-qubit gate, flips target if both controls are 1.

## Building a Bell pair
1. Start with |00>.
2. Apply H to qubit 0 -> (|00> + |10>)/sqrt(2).
3. Apply CNOT(control=0, target=1) -> (|00> + |11>)/sqrt(2).

This is the "hello world" of entanglement and appears throughout
qoherence-algorithms.
