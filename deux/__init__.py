# -*- coding: utf-8 -*-
"""Multifactor Authentication for Django Rest Framework"""
# :copyright: (c) 2016, Robinhood Markets.
#             All rights reserved.
# :license:   BSD (3 Clause), see LICENSE for more details.

from __future__ import absolute_import, unicode_literals

from collections import namedtuple

version_info_t = namedtuple(
    'version_info_t', ('major', 'minor', 'micro', 'releaselevel', 'serial'),
)

VERSION = version_info = version_info_t(1, 2, 0, '', '')

__version__ = '{0.major}.{0.minor}.{0.micro}{0.releaselevel}'.format(VERSION)
__author__ = 'Robinhood Markets'
__contact__ = 'opensource@robinhood.com'
__homepage__ = 'https://github.com/robinhood/deux'
__docformat__ = 'restructuredtext'

# -eof meta-

__all__ = []
