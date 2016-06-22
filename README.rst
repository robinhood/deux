=====================================================================
 Multifactor Authentication for Django Rest Framework
=====================================================================

:Version: 1.0.0
:Web: http://drf_mfa.readthedocs.org/
:Download: http://pypi.python.org/pypi/drf_mfa
:Source: http://github.com/robinhood/drf-mfa
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

You can install drf_mfa either via the Python Package Index (PyPI)
or from source.

Requirements
------------

``drf_mfa`` version 1.0.0 runs on Python (2.7, 3.4, 3.5).

Installing with pip
-------------------

To install using `pip`:
::

    $ pip install -U drf_mfa

.. _installing-from-source:

Downloading and installing from source
--------------------------------------

Download the latest version of drf_mfa from
http://pypi.python.org/pypi/drf_mfa

You can install it by doing the following:
::

    $ tar xvfz drf_mfa-0.0.0.tar.gz
    $ cd drf_mfa-0.0.0
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

    $ pip install https://github.com/robinhood/drf-mfa/zipball/master#egg=drf_mfa

