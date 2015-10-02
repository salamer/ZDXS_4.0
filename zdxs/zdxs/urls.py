"""zdxs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import handler404

from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),


    url(r'^$','home.views.index',name='home'),
    url(r'^register/$','home.views.register',name='register'),
    url(r'^login/$','home.views.login',name='login'),

    url(r'^joinshow/$','home.views.join_show',name='join_show'),

    url(r'^career/$','home.views.career',name='career'),
    url(r'^howtojoin/$','home.views.howtojoin',name='howtojoin'),

    url(r'^logout/$','home.views.logout',name='logout'),
    url(r'^data/',include('data.urls')),
    url(r'^blog/',include('blog.urls')),
    url(r'^user/(?P<id>\w+)/$','home.views.person',name='person'),
    url(r'^newman/(?P<id>\w+)/$','home.views.NewManShow',name='newmanshow'),
    url(r'^about/',include('about.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404='home.views.my_404_view'
