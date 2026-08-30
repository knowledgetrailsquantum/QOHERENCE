# Qoherence Architecture

Qoherence is organized into seven repositories:

1. **qoherence-core** - qubit, gate, and circuit abstractions
2. **qoherence-algorithms** - reference algorithm implementations
3. **qoherence-hardware** - backend adapters for real QPUs
4. **qoherence-mitigate** - error correction and mitigation
5. **qoherence-sim** - classical simulation engines
6. **qoherence-bench** - benchmarking harness
7. **qoherence-docs** - this repository

## Data Flow
circuit (core) -> algorithm (algorithms) -> backend/simulator (hardware/sim) -> mitigation (mitigate) -> benchmark (bench)
