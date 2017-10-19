#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Raphaël Doursenaud'
AUTHOR_EMAIL = 'rdoursenaud@gmail.com'
SITENAME = 'Experiences'
SITEDESC = 'Raphaël Doursenaud\'s Web Space'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'files', 'extra']
ARTICLE_EXCLUDES = STATIC_PATHS
EXTRA_PATH_METADATA = {
    'extra/keybase.txt': {'path': 'keybase.txt'},
    'extra/google4801127235adabeb.html': {'path': 'google4801127235adabeb.html'}
}

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/rdoursenaud'),
    ('Google plus', 'https://plus.google.com/+RaphaëlDoursenaudGPCsolutions'),
    ('Twitter', 'https://twitter.com/rdoursenaud'),
    ('LinkedIn', 'https://www.linkedin.com/in/rdoursenaud')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['../pelican-plugins', '../pelican-materialize']
PLUGINS = ['assets', 'gravatar', 'materialize', 'pandoc_reader', 'sitemap']

# Pandoc options
PANDOC_ARGS = []
PANDOC_EXTENSIONS = []

# Sitemap options
SITEMAP = {'format': 'xml'}

# Theme options
PRIMARY_COLOR = 'Blue Grey'
ACCENT_COLOR = 'Indigo'
GOOGLE_PLUS_COMMENTS = True
USER_LOGO_URL = SITEURL + '/images/logo.png'
USER_AVATAR_URL = SITEURL + '/images/avatar.png'

# Theme
THEME = "../materialistic-pelican/"
