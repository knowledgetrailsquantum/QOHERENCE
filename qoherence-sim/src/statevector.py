import numpy as np

class StateVectorSimulator:
    """Classical state-vector simulator for small quantum circuits."""
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros(2 ** num_qubits, dtype=complex)
        self.state[0] = 1.0

    def apply_gate(self, gate_matrix, qubit_index):
        raise NotImplementedError("Tensor the gate into full Hilbert space and apply")

    def measure(self):
        probs = np.abs(self.state) ** 2
        return np.random.choice(len(self.state), p=probs)
