#!/usr/bin/env python
import os
import numpy as np


def find_N(ds, de, er, L):
    n = 1
    d_list = [0]
    while L > np.sum(d_list):
        n += 1
        r = er**(1/(n-1))
        d_list = [ds*r**n for n in range(n)]
    return n


ds = .00728172785668116513
i = 15
de = 1/i
er = de/ds
n = find_N(ds, de, er, 1)


os.environ['yNet'] = str(i * 15 + n)
os.environ['xNet1'] = str(i * 5)
os.environ['xNet2'] = str(i * 1)
os.environ['xNet3'] = str(i * 20)
os.environ['wallNCell'] = str(n)
os.environ['wallER'] = str(er)

os.system("./Allrun")
