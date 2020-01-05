from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

# Create your models here.
# MVC for Employee Space

class EmployeeUserModelManager(BaseUserManager):
	def create_user(self, iNum, name, designation, tier, grade, experience, isManagement, password=None):#, password1, password2):
		if not iNum or not password:
			raise ValueError('Please provide iNum/Password')
		user_obj = self.model(
				iNum = self.normalize_email(iNum)
			)
		user_obj.set_password(password)

		return user_obj

	# TODO: create staff user, admin, superuser, etc
	# def create_staff():
		# pass

	def create_superuser(self, iNum, password=None):
		print("iNum", iNum)
		print("password", password)
		if not iNum or not password:
			raise ValueError('Please provide iNum/password')
		user_obj = self.model(
				iNum = self.normalize_email(iNum)
			)
		user_obj.set_password(password)
		user_obj.is_superuser = True
		user_obj.is_active = True
		user_obj.is_staff = True

		return user_obj

class Activation(models.Model):
	user = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	code = models.CharField(max_length=50)

class Employee(AbstractBaseUser):
	"""docstring for Employee"""
	# validators=[RegexValidator(regex='^I[0-9]{6}$', message='Incorrect I-Number', code='nomatch')]
	iNum 			= models.CharField(unique=True, max_length = 7, null=False, blank=False, default='None')
	name 			= models.CharField(max_length=100)
	designation 	= models.CharField(max_length=100, null=False, blank=False, default='None')
	tier 			= models.CharField(max_length=2, null=False, blank=False, default='None')
	grade 			= models.CharField(max_length=2, null=False, blank=False, default='None')
	experience 		= models.IntegerField(default=0)
	isManagement 	= models.BooleanField(default=False)
	created 		= models.DateTimeField(auto_now_add=True, null=False, blank=False)
	# password1		= models.CharField(max_length=100, null=False, blank=False, default='None')
	# password2		= models.CharField(max_length=100, null=False, blank=False, default='None')
	
	USERNAME_FIELD = 'iNum'
	REQUIRED_FILEDS = []
	# REQUIRED_FILEDS	= [name, designation, tier, grade, experience, isManagement]#, password1, password2]
	# REQUIRED_FILEDS = [name, isStaffed, designation, experience, isManagement, password]

	objects = EmployeeUserModelManager()

	def __str__(self):
		return

	def get_details(self):
		return



	# name = models.CharField(max_length=100)
	# skills = models.TextField()
	# iNum 			= models.CharField(max_length=100) 

	# def __init__(self, arg):
		# super(Employee, self).__init__()
		# self.arg = arg
	# def __init__(self):
	# 	self.iNum()
	
	
class Profile(models.Model):
	# employee = models.OneToOne(Employee)
	# append extra user
	pass