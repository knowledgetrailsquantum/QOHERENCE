"""Fidelity benchmarking across backends."""

def compute_fidelity(ideal_state, measured_state):
    import numpy as np
    return abs(np.vdot(ideal_state, measured_state)) ** 2
