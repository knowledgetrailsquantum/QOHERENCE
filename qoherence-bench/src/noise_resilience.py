"""Noise-resilience comparison across algorithms and backends."""

def run_noise_sweep(circuit, noise_levels, backend):
    results = {}
    for level in noise_levels:
        results[level] = backend.submit(circuit, shots=1024)
    return results
