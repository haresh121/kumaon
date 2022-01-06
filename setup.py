import setuptools
from setuptools import setup

setup(name='kumaon',
      version='0.0.1',
      zip_safe=False,
      packages=setuptools.find_packages(),
      include_package_data=True,
      package_dir={"kumaon.*": "kumaon",
                   "kumaon.readers.*": "kumaon/readers", 
                   "kumaon.utils.*": "kumaon/utils"
                   },
      package_data={},
      scripts=[],
      install_requires=[],
      extras_require={},
      dependency_links=[],
      classifiers=[],
      keywords='',
      )
