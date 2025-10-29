#!/usr/bin/env python
import pyvista as pv
import os
import numpy as np
import matplotlib.pyplot as plt
folders = [d for d in os.listdir(
    ".") if os.path.isdir(os.path.join(".", d))]
dirs = []
for i in folders:
    dirs.append(int(i))

dirs.sort()
plt.ion()                    # interactive mode ON
fig, ax = plt.subplots(len(dirs)//2, 2)
plt.show()

while True:
    try:
        for n, i in enumerate(dirs):
            root = f"{i}/postProcessing/residuals/0/residuals.dat"
            # 10/postProcessing/residuals/0/residuals.dat
            data = np.loadtxt(root, skiprows=3)
            Time, p, Ux, Uy, k, epsilon = data.T
            # print('case', i , "Time", Time, 'p' , p, 'Ux', Ux, 'Uy', Uy, 'k' , k, 'epsilon'  , epsilon )
            ax[n//2, n % 2].clear()
            ax[n//2, n % 2].set_title(f'{i}')
            ax[n//2, n % 2].semilogy(Time, p, label="p")
            ax[n//2, n % 2].semilogy(Time, Ux, label="Ux")
            ax[n//2, n % 2].semilogy(Time, Uy, label="Uy")
            ax[n//2, n % 2].semilogy(Time, k, label="k")
            ax[n//2, n % 2].semilogy(Time, epsilon, label="epsilon")
            ax[n//2, n % 2].set_xlabel("t")
            ax[n//2, n % 2].grid()
            ax[n//2, n % 2].legend(loc='upper right')
        plt.tight_layout()
        plt.pause(30)       # wait & update

    except KeyboardInterrupt:
        break
