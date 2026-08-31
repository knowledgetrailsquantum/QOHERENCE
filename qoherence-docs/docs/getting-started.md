# Getting Started

## Recommended path
This repo set is designed to be read and used in a specific order — see the repo root's `LEARNING-PATH.md` for the full tiered reading plan. The short version:

1. Install dependencies for `qoherence-core` (`pip install -r requirements.txt` in that repo).
2. Read `qoherence-core/docs/01-beginner/` in order (what is a qubit, superposition/entanglement, gates/circuits) — this vocabulary is assumed everywhere else in the repo set.
3. Run the example: `python qoherence-core/examples/basic_circuit.py` — this builds and runs a small circuit using the exact concepts from step 2, and is the fastest way to confirm your environment works before going further.
4. From there, follow whichever thread matches your interest: `qoherence-algorithms` for algorithm design, `qoherence-hardware` for real-device engineering, `qoherence-sim` for simulation techniques, `qoherence-mitigate` for noise handling, `qoherence-bench` for rigorous evaluation.

## A minimal working example
```python
from src.circuit import Circuit
from src.gate import H, CNOT

# Build a Bell pair -- the "hello world" of quantum computing
c = Circuit(num_qubits=2)
c.apply(H, 0)
c.apply(CNOT, 0, 1)

result = c.run()
print(result.sample(shots=1000))
# Expect roughly 50% "00" and 50% "11", and (on an ideal simulator) never "01" or "10"
```

If you see anything other than roughly a 50/50 split between "00" and "11" on an ideal simulator backend, something in your circuit construction is wrong — this two-line circuit is the standard sanity check used throughout the quantum computing community (real or simulated) precisely because its expected output is so simple and unambiguous.

## Where to go next depending on your goal
- **"I want to understand quantum computing conceptually"** → finish `qoherence-core/docs` through all four tiers, then read `industry-landscape.md` in this repo for real-world grounding.
- **"I want to design quantum algorithms"** → `qoherence-algorithms/docs`.
- **"I want to understand real quantum hardware"** → `qoherence-hardware/docs`.
- **"I want to understand why quantum computers are noisy and what's done about it"** → `qoherence-mitigate/docs`.
- **"I want to run and compare things rigorously"** → `qoherence-sim/docs` (for simulation) and `qoherence-bench/docs` (for measurement methodology).

## Next
`industry-landscape.md` in this repo ties every technical concept above back to specific companies, products, and public milestones from IBM, Google, Microsoft, IonQ, Quantinuum, Rigetti, Amazon, and others.
