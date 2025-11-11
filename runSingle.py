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


ds = .0094
i = 14
de = 1/i
er = de/ds
n = find_N(ds, de, er, 1)
ni = find_N(ds, de, er, .2)


os.environ['yNet'] = str(i * 14 + n)
os.environ['NYCore'] = str(i * 14)
os.environ['NXCore'] = str(int(i * .6))
os.environ['xNet1'] = str(i * 5)
os.environ['xNet2'] = str(int(i * .6)+ni*2)
os.environ['xNet3'] = str(i * 19+n)
os.environ['xNet3Core'] = str(i * 19)
os.environ['wallNCell'] = str(n)
os.environ['wallER'] = str(er)
os.environ['wallER_inv'] = str(1/er)
os.environ['wallNiCell'] = str(ni)

os.system("echo $xNet2")
os.system("./Allrun")
