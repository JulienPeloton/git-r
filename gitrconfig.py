# Copyright 2017 Julien Peloton
# Licensed under the GPL-3.0 License, see LICENSE file for details.
## Author: j.peloton@sussex.ac.uk
from __future__ import division, absolute_import, print_function

import ConfigParser
import commands
import os

def print_path(func):
    """
    """
    def wrapper(*args, **kwargs):
        """
        """
        print('Repo: ', args[0].path)
        res = func(*args, **kwargs)
        return res
    return wrapper

def checkrc(func):
    """
    """
    def wrapper(*args, **kwargs):
        """
        """
        msg = 'Cannot find {}'.format(args[0].rcfile)
        assert os.path.isfile(args[0].rcfile), AssertionError(msg)

        res = func(*args, **kwargs)

        return res
    return wrapper

class Repository():
    """ """
    def __init__(self, reponame=''):
        """
        Generic class for repositories.

        Note: should contain git commands used by all repo
        """
        ## name of the repo
        self.reponame = reponame

        ## Define useful path
        self.current_location = commands.getoutput('pwd')
        self.HOME = commands.getoutput('ls $HOME')
        self.rcfile = commands.getoutput('ls $HOME/.git-rrc')

        ## Load the parameter(s) in the rc file for this repo
        self.readrc()

    @checkrc
    def readrc(self):
        """
        """
        Config = ConfigParser.ConfigParser()
        Config.read(self.rcfile)

        msg = 'The repo {} is not registered in this file.'.format(
            self.reponame)
        assert self.reponame in Config._sections, AssertionError(msg)

        self.path = Config._sections[self.reponame]['path']

    @print_path
    def run(self, command, options=''):
        """
        """
        walkin = 'cd {};'.format(self.path)
        walkback = 'cd {};'.format(self.current_location)
        com = 'git {} '.format(command)
        for op in options:
            com += op + ' '
        com += ';'

        os.system(walkin + com + walkback)
