# Multi-Qubit Systems (Intermediate)

## In Plain English

Go back to the two linked spinning coins from `01-beginner/02-superposition-and-entanglement.md`. Now imagine 10 coins, all potentially linked to each other in complicated, tangled ways — not just pairwise, but genuinely all-at-once correlated, so that knowing "what the group is doing" isn't the same as knowing "what each coin is doing" summed up. To fully describe what such a tangled group of coins is doing at any instant, you can't get away with 10 separate descriptions — you need to describe every possible *combination* of outcomes, because the entanglement lives in the relationships between coins, not in any one coin.

This is where quantum computing's famous exponential comes from, and it's worth feeling the size of it rather than just reading the word "exponential." Ten coins have 1,024 possible combined outcomes (heads/tails for each of 10 coins). Thirty coins have over a billion. Fifty coins have over a quadrillion — more combined outcomes than there are grains of sand on every beach on Earth, many times over. Three hundred coins have more possible combined outcomes than there are atoms in the entire observable universe. A classical computer trying to track every one of those combinations, the way it would need to for a fully general tangled system, runs out of room to even *write down* the description long before it runs out of time to compute anything — this is exactly why simulating a large, deeply entangled quantum system is so punishingly hard for ordinary computers (see `qoherence-sim`), and exactly why a real quantum computer, which doesn't need to write the description down at all — it just *is* that system — has a shot at doing things no classical machine ever could.

Not every group of qubits is this tangled, though, and that distinction matters. If your 10 coins are all spinning completely independently of each other — no linking at all — then you genuinely *can* describe them cheaply: just describe each coin on its own, 10 short descriptions instead of one impossibly long one. It's only when entanglement enters the picture that the "must describe every combination together" requirement kicks in. This is the precise, correct version of the popular but slightly-too-strong claim that "quantum computers get their power from entanglement" — it's more accurate to say entanglement is what makes a quantum system *expensive to fake classically*, which is a necessary ingredient for quantum advantage, though not by itself a sufficient one.

## Now With the Math

**The exponential, precisely.** One qubit needs 2 amplitudes (`α`, `β`). Two qubits need 4 (one for each of `|00⟩, |01⟩, |10⟩, |11⟩`). In general, `n` qubits need `2ⁿ` amplitudes — the superscript `n` here means "2 multiplied by itself n times," and it's why the growth is called exponential rather than merely "a lot": each additional qubit *doubles* the amount of bookkeeping required, rather than just adding a fixed amount.

| Qubits (n) | Amplitudes (2ⁿ) | Rough size |
|---|---|---|
| 10 | 1,024 | trivial |
| 30 | ~1.07 billion | tens of GB |
| 50 | ~1.13 quadrillion | petabytes |
| 300 | ~2×10⁹⁰ | more than atoms in the observable universe |

**The tensor product, `⊗` — how independent (unentangled) states combine.** If qubit A is in state `|ψ_A⟩ = α|0⟩+β|1⟩` and qubit B is in state `|ψ_B⟩ = γ|0⟩+δ|1⟩`, and they are *not* entangled with each other, their combined state is written `|ψ_A⟩ ⊗ |ψ_B⟩` (the `⊗` symbol, called "tensor product," just means "combine these two independent things into one joint description"). Multiplying it out:

  `|ψ_A⟩ ⊗ |ψ_B⟩ = αγ|00⟩ + αδ|01⟩ + βγ|10⟩ + βδ|11⟩`

Notice this four-amplitude combined state is entirely built from just 4 starting numbers (`α, β, γ, δ`) — cheap, exactly as the "describe each coin separately" plain-English argument promised.

**What makes a state entangled, in symbols.** The Bell pair `(|00⟩+|11⟩)/√2` from `01-beginner/02-superposition-and-entanglement.md` has zero amplitude on `|01⟩` and `|10⟩`. Try to find any `α, β, γ, δ` whose tensor product reproduces that — you can't; there's no way to make both cross-terms `αδ` and `βγ` vanish while `αγ` and `βδ` stay equal and nonzero. A state that *cannot* be written as a tensor product of smaller pieces is, by definition, entangled. This inability to factor is the exact mathematical fingerprint of the "can't describe them separately" idea from the plain-English section above.

**Partial measurement.** You can measure just some of the qubits in a register, not all at once. Doing so partially collapses the whole joint state: whatever wasn't measured becomes correlated with the result that *was* measured, according to the entanglement structure — the multi-qubit generalization of "measure one half of a Bell pair and the other half's outcome becomes fixed too."

## In code
```python
from src.circuit import Circuit
from src.gate import H, CNOT

c = Circuit(num_qubits=4)
for q in range(4):
    c.apply(H, q)             # spin all 4 qubits independently: 16 equally-weighted outcomes
c.apply(CNOT, 0, 1)
c.apply(CNOT, 2, 3)
result = c.run()
print(len(result.amplitudes))  # 16 -- this is 2**4, growing exponentially with num_qubits
```

## Next
Read `02-linear-algebra-foundations.md` for the matrix mechanics underneath all of this.

## A Bit of History
Richard Feynman is usually credited with the spark that started it all: in a now-famous 1981 keynote at MIT titled "Simulating Physics with Computers," he pointed out that simulating quantum systems on classical computers seemed to require exponentially growing resources, and asked, half rhetorically, whether nature itself might be doing something computers couldn't efficiently copy. "Nature isn't classical, dammit," he told the room, "and if you want to make a simulation of nature, you'd better make it quantum mechanical." That offhand challenge is widely seen as the moment quantum computing became a field people worked on, rather than a curiosity.

---
**[◀ Gates and Circuits](../01-beginner/03-gates-and-circuits.md)**  |  [Index](../../../README.md)  |  **[Linear Algebra Foundations ▶](02-linear-algebra-foundations.md)**
