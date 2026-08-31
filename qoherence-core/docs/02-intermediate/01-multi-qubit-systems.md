# Multi-Qubit Systems (Intermediate)

## The exponential, precisely
One qubit needs 2 complex amplitudes to describe (α, β). Two qubits need 4: the state is a superposition over |00⟩, |01⟩, |10⟩, |11⟩. n qubits need 2ⁿ amplitudes, because a general multi-qubit state can hold a distinct amplitude for *every possible combination* of basis outcomes, not just n independent single-qubit states glued together. This is the mathematical heart of both quantum computing's promise and its simulation difficulty:

- 10 qubits → 1,024 amplitudes (trivial, fits in a spreadsheet cell's memory footprint many times over)
- 30 qubits → ~1 billion amplitudes (tens of GB — the edge of a beefy workstation)
- 50 qubits → ~1 quadrillion amplitudes (petabytes — requires the world's largest supercomputers, and even then only approximately)
- 300 qubits → more amplitudes than atoms in the observable universe

That last line is not hyperbole — it's arithmetic (2³⁰⁰ ≈ 2×10⁹⁰, versus an estimated ~10⁸⁰ atoms in the observable universe). No classical computer, now or ever (barring new physics), can hold a general 300-qubit state vector in memory. This is precisely the gap `qoherence-sim` is built to explore the edges of, and it is why factoring large numbers with Shor's algorithm (needing thousands of clean logical qubits) remains out of reach today even as small demonstrations run on 20–100 physical qubits.

## Tensor products: how multi-qubit states are built (when unentangled)
If qubit A is in state |ψ_A⟩ and qubit B is in state |ψ_B⟩ *independently* (not entangled), their combined state is the tensor product |ψ_A⟩ ⊗ |ψ_B⟩. Concretely, if |ψ_A⟩ = α|0⟩+β|1⟩ and |ψ_B⟩ = γ|0⟩+δ|1⟩:

  |ψ_A⟩ ⊗ |ψ_B⟩ = αγ|00⟩ + αδ|01⟩ + βγ|10⟩ + βδ|11⟩

Notice this state's four amplitudes are fully determined by just 4 numbers (α, β, γ, δ) — it's "separable." An *entangled* state like the Bell pair (|00⟩+|11⟩)/√2 cannot be factored this way — no choice of α, β, γ, δ reproduces it, because it has zero amplitude on |01⟩ and |10⟩ while having equal, correlated amplitude on |00⟩ and |11⟩. This is the formal signature of entanglement, and it's why entangled states are the "expensive" ones to represent and simulate — you genuinely need all 2ⁿ numbers, not n pairs of numbers.

## Analogy: orchestras vs. soloists
An unentangled multi-qubit system is like n soloists each playing independently — describing the whole performance is just describing each soloist. An entangled system is like an orchestra where the musicians are all listening and responding to each other in a way that can't be decomposed into independent parts — you have to describe the *whole performance* to capture what's happening, even though it's still built from the same instruments.

## Partial measurement and reduced states
You don't have to measure every qubit in a register at once — you can measure a subset. Measuring qubit k of an entangled register partially collapses the whole state: outcomes on the un-measured qubits become correlated with whatever result came out on qubit k, per the entanglement structure. This is the multi-qubit generalization of the Bell-pair correlation from `01-beginner/02-superposition-and-entanglement.md`, and it's the mechanism behind mid-circuit measurement, a technique both IBM and Quantinuum have invested heavily in because it enables error correction *during* a computation rather than only at the end.

## Registers in qoherence-core
```python
from src.circuit import Circuit
from src.gate import H, CNOT

c = Circuit(num_qubits=4)
for q in range(4):
    c.apply(H, q)             # put all 4 qubits in superposition: 16 equally-weighted basis states
c.apply(CNOT, 0, 1)
c.apply(CNOT, 2, 3)
result = c.run()
print(len(result.amplitudes))  # 16 — this is 2**4, growing exponentially with num_qubits
```

## Next
Read `02-linear-algebra-foundations.md` for the matrix mechanics underneath all of this — tensor products, unitary matrices, and inner products — which is the mathematical machinery that makes multi-qubit gate simulation precise rather than hand-wavy.
