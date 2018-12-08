import hashlib
import numpy as np
import math


class HllppCounter:
    p = None
    m = None
    M = None

    def __init__(self):
        self.p = 10
        self.m = 2 ** self.p
        self.M = [-math.inf] * self.m

    def add(self, node):
        hash_value = hashlib.md5(str(node).encode())
        hexadecimal = hash_value.hexdigest()
        hash_int = int(hexadecimal, 16)
        bitstring = bin(hash_int)[2:]
        bucket_id = int(bitstring[-self.p:], 2)
        core_bitstring = bitstring[:-self.p]
        self.M[bucket_id] = max(self.M[bucket_id], trailing_zeroes(core_bitstring))

    def size(self):
        Z = 0
        for register in self.M:
            Z += 2 ** -register

        Z = 1 / Z

        alpha = 0.7213 / (1 + 1.079 / self.m)
        estimate = alpha * self.m ** 2 * Z

        # maxZeroes = np.trim_zeros(self.M)
        # meanTrailingZeros = (float(sum(maxZeroes)) / self.m)
        # alpha = 0.7213 / (1 + 1.079 / self.m)
        #
        # estimate = 2 ** meanTrailingZeros * self.m * alpha

        return estimate


def trailing_zeroes(bitstring):
    return len(bitstring) - len(bitstring.rstrip('0'))
