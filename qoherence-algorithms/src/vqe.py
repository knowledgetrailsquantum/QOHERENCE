"""Variational Quantum Eigensolver (VQE) reference implementation."""

def vqe_minimize(hamiltonian, ansatz, optimizer, max_iter=100):
    params = ansatz.init_params()
    for _ in range(max_iter):
        energy = hamiltonian.expectation(ansatz, params)
        params = optimizer.step(params, energy)
    return params
