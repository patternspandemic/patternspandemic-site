#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brad J. Christensen'
SITENAME = 'patternspandemic'
SITEURL = ''
SITESUBTITLE = None
SITESUBURL = ''

# Metadata
DEFAULT_METADATA = {
    'author': AUTHOR,
    'status': 'draft'
}

# Paths
PATH = 'content'
STATIC_PATHS = ['images', 'extras']
SLUG_SUBSTITUTIONS = [(' ', '-')]

# URLs
RELATIVE_URLS = True
ARTICLE_URL = '{date:%Y}/{date:%-m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%-m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DRAFT_URL = 'patterns/{slug}.html'
DRAFT_SAVE_AS = 'patterns/{slug}.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_SAVE_AS = ''  # Prevent generation of year archives
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%-m}/index.html'
DAY_ARCHIVE_SAVE_AS = ''  # Prevent generation of day archives
CATEGORIES_SAVE_AS = ''  # Prevent generation of categories pages
CATEGORY_SAVE_AS = ''  # Prevent generation of category pages
AUTHORS_SAVE_AS = ''  # Prevent generation of authors pages
AUTHOR_SAVE_AS = ''  # Prevent generation of author pages

# Template Business
DIRECT_TEMPLATES = ['index', 'archives', 'tags']
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = 7
DEFAULT_ORPHANS = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Code inclusion
PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}

# Dates, Times, Locales and Lang
TIMEZONE = 'America/Phoenix'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %-d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme and Look
THEME = '../patternspandemic-theme'
TYPOGRIFY = False


# Other Theme specific Stuff, change as needed.

GITHUB_URL = 'https://github.com/patternspandemic/'

# Menu Links
MENUITEMS = [
    ('archives', SITEURL + '/' + ARCHIVES_URL),
    ('tags', SITEURL + '/' + TAGS_URL),
]

# Header Links
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social Links
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Output
OUTPUT_RETENTION = ['.git']
# OUTPUT_PATH = '../patternspandemic.github.io/'
