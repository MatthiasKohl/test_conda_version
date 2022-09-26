from setuptools import find_packages

from distutils.core import setup

setup(name='conda_version_pkg',
      version='0.14a',
      description='Conda version test',
      author='Matthias Jouanneaux',
      author_email='mjoux@nvidia.com',
      packages=find_packages(),
     )
