"""Readout error correction using a calibration matrix."""
import numpy as np

def correct_readout(counts, calibration_matrix):
    vec = np.array(list(counts.values()))
    corrected = np.linalg.inv(calibration_matrix) @ vec
    return dict(zip(counts.keys(), corrected))
