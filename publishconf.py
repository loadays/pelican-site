#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Loadays Crew"
SITENAME = u"LOADays"
SITEURL = 'http://www.loadays.org'
TIMEZONE = 'Europe/Brussels'
DEFAULT_LANG = 'en'

FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

MD_EXTENSIONS = ['codehilite', 'extra', 'toc', 'fenced_code', 'footnotes']
MARKUP = ['md', 'rst', 'html' ]

THEME = 'content/theme/loadays'

OUTPUT_PATH = "output/"
DELETE_OUTPUT_DIRECTORY = False

PATH= ('content/')
PAGE_PATHS = ['pages/']
ARTICLE_PATHS = ['posts/']
MENUITEMS = (('Home', 'http://loadays.org'),)
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = False
STATIC_PATHS = ["archives", "images" , "slides", "CNAME" ]

# Sponsor section
SPONSORGOLD =   (
                    ('Don Bosco Wilrijk','http://www.donboscowilrijk.be/','/images/logo_don_bosco.png'),
                    ('Inuits','http://www.inuits.eu/','/images/logo_inuits.png'),
#                    ('Proxy','http://www.proxy.nl/','/static/images/logo_proxy.png'),
#                    ('Nucleus','http://www.nucleus.be/','/images/logo_nucleus.png'),
#                    ('Combell','http://www.combell.be/','/images/logo_combell.png'),
#                    ('Openminds','http://www.openminds.be/','/images/logo_openminds.jpg'),
                    ('Trilands','http://www.trilands.be/','/images/logo_trilands.png'),
                    ('Kangaroot','http://www.kangaroot.net/','/images/logo_kangaroot.png'),
                    ('Percona','http://www.percona.com/','/images/logo_percona.jpg'),
                )
SPONSORSILVER = (
                    ('VanTosh','http://www.vantosh.com/','/images/logo_vantosh.png'),
                    ('Skyscrapers','http://skyscrapers.eu/','/images/logo_skyscrapers.png'),
#                    ('O\'Reilly','http://www.oreilly.com/','/images/logo_oreilly.gif'),
#                    ('Red Hat','http://www.redhat.com/','/static/images/logo_redhat.jpg'),
#                    ('SuSE','http://www.suse.com/','/static/images/logo_suse.png'),
                )
SPONSORBRONZE = (
                    ('Oracle','http://www.oracle.com/','/images/logo_oracle.gif'),
#                    ('Symas','http://www.symas.com/','/static/images/logo_symas.png'),
                    ('IT Partners','','/images/logo_itpartners.png'),
#                    ('Open Future','http://www.open-future.be/','/images/logo_openfuture.png'),
#                    ('Unix Solutions','http://www.unix-solutions.be/','/images/logo_unixsolutions.png'),
#                    ('LPI','http://www.lpi.org/','/images/logo_lpi.png'),

                )
#BUTTONS = (
            #('<div style="width:195px; text-align:center;" ><iframe  src="https://www.eventbrite.com/countdown-widget?eid=5872485763" frameborder="0" height="291" width="195" marginheight="0" marginwidth="0" scrolling="no" allowtransparency="true"></iframe><div style="font-family:Helvetica, Arial; font-size:10px; padding:5px 0 5px; margin:2px; width:195px; text-align:center;" ><a style="color:#ddd; text-decoration:none;" target="_blank" href="http://www.eventbrite.com/r/ecount">Online Ticketing</a><span style="color:#ddd;"> for </span><a style="color:#ddd; text-decoration:none;" target="_blank" href="http://centosdojoantwerp2013.eventbrite.com?ref=ecount">CentOS Dojo Antwerp 2013</a> <span style="color:#ddd;">powered by</span> <a style="color:#ddd; text-decoration:none;" target="_blank" href="http://www.eventbrite.com?ref=ecount">Eventbrite</a></div></div>'),
            #('<div style="border=1px solid black; text-align=center;"><a href="https://lpievent.lpice.eu/index.php">LPI Exam at LOADays<br><img src="https://lpievent.lpice.eu/pictures/lpi-tux-3-lowres.jpg" alt="LPI Exam subscription"><br>Write yourself here</a></div>'),
 #         )

# Social connections
# GITHUB_URL = 'https://github.com/loadays/pelican-site/'
# GITHUB_POSITION = 'left'

# Plugins
# PLUGINS = [ 'pelican.plugins.sitemap',
#            'pelican.plugins.gzip_cache',
#            'pelican.plugins.multi_part'
#          ]

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
META_DESCRIPTION = 'LOADays - Linux Open Administration Days - 11/04/2015 & 12/04/2015'
META_KEYWORDS = 'loadays,load days,load,conference,antwerp,linux,open source'
DEFAULT_METADATA = ( ('loadays','load days'),('load','load'),)
