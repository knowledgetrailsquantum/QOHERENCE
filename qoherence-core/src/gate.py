import numpy as np

class Gate:
    """Base class for quantum gates represented as unitary matrices."""
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def apply(self, state_vector):
        return self.matrix @ state_vector

X_GATE = Gate([[0, 1], [1, 0]])
H_GATE = Gate([[1, 1], [1, -1]]) / np.sqrt(2)
