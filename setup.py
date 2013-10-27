from setuptools import setup, Extension, find_packages

setup(name='pycapsicum',
      version='0.1',
      description="python interface to capsicum security",
      author="Chris Stillson",
      author_email="stillson@gmail.com",
      license="New BSD license",
      ext_modules=[Extension('_pycapsi', ['pycapsicum.c'])],
      py_modules = ['pycapsicum',],
)
