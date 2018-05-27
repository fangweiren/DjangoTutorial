"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import index, post_detail, archives, category, tag, get_rss
from blog.feeds import AllPostsRssFeed

urlpatterns = [
	url(r'^$', index, name='index-url'),
	url(r'^post/(\d+)/$', post_detail, name='post_detail-url'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', archives, name='archives-url'),
	url(r'^category/(?P<category_id>[0-9]+)/$', category, name='category-url'),
	url(r'^tag/(?P<tag_id>[0-9]+)/$', tag, name='tag-url'),
	url(r'^search/', include('haystack.urls')),
	url(r'^all/rss/$', AllPostsRssFeed(), name='rss-url'),
	url(r'^all/rss/(\d+)/', get_rss),
    url(r'^admin/', admin.site.urls),
    url(r'^markdownx/', include('markdownx.urls')),
]
