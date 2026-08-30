# Hardware Backends

## Why an Abstraction Layer?
Different quantum hardware providers expose different APIs, native gate
sets, and connectivity graphs. `base_backend.py` defines a common
`Backend` interface (`submit`, `status`) so algorithm code in
qoherence-algorithms doesn't need to know which provider it's running on.

## Supported Adapters
- **IBMBackend** — connects to IBM Quantum devices/simulators via Qiskit runtime.
- **IonQBackend** — connects to IonQ trapped-ion QPUs.
- **RigettiBackend** — connects to Rigetti superconducting QPUs via pyQuil/QCS.

## Adding a New Backend
1. Subclass `Backend`.
2. Implement `submit(circuit, shots)` to translate a Qoherence `Circuit`
   into the provider's native format and send the job.
2. Implement `status(job_id)` to poll job completion.
3. Register the backend in your app config.

## Noise Considerations
Real hardware has gate errors, decoherence, and readout errors. Pair
hardware execution with `qoherence-mitigate` for error correction/mitigation.
