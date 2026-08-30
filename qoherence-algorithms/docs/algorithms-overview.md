# Algorithms Overview

## Grover's Search (`grover.py`)
Provides quadratic speedup for unstructured search. Given an oracle that
marks a target item among N, Grover's algorithm finds it in O(sqrt(N))
queries instead of O(N) classically, via repeated amplitude amplification.

## Shor's Factoring (`shor.py`)
Factors large integers exponentially faster than the best known classical
algorithms by finding the period of a modular exponentiation function using
the quantum Fourier transform. Threatens RSA-style cryptography at scale.

## Variational Quantum Eigensolver — VQE (`vqe.py`)
A hybrid quantum-classical algorithm for finding the ground-state energy of
a Hamiltonian. A parameterized quantum circuit (ansatz) is optimized
classically to minimize expected energy. Popular for quantum chemistry.

## QAOA (`qaoa.py`)
Quantum Approximate Optimization Algorithm — a hybrid algorithm for
combinatorial optimization problems (e.g. Max-Cut). Alternates between a
cost Hamiltonian and mixer Hamiltonian across `p` layers, tuned classically.

## When to Use What
| Algorithm | Problem Type            | Speedup           |
|-----------|--------------------------|-------------------|
| Grover    | Unstructured search      | Quadratic         |
| Shor      | Integer factoring        | Exponential       |
| VQE       | Ground-state energy      | Heuristic/hybrid  |
| QAOA      | Combinatorial optimization | Heuristic/hybrid |
