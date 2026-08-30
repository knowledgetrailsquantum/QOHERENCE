class Circuit:
    """A sequence of gates applied to a register of qubits."""
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.operations = []

    def add(self, gate, qubit_index):
        self.operations.append((gate, qubit_index))
        return self

    def run(self, initial_state):
        state = initial_state
        for gate, _ in self.operations:
            state = gate.apply(state)
        return state
