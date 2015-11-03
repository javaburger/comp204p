"""COMP204P URL Configuration

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

from ToDoList import views

urlpatterns = [
    url(r'^login/', views.login_view, name='login'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^signupfail/$', views.signupfail_view, name='signupfail'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^list/(?P<id>\d+)/', views.list_detail, name='list_detail'),
    url(r'^editlist/(?P<id>\d+)/', views.list_form, name='list_form'),
    url(r'^edititem/(?P<id>\d+)/', views.item_form, name='item_form'),
    url(r'^deleteitem/(?P<id>\d+)/', views.delete_item, name='delete_item'),
    url(r'^deletelist/(?P<id>\d+)/', views.delete_list, name='delete_list'),
    url(r'^admin/', include(admin.site.urls)),
]
