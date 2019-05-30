import numpy as np
from .units import pow2db, db2pow


def awgn(signal, snr_dB):
    pow_sig_avg = np.mean(np.abs(signal) ** 2)
    pow_noise_avg = pow_sig_avg / db2pow(snr_dB);

    mu = 0
    if (not(all(np.isreal(signal)))):
        sigma = np.sqrt(pow_noise_avg / 2)
        noise = np.random.normal(mu, sigma, len(signal)) + 1j * np.random.normal(mu, sigma, len(signal))
    else:
        sigma = np.sqrt(pow_noise_avg)
        noise = np.random.normal(mu, sigma, len(signal))

    return signal + noise
