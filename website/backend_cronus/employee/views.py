# Standard libraries
# from django.contrib.auth.views import logout, login
from django.contrib import messages
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
	LogoutView as BaseLogoutView, PasswordChangeView as BasePasswordChangeView,
	PasswordResetDoneView as BasePasswordResetDoneView, PasswordResetConfirmView as BasePasswordResetConfirmView,
)
from django.shortcuts import get_object_or_404, redirect
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View, FormView
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# 3rd party libraries

# Custom libraries

from .utils import (
	 send_activation_email,
	 # send_activation_email, send_reset_password_email, send_forgotten_username_email, send_activation_change_email,
)
from .forms import (
	 LoginForm, RegisterForm,
	 # SignUpForm,
#	 SignInViaUsernameForm, SignInViaEmailForm, SignInViaEmailOrUsernameForm, SignUpForm,
#	 RestorePasswordForm, RestorePasswordViaEmailOrUsernameForm, RemindUsernameForm,
#	 ResendActivationCodeForm, ResendActivationCodeViaEmailForm, ChangeProfileForm, ChangeEmailForm,
)
from .models import Employee, Activation

# Create your views here.

# Codes : E : Employee, A : Authenticated, DC : Don't Care, NA : Not Authenticated, 0 : BEGIN/Start, 1 : END
# BEGIN E A 0 : Only Authenticated Users can access contents within these lines

# END E A 1 

# BEGIN E NA 0 : 

# END E NA 1 

# BEGIN E DC 0:

# END E DC 1

class GuestOnlyView(View):
	def dispatch(self, request, *args, **kwargs):
		# Redirect to the index page if the user already authenticated
		if request.user.is_authenticated:
			return redirect(settings.LOGIN_REDIRECT_URL)

		return super().dispatch(request, *args, **kwargs)

# class SignUpView(GuestOnlyView, FormView):
# 	# template_name = 'employee/sign_up.html'
# 	template_name = 'employee/register.html'
# 	form_class = SignUpForm

# 	# @csrf_exempt
# 	def form_valid(self, form):
# 		request = self.request
# 		user = form.save(commit=False)

# 		if settings.DISABLE_USERNAME:
# 			# Set a temporary username
# 			user.username = get_random_string()
# 		else:
# 			user.username = form.cleaned_data['username']

# 		if settings.ENABLE_USER_ACTIVATION:
# 			user.is_active = False

# 		# Create a user record
# 		user.save()

# 		# Change the username to the "user_ID" form
# 		if settings.DISABLE_USERNAME:
# 			user.username = f'user_{user.id}'
# 			user.save()

# 		if settings.ENABLE_USER_ACTIVATION:
# 			code = get_random_string(50)
# 			act = Activation()
# 			act.code = code
# 			act.user = user
# 			act.save()
# 			if settings.DEBUG:
# 				print("Activation Code for [", user, "] :", code)

# 			send_activation_email(request, user.email, code)

# 			# messages.success(request, _('You are signed up. To activate the account, follow the link sent to the mail.'))
# 		else:
# 			raw_password = form.cleaned_data['password2']
# 			# print(user.email)
# 			user = authenticate(username=user.username, password=raw_password)
# 			if user is not None:
# 				login(request, user)

# 				# messages.success(request, _('You are successfully signed up!'))

# 				return redirect('employee:employee_login')
# 			else:
# 				return redirect('employee:index')

# 		return redirect('employee:index')

class ActivateView(View):
	@staticmethod
	def get(request, code):
		try:
			act = get_object_or_404(Activation, code=code)

			# Activate profile
			user = act.user
			# print(type(user))
			# TODO: Fix type(user) from 'str' to 'django.contrib.auth.models.User'
			# user.is_active = True	
			# user.save()

			# Remove the activation record
			act.delete()

			# messages.success(request, _('You have successfully activated your account!'))

		except:
			# messages.success(request, _('Activation code is Invalid!'))
			print("Activation code : Invalid!")
			# pass
		return redirect('employee:employee_login')

def index(request):
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# ReDirect to login, if authenticated
	# request.user.is_authenticated
	if request.user.is_authenticated:
		return redirect(settings.LOGIN_REDIRECT_URL)
	template = loader.get_template('employee/index.html')
	context = {
		# 'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))
	# return HttpResponse("Employee Space")

# def employee_login(request):
# 	if request.user.is_authenticated:
# 		return redirect(settings.LOGIN_REDIRECT_URL)
# 	template = loader.get_template('employee/login.html')
# 	context = {
# 	# 'latest_question_list': latest_question_list,
# 	}
# 	return HttpResponse(template.render(context, request))
# 	# return HttpResponse("Employee Login Page")

# @csrf_protect
class LoginView(FormView):
	template_name = 'employee/login.html'
	form_class = LoginForm

	def dispatch(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			# messages.add_message(self.request, messages.INFO, "User already logged in")
			return redirect('employee:dashboard')
		else:
			return super().dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		username = self.request.POST['username']
		password = self.request.POST['password']
		# print(username, password)
		user = authenticate(username=username, password=password)
		# print(user, username, password)
		# print(self.request)
		if user is not None:
			messages.success(self.request, 'Login Successful')
			login(self.request, user)
			return redirect('employee:dashboard')
		else:
			messages.error(self.request, 'Login Failed!')
			return redirect('employee:employee_login')


def register(request):
	template = loader.get_template('employee/register.html')
	context = {
	# 'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))
	# return HttpResponse("Employee Register Page")

def pageNotFound(request):
	template = loader.get_template('pageNotFound.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

#@login_required
def dashboard(request):
	template = loader.get_template('employee/dashboard.html')
	context = {
	}
	# print(request)
	if request.user.is_authenticated:
		#messages.success(request, 'Welcome '+request.user.name)
		return HttpResponse(template.render(context, request))
	else:
		messages.error(request, _('Login FAILED!'))
		return redirect('employee:employee_login')

# def logout(request):
def logout(request, *args, **kwargs):
	"""
	TODO: find if this is the best practice
	Info on why this exists: http://code.djangoproject.com/ticket/6941
	Clears out any session data on logout that would otherwise persist
	for any subsequent logins regardless of user_id.
	"""
	try:
		session_keys = request.session.keys()
		for sesskey in session_keys:
			del request.session[sesskey]

		# if len(session_keys) == 1:
		# 	# messages.success(request, _('You have been logged out!'))
		# elif len(session_keys) == 0:
		# 	# messages.warning(request, _('You need to login first!'))
		# else:
		# 	# messages.warning(request, _('This is strange. The session seems to be messed up!'))
	except Exception as e:
		print("Exception : ", str(e))
		# messages.warning(request, _('You need to login first!'))
	return redirect('employee:employee_login')

# @csrf_exempt
# @csrf_protect
# def validateLogin(request, *args, **kwargs):
# 	"""
# 		TODO:
# 			* 
# 	"""
# 	for i in request:
# 		print("##:", i)
# 	username = request.GET['username']
# 	password = request.GET['password']
# 	user = authenticate(username=username, password=password)

# 	if user is not None:
# 		# messages.success(request, _('Welcome back'))
# 		login(request, user)
# 		return redirect('employee:dashboard')
# 	else:
# 		# messages.warning(request, _('Incorrect username/password'))
# 		return redirect('employee:employee_login')

# def register(request, *args, **kwargs):
# 	"""
# 		TODO:
# 			* 
# 	"""
# 	template = loader.get_template('employee/register.html')
# 	context = {
# 	# 'latest_question_list': latest_question_list,
# 	}
# 	return HttpResponse(template.render(context, request))

class RegisterView(GuestOnlyView, FormView):
	template_name = 'employee/register.html'
	form_class = RegisterForm

	def form_valid(self, form):
		request = self.request
		user = form.save(commit=False)

		# Create a user record

		# print(user.username, user.password)
		user.set_password(form.cleaned_data["password"])
		# print("Hashed:", user.password)
		user.save()

		raw_password = form.cleaned_data['password']
		user = authenticate(username=user.username, password=raw_password)
		if user is not None:
			login(request, user)
			messages.success(request, _('You are successfully signed up!'))
			return redirect('employee:employee_login')
		else:
			messages.error(request, _('Error occured at login!'))
			return redirect('employee:employee_login')

