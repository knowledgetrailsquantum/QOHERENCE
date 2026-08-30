from src.grover import grover_search

result = grover_search(oracle=lambda x: x == 5, n_qubits=3)
print(result)
