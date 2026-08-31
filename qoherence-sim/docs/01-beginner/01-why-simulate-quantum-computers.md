# Why Simulate Quantum Computers? (Beginner)

## Simulation as a stepping stone, and as a permanent tool
It might seem strange to *classically* simulate a quantum computer — isn't the whole point that classical computers can't efficiently do what quantum computers do? The resolution: classical simulation is exponentially expensive in general (see `02-intermediate/01-state-vector-limits.md`), but for *small enough* qubit counts (roughly up to 30–50 depending on available memory and the circuit's structure) it's entirely tractable, and extremely useful for:
- **Learning and prototyping**: testing whether an algorithm's logic is correct before spending limited, costly, and queued real-hardware time on it.
- **Debugging**: real hardware only gives you noisy measurement statistics; a simulator can give you exact amplitudes, letting you pinpoint exactly where a circuit's logic diverges from expectation.
- **Noise-model research**: simulating hardware noise deliberately (rather than avoiding it) to study how algorithms degrade under realistic error conditions, informing which mitigation techniques (`qoherence-mitigate`) are worth applying.
- **Benchmarking classical limits**: understanding exactly where classical simulation breaks down is itself how the field identifies genuine "quantum advantage" — a task is only a meaningful quantum advantage claim if classical simulation, including clever approximate methods, genuinely can't keep up (see `qoherence-core/docs/03-advanced/03-complexity-theory.md` on supremacy/advantage claims).

## Two fundamentally different simulation strategies
qoherence-sim implements both approaches found across the industry's own simulation tools (IBM's Qiskit Aer, Google's qsim, Nvidia's cuQuantum):
- **State-vector simulation** (`src/statevector.py`): track the full 2ⁿ-length amplitude vector exactly — general-purpose but exponentially memory-limited (see next doc).
- **Tensor-network simulation** (`src/tensor_network.py`): represent the quantum state more compactly using tensor decompositions, exploiting *limited entanglement* in many real circuits to simulate far more qubits than state-vector methods allow — but only for circuits whose entanglement structure stays manageable (see `03-advanced/01-tensor-network-methods.md`).

## Analogy: a flight simulator for pilots
Classical quantum simulation is much like a flight simulator: genuinely useful for training, debugging procedures, and understanding a system's behavior in controlled, well-understood conditions — but it isn't the real aircraft, and there are regimes (extreme maneuvers, or in the quantum case, high-entanglement large-qubit-count circuits) where the simulator becomes an increasingly imperfect and eventually completely infeasible stand-in for the real thing.

## Why the industry still invests heavily in classical simulators
Even as real hardware improves, better classical simulators remain commercially and scientifically important — IBM, Google, Nvidia (via cuQuantum, aimed at GPU-accelerated quantum simulation), and Microsoft all maintain serious classical quantum simulation tools, partly because the boundary of what's classically simulable is exactly the boundary that defines genuine quantum advantage, and partly because most quantum software development and debugging happens on simulators long before (and often instead of) real hardware, given hardware access costs and queue times.

## Next
Read `02-intermediate/01-state-vector-limits.md` for the precise memory math behind why state-vector simulation caps out where it does.
