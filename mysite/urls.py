"""mysite URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
               url(r'wheretostay','polls.views.wheretostay',name='wheretostay'),
               url(r'story','polls.views.story',name='story'),
               url(r'specialoffers','polls.views.specialoffers',name='specialoffers'),
               url(r'articles','polls.views.articles',name='articles'),
               url(r'contact','polls.views.contact',name='contact'),
               url(r'thanks','polls.views.thanks',name='thanks'),
               url(r'parisguide','polls.views.parisguide',name='parisguide'),
               url(r'^admin/', include(admin.site.urls)),
               url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
               url(r'^$', 'polls.views.index',name='index'),
               url(r'index', 'polls.views.index',name='index'),
               url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
               url(r'^ckeditor/', include('ckeditor.urls')), 
               url(r'^category/(?P<slug>[^\.]+).html', 'polls.views.view_categories', name='view_categories'), 
               url(r'(?P<slug>[^\.]+).html','polls.views.view_post', name='view_post'),
               
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
