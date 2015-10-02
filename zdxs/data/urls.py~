from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    
    url(r'^$','data.views.index',name='data_index'),
    url(r'^write/$','data.views.write',name='data_write'),
    url(r'^category/$','data.views.category_search',name='data_category'),
    url(r'^post/(?P<id>\d+)/$','data.views.post',name='data_post'),
    url(r'^edit/(?P<id>\d+)/$','data.views.edit',name='data_edit'),
]
