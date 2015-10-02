from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    
    url(r'^$','blog.views.index',name='blog_index'),
    url(r'^write/$','blog.views.write',name='blog_write'),
    url(r'^post/(?P<id>\d+)/$','blog.views.post',name='blog_post'),
    url(r'^edit/(?P<id>\d+)/$','blog.views.edit',name='blog_edit'),
]
