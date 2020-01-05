from django.db import models

# Create your models here.

class Post(models.Model):
	"""docstring for Posts"""
	# def __init__(self, arg):
	# 	super(Posts, self).__init__()
	# 	self.arg = arg
	
	title = models.CharField(max_length = 120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

