# Quantum Neural Networks

## In Plain English

A quantum neural network (QNN) pushes the VQC idea (`02-intermediate/01-variational-quantum-classifiers.md`) further: instead of one classifier circuit, you stack multiple layers of parameterized gates, similar to how a classical deep neural network stacks multiple layers of neurons. Data flows through layer after layer of rotations and entangling gates, each layer transforming the quantum state a bit further, until a final measurement gives an output.

The analogy to classical deep learning is close on purpose: researchers borrow the "layers, depth, and stacking" mental model directly, then ask which classical deep-learning intuitions (deeper is more expressive, more layers can learn more complex patterns) still hold true in the quantum setting — and which break down (as `03-barren-plateaus.md` covers, deeper quantum circuits often become *harder*, not easier, to train, which is a real and important difference from classical deep nets).

## Now With the Math

- **Layer / block** — one repeated unit of gates (some fixed, some parameterized by θ) applied across all the qubits, analogous to one layer of a classical neural network. QNN "depth" = number of stacked layers.
- **Entangling gates** — gates (like CNOT, see `qoherence-core`) that link qubits together within a layer, playing a role similar to how classical neural-network layers mix information across neurons — without entangling gates, a QNN can't capture correlations between different input features.
- **Expressibility** — a measure of how much of the full range of possible quantum states a given QNN architecture can reach as its θ values vary. Higher expressibility sounds good, but (surprisingly) correlates with the barren-plateau training problem — a genuine trade-off unlike most classical deep-learning intuitions.
- **Readout / measurement layer** — the final step converting the quantum state into a classical number (a prediction), typically by measuring one or more qubits and mapping the result (0 or 1, or an expectation value) to a class label or numeric output.

## A Bit of History

Farhi and Neven's 2018 paper "Classification with Quantum Neural Networks on Near Term Processors" is generally credited as popularizing the specific "QNN" terminology and layered-circuit design pattern used today, building directly on Google's contemporaneous quantum hardware efforts. TensorFlow Quantum, released by Google in 2020, was purpose-built to let ML researchers already fluent in Keras/TensorFlow define and train QNNs with minimal new syntax — an explicit bet that borrowing the classical deep-learning toolkit's *feel* would speed adoption, even though the underlying math (unitary operations on quantum states, rather than arbitrary matrix multiplications) is quite different under the hood.

---
**[◀ Tensor Networks for ML](../02-intermediate/04-tensor-networks-for-ml.md)**  |  [Index](../../../README.md)  |  **[Hybrid Training Loops ▶](02-hybrid-training-loops.md)**
