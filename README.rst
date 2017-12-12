=============================
git-r
=============================

.. contents:: **Table of Contents**

What is git-r?
===============
git-r is a python module to manage git repositories from a another folder.


Requirements
===============

No special dependencies. Work for both python2.7 and python 3.X

Installation
===============

The best is to use pip

::

    pip install git-r

Make sure that the executable is in your path.

Quick examples
===============

The general usage is very simple

::

    git-r <repo_name> <command> [<options>]

Note that ``command`` can be any git commands.

Say now I have a repo at `/some/path/repo`. First, you need to create a .git-rrc file in
your `$HOME` and register `repo` (see the example provided).

**Example 1: Pull**

Imagine I am working from a folder distant `/some/other/path/workspace` (but still the same machine!)
and I want to pull the latest change from `repo`:

::

    julien:workspace$ git-r repo pull
    Repo: /some/path/repo
    <can ask password>
    Already up-to-date.
    julien:workspace$

**Example 2: Changing branch**

Imagine I am working from a folder distant `/some/other/path/workspace` (but still the same machine!)
and I want to switch from the `master` branch to `mybranch` branch in `repo`:

::

    julien:workspace$ git-r repo checkout mybranch
    Repo: /some/path/repo
    Switched to branch 'mybranch'
    Your branch is up-to-date with 'origin/mybranch'.
    julien:workspace$


Support
===============

.. raw:: html

    <img src="https://github.com/JulienPeloton/git-r/blob/master/erc.jpg" height="200px">
