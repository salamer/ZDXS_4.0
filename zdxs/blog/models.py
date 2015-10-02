from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
	title=models.CharField(max_length=80)
	summury=models.CharField(max_length=300)
	data_time=models.DateTimeField(auto_now_add=True)
	editor=models.ForeignKey(User)
	body=models.TextField()
	counts=models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.title

	class Meta:
		permissions=(
			("can_write","can write the blog"),
			("can_read","can read the blog"),
			)


