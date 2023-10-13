import numpy as np

import tstools

timeseries = np.genfromtxt("./data/brownian.csv", delimiter=",")

# instead of mean, var = tstools.moments.get_mean_and_var(...)
# mean, var = tstools.get_mean_and_var(timeseries)    # with from .moments import * in __init__
mean, var = tstools.moments.get_mean_and_var(timeseries)     # with from . import moments in __init__


# instead of fig, ax = tstools.vis.plot_histogram(...)
#fig, ax = tstools.plot_histogram(timeseries, 4*np.sqrt(float(var))) 
