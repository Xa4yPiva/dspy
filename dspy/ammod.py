import numpy as np


def ammod(sig_in, freq_carrier_Hz, sample_rate_Hz, ampl_carrier=0, mod_idx=0.5, phase_ini=0):
    dt = 1 / sample_rate_Hz
    time = np.arange(0, len(sig_in)) * dt
    sig_carrier = np.cos(2 * np.pi * freq_carrier_Hz * time + phase_ini)
    sig_out = (ampl_carrier + mod_idx * sig_in / np.max(sig_in)) * sig_carrier
    return sig_out