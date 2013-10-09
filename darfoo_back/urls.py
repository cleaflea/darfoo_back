from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from darfoo_back import settings
from darfoo_back import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'darfoo_back.views.home', name='home'),
    # url(r'^darfoo_back/', include('darfoo_back.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^depot/', include('darfoo_depot.urls')),
    url(r'^wechat/', include('darfoo.urls')),
    url(r'^md/', include('markcleadown.urls')),
    url(r'^team/', include('darfoo_team.urls')),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
    url(r'^plugins/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PLUGIN_PATH}),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
