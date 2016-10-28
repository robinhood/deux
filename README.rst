.. image:: https://deux.readthedocs.io/en/latest/_images/deux_banner.png
   :align: center
   :width: 721
   :height: 250

|build-status| |codecov| |license| |wheel| |pyversion| |pyimp|

:Version: 1.2.0
:Web: https://deux.readthedocs.org/
:Download: https://pypi.python.org/pypi/deux
:Source: https://github.com/robinhood/deux
:Keywords: authentication, two-factor, multifactor

About
=====

Multifactor Authentication provides multifactor authentication integration for
the Django Rest Framework. It integrates with Token Authentication built into
DRF and OAuth2 provided by django-oauth-toolkit_.

What is Multifactor Authentication?
====================================

Multifactor Authentication (MFA) is a security system that requires more than
one method of authentication from independent categories of credentials to
verify the user's identity for a login or other transaction.
(Source: SearchSecurity_)

.. _django-oauth-toolkit: https://django-oauth-toolkit.readthedocs.io/
.. _SearchSecurity: http://searchsecurity.techtarget.com/definition/multifactor-authentication-MFA

.. _installation:

Installation
============

You can install deux either via the Python Package Index (PyPI)
or from source.

Requirements
------------

``deux`` version 1.2.0 runs on Python (2.7, 3.4, 3.5).

Installing with pip
-------------------

To install using `pip`:
::

    $ pip install -U deux

.. _installing-from-source:

Downloading and installing from source
--------------------------------------

Download the latest version of deux from
http://pypi.python.org/pypi/deux

You can install it by doing the following:
::

    $ tar xvfz deux-0.0.0.tar.gz
    $ cd deux-0.0.0
    $ python setup.py build
    # python setup.py install

The last command must be executed as a privileged user if
you are not currently using a virtualenv.

.. _installing-from-git:

Using the development version
-----------------------------

With pip
~~~~~~~~

You can install it by doing the following:
::

    $ pip install https://github.com/robinhood/deux/zipball/master#egg=deux

.. |build-status| image:: https://travis-ci.org/robinhood/deux.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.org/robinhood/deux

.. |license| image:: https://img.shields.io/pypi/l/deux.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/deux.svg
    :alt: Deux can be installed via wheel
    :target: https://pypi.python.org/pypi/deux/

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/deux.svg
    :alt: Supported Python versions.
    :target: https://pypi.python.org/pypi/deux/

.. |pyimp| image:: https://img.shields.io/pypi/implementation/deux.svg
    :alt: Support Python implementations.
    :target: https://pypi.python.org/pypi/deux/

.. |codecov| image:: https://codecov.io/gh/robinhood/deux/branch/master/graph/badge.svg
  :alt: Code Coverage
  :target: https://codecov.io/gh/robinhood/deux

