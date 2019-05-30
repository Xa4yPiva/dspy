import numpy as np


def mag2db(mag):
    return 20 * np.log10(mag)


def db2mag(db):
    return 10. ** (db/20.)


def pow2db(pow):
    return 10 * np.log10(pow)


def db2pow(db):
    return 10. ** (db/10.)