from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$','stories.views.index'),
   
]