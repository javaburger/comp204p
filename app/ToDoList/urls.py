from django.conf.urls import url

from . import views
from secure import GITHUB_WEBHOOK_URL

urlpatterns = [   
	url(r'^$', views.index, name='index'),
	url(r'^login/', views.login_view, name='login'),
	url(r'^signup/$', views.signup_view, name='signup'),
	url(r'^signupfail/$', views.signupfail_view, name='signupfail'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^list/(?P<id>\d+)/', views.list_detail, name='list_detail'),
	url(r'^editlist/(?P<id>\d+)/', views.list_form, name='list_form'),
	url(r'^edititem/(?P<id>\d+)/', views.item_form, name='item_form'),
	url(r'^deleteitem/(?P<id>\d+)/', views.delete_item, name='delete_item'),
	url(r'^deletelist/(?P<id>\d+)/', views.delete_list, name='delete_list'),
	url(GITHUB_WEBHOOK_URL, views.github, name='githubWebhook'),
]