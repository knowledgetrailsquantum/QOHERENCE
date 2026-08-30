# Gates & Circuits (Beginner)

## What is a gate?
A quantum gate is an operation you apply to one or more qubits to change
their state — similar to how AND/OR/NOT gates work on classical bits, but
quantum gates must be reversible and preserve total probability.

## Two gates to know first

### X gate (quantum NOT)
Flips |0> to |1> and vice versa. Same idea as a classical NOT gate.

### H gate (Hadamard)
Takes a definite state like |0> and turns it into an equal superposition of
|0> and |1>. This is usually the very first gate you apply to "activate"
quantum behavior in a qubit.

## What is a circuit?
A circuit is just an ordered list of gates applied to your qubits, ending
in a measurement. Read circuits left to right, like a recipe of steps.

## Your first circuit (conceptually)
1. Start with a qubit in state |0>.
2. Apply an H gate -> qubit is now in superposition.
3. Measure -> get 0 or 1, each with 50% probability.

```python
from src.circuit import Circuit
from src.gate import H_GATE

circuit = Circuit(num_qubits=1).add(H_GATE, 0)
```

## Next
Move to `02-intermediate/` once this all feels familiar.
