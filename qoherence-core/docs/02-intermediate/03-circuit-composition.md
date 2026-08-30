# Circuit Composition Patterns (Intermediate)

## Sequential composition
Circuits are built by chaining gate operations — order matters, since
quantum gates generally don't commute (applying H then X differs from X
then H).

## Common building blocks
- **State preparation**: gates applied at the start to set up a specific
  initial superposition or entangled state (e.g. Bell pairs, GHZ states).
- **Oracle blocks**: circuits that encode a problem-specific function,
  used heavily in Grover's algorithm and QAOA.
- **Uncompute steps**: reversing intermediate computation to clean up
  ancilla (helper) qubits before measurement, common in larger algorithms.

## Circuit depth vs width
- **Width** = number of qubits used.
- **Depth** = number of sequential gate layers.
Real hardware has limited **coherence time**, so lower depth circuits are
more robust to noise — a key design constraint covered further in
qoherence-mitigate docs.

## Composing with qoherence-core
```python
circuit = Circuit(num_qubits=2)
circuit.add(H_GATE, 0)
circuit.add(CNOT_GATE, (0, 1))  # conceptual; extend Circuit/Gate for multi-qubit ops
```

## Next
Move to `03-advanced/` for the math behind quantum algorithms.
