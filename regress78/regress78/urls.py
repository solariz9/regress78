"""regress78 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from filebrowser.sites import site as filebrowser_site
from index.views import IndexView
from blog.views import (
    BlogList,
    BlogTopic,
    LightList,
    LightItem
)
from photo.views import (
    PhotoList,
    PhotoGallery,
)
from django.conf import settings
from django import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(filebrowser_site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^blog/$', BlogList.as_view(), name='blog_list'),
    url(r'^blog/(?P<page>[0-9]+)/$', BlogList.as_view(), name='blog_list'),
    url(r'^blog/topic/([0-9]+)/$', BlogTopic.as_view(), name='blog_topic'),
    url(r'^photo/$', PhotoList.as_view(), name='photo_list'),
    url(r'^photo/gallery/([0-9]+)/$', PhotoGallery.as_view(), name='photo_gallery'),
    url(r'^events/$', LightList.as_view(), {"name": 'event_list',
                                            "topic_type": 1,
                                            "detail_item_uri": "/event/date/"}),
    url(r'^event/date/(?P<id>[0-9]+)/', LightItem.as_view(), {"name": 'event_item',
                                                              "topic_type": 1}),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', views.static.serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
