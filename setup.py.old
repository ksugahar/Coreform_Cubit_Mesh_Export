# Author: Kengo Sugahara <ksugahar@gmail.com>
# Copyright (c) 2024 Kengo Sugahara
# License: BSD 3 clause

from setuptools import setup, find_packages

DESCRIPTION = "Cubit_Mesh_Export: Cubit mesh export to Gmsh format"
NAME = 'Coreform_Cubit_Mesh_Export'
AUTHOR = 'Kengo Sugahara'
AUTHOR_EMAIL = 'ksugahar@gmail.com'
URL = 'https://github.com/ksugahar/Coreform_Cubit_Mesh_Export'
LICENSE = 'BSD 3-Clause'
DOWNLOAD_URL = 'https://github.com/ksugahar/Coreform_Cubit_Mesh_Export'
VERSION =  '0.9.2'
PYTHON_REQUIRES = ">=3.7"

INSTALL_REQUIRES = [
	'numpy >=1.20.3',
	'scipy>=1.6.3',
]

EXTRAS_REQUIRE = {
}

PACKAGES = find_packages()
PY_MODULES = ['cubit_mesh_export']

CLASSIFIERS = [
	'Intended Audience :: Science/Research',
	'License :: OSI Approved :: BSD License',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
	'Programming Language :: Python :: 3.8',
	'Programming Language :: Python :: 3.9',
	'Programming Language :: Python :: 3 :: Only',
	'Topic :: Scientific/Engineering',
	'Topic :: Scientific/Engineering :: Artificial Intelligence',
]

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=open('README.md', 'r', encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      packages=PACKAGES,
      py_modules=PY_MODULES,
      classifiers=CLASSIFIERS,
    )
