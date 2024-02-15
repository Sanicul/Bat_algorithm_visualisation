import numpy as np
import math


def easom(d):
    res = 1
    for i in d:
        res = res * math.cos(i) * math.exp(np.sum(-1.0 * (np.array(d) - math.pi * np.ones(np.array(d).shape)) ** 2))
    if len(d) % 2 == 0:
        res = -1 * res
    return res


def rosenbroke(d):
    res = 0
    for i in range(0, np.shape(d)[0]-2):
        res += 100*(d[i+1]-d[i]**2)+(d[i]-1)**2
    return res

def shubert(d):
    res = 1
    for x in d:
        loc_res = 0
        for i in range(1, 6):
            loc_res += i * np.cos((i + 1) * x + i)
        res = res * loc_res
    return res


def quadratic(d):
    res = 0
    for i in d:
        res = res + i ** 2
    return res
