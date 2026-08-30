# Benchmarking

## Fidelity Benchmarking (`fidelity_bench.py`)
Measures how close an actual (measured/simulated) quantum state is to the
ideal target state, using the overlap |<ideal|measured>|^2.

## Runtime Benchmarking (`runtime_bench.py`)
Times execution of any function (circuit run, algorithm call) to compare
performance across backends/simulators.

## Noise-Resilience Sweeps (`noise_resilience.py`)
Runs the same circuit across a range of noise levels on a given backend to
characterize how algorithm/circuit performance degrades under real-world
noise conditions.

## Recommended Workflow
1. Run circuit on `qoherence-sim` (ideal, no noise) to get baseline fidelity.
2. Run on `qoherence-hardware` backend to get real-world results.
3. Use `fidelity_bench` to compare, `runtime_bench` to compare speed,
   and `noise_resilience` to study degradation trends.
