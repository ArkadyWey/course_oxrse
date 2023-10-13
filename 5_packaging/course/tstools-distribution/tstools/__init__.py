from os.path import basename
filename = basename(__file__) # __file__ is this file

print(f"Hello from {filename}") # so __init__.py prints 'hello from __init__.py when run'
                                # that means we'll see this whenever we run any other file in this dir
                                # meaning that this dir is now a package or subpackage (i.e. a collection
                                # of modules)

#print("hello from {}".format(tstools.moments))
#from .moments import * #get_mean_and_var # allows me to view functions in any submodule as being in the top  module
#from .vis import *     #plot_histogram

# We need to add places where we will look for functions:
# In general, can do any of the following...

# import package.subpackage.module ... means we can do package.module instead of package.subpackage.module in a file
# from package.subpackage import module  
# from module import attribute1

# 1.
#import tstools.moments # can do import tstools then do tstools.moments.func(*)

# 2.
#from tstools import moments # can do same as above

# 3.
#from .moments import * # makes it so everything in moments is in tstools

# 4.
#from tstools.moments import * # same as above


# I am going to always stick with the following convention... 
# I will make it so you have to print out everything unless you want to shorten it in 
# the file itself.
import tstools.moments # this basically makes it so you can write tstools.moments.func() ... i.e. it imports moments as a python module
import tstools.vis # this basically makes it so you can write tstools.vis.func()  ... i.e. it import vis as a python module