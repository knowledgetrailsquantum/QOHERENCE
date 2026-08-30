# Simulators

## State-Vector Simulator (`statevector.py`)
Represents the full quantum state as a 2^n-dimensional complex vector and
applies gates as matrix operations. Exact but memory scales exponentially
with qubit count — practical up to roughly 25-30 qubits.

## Tensor-Network Simulator (`tensor_network.py`)
Represents state as a network of contracted tensors (e.g. matrix product
states), controlled by a `bond_dim` parameter. Can scale to far more qubits
than state-vector simulation when entanglement is limited, at the cost of
approximation for highly entangled states.

## Choosing a Simulator
| Simulator       | Qubit Count | Accuracy | Best For                     |
|------------------|-------------|----------|-------------------------------|
| State-vector     | Small (<30) | Exact    | Algorithm correctness testing |
| Tensor-network   | Larger      | Approx.  | Low-entanglement circuits     |
