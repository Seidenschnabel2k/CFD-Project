#!/usr/bin/env python
import os
import asyncio
import shutil
import numpy as np


mesh_step = [14, 15, 18, 20]


def find_N(ds, de, er, L):
    n = 1
    d_list = [0]
    while L > np.sum(d_list):
        n += 1
        r = er**(1/(n-1))
        d_list = [ds*r**n for n in range(n)]
    return n


async def main():
    procs = []
    for i in mesh_step:
        shutil.copytree("../CFD_Labor_Group1/",
                        f"{i}", dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns('.git'))
        ds = .0094
        i = 14
        de = 1/i
        er = de/ds
        n = find_N(ds, de, er, 1)
        ni = find_N(ds, de, er, .2)

        os.environ['yNet'] = str(i * 14 + n)
        os.environ['xNet1'] = str(i * 5)
        os.environ['xNet2'] = str(int(i * .6)+ni*2)
        os.environ['xNet3'] = str(i * 20)
        os.environ['wallNCell'] = str(n)
        os.environ['wallER'] = str(er)
        os.environ['wallER_inv'] = str(1/er)

        p = await asyncio.create_subprocess_exec(f"{i}/Allrun")
        procs.append(p)

    await asyncio.gather(*(p.wait() for p in procs))

asyncio.run(main())
