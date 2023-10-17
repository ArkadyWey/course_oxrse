from setuptools import setup

setup(name='tstools',
      version='0.1',
      description='A package to analyse timeseries',
      url='myfancywebsite.com',
      author='Arkady Wey',
      author_email="arkady.wey@maths.ox.ac.uk",
      packages=['tstools'],
      install_requires = ["numpy", "matplotlib", "scipy"],
      license='GPLv3')

# setup.py makes a call to setup function which is part of the setuptools package
# this gives pip some info about the package

# first line means tell pip to tell setuptools to install the dir tstools that's located in the same dir as setup.py
# so setup.py needs to be in the same dir as the package.

# These days people use pyproject.toml instead of  setup.py or with it. 
# if used with it then only need to direct toml to setup.py
# if used withouut it then needs all metadata

# could also use flit, hatchling, PDM... these are just other setup packages. 
# We will focus on setuptools

# install package using python setup.py install (with venv active)
# or 
# python -m pip install . # . is directory where setup.py is found i.e. the dist directory
# or 
# pip install . 
# or 
# pip install -e . # this means install directs to a local package that can be edited  rather than installing a fixed version of the package
# it writes a file <package-name>.egg-link at the installation location rather than copying the actual package there 
# installation location as in site-packages in the venv, found in sys.path