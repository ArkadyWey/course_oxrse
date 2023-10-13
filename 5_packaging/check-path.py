import sys

for direc in sys.path:
    print(direc)

# we see the places where python looks for packages
# we need to add our package to */site-packages
# to do this, we first need to make the package, and then install it using pip
# pip is the package manager for python
# it manages local packages and those inside the python package index (pypi)

# we want to be able to do  pip install ./tstools
# this doesn't work because we are missing files we need.. setup.py or pyproject.toml