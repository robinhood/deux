# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

from sphinx_celery import conf

globals().update(conf.build_config(
    'deux', __file__,
    project='deux',
    canonical_url='http://deux.readthedocs.io',
    webdomain='robinhood.com',
    github_project='robinhood/deux',
    copyright='2016',
    html_logo='images/logo.png',
    html_favicon='images/favicon.ico',
    html_static_path=[],
    include_intersphinx={'python', 'sphinx'},
    django_settings='test_proj.settings',
    apicheck_package='deux',
    apicheck_ignore_modules=[
        'deux.authtoken.tests.*',
        'deux.authtoken.urls',
        'deux.migrations.*',
        'deux.locale.*',
        'deux.oauth2.tests.*',
        'deux.oauth2.urls',
        'deux.tests.*',
        'deux.urls',
        'deux.app_settings',
    ],
    spelling_word_list_filename='spelling/spelling_wordlist.txt',
))

html_theme_path = ['theme']
html_theme = 'deux'

def configcheck_project_settings():
    return set()
