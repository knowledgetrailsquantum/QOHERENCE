# API Reference — qoherence-core

## `Qubit`
Represents a single-qubit state with amplitudes `alpha`, `beta`.

```python
from src.qubit import Qubit
q = Qubit(alpha=1.0, beta=0.0)
```

## `Gate`
Wraps a unitary matrix and applies it to a state vector.

```python
from src.gate import H_GATE
new_state = H_GATE.apply(state_vector)
```

Predefined gates: `X_GATE`, `H_GATE`.

## `Circuit`
Builds a sequence of gate operations and runs them against an initial state.

```python
from src.circuit import Circuit
from src.gate import H_GATE

circuit = Circuit(num_qubits=1).add(H_GATE, 0)
final_state = circuit.run(initial_state)
```
