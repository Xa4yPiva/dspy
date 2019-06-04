import numpy as np


def nextpow2(n):
    return int(np.ceil(np.log2(n)))


def lenpow2(l):
    return int(2 ** nextpow2(l))
