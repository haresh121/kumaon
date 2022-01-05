import setuptools
from setuptools import setup

# read the contents of your README file
import os

# from pathlib import Path
# os.chdir(Path(__file__).parent.absolute())

setup(name='kumaon',
      version='0.0.1',
      zip_safe=False,
      packages=setuptools.find_namespace_packages(where='./kumaon/*'),
      package_dir={'kumaon': './kumaon/readers', 'kumaon': './kumaon/textutils'},
      package_data={},
      scripts=[],
      install_requires=[],
      extras_require={},
      dependency_links=[],
      classifiers=[],
      keywords='',
      )
