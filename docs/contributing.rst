.. _contributing:

==============
 Contributing
==============

Welcome!

This document is fairly extensive and you are not really expected
to study this in detail for small contributions;

    The most important rule is that contributing must be easy
    and that the community is friendly and not nitpicking on details
    such as coding style.

If you're reporting a bug you should read the Reporting bugs section
below to ensure that your bug report contains enough information
to successfully diagnose the issue, and if you're contributing code
you should try to mimic the conventions you see surrounding the code
you are working on, but in the end all patches will be cleaned up by
the person merging the changes so don't worry too much.

.. contents::
    :local:

.. _community-code-of-conduct:

Community Code of Conduct
=========================

The goal is to maintain a diverse community that is pleasant for everyone.
That is why we would greatly appreciate it if everyone contributing to and
interacting with the community also followed this Code of Conduct.

The Code of Conduct covers our behavior as members of the community,
in any forum, mailing list, wiki, website, Internet relay chat (IRC), public
meeting or private correspondence.

The Code of Conduct is heavily based on the `Ubuntu Code of Conduct`_, and
the `Pylons Code of Conduct`_.

.. _`Ubuntu Code of Conduct`: http://www.ubuntu.com/community/conduct
.. _`Pylons Code of Conduct`: http://docs.pylonshq.com/community/conduct.html

Be considerate.
---------------

Your work will be used by other people, and you in turn will depend on the
work of others.  Any decision you take will affect users and colleagues, and
we expect you to take those consequences into account when making decisions.
Even if it's not obvious at the time, our contributions to Deux will impact
the work of others.  For example, changes to code, infrastructure, policy,
documentation and translations during a release may negatively impact
others work.

Be respectful.
--------------

The Deux community and its members treat one another with respect.  Everyone
can make a valuable contribution to Deux.  We may not always agree, but
disagreement is no excuse for poor behavior and poor manners.  We might all
experience some frustration now and then, but we cannot allow that frustration
to turn into a personal attack.  It's important to remember that a community
where people feel uncomfortable or threatened is not a productive one.  We
expect members of the Deux community to be respectful when dealing with
other contributors as well as with people outside the Deux project and with
users of Deux.

Be collaborative.
-----------------

Collaboration is central to Deux and to the larger free software community.
We should always be open to collaboration.  Your work should be done
transparently and patches from Deux should be given back to the community
when they are made, not just when the distribution releases.  If you wish
to work on new code for existing upstream projects, at least keep those
projects informed of your ideas and progress.  It many not be possible to
get consensus from upstream, or even from your colleagues about the correct
implementation for an idea, so don't feel obliged to have that agreement
before you begin, but at least keep the outside world informed of your work,
and publish your work in a way that allows outsiders to test, discuss and
contribute to your efforts.

When you disagree, consult others.
----------------------------------

Disagreements, both political and technical, happen all the time and
the Deux community is no exception.  It is important that we resolve
disagreements and differing views constructively and with the help of the
community and community process.  If you really want to go a different
way, then we encourage you to make a derivative distribution or alternate
set of packages that still build on the work we've done to utilize as common
of a core as possible.

When you are unsure, ask for help.
----------------------------------

Nobody knows everything, and nobody is expected to be perfect.  Asking
questions avoids many problems down the road, and so questions are
encouraged.  Those who are asked questions should be responsive and helpful.
However, when asking a question, care must be taken to do so in an appropriate
forum.

Step down considerately.
------------------------

Developers on every project come and go and Deux is no different.  When you
leave or disengage from the project, in whole or in part, we ask that you do
so in a way that minimizes disruption to the project.  This means you should
tell people you are leaving and take the proper steps to ensure that others
can pick up where you leave off.

.. _reporting-bugs:


Reporting Bugs
==============

.. _vulnsec:

Security
--------

You must never report security related issues, vulnerabilities or bugs
including sensitive information to the bug tracker, or elsewhere in public.
Instead sensitive bugs must be sent by email to ``security@robinhood.com``.

If you'd like to submit the information encrypted our PGP key is::


    -----BEGIN PGP PUBLIC KEY BLOCK-----
    Version: SKS 1.1.5

    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
    HBu2dHUJXU7b845lvTo=
    =JVgV
    -----END PGP PUBLIC KEY BLOCK-----

Other bugs
----------

The best way to report an issue and to ensure a timely response is to use the
issue tracker.

1) **Create a GitHub account.**

You need to `create a GitHub account`_ to be able to create new issues
and participate in the discussion.

.. _`create a GitHub account`: https://github.com/signup/free

2) **Determine if your bug is really a bug.**

You should not file a bug if you are requesting support.

3) **Make sure your bug hasn't already been reported.**

Search through the appropriate Issue tracker.  If a bug like yours was found,
check if you have new information that could be reported to help
the developers fix the bug.

4) **Check if you're using the latest version.**

A bug could be fixed by some other improvements and fixes - it might not have
an existing report in the bug tracker. Make sure you're using the latest
release of Deux, and try the development version to see if the issue is
already fixed and pending release.

5) **Collect information about the bug.**

To have the best chance of having a bug fixed, we need to be able to easily
reproduce the conditions that caused it.  Most of the time this information
will be from a Python traceback message, though some bugs might be in design,
spelling or other errors on the website/docs/code.

    A) If the error is from a Python traceback, include it in the bug report.

    B) We also need to know what platform you're running (Windows, macOS,
       Linux, etc.), the version of your Python interpreter, and the version of
       Deux, and related packages that you were running when the bug occurred.

6) **Submit the bug.**

By default `GitHub`_ will email you to let you know when new comments have
been made on your bug. In the event you've turned this feature off, you
should check back on occasion to ensure you don't miss any questions a
developer trying to fix the bug might ask.

.. _`GitHub`: https://github.com

.. _issue-tracker:

Issue Tracker
-------------

The Deux issue tracker can be found at GitHub:
https://github.com/robinhood/deux

.. _versions:

Versions
========

Version numbers consists of a major version, minor version and a release
number, and conforms to the SemVer versioning spec: http://semver.org.

Stable releases are published at PyPI
while development releases are only available in the GitHub git repository as
tags.  All version tags starts with “v”, so version 0.8.0 is the tag v0.8.0.

.. _git-branches:

Branches
========

Current active version branches:

* master (https://github.com/robinhood/deux/tree/master)

You can see the state of any branch by looking at the Changelog:

    https://github.com/robinhood/deux/blob/master/Changelog

If the branch is in active development the topmost version info should
contain meta-data like:

.. code-block:: restructuredtext

    2.4.0
    ======
    :release-date: TBA
    :status: DEVELOPMENT
    :branch: master

The ``status`` field can be one of:

* ``PLANNING``

    The branch is currently experimental and in the planning stage.

* ``DEVELOPMENT``

    The branch is in active development, but the test suite should
    be passing and the product should be working and possible for users to test.

* ``FROZEN``

    The branch is frozen, and no more features will be accepted.
    When a branch is frozen the focus is on testing the version as much
    as possible before it is released.

``master`` branch
-----------------

The master branch is where development of the next version happens.

Maintenance branches
--------------------

Maintenance branches are named after the version, e.g. the maintenance branch
for the 2.2.x series is named ``2.2``.  Previously these were named
``releaseXX-maint``.

The versions we currently maintain is:

* 1.0

  This is the current series.

Archived branches
-----------------

Archived branches are kept for preserving history only,
and theoretically someone could provide patches for these if they depend
on a series that is no longer officially supported.

An archived version is named ``X.Y-archived``.

Deux does not currently have any archived branches.


Feature branches
----------------

Major new features are worked on in dedicated branches.
There is no strict naming requirement for these branches.

Feature branches are removed once they have been merged into a release branch.

Tags
====

Tags are used exclusively for tagging releases.  A release tag is
named with the format ``vX.Y.Z``, e.g. ``v2.3.1``.
Experimental releases contain an additional identifier ``vX.Y.Z-id``, e.g.
``v3.0.0-rc1``.  Experimental tags may be removed after the official release.

.. _contributing-changes:

Working on Features & Patches
=============================

.. note::

    Contributing to Deux should be as simple as possible,
    so none of these steps should be considered mandatory.

    You can even send in patches by email if that is your preferred
    work method. We won't like you any less, any contribution you make
    is always appreciated!

    However following these steps may make maintainers life easier,
    and may mean that your changes will be accepted sooner.

Forking and setting up the repository
-------------------------------------

First you need to fork the Deux repository, a good introduction to this
is in the GitHub Guide: `Fork a Repo`_.

After you have cloned the repository you should checkout your copy
to a directory on your machine:

.. code-block:: console

    $ git clone git@github.com:username/deux.git

When the repository is cloned enter the directory to set up easy access
to upstream changes:

.. code-block:: console

    $ cd deux
    $ git remote add upstream git://github.com/robinhood/deux.git
    $ git fetch upstream

If you need to pull in new changes from upstream you should
always use the ``--rebase`` option to ``git pull``:

.. code-block:: console

    git pull --rebase upstream master

With this option you don't clutter the history with merging
commit notes. See `Rebasing merge commits in git`_.
If you want to learn more about rebasing see the `Rebase`_
section in the GitHub guides.

If you need to work on a different branch than ``master`` you can
fetch and checkout a remote branch like this::

    git checkout --track -b 3.0-devel origin/3.0-devel

.. _`Fork a Repo`: http://help.github.com/fork-a-repo/
.. _`Rebasing merge commits in git`:
    http://notes.envato.com/developers/rebasing-merge-commits-in-git/
.. _`Rebase`: http://help.github.com/rebase/

.. _contributing-testing:

Running the unit test suite
---------------------------

To run the Deux test suite you need to install a few dependencies.
A complete list of the dependencies needed are located in
:file:`requirements/test.txt`.

If you're working on the development version, then you need to
install the development requirements first:

.. code-block:: console

    $ pip install -U -r requirements/dev.txt

Both the stable and the development version have testing related
dependencies, so install these next:

.. code-block:: console

    $ pip install -U -r requirements/test.txt
    $ pip install -U -r requirements/default.txt

After installing the dependencies required, you can now execute
the test suite by calling:

.. code-block:: console

    $ python setup.py test

This will run all of the test.

.. _contributing-pull-requests:

Creating pull requests
----------------------

When your feature/bugfix is complete you may want to submit
a pull requests so that it can be reviewed by the maintainers.

Creating pull requests is easy, and also let you track the progress
of your contribution.  Read the `Pull Requests`_ section in the GitHub
Guide to learn how this is done.

You can also attach pull requests to existing issues by following
the steps outlined here: http://bit.ly/koJoso

.. _`Pull Requests`: http://help.github.com/send-pull-requests/

.. _contributing-coverage:

Calculating test coverage
~~~~~~~~~~~~~~~~~~~~~~~~~

To calculate test coverage you must first install the :pypi:`coverage` module.

Installing the :pypi:`coverage` module:

.. code-block:: console

    $ pip install -U coverage

Code coverage in HTML:

.. code-block:: console

    $ make cov

The coverage output will then be located at
:file:`cover/index.html`.

.. _contributing-tox:

Running the tests on all supported Python versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is a :pypi:`tox` configuration file in the top directory of the
distribution.

To run the tests for all supported Python versions simply execute:

.. code-block:: console

    $ tox

Use the ``tox -e`` option if you only want to test specific Python versions:

.. code-block:: console

    $ tox -e 2.7

Building the documentation
--------------------------

To build the documentation you need to install the dependencies
listed in :file:`requirements/docs.txt`:

.. code-block:: console

    $ pip install -U -r requirements/docs.txt

After these dependencies are installed you should be able to
build the docs by running:

.. code-block:: console

    $ cd docs
    $ rm -rf _build
    $ make html

Make sure there are no errors or warnings in the build output.
After building succeeds the documentation is available at :file:`_build/html`.

.. _contributing-verify:

Verifying your contribution
---------------------------

To use these tools you need to install a few dependencies.  These dependencies
can be found in :file:`requirements/pkgutils.txt`.

Installing the dependencies:

.. code-block:: console

    $ pip install -U -r requirements/pkgutils.txt

pyflakes & PEP8
~~~~~~~~~~~~~~~

To ensure that your changes conform to PEP8 and to run pyflakes
execute:

.. code-block:: console

    $ make flakecheck

To not return a negative exit code when this command fails use
the ``flakes`` target instead:

.. code-block:: console

    $ make flakes

API reference
~~~~~~~~~~~~~

To make sure that all modules have a corresponding section in the API
reference please execute:

.. code-block:: console

    $ make apicheck
    $ make configcheck

If files are missing you can add them by copying an existing reference file.

If the module is internal it should be part of the internal reference
located in :file:`docs/internals/reference/`.  If the module is public
it should be located in :file:`docs/reference/`.

For example if reference is missing for the module ``deux.awesome``
and this module is considered part of the public API, use the following steps:


Use an existing file as a template:

.. code-block:: console

    $ cd docs/reference/
    $ cp deux.request.rst deux.awesome.rst

Edit the file using your favorite editor:

.. code-block:: console

    $ vim deux.awesome.rst

        # change every occurrence of ``deux.request`` to
        # ``deux.awesome``


Edit the index using your favorite editor:

.. code-block:: console

    $ vim index.rst

        # Add ``deux.awesome`` to the index.


Commit your changes:

.. code-block:: console

    # Add the file to git
    $ git add deux.awesome.rst
    $ git add index.rst
    $ git commit deux.awesome.rst index.rst \
        -m "Adds reference for deux.awesome"

.. _coding-style:

Coding Style
============

You should probably be able to pick up the coding style
from surrounding code, but it is a good idea to be aware of the
following conventions.

* All Python code must follow the `PEP-8`_ guidelines.

`pep8.py`_ is an utility you can use to verify that your code
is following the conventions.

.. _`PEP-8`: http://www.python.org/dev/peps/pep-0008/
.. _`pep8.py`: http://pypi.python.org/pypi/pep8

* Docstrings must follow the `PEP-257`_ conventions, and use the following
  style.

    Do this:

    .. code-block:: python

        def method(self, arg):
            """Short description.

            More details.

            """

    or:

    .. code-block:: python

        def method(self, arg):
            """Short description."""


    but not this:

    .. code-block:: python

        def method(self, arg):
            """
            Short description.
            """

.. _`PEP-257`: http://www.python.org/dev/peps/pep-0257/

* Lines should not exceed 78 columns.

  You can enforce this in :command:`vim` by setting the ``textwidth`` option:

  .. code-block:: vim

        set textwidth=78

  If adhering to this limit makes the code less readable, you have one more
  character to go on, which means 78 is a soft limit, and 79 is the hard
  limit :)

* Import order

    * Python standard library (`import xxx`)
    * Python standard library ('from xxx import`)
    * Third-party packages.
    * Other modules from the current package.

    or in case of code using Django:

    * Python standard library (`import xxx`)
    * Python standard library ('from xxx import`)
    * Third-party packages.
    * Django packages.
    * Other modules from the current package.

    Within these sections the imports should be sorted by module name.

    Example:

    .. code-block:: python

        import threading
        import time

        from collections import deque
        from Queue import Queue, Empty

        from .datastructures import TokenBucket
        from .five import zip_longest, items, range
        from .utils import timeutils

* Wild-card imports must not be used (`from xxx import *`).

* For distributions where Python 2.5 is the oldest support version
  additional rules apply:

    * Absolute imports must be enabled at the top of every module::

        from __future__ import absolute_import

    * If the module uses the :keyword:`with` statement and must be compatible
      with Python 2.5 (deux is not) then it must also enable that::

        from __future__ import with_statement

    * Every future import must be on its own line, as older Python 2.5
      releases did not support importing multiple features on the
      same future import line::

        # Good
        from __future__ import absolute_import
        from __future__ import with_statement

        # Bad
        from __future__ import absolute_import, with_statement

     (Note that this rule does not apply if the package does not include
     support for Python 2.5)


* Note that we use "new-style` relative imports when the distribution
  does not support Python versions below 2.5

    This requires Python 2.5 or later:

    .. code-block:: python

        from . import submodule


.. _feature-with-extras:

Contributing features requiring additional libraries
====================================================

Some features like a new result backend may require additional libraries
that the user must install.

We use setuptools `extra_requires` for this, and all new optional features
that require third-party libraries must be added.

1) Add a new requirements file in `requirements/extras`

    E.g. for a Cassandra backend this would be
    :file:`requirements/extras/cassandra.txt`, and the file looks like this:

    .. code-block:: text

        pycassa

    These are pip requirement files so you can have version specifiers and
    multiple packages are separated by newline.  A more complex example could
    be:

    .. code-block:: text

        # pycassa 2.0 breaks Foo
        pycassa>=1.0,<2.0
        thrift

2) Modify ``setup.py``

    After the requirements file is added you need to add it as an option
    to :file:`setup.py` in the ``extras_require`` section::

        extra['extras_require'] = {
            # ...
            'cassandra': extras('cassandra.txt'),
        }

3) Document the new feature in :file:`docs/includes/installation.txt`

    You must add your feature to the list in the Bundles section
    of :file:`docs/includes/installation.txt`.

    After you've made changes to this file you need to render
    the distro :file:`README` file:

    .. code-block:: console

        $ pip install -U requirements/pkgutils.txt
        $ make readme


That's all that needs to be done, but remember that if your feature
adds additional configuration options then these needs to be documented
in :file:`docs/configuration.rst`.

.. _contact_information:

Contacts
========

This is a list of people that can be contacted for questions
regarding the official git repositories, PyPI packages
Read the Docs pages.

If the issue is not an emergency then it is better
to :ref:`report an issue <reporting-bugs>`.


Committers
----------

Abhishek Fatehpuria
~~~~~~~~~~~~~~~~~~~

:github: https://github.com/abhishek776


Jamshed Vesuna
~~~~~~~~~~~~~~

:github: https://github.com/JamshedVesuna

.. _packages:

Packages
========

``Deux``
---------

:git: https://github.com/robinhood/deux
:CI: http://travis-ci.org/#!/robinhood/deux
:Windows-CI: https://ci.appveyor.com/project/robinhood/deux
:PyPI: http://pypi.python.org/pypi/deux
:docs: http://deux.readthedocs.io

.. _release-procedure:


Release Procedure
=================

Updating the version number
---------------------------

The version number must be updated two places:

    * :file:`deux/__init__.py`
    * :file:`docs/include/introduction.txt`

After you have changed these files you must render
the :file:`README` files.  There is a script to convert Sphinx syntax
to generic reStructured Text syntax, and the make target `readme`
does this for you:

.. code-block:: console

    $ make readme

Now commit the changes:

.. code-block:: console

    $ git commit -a -m "Bumps version to X.Y.Z"

and make a new version tag:

.. code-block:: console

    $ git tag vX.Y.Z
    $ git push --tags

Releasing
---------

Commands to make a new public stable release:

.. code-block:: console

    $ make distcheck  # checks pep8, autodoc index, runs tests and more
    $ make dist  # NOTE: Runs git clean -xdf and removes files not in the repo.
    $ python setup.py sdist upload --sign --identity='Ask Solem'
    $ python setup.py bdist_wheel upload --sign --identity='Ask Solem'

If this is a new release series then you also need to do the
following:

* Go to the Read The Docs management interface at:
    http://readthedocs.org/projects/deux

* Enter "Edit project"

    Change default branch to the branch of this series, e.g. ``2.4``
    for series 2.4.

* Also add the previous version under the "versions" tab.
