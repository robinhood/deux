# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

from sphinx_celery import conf

globals().update(conf.build_config(
    'drf_mfa', __file__,
    project='drf_mfa',
    canonical_url='http://drf_mfa.readthedocs.io',
    webdomain='robinhood.com',
    github_project='robinhood/drf-mfa',
    copyright='2016',
    html_static_path=[],
    include_intersphinx={'python', 'sphinx'},
    django_settings='test_proj.settings',
    apicheck_package='drf_mfa',
    apicheck_ignore_modules=[
        'drf_mfa.authtoken.tests.*',
        'drf_mfa.authtoken.urls',
        'drf_mfa.migrations.*',
        'drf_mfa.locale.*',
        'drf_mfa.oauth2.tests.*',
        'drf_mfa.oauth2.urls',
        'drf_mfa.tests.*',
        'drf_mfa.urls',
        'drf_mfa.app_settings',
    ],
    spelling_word_list_filename='spelling/spelling_wordlist.txt',
))

html_theme_path = ['theme']
html_theme = 'drf_mfa'

def configcheck_project_settings():
    return set()
