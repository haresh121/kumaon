import setuptools
from setuptools import setup

setup(name='kumaon',
      version='0.0.1',
      zip_safe=False,
      packages=setuptools.find_packages(include=('kumaon.*',)),
      include_package_data=True,
      package_dir={'.': 'kumaon'},
      package_data={},
      scripts=[],
      install_requires=[],
      extras_require={},
      dependency_links=[],
      classifiers=[],
      keywords='',
      )
