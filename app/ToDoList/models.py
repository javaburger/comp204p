from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

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

class ListAddForm(ModelForm):
    class Meta:
        model = List
        fields = ['title']

class ItemAddForm(ModelForm):
    class Meta:
        model = Item
        fields = ['list','content']
        
class ItemEditForm(ModelForm):
    class Meta:
        model = Item
        fields = ['content']
        
class LogInForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']