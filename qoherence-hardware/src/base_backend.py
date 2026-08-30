class Backend:
    """Abstract base class for hardware backend adapters."""
    def submit(self, circuit, shots=1024):
        raise NotImplementedError

    def status(self, job_id):
        raise NotImplementedError
