#!/usr/bin/env python
import numpy as np

case = np.array([12, 15, 20])
ds = .01009101846378875865
de = 1/case
er = de/ds
L = 1


@np.vectorize
def find_N(ds, de, er, L):
    n = 1
    d_list = [0]
    while L > np.sum(d_list):
        n += 1
        r = er**(1/(n-1))
        d_list = [ds*r**n for n in range(n)]
    return n


for case, ratio, N in zip(case, er, find_N(ds, de, er, L)):
    print("case:", case,
          "expantion Ratio:", f"{ratio:.06f}",
          "number of cells in last L:", N)
