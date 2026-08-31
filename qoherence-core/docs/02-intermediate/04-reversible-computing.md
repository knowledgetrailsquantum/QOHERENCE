# Reversible Computing (Intermediate)

## In Plain English

Ordinary computers throw information away constantly. An AND gate takes two bits in and gives one bit out — if the output is 0, you can't tell whether the inputs were (0,0), (0,1), or (1,0). That's fine classically. It's not fine for a quantum computer, because every quantum gate must be reversible (see `01-beginner/03-gates-and-circuits.md`) — you must always be able to undo it and get the input back.

So before you can run an ordinary classical calculation — adding numbers, checking a Boolean condition, evaluating a function — on a quantum computer, you first have to rewrite it in a form that never throws anything away. This rewriting is called **reversible computing**, and it's a genuinely separate skill from writing normal code.

The standard trick is simple: instead of overwriting an answer, write it *next to* the inputs, keeping everything around. Given inputs `a` and `b`, instead of computing `a AND b` and discarding `a` and `b`, you compute a new bit that holds `a AND b`, while `a` and `b` themselves stay untouched. Nothing is lost, so the whole operation can be run backward.

## A Simple Example: The Toffoli Gate

The classical AND gate has a reversible cousin called the **Toffoli gate** (also called CCNOT — "controlled-controlled-NOT"). It takes three bits in: two "control" bits `a` and `b`, and a target bit `c`. It flips `c` only if both `a` and `b` are 1, and leaves `a` and `b` unchanged.

If you start with `c = 0`, the Toffoli gate's output on `c` is exactly `a AND b` — and because `a` and `b` are still sitting there afterward, the whole operation is reversible (running it twice in a row undoes it completely). This one gate, repeated and combined, is enough to build any classical Boolean circuit — AND, OR, NOT, everything — in reversible form.

## Why This Matters Here

This is the hidden first step behind Shor's algorithm's modular exponentiation (`qoherence-algorithms/docs/04-expert/01-implementing-shors-period-finding.md`), and behind turning any classical function into something Grover's algorithm can search over (`qoherence-algorithms/docs/02-intermediate/01-grover-and-shor-explained.md`). Before a quantum computer can use ordinary classical logic as part of a bigger algorithm, that logic has to be translated into reversible gates like Toffoli first.

## A Bit of History

Reversible computing wasn't invented for quantum computers at all. In 1973, physicist Charles Bennett showed that ordinary classical computers *could* be made fully reversible, by keeping extra "scratch" bits around instead of erasing intermediate results — years before anyone thought seriously about qubits. His motivation was actually about physics, not quantum mechanics: erasing a bit of information necessarily releases a tiny bit of heat (a fact known as Landauer's principle, discovered by Rolf Landauer in 1961), so a fully reversible computer would, in principle, use less energy. Quantum computing didn't invent this constraint — it inherited it, for a completely different reason.

## Next
Read `03-advanced/01-quantum-fourier-transform.md` — the next building block, and one that (like everything else) has to be reversible too.

---
**[◀ Circuit Composition](03-circuit-composition.md)**  |  [Index](../../../README.md)  |  **[Quantum Fourier Transform ▶](../03-advanced/01-quantum-fourier-transform.md)**
