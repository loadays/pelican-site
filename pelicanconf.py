#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Loadays Crew"
SITENAME = u"LOADays"
SITEURL = 'http://www.loadays.org'
TIMEZONE = 'Europe/Brussels'
DEFAULT_LANG = 'en'

FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
#ARTICLE_URL = '{slug}'
#DEFAULT_CATEGORY = ''

#THEME = 'loadays'
THEME = 'content/theme/loadays'

OUTPUT_PATH = "output/"
#DELETE_OUTPUT_DIRECTORY = True

PAGE_DIR = ('pages/')
ARTICLE_DIR = ('posts/')
CATEGORY_URL = ('category/{slug}.html')
MENUITEMS = (('Home', 'http://loadays.org'),)
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = False
FILES_TO_COPY = (('CNAME', 'CNAME'),)

# Plugins
PLUGINS = [ 'pelican.plugins.sitemap',
            'pelican.plugins.gzip_cache',
            'pelican.plugins.multi_part'
          ]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.6,
        'pages': 0.9
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily'
    }
}

# Metadata
META_DESCRIPTION = 'LOADays - Linux Open Administration Days - 6/4/2013 & 7/4/2013'
META_KEYWORDS = 'loadays , load days , load '
DEFAULT_METADATA = ( ('loadays','load days'),('load','load'),)

