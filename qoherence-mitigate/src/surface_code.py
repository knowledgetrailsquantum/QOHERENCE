"""Surface code quantum error correction."""

class SurfaceCode:
    def __init__(self, distance=3):
        self.distance = distance

    def encode(self, logical_qubit):
        raise NotImplementedError("Encode logical qubit into surface code lattice")

    def decode(self, syndrome):
        raise NotImplementedError("Run minimum-weight perfect matching decoder")
