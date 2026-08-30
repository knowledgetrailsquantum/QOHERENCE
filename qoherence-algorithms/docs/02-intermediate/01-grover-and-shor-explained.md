# Grover & Shor, Explained (Intermediate)

## Grover's Search
Given a "black box" oracle function that flags a target item, Grover's
algorithm amplifies the amplitude of the target state through repeated
"inversion about the mean" steps, making it far more likely to be measured.
Requires ~ (pi/4)*sqrt(N) iterations for N items — quadratically faster
than classical brute-force search.

## Shor's Factoring
Factoring N = p*q reduces to finding the period r of f(x) = a^x mod N for
random a. Classically, period-finding is hard; quantum computers use the
Quantum Fourier Transform (see qoherence-core advanced docs) to find r
exponentially faster, then classical math recovers p and q from r.

## Reading the code
`grover.py` computes the optimal iteration count; `shor.py` stubs the
classical pre/post-processing around the (not-yet-implemented) quantum
period-finding core — a good exercise once you've studied QFT.
