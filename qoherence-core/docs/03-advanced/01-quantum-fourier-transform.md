# Quantum Fourier Transform (Advanced)

## Why it matters
The Quantum Fourier Transform (QFT) is the quantum analogue of the
classical Discrete Fourier Transform, and is a key subroutine in Shor's
algorithm (period finding) and quantum phase estimation.

## Definition
QFT maps a basis state |x> to a superposition:
QFT|x> = (1/sqrt(N)) * sum_y [ e^(2*pi*i*x*y/N) |y> ]
where N = 2^n for n qubits.

## Circuit implementation
QFT is implemented with a combination of Hadamard gates and controlled
phase-rotation gates, applied in a specific pattern across all qubits,
followed by a qubit-order reversal (swap network). It requires O(n^2)
gates for n qubits — exponentially cheaper than the classical FFT's
O(n * 2^n) for equivalent problem size, which is the source of the
quantum advantage in phase-estimation-based algorithms.

## Where qoherence-core fits in
QFT would be implemented as a reusable `Circuit` subroutine (a set of
Gate operations) that qoherence-algorithms' `shor.py` builds on top of for
the period-finding step. It's a good exercise to implement using the
Gate/Circuit primitives once you're comfortable with tensor products.

## Further reading
Nielsen & Chuang, "Quantum Computation and Quantum Information", Ch. 5.
