from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    
    url(r'^$','about.views.index',name='about_index'),
    url(r'^website/$','about.views.website',name='about_website'),
    
]