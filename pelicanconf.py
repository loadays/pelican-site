#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Loadays Crew"
SITENAME = u"LOADays"
SITEURL = 'http://www.loadays.org'
TIMEZONE = 'Europe/Brussels'
DEFAULT_LANG = 'en'

FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

MD_EXTENSIONS = [ 'codehilite' , 'extra' , 'toc' , 'fenced_code' , 'footnotes' ]
MARKUP = [ 'md' , 'rst' , 'html' ]

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
#          <a href="https://plus.google.com/115345896801995085563" rel="publisher">Google+</a>.
#ARTICLE_URL = '{slug}'
#DEFAULT_CATEGORY = ''

#THEME = 'loadays'
THEME = 'content/theme/loadays'

OUTPUT_PATH = "output/"
DELETE_OUTPUT_DIRECTORY = True

PAGE_DIR = ('pages/')
ARTICLE_DIR = ('posts/')
CATEGORY_URL = ('category/{slug}.html')
MENUITEMS = (('Home', 'http://loadays.org'),)
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = False
FILES_TO_COPY = (('CNAME', 'CNAME'),)
STATIC_PATHS = ["archives", "images"]

# Sponsor section
SPONSORGOLD =   (
                    ('Don Bosco Wilrijk','http://www.donboscowilrijk.be/','/static/images/logo_don_bosco.png'),
                    ('Inuits','http://www.inuits.eu/','/static/images/logo_inuits.png'),
                    ('Nucleus','http://www.nucleus.be/','/static/images/logo_nucleus.png'),
                    ('Combell','http://www.combell.be/','/static/images/logo_combell.png'),
                    ('Open Minds','http://www.openminds.be/','/static/images/logo_openminds.jpg'),
                    ('Kumina','http://www.kumina.nl/','/static/images/logo_kumina.png'),
                    ('Kangaroot','http://www.kangaroot.net/','/static/images/logo_kangaroot.png'),
                    ('Percona','http://www.percona.com/','/static/images/logo_percona.jpg'),
                )
SPONSORSILVER = (
                )
SPONSORBRONZE = (
                    ('VanTosh','http://www.vantosh.com/','/static/images/logo_vantosh.png'),
                    #('IT Partners','','/static/images/logo_itpartners.gif'),
                )

# Social connections
GITHUB_URL = 'https://github.com/loadays/pelican-site/'
GITHUB_POSITION = 'left'

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
