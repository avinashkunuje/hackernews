from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$','stories.views.index',name='index'),
   	url(r'^story/$','stories.views.story',name='story'),
   	url(r'^vote/$','stories.views.vote',name='vote'),
   	#url(r'^login/$','django.contrib.auth.views.login',{'template_name':'auth/login.html'},name='login'),
   	#url(r'^logout/$','django.contrib.auth.views.logout',{'next_page':'/'},name='logout'),

]