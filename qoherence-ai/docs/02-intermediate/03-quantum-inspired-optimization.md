# Quantum-Inspired Optimization (Annealing)

## In Plain English

Picture a hilly landscape where the lowest valley represents the best possible answer to some hard problem — say, the most efficient delivery route for a fleet of trucks. Finding that lowest valley by just trying random spots is slow. Quantum annealing's idea is: shake the *entire* landscape at once, using quantum effects, so a ball placed anywhere can "tunnel" through hills instead of only rolling around them, settling into the lowest valley faster.

**Quantum-inspired annealing** takes that same landscape-search idea and runs it on regular, classical computers, using clever math and sometimes specialized (but non-quantum) chips to mimic the effect. It's like a really good simulation of a snow globe settling, using pure math instead of actual physics — no quantum hardware required, but capturing much of the same "explore broadly, then settle" behavior.

Two real, shipping examples: Fujitsu's Digital Annealer and Toshiba's Simulated Bifurcation Machine — both purpose-built classical chips designed specifically to solve these landscape-search ("optimization") problems fast, without being quantum computers at all.

## Now With the Math

- **Energy landscape** — a way of describing an optimization problem as "find the input that produces the lowest output of some cost function," visualized as a landscape where height = cost, and the goal is the lowest point.
- **Simulated annealing** — the classical, older ancestor: gradually lower a "temperature" parameter so the search moves around wildly at first (escaping bad local dips) and settles down later (refining a good answer). Directly inspired by metallurgical annealing — heating metal, then cooling it slowly so its atoms settle into a low-defect crystal structure.
- **Quantum annealing** — a real quantum hardware approach (D-Wave's systems are the best-known example) using actual quantum tunneling instead of simulated randomness to escape bad local dips in the landscape.
- **Simulated bifurcation** — the mathematical technique behind Toshiba's chip: it models the search as a physical system of oscillators splitting ("bifurcating") into stable states, computed classically but inspired by quantum adiabatic dynamics.

## A Bit of History

Simulated annealing (1983, Kirkpatrick/Gelatt/Vecchi) came decades before quantum computers were practical, but its "landscape and temperature" language became the shared vocabulary the whole optimization field still uses. D-Wave Systems built the first commercial quantum annealer in 2011, explicitly quantum but limited to optimization-style problems rather than general computation. Seeing D-Wave's approach — and its limits — inspired competitors to ask: "can we get most of the benefit classically, with purpose-built chips instead of actual quantum hardware?" Fujitsu's Digital Annealer (announced 2018) and Toshiba's Simulated Bifurcation Machine (research from 2019, commercialized later) are direct answers, and both are used today in real logistics and finance optimization pilots — an early, concrete example of "quantum-inspired" ideas already delivering commercial value even where actual quantum hardware isn't ready yet.

---
**[◀ Quantum Kernels](02-quantum-kernels.md)**  |  [Index](../../../README.md)  |  **[Tensor Networks for ML ▶](04-tensor-networks-for-ml.md)**
