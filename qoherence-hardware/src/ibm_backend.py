from .base_backend import Backend

class IBMBackend(Backend):
    """Adapter for IBM Quantum devices."""
    def __init__(self, api_token=None, device="ibmq_qasm_simulator"):
        self.api_token = api_token
        self.device = device

    def submit(self, circuit, shots=1024):
        raise NotImplementedError("Connect to IBM Quantum API here")
