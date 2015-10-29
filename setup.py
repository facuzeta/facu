import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "facu",
    version = "0.0.1",
    author = "facu",
    author_email = "fcarrillo@dc.uba.ar",
    description = ("always the same imports"),
    license = "BSD",
    keywords = "",
    url = "http://liaa.dc.uba.ar",
    packages=['facu'],
    install_requires=['numpy','scipy','matplotlib','pandas','pymongo','gensim','multiprocessing'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
