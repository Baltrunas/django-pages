from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^tag/(?P<slug>[-_\w]+)/$', views.tag, name='pages_tag'),
]
