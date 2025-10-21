#!/usr/bin/env python
import pyvista as pv
import os
import numpy as np
pen = []
folders = [d for d in os.listdir(
    ".") if os.path.isdir(os.path.join(".", d))]
dirs = []
for i in folders:
    dirs.append(int(i))

dirs.sort()
for i in dirs:
    root = f"{i}/postProcessing/streamlinesPoints/"
    num = 0
    for name in os.listdir(root):
        num = max(num, int(name))
    filename = root+str(num)+"/tracks.vtk"

    m = pv.read(filename)
    pts = m.points
    y = pts[:, 1]
    ymax = y.max()
    pen.append(ymax)

    print("case:", i, "iteration", num, "pen:", ymax)

pen = np.array(pen)
print(np.abs((pen[:-1] / pen[1:])-1)*100, "%")
