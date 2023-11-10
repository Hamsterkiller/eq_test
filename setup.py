from distutils.core import setup
from Cython.Build import cythonize

setup(name="equillibrium_tester", ext_modules=cythonize("./cython_cpp_structs.pyx"))