from .base_backend import Backend

class RigettiBackend(Backend):
    """Adapter for Rigetti QPUs via pyQuil."""
    def __init__(self, lattice="Aspen-M"):
        self.lattice = lattice

    def submit(self, circuit, shots=1024):
        raise NotImplementedError("Connect to Rigetti QCS here")
