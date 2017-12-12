# -*- coding: utf-8 -*-
# Copyright 2017 Julien Peloton
# Licensed under the GPL-3.0 License, see LICENSE file for details.
## Author: j.peloton@sussex.ac.uk
from setuptools import find_packages
from numpy.distutils.core import setup


if __name__ == "__main__":
    ## version
    version = '0.1.3'

    ## Download url
    d_url = 'https://github.com/JulienPeloton/git-r/archive/{}.tar.gz'.format(
        version)

    des = 'Manage git repo from a distant location (within the same machine)'

    setup(
        name='git-r',
        version=version,
        url='https://github.com/JulienPeloton/git-r',
        download_url=d_url,
        license='GPL-3.0',
        author='Julien Peloton',
        author_email='j.peloton@sussex.ac.uk',
        description=des,
        long_description=open('README.rst', 'r').read(),
        platforms='any',
        py_modules=['gitrconfig'],
        scripts=['git-r'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Version Control'
        ]
    )
