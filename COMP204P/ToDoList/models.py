from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length = 140)
	id = models.AutoField(primary_key=True)
	def __str__(self):
		return "%s by %s" % (self.title, self.user.username)

class Item(models.Model):
	list = models.ForeignKey(List)
	content = models.CharField(max_length = 140)
	id = models.AutoField(primary_key=True)
	def __str__(self):
		return "%s in %s by %s" % (self.content, self.list.title, self.list.user.username)