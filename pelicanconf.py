#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"loadays"
SITENAME = u"loadays"
SITEURL = 'http://loadays.org'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
FEED_RSS = 'feed.xml'
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

THEME = 'loadays'

PAGE_DIR = ('pages/')
ARTICLE_DIR = ('posts/')
CATEGORY_URL = ('category/{slug}.html')
MENUITEMS = (('Home', 'http://loadays.org'),)
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = False
FILES_TO_COPY = (('CNAME', 'CNAME'),)
