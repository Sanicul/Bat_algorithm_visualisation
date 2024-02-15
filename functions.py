import numpy as np
import math
def easom(d):
    res = 1
    for i in d:
        res = res * math.cos(i) * math.exp(np.sum(-1.0 * (np.array(d) - math.pi * np.ones(np.array(d).shape)) ** 2))
    if len(d) % 2 == 0:
        res = -1 * res
    return res
