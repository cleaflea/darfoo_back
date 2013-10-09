from django.conf.urls import patterns, include, url

from darfoo import views

urlpatterns = patterns('',
    url(r'$', views.weichatindex),

)
