from django.conf.urls.defaults import *
from django.contrib.sitemaps import FlatPageSitemap

from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'


sitemaps = {
    'flatpages': FlatPageSitemap,
}

urlpatterns = patterns('',
    (r'^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    (r'^admin/', include(admin.site.urls)),
#     (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
