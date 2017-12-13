# -*- coding: utf-8 -*-
# Copyright 2017 Julien Peloton
# Licensed under the GPL-3.0 License, see LICENSE file for details.
## Author: j.peloton@sussex.ac.uk
from setuptools import find_packages
from numpy.distutils.core import setup


if __name__ == "__main__":
    ## version
    version = '0.1.4'

    ## Download url
    d_url = 'https://github.com/JulienPeloton/git-r/archive/{}.tar.gz'.format(
        version)

    des = 'Manage git repo from a distant location (within the same machine)'
    long_des = """
    git-r is a python module to manage git repositories from a distant folder.
    We provide an executable ``git-r`` which is a wrapper around the
    traditional ``git`` command and can be called from any location
    to make change to a particular git repository on the machine.
    """

    setup(
        name='git-r',
        version=version,
        url='https://github.com/JulienPeloton/git-r',
        download_url=d_url,
        license='GPL-3.0',
        author='Julien Peloton',
        author_email='j.peloton@sussex.ac.uk',
        description=des,
        long_description=long_des,
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
