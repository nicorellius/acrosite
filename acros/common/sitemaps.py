from django.contrib.sitemaps import Sitemap, FlatPageSitemap
from django.core.urlresolvers import reverse


from datetime import datetime


class SitePageSitemap(Sitemap):

    priority = 0.6

    def __init__(self, names):
        self.names = names

    def items(self):
        return ['index']

    def changefreq(self, item):
        return 'weekly'

    def lastmod(self, item):
        return datetime.now()

    def location(self, item):
        return reverse(item)


class SiteFlatPageSitemap(FlatPageSitemap):

    changefreq = 'monthly'
    priority = 0.5

    def lastmod(self, item):
        return datetime.now()