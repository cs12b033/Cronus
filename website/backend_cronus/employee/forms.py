from datetime import timedelta

from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from .models import Employee

# class SignUpForm(UserCreationForm):
	# class Meta:
		# model = CustomUser
		# model = User
		# fields = settings.SIGN_UP_FIELDS

	# email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'))

	# def clean_email(self):
	#	 email = self.cleaned_data['email']

	#	 user = User.objects.filter(email__iexact=email).exists()
	#	 if user:
	#		 raise ValidationError(_('You can not use this email address.'))

	#	 return email

class LoginForm(forms.Form):
	# iNum = forms.CharField()
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	# password = forms.CharField()

	class Meta:
		fields = ['username','password']


class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	# password = forms.CharField()


	class Meta:
		# model = Employee
		model = User
		fields = settings.SIGN_UP_FIELDS