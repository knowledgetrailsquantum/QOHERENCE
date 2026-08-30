# Mitigation vs Correction (Intermediate)

- **Mitigation** (ZNE, readout correction): cheap, statistical fixes
  applied after running noisy circuits — doesn't need extra qubits.
- **Correction** (surface codes): actively encodes and fixes errors during
  computation, needs many extra physical qubits per logical qubit.

Near-term (NISQ) hardware relies on mitigation; large-scale fault-tolerant
computing (see qoherence-core expert docs) requires full correction.
