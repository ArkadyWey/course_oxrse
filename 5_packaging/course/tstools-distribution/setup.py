from setuptools import setup

setup(name='./tstools',
      version='0.1',
      description='A package to analyse timeseries',
      url='myfancywebsite.com',
      author='Spam Eggs',
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