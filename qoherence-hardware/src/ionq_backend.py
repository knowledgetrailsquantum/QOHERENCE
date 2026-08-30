from .base_backend import Backend

class IonQBackend(Backend):
    """Adapter for IonQ devices."""
    def __init__(self, api_key=None, target="simulator"):
        self.api_key = api_key
        self.target = target

    def submit(self, circuit, shots=1024):
        raise NotImplementedError("Connect to IonQ API here")
