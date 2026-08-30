# Error Correction & Mitigation

## Surface Codes (`surface_code.py`)
A topological quantum error-correcting code that encodes one logical qubit
across many physical qubits arranged on a 2D lattice. Errors are detected
via syndrome measurements and corrected without disturbing encoded data.
Code `distance` determines how many errors can be corrected.

## Zero-Noise Extrapolation — ZNE (`zne.py`)
A mitigation technique (not full correction) that runs the same circuit at
artificially scaled noise levels, then extrapolates results back to the
zero-noise limit. Useful on near-term (NISQ) hardware without full QEC.

## Readout Error Correction (`readout_correction.py`)
Corrects measurement (readout) errors using a calibration matrix built from
known reference states, inverting the matrix to recover true probabilities.

## Correction vs. Mitigation
- **Correction** (surface codes): actively fixes errors during computation,
  requires significant qubit overhead.
- **Mitigation** (ZNE, readout correction): statistically compensates for
  errors post-hoc, cheaper but less robust than full QEC.
