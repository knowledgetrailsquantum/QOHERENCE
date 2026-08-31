# Variational Quantum Classifiers

## In Plain English

A variational quantum classifier (VQC) is the QML version of a simple classical classifier, like the ones that decide "spam or not spam." Instead of adjustable numbers living in a classical neural network, the adjustable numbers are the rotation angles of a quantum circuit.

Here's the recipe: take a data point (say, a patient's test results), encode it into a quantum circuit's initial state, run the circuit through a series of tunable rotation gates, measure the output, and interpret the measurement as a prediction ("healthy" or "at risk"). Then — just like classical training — compare the prediction to the right answer, and nudge the rotation angles slightly to do better next time. Repeat thousands of times.

The "variational" part just means the circuit has knobs (angles) you vary during training, the same way a classical model has weights you vary during training.

## Now With the Math

- **θ (theta)** — the rotation angle(s) inside the circuit's gates; these are the model's trainable "weights." A circuit might have dozens or hundreds of θ values.
- **Parameterized circuit** — a quantum circuit where some gates are rotations by an angle θ rather than fixed operations, so the same circuit "shape" can behave very differently depending on θ.
- **Cost function** — same idea as classical loss: a number saying how wrong the current θ values are, computed by comparing measured outputs to correct labels across a batch of training examples.
- **Parameter-shift rule** — a quantum-specific trick for estimating how the cost function changes if you nudge one θ slightly, without needing calculus in the classical sense — you literally run the circuit twice, at θ+shift and θ−shift, and the difference tells you the gradient direction. This is analogous to classical gradient descent's "which way is downhill" step, adapted for a device where you can only take measurements, not read internal values directly.

## A Bit of History

VQCs emerged from the broader "variational quantum algorithm" family that also produced VQE (see `qoherence-algorithms/docs/03-advanced/01-vqe-and-qaoa-theory.md`), designed specifically to be useful on the noisy, small quantum computers of the 2018-2025 era — this era is often called NISQ (Noisy Intermediate-Scale Quantum), a term coined by physicist John Preskill in 2018. IBM's Qiskit Machine Learning library and Google's TensorFlow Quantum (2020) both shipped ready-made VQC building blocks, making this one of the most experimented-with QML techniques by students and researchers, precisely because it doesn't need a fault-tolerant, error-corrected quantum computer (which doesn't exist yet) — it's designed to tolerate a fair amount of the noise real hardware has today.

```python
# Qiskit-style sketch, illustrative only
from qiskit_machine_learning.algorithms import VQC
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes

feature_map = ZZFeatureMap(feature_dimension=4)
ansatz = RealAmplitudes(num_qubits=4, reps=3)  # the trainable circuit
vqc = VQC(feature_map=feature_map, ansatz=ansatz)
vqc.fit(X_train, y_train)
predictions = vqc.predict(X_test)
```

---
**[◀ Why Quantum Might Help AI](../01-beginner/03-why-quantum-might-help-ai.md)**  |  [Index](../../../README.md)  |  **[Quantum Kernels ▶](02-quantum-kernels.md)**
