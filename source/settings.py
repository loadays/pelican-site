#!/usr/bin/env python
# -*- coding: utf-8 -*- #


# Default Website settings
AUTHOR = u"LOADays Crew"
AUTHOR_EMAIL = 'info@loadays.org'
SITENAME = u"LOADays 2013"
SITEURL = 'http://loadays.org'
TIMEZONE = 'Europe/Brussels'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 3
REVERSE_CATEGORY_ORDER = True


# Content information
MD_EXTENSIONS = ['codehilite', 'extra', 'toc', 'fenced_code']
MARKUP = ('md')
DISPLAY_PAGES_ON_MENU=True
#ARTICLE_EXCLUDES = ('pages')
STATIC_PATHS = ['images']
#FILES_TO_COPY = (('extra/favicon.ico', 'favicon.ico'),)


# Statistics
#PIWIK_URL
#PIWIK_SSL_URL
#PIWIK_SITE_ID


# Blogroll
LINKS =  ( ('VanTosh', 'http://www.vantosh.com/?toshaan'),
           ('Trilands', 'http://www.trilands.be/?toshaan'),
           ('Planet Grep', 'http://planet.grep.be/'),
         )


# Social widget
SOCIAL = (
          ('LinkedIn', 'http://be.linkedin.com/in/toshaan'),
          ('@toshywoshy', 'http://twitter.com/toshywoshy'),
          ('GitHub', 'https://github.com/toshywoshy'),
          ('SpeakerDeck', 'http://speakerdeck.com'),
          ('About', 'http://about.me/toshaan')
         )


# Plugins
PLUGINS = [ 'pelican.plugins.gravatar',
            'pelican.plugins.github_activity',
            'pelican.plugins.related_posts',
          ]


# Feeds
FEED_DOMAIN = ''
FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss.xml'
TWITTER_USERNAME = 'loadays'
GITHUB_URL = 'https://github.com/loadays'
GITHUB_ACTIVITY_FEED = ''


# Comments
#DISQUS_SITENAME=


# Metadata
META_DESCRIPTION = 'LOADays - Linux Open Administration Days'
META_KEYWORDS = 'loadays , load days , load , loaddays , linux open administration days'
