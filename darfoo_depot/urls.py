
from django.conf.urls.defaults import *
from models import *
from views import *

urlpatterns = patterns('',

    url(r'home/$', home),
    url(r'index/$', index),
    url(r'phone/$', phone),
    (r'darfooplugin/create/$', create_darfooplugin),
    (r'darfooplugin/list/$', list_darfooplugin ),
    (r'darfooplugin/edit/(?P<id>[^/]+)/$', edit_darfooplugin),
    (r'darfooplugin/view/(?P<id>[^/]+)/$', view_darfooplugin),
    (r'darfooplugin/delete/(?P<id>[^/]+)/$', delete_darfooplugin),

    url(r'pluginlist/$', plugin_list),
    url(r'plugindetail/(?P<id>[0-9]+)/$', plugin_detail),

    url(r'customlist/$', custom_list),
    url(r'customdetail/(?P<id>[0-9]+)/$', custom_detail),
    url(r'postcustom/$', postcustom),
    
    url(r'postsettings/$', postsettings),
    url(r'getsettings/$', getsettings),
)
