#-*- coding: UTF-8 -*- 
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SEX=(
	("M","男"),
	("W","女"),
	("U","不明"),
)
JOIN=(
	("1","加入"),
	("2","考虑一下"),
)


class UserProfile(models.Model):
	user=models.OneToOneField(User)
	has_profile=models.BooleanField(default=False)
	name=models.CharField(max_length=100,blank=True)
	sex=models.CharField(max_length=1,choices=SEX)
	subject=models.CharField(max_length=150,blank=True)
	classname=models.CharField(max_length=100,blank=True)
	birthday=models.CharField(max_length=100,blank=True)
	race=models.CharField(max_length=50,blank=True)
	avatar=models.ImageField(upload_to='avatar')
	has_avatar=models.BooleanField(default=False)
	contact=models.CharField(max_length=400,blank=True)
	introduction=models.TextField(blank=True)
	something=models.TextField(blank=True)
	make_sure_to_join=models.CharField(max_length=1,
						choices=JOIN,
						blank=True,
						default="2")
	team=models.CharField(max_length=100,blank=True)

	has_been_deal_with=models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.username

	class Meta:
		permissions=(
			("can_check_the_table","can_check_the_join_table"),
			)

