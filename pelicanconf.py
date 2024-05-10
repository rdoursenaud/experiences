#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Raphaël Doursenaud'
AUTHOR_EMAIL = 'rdoursenaud@gmail.com'
SITENAME = 'Expériences // Experiments'
SITEDESC = 'Raphaël Doursenaud\'s Web Space'
SITEURL = ''  # Overridden by publishconf.py

PATH = 'content'
STATIC_PATHS = ['images', 'files', 'extra']
ARTICLE_EXCLUDES = STATIC_PATHS
EXTRA_PATH_METADATA = {
    'extra/keybase.txt': {'path': 'keybase.txt'},
    'extra/google4801127235adabeb.html': {'path': 'google4801127235adabeb.html'}
}

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navigation
NAV = (
    ('Blog', 'index'),
    ('CV', 'pages/cv'),
    ('Archives', 'archives'),
    ('À propos', 'pages/about'),
)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/rdoursenaud'),
    ('GitLab', 'https://gitlab.com/rdoursenaud'),
    ('LinkedIn', 'https://www.linkedin.com/in/rdoursenaud'),
    ('X-Twitter', 'https://twitter.com/rdoursenaud'),
)

# Footer
CONTRIB = (
    ('AUR', 'https://aur.archlinux.org/packages/?SeB=m&K=rdoursenaud'),
    ('GitHub', 'https://github.com/rdoursenaud'),
    ('GitLab', 'https://gitlab.com/rdoursenaud'),
    ('Open Hub', 'https://www.openhub.net/accounts/215754?ref=Detailed'),
    ('Python Package Index', 'https://pypi.org/user/rdoursenaud/'),
)

MEMBER = (
    ('April', 'http://www.april.org/adherer'),
    ('EFF', 'https://www.eff.org/join'),
    ('FSF', 'http://www.fsf.org/'),
    ('FSFE', 'https://fellowship.fsfe.org/'),
    ('Internety Society', 'https://www.internetsociety.org/become-a-member/'),
)

LINKS = (
    # ('Association TTS', 'https://tts.rocks/'),
    ('EMA Tech.', 'https://ematech.github.io/'),
    ('GPC.solutions', 'https://gpcsolutions.fr/'),
    ('FAI associatif Stolon', 'https://stolon.fr/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True  # Overridden by publishconf.py

# Plugins
PLUGIN_PATHS = ['../pelican-plugins', '../pelican-materialize']
PLUGINS = ['assets', 'gravatar', 'materialize', 'pandoc_reader', 'sitemap']

# Pandoc options
PANDOC_ARGS = []
PANDOC_EXTENSIONS = []

# Sitemap options
SITEMAP = {'format': 'xml'}

# Theme options
PRIMARY_COLOR = 'Amber'
ACCENT_COLOR = 'Deep Orange'
GOOGLE_PLUS_COMMENTS = False  # Google Plus is defunct!
USER_LOGO_URL = '/images/logo.webp'
USER_AVATAR_URL = '/images/avatar.webp'

# Theme
THEME = "../materialistic-pelican/"
WEBASSETS = True

# Articles
DEFAULT_METADATA = {
    'status': 'draft',
}