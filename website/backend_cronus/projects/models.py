from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Project(models.Model):
	"""docstring for Project"""
	# def __init__(self, arg):
	# 	super(Project, self).__init__()
	# 	self.arg = arg
	
	projectId = models.CharField("Project ID", max_length = 10, validators=[RegexValidator(regex='^[a-zA-Z0-9]+$', message='Invalid projectId', code='nomatch')])
	projectName = models.CharField(max_length=100)
	jobs = models.TextField()
