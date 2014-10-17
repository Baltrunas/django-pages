# -*- coding: utf-8 -*
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('pages.views',
	url(r'^tag/(?P<slug>[-_\w]+)/$', 'tag', name='pages_tag'),
)
