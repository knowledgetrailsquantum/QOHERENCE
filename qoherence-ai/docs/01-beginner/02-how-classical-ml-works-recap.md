# How Classical Machine Learning Works (A Quick Recap)

## In Plain English

Before asking "can quantum help AI," it helps to remember what AI is actually doing underneath. Most machine learning is a very structured form of trial and error: you show a model lots of examples (like photos labeled "cat" or "not cat"), the model makes a guess, you tell it how wrong it was, and it nudges its internal settings a tiny bit to be less wrong next time. Repeat millions of times, and the model gets good at the pattern.

Those "internal settings" are just numbers — often billions of them, in a modern neural network. Training is really a giant, extremely high-dimensional search for the setting-combination that makes the fewest mistakes. That search is expensive, which is exactly the kind of problem people wonder if quantum computers could speed up.

## Now With the Math

- **Weights** — the adjustable numbers inside a model. A simple model might have a formula like `y = w1*x1 + w2*x2 + b`, where `w1`, `w2` (the weights) and `b` (a bias, a starting offset) get adjusted during training.
- **Loss function** — a single number measuring "how wrong" the model currently is on its examples. Lower is better. Training is the process of trying to make this number as small as possible.
- **Gradient descent** — the standard way to adjust weights: for each weight, estimate which direction (up or down) would reduce the loss, and take a small step that way. Do this repeatedly. It's like walking downhill in fog by always taking a step in whichever direction feels most downhill from where you're standing right now.
- **Kernel** — a way of measuring how "similar" two pieces of data are, used by some classical models (support vector machines) instead of a full neural network. Quantum kernels (covered in `02-intermediate/02-quantum-kernels.md`) reuse this exact idea with a quantum twist.

## A Bit of History

The gradient-descent idea is genuinely old — mathematically it traces to Cauchy in 1847 — but it only became the engine of modern AI once (a) enough labeled data existed and (b) enough cheap computing power (especially GPUs, originally built for video game graphics) existed to run it billions of times over. The 2012 "AlexNet" result, where a neural network trained on GPUs dramatically beat older approaches at image recognition, is widely seen as the moment classical deep learning went mainstream. That single event is worth remembering throughout this repo: today's AI boom happened not because of a new algorithm, but because existing algorithms met new hardware. Quantum AI is, in part, a bet that the same pattern could repeat — new hardware unlocking algorithms that already existed on paper.

---
**[◀ What Is Quantum AI?](01-what-is-quantum-ai.md)**  |  [Index](../../../README.md)  |  **[Why Quantum Might Help AI ▶](03-why-quantum-might-help-ai.md)**
