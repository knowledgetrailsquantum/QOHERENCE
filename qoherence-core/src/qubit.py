class Qubit:
    """Represents a single qubit state."""
    def __init__(self, alpha=1.0, beta=0.0):
        self.alpha = alpha
        self.beta = beta

    def __repr__(self):
        return f"Qubit(alpha={self.alpha}, beta={self.beta})"
