# Tensor Network Methods (Advanced)

Matrix Product States (MPS) represent a state as a chain of small tensors
connected by "bond" indices of dimension `bond_dim`. Low-entanglement
circuits need small bond dimension (cheap); highly entangled circuits need
bond dimension to grow exponentially too — so tensor networks trade exact
generality for efficiency on a useful subclass of circuits.
