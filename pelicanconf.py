#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from pytz import timezone

AUTHOR = 'Brad Christensen'
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
DEFAULT_PAGINATION = 2
# DEFAULT_ORPHANS = 0
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
BUILD_DATETIME = datetime.now(tz=timezone(TIMEZONE))

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme and Look
THEME = '../patternspandemic-theme'
TYPOGRIFY = False

# Output
OUTPUT_RETENTION = ['.git']
# OUTPUT_PATH = '../patternspandemic.github.io/'


# Other Theme specific Stuff, change as needed.

ABOUT = [
    "I'm Brad Christensen, a technical artist and developer who has found "
    "interest in the intersection of interactive agents, flow-based "
    "programming, computer graphics, and animation.",

    "Some of my favorite things are the Delaunay / Voronoi dual graph, the "
    "sport of Ultimate, and classical guitar."
]

# Social Links
GITHUB_URL = 'https://github.com/patternspandemic/'
TWITTER_URL = 'https://twitter.com/pttrnspndmc'
TELEGRAM_URL = 'https://telegram.me/patternspandemic'

SOCIALITEMS = [  # url, class, font-awesome
    (GITHUB_URL, 'github', 'github-alt'),
    (TWITTER_URL, 'twitter', 'twitter'),
    (TELEGRAM_URL, 'telegram', 'paper-plane')
]

# Menu Links
MENUITEMS = [
    ('archives', SITEURL + '/' + ARCHIVES_URL),
    ('tags', SITEURL + '/' + TAGS_URL),
]

# Project Links (name, link, desc, img)
PROJECTS = (('Ultibot', '#', ''),
            ('AssistON', '#', ''),
            ('Flohx', '#', ''))
