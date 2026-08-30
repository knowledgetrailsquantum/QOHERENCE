# VQE & QAOA Theory (Advanced)

## VQE
Minimizes <psi(theta)|H|psi(theta)> over parameters theta, where H is a
problem Hamiltonian (e.g. molecular electronic structure) and |psi(theta)>
is prepared by a parameterized circuit (ansatz). A classical optimizer
(gradient descent, COBYLA, etc.) updates theta based on measured energy.

## QAOA
Alternates applying e^(-i*gamma*H_cost) and e^(-i*beta*H_mixer) for p
layers, with (gamma, beta) parameters tuned classically to maximize the
probability of measuring a good solution to the underlying combinatorial
problem (e.g. Max-Cut maps directly onto an Ising-model H_cost).

## Barren plateaus
A key practical challenge: as circuits grow, gradients of the cost function
w.r.t. parameters can vanish exponentially, making optimization difficult.
Active research area — informs ansatz design choices in `vqe.py`/`qaoa.py`.
