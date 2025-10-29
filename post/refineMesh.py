#!/usr/bin/env python
import os
import asyncio
import shutil


# mesh_step = [14, 15, 18, 20]
mesh_step = [12, 13]


async def main():
    procs = []
    for i in mesh_step:
        shutil.copytree("../CFD_Labor_Group1/",
                        f"{i}", dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns('.git'))
        os.environ['yNet'] = str(i * 19)
        os.environ['xNet1'] = str(int(i * 5))
        os.environ['xNet2'] = str(int(i * 1))
        os.environ['xNet3'] = str(int(i * 20))
        p = await asyncio.create_subprocess_exec(f"{i}/Allrun")
        procs.append(p)

    await asyncio.gather(*(p.wait() for p in procs))

asyncio.run(main())
