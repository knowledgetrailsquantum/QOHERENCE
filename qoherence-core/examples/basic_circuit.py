from src.qubit import Qubit
from src.circuit import Circuit
from src.gate import H_GATE

q = Qubit()
circuit = Circuit(1).add(H_GATE, 0)
print("Initial:", q)
