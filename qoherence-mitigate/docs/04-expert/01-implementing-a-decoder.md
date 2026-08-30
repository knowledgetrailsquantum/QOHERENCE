# Implementing a Surface Code Decoder (Expert)

To complete `surface_code.py`'s `decode()`:
1. Build a graph where nodes are detected syndrome defects.
2. Weight edges by the probability of a physical error chain connecting
   them (based on hardware error rates).
3. Run minimum-weight perfect matching (e.g. via `networkx` or a dedicated
   library like PyMatching) to infer the most likely correction.
4. Apply the correction to recover the logical qubit state.
