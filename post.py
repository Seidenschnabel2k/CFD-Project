import pyvista as pv
import os
import numpy as np
pen = []
for i in [5, 8, 9, 10, 11, 12]:
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

    print("case:", i, "time", num, "pen:", ymax)

pen = np.array(pen)
print(np.abs((pen[0:-2] / pen[1:-1])-1)*100, "%")
