# Building a Custom Backend Adapter (Expert)

1. Subclass `Backend`, implement `submit()` translating a Qoherence
   `Circuit` into the provider's native circuit representation.
2. Handle authentication (API tokens) securely — never commit credentials.
3. Implement `status()` for async job polling, and a `result()` method
   returning measurement counts in a normalized format shared across
   backends (so qoherence-bench can compare them apples-to-apples).
4. Add hardware-specific noise characterization hooks for qoherence-mitigate
   to consume (e.g. calibration matrices for readout correction).
