from django.conf.urls import patterns, include, url


urlpatterns = [
	url(r'^$','stories.views.index'),
   
]