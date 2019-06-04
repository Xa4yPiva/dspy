import numpy as np


def fmmod(sig_in, freq_carrier_Hz, sample_rate_Hz, freq_dev_Hz, phase_ini=0):
    dt = 1 / sample_rate_Hz
    time = np.arange(0, len(sig_in)) * dt
    int_sig_in = np.cumsum(sig_in / np.max(np.abs(sig_in))) * dt
    sig_out = np.cos(2 * np.pi * (freq_carrier_Hz * time + int_sig_in * freq_dev_Hz) + phase_ini)

    return sig_out
