#!/usr/bin/env python
import os
import asyncio
import shutil
from pathlib import Path


mesh_step = [5, 8, 9, 10, 11, 12]


async def main():
    procs = []
    for i in mesh_step:
        shutil.copytree("../CFD_Labor_Group1/",
                        f"{i}", dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns('.git'))
        os.environ['yNet'] = str(i * 15)
        os.environ['xNet1'] = str(i * 5)
        os.environ['xNet2'] = str(i * 1)
        os.environ['xNet3'] = str(i * 20)
        p = await asyncio.create_subprocess_exec(f"{i}/Allrun")
        procs.append(p)

    await asyncio.gather(*(p.wait() for p in procs))

asyncio.run(main())
