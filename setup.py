from distutils.core import setup
setup(
  name = 'pymbta',
  packages = ['pymbta'], # this must be the same as the name above
  version = '1.1',
  description = 'Simplifying the MBTA API to find bus and train locations.',
  author = 'John Liao',
  author_email = 'john@johnliao.org',
  url = 'https://github.com/johnsliao/pymbta', # use the URL to the github repo
  download_url = 'https://github.com/johnsliao/pymbta/tarball/1.1', # I'll explain this in a second
  keywords = ['mbta', 'pymbta', 'wrapper'], # arbitrary keywords
  classifiers = [],
  install_requires=['requests']
)