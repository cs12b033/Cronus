from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'employee'

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	url(r'^index$|^home$|^$', views.index, name='index'),
	# url(r'^login', views.employee_login, name='employee_login'),
	url(r'^login', views.LoginView.as_view(), name='employee_login'),
	# url(r'^login/$', auth_views.login, {'template_name': 'employee/login.html'}),
	url(r'^logout$', views.logout, name='logout'),
	# url(r'^logout$', auth_views.logout),
	# url(r'^register$', views.register, name='register'),
	url(r'^register$', views.RegisterView.as_view(), name='register'),
	# url(r'^sign_up$', views.SignUpView.as_view(), name='sign_up'),
	# url(r'^validateLogin$', views.validateLogin, name='validateLogin'),
	url(r'^activate/<code>/$', views.ActivateView.as_view(), name='activate'),
	url(r'^dashboard$', views.dashboard, name='dashboard'),
	url(r'^.*$', views.pageNotFound, name='pageNotFound'),
]

# url(r'^register', views.register, name='register'),
# url(r'^activate/<code>/', views.ActivateView.as_view(), name='activate'),