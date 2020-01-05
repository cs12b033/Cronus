from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'management'
urlpatterns = [
	# url(r'^login$', views.login, name='login'),
	# url(r'^dashboard$', views.dashboard, name='dashboard'),
	# url(r'^$', views.index, name='index'),
	url(r'^index$|^home$|^$|^login$', views.indexPageView, name='index'),
	# url(r'^index$|^home$', views.indexPageView, name='index'),
	# url(r'^login$', views.index, name='login'),
	url(r'^.*$', views.pageNotFoundView, name='pageNotFound'),
]