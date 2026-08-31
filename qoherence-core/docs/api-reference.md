# API Reference: qoherence-core

## `src.qubit.Qubit`
Represents a single, unentangled qubit's pure state (see `01-beginner/01-what-is-a-qubit.md`).

```python
Qubit(alpha: complex, beta: complex)
```
- Raises on construction if `|alpha|**2 + |beta|**2` is not ≈1 (normalization is not automatic — this is intentional, to catch bugs early rather than silently renormalize).
- `.probabilities()` → `(p0, p1)`.
- `.measure()` → collapses to `0` or `1` per the Born rule, mutating internal state (see `03-advanced/02-density-matrices-and-mixed-states.md` for what "collapse" means formally).

Note: `Qubit` is primarily a teaching/introspection object for single, unentangled qubits. Multi-qubit circuits (below) use a full state vector internally, since general multi-qubit states cannot be decomposed into independent `Qubit` objects once entangled — see `02-intermediate/01-multi-qubit-systems.md`.

## `src.gate` module
Defines standard unitary gates as matrices: `X`, `Y`, `Z`, `H`, `S`, `T`, `CNOT`, and parameterized rotation gates. See `01-beginner/03-gates-and-circuits.md` and `02-intermediate/02-linear-algebra-foundations.md` for what each does and why it's unitary.

## `src.circuit.Circuit`
```python
Circuit(num_qubits: int)
c.apply(gate, *qubit_indices)   # append a gate op to the circuit
c.run() -> Result                # simulate; returns amplitudes + measurement statistics
```
- Internally maintains a `2**num_qubits`-length complex state vector (see `02-intermediate/01-multi-qubit-systems.md` for why this grows exponentially, and why it caps out around 25-30 qubits on commodity hardware — `qoherence-sim` provides alternative backends for larger circuits).
- `Result.amplitudes` — raw complex amplitude array (ideal/noise-free).
- `Result.sample(shots=N)` — simulate N measurement shots, returning bitstring counts, mimicking how real hardware (and `qoherence-hardware`) reports results as shot counts rather than exact probabilities.

## Extending this API
See `04-expert/02-extending-qoherence-core.md` for how to add gates, backends, and tests correctly.
