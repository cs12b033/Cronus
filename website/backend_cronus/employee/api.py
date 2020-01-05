# from django.contrib.auth.views import logout, login
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, REDIRECT_FIELD_NAME
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

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


class EmployeeLoginView(views.APIView):

	def post(self, request):
		user = authenticate(
			username = request.data.get("username"),
			password = request.data.get("password"))
		if user is None:
			return Response({
					'status' : 'Unathorized',
					'message' : 'Username or Password is incorrect'
				}, status=status.HTTP_401_UNAUTHORIZED)
		login(request, user)
		return Response(UserSerializer(user).data)