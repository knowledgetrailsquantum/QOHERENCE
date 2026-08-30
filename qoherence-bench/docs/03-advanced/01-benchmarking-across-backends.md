# Benchmarking Across Backends (Advanced)

Fair comparison across qoherence-hardware backends requires controlling
for: shot count, native gate set differences (after transpilation), and
queue-time variance. Always benchmark the same logical circuit, and report
both raw and transpiled circuit depth alongside fidelity numbers.
