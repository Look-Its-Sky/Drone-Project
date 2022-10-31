import cython
from setuptools import setup
from Cython.Build import cythonize

setup(
    name = "main",
    ext_modules = cythonize(["main.py", "jude_speech.py", "jude_codrone.py"]),
)