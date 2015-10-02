from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
	tag=models.CharField(max_length=200)

	def __unicode__(self):
		return self.tag

class Category(models.Model):
	category=models.CharField(max_length=200)
	category_image=models.CharField(max_length=200)
	tag=models.ForeignKey(Tag)

	def __unicode__(self):
		return self.category

class Data(models.Model):
	title=models.CharField(max_length=80)
	summury=models.CharField(max_length=300)
	data_time=models.DateTimeField(auto_now_add=True)
	editor=models.ForeignKey(User)
	data=models.TextField()
	counts=models.IntegerField(default=0)

	data_category=models.ForeignKey(Category)

	def __unicode__(self):
		return self.title

	class Meta:
		permissions=(
			("can_write","can write the data"),
			)
	
class DataComment(models.Model):
	editor=models.CharField(max_length=100)
	comment=models.TextField()
	data_time=models.DateTimeField(auto_now_add=True)
	link=models.ForeignKey(Data)

	def __unicode__(self):
		return self.comment
