#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Neil C Ford'
SITENAME = 'Irreverent and Inappropriate'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

THEME = '/Users/neil/nubenu.pelican/pelican-elegant'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/neilcford'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
DISPLAY_CATEGORIES_ON_SIDEBAR=True
DISPLAY_CATEGORIES_ON_MENU=True
DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_TAGS_INLINE=True
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_NAVBAR_INVERSE=True

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['tag_cloud']

# Static paths
STATIC_PATHS = ['static']
