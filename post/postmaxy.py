#!/usr/bin/env python
import pyvista as pv
import os
import numpy as np
import matplotlib.pyplot as plt
pen = []
folders = [d for d in os.listdir(
    ".") if os.path.isdir(os.path.join(".", d))]
dirs = []
for i in folders:
    dirs.append(int(i))

dirs.sort()
case = {}
for i in dirs:
    root = f"{i}/postProcessing/streamlinesPoints/"
    num = 0
    for name in os.listdir(root):
        num = max(num, int(name))
    filename = root+str(num)+"/tracks.vtk"

    m = pv.read(filename)
    pts = m.points
    y = pts[:, 1]
    case[f"{i}"] = pts
    ymax = y.max()
    pen.append(ymax)

    print("case:", i, "iteration", num, "pen:", ymax)

pen = np.array(pen)
print(np.abs((pen[:-1] / pen[1:])-1)*100, "%")

fig = plt.figure()
ax = fig.add_subplot()


for i in case:
    x = case[i][:, 0]
    y = case[i][:, 1]
    ax.plot(x, y, label=f'case: {i}')

ax.grid()
ax.legend(loc='upper center', bbox_to_anchor=(.5, 0))
ax.set_aspect('equal', adjustable='box')
plt.tight_layout()
plt.show()
