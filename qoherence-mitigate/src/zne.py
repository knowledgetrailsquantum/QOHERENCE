"""Zero-Noise Extrapolation (ZNE) error mitigation."""

def zero_noise_extrapolate(results_by_scale_factor):
    scales = sorted(results_by_scale_factor.keys())
    values = [results_by_scale_factor[s] for s in scales]
    # Simple linear extrapolation to zero noise
    slope = (values[-1] - values[0]) / (scales[-1] - scales[0])
    return values[0] - slope * scales[0]
