# analysis2/analysis2.py

import matplotlib.pyplot as plt
import numpy as np

import sys
print(sys.path) # to find package or module, it must be in path 
# at the moment, analysis1 isn't in path and so we can't use tstools package or any of its modules
# could add it manually...
sys.path.append("/home/user/projects/courses/oxrse/oxrse/5_packaging/course/analysis1")

# else add the directory to one of the other directories in sys.path

# These are all bad ideas.. and we should create a package and install it instead!

import tstools


timeseries = np.genfromtxt("./data/hotwire.csv", delimiter=",")
fig, ax = tstools.vis.plot_trajectory_subset(timeseries, 0, 0.25)

ax.set_ylabel("$u_x(t)$ (m/s)", fontsize=16)
ax.set_xlabel("$t$ (s)", fontsize=16)

ax.plot()
plt.show()
