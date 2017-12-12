# Copyright 2017 Julien Peloton
# Licensed under the GPL-3.0 License, see LICENSE file for details.
## Author: j.peloton@sussex.ac.uk
from __future__ import absolute_import, print_function

import ConfigParser
import commands
import os

def print_path(func):
    """
    Wrapper to print the path of the distant repository
    To be used as a decorator.

    Parameters
    ----------
    func: function
        The function for the decorator.

    Returns
    ----------
    wrapper: function
        The wrapped function.

    """
    def wrapper(*args, **kwargs):
        """ The wrapper """
        print('Repo: ', args[0].path)
        res = func(*args, **kwargs)
        return res
    return wrapper

def checkrc(func):
    """
    Check that the .git-rrc exists. Raise an error if not.
    To be used as a decorator.

    Parameters
    ----------
    func: function
        The function for the decorator.

    Returns
    ----------
    wrapper: function
        The wrapped function.

    """
    def wrapper(*args, **kwargs):
        """ The wrapper """
        msg = 'Cannot find {}'.format(args[0].rcfile)
        assert os.path.isfile(args[0].rcfile), AssertionError(msg)
        res = func(*args, **kwargs)
        return res
    return wrapper

class Repository():
    """ Generic class for repository """
    def __init__(self, reponame):
        """
        Contains current path and path to the distant repository.
        Mostly rely on os.system to wrap traditional git commands.

        Parameters
        ----------
        reponame: string
            The name of the distant repo.

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
        Check that the name of the repo is registered in the .git-rrc file.

        """
        Config = ConfigParser.ConfigParser()
        Config.read(self.rcfile)

        msg = 'The repo {} is not registered in this file.'.format(
            self.reponame)
        assert self.reponame in Config._sections, AssertionError(msg)

        self.path = Config._sections[self.reponame]['path']

    @print_path
    def run(self, command, options=['']):
        """
        Routine to execute git command inside the distant repository.

        Parameters
        ----------
        command: string
            Git command to execute.
        options: list of strings, optional
            Other option to git command. Can be a filename (if doing a diff),
            or a branch name (if doing a checkout) for example.

        """
        walkin = 'cd {};'.format(self.path)
        walkback = 'cd {};'.format(self.current_location)
        com = 'git {} '.format(command)
        for op in options:
            com += op + ' '
        com += ';'

        os.system(walkin + com + walkback)
