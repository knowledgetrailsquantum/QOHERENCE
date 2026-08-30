# Density Matrices & Mixed States (Advanced)

## Beyond pure states
So far, qubit states have been "pure" — describable by a single state
vector. Real systems interacting with an environment (noise) often end up
in **mixed states** — statistical mixtures of pure states, which a single
vector cannot represent.

## Density matrix formalism
A density matrix rho represents a (possibly mixed) quantum state:
rho = sum_i p_i |psi_i><psi_i|
where p_i are classical probabilities of being in pure state |psi_i>.

- Pure state: rho has rank 1 (rho = |psi><psi|), Tr(rho^2) = 1
- Mixed state: Tr(rho^2) < 1

## Why this matters for noise & error correction
Noise processes (decoherence, gate errors) are naturally described as
operations on density matrices, not state vectors. This is the mathematical
foundation for qoherence-mitigate's error correction and mitigation
techniques — surface codes and ZNE are both about controlling and reversing
the mixed-state effects of noise.

## Partial trace
When you have entangled qubits and only look at one of them, you get a
mixed state described by "tracing out" the other qubit — this is why
individual qubits in an entangled system don't have a well-defined pure
state on their own.

## Extending qoherence-core
A `DensityMatrix` class (analogous to `Qubit`/state-vector) is a natural
advanced extension point for those wanting to model noisy circuits more
precisely than qoherence-sim's ideal state-vector simulator.
