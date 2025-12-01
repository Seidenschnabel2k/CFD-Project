#!/usr/bin/env python
import pyvista as pv
import os
import numpy as np
import matplotlib.pyplot as plt
pen = [0]
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

    print("case:", i, "iteration:", num, "max y value:",
          f"{ymax:.06f}", "change:", f"{(ymax/pen[-1] - 1)*100:.06f}", "%")
    pen.append(ymax)

pen = np.array(pen)
# print(np.abs((pen[:-1] / pen[1:])-1)*100, "%")

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot()


for i in case:
    x = case[i][:, 0]
    y = case[i][:, 1]
    ax.plot(x, y, label=str(f"case: {i}"+r" $y_{max}$ :" + f"{max(y):0.6f}"))

ax.grid()
ax.legend(loc='center right', ncol=3, bbox_to_anchor=(1.0, 1.1))
ax.set_aspect('equal', adjustable='box')
plt.tight_layout()
plt.savefig("fig.pdf")
plt.show()
