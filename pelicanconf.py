AUTHOR = 'karla muller'
SITENAME = 'karla muller'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images', 'static']

EXTRA_PATH_METADATA = {
    'js/particles.json': {'path': 'particles.json'},
}

THEME = 'neon_theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('GitHub', 'https://github.com/kaylimepy'),
         ('Python.org', 'https://www.python.org/'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True