from django.conf.urls import patterns, include, url

from darfoo_team import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'darfoo_back.views.home', name='home'),
    # url(r'^darfoo_back/', include('darfoo_back.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'cleantha/$', views.cleantha),
)
