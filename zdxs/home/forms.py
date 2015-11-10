#-*- coding: UTF-8 -*- 
'''
from django import forms
from django.contrib.auth.models import User
import re
from PIL import Image
from home.models import UserProfile

class LoginForm(forms.Form):
	email=forms.EmailField(label="your email",
				required=True,
				error_messages={'required':'请写上你的正确的邮箱'},
				widget=forms.EmailInput(attrs={"class":'form-control',"placeholder":"邮箱"}))
	password=forms.CharField(label="password",
					required=True,
					error_messages={'required':'请写上你正确的密码'},
					widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"密码"})
				)
		

class RegisterForm(forms.Form):
	name=forms.CharField(label="your name",
				max_length=100,
				required=True,
				error_messages={'required':'请写上名字!'},
				widget=forms.TextInput(attrs={'class':"form-control","placeholder":"写下你的姓名"}))
	email=forms.EmailField(label="your email",
				required=True,
				error_messages={'required':'请写上正确的邮箱'},
				widget=forms.EmailInput(attrs={"class":'form-control',"placeholder":"写下你的邮箱，邮箱用来登录"}))
	password1=forms.CharField(label="password",
					required=True,
					error_messages={'required':'请写上你的密码'},
					widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"你的密码"})
				)
	password2=forms.CharField(label="password",
					required=True,
					error_messages={'required':'请再输入一次'},
					widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"检查密码"})
				)

	def clean_name(self):
		name=self.cleaned_data['name']
		if ' ' in name:
			raise forms.ValidationError('不能有空格')
		if not re.search(r'^\w+$',name):
			raise forms.ValidationError('名字只能是字母或数字')
		try:
			the_name=User.objects.get(username=name)
		except User.DoesNotExist:
			return name
		raise forms.ValidationError("这个用户名被注册了")

		return name

	def clean_password1(self):
		password=self.cleaned_data['password1']
		cha_num=len(password)
		if cha_num<6:
			raise forms.ValidationError("密码应该大于6个字符")
		return password

	def clean_email(self):
		email=self.cleaned_data['email']
		try:
			user=User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('该邮箱已经被注册了')

	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1=self.cleaned_data['password1']
			password2=self.cleaned_data['password2']
			if password1==password2:
				return password2
			raise forms.ValidationError('两次密码输入不一致')
		
SEX=(
	("M","男"),
	("W","女"),
	("U","不明"),
)
JOIN=(
	
	("2","考虑一下"),
	("1","加入"),
)

class CareerForm(forms.Form):
	name=forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你的真实姓名"})
		)

	sex=forms.ChoiceField(
		choices=SEX,
		required=False,
		widget=forms.Select(attrs={'class':"form-control"})
		)

	subject=forms.CharField(
		max_length=200,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你的专业"})
		)

	classname=forms.CharField(
		max_length=200,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你所在的班级"})
		)

	birthday=forms.CharField(
		max_length=200,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你的生日"})
		)

	race=forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你的民族"})
		)


	contact=forms.CharField(
		max_length=400,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你的联系方式"})
		)
	introduction=forms.CharField(
		required=False,
		widget=forms.Textarea(attrs={"class":'form-control',"style":"height:250px;","placeholder":"请对自己进行介绍，越多越好"})
		)
	something=forms.CharField(
		required=False,
		widget=forms.Textarea(attrs={"class":'form-control',"style":"height:250px;","placeholder":"你想对扎堆做什么"})
		)
	make_sure_to_join=forms.ChoiceField(
		choices=JOIN,
		
		widget=forms.Select(attrs={'class':"form-control"})
		)
	team=forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={"class":"form-control","placeholder":"您希望加入的组"})
		)

	


class PicForm(forms.Form):
	avatar=forms.ImageField(

		required=True,

		error_messages={'required':"其他都可不填，但是照片必须填，并且填了就无法修改"},
		
		)
	def clean_avatar(self):
		

		image=self.cleaned_data.get("avatar",None)
		if image:
			if image.content_type not in ['image/jpeg','image/png']:
				raise forms.ValidationError("你传的是照片么")
			else:
				img=Image.open(image)
				w,h=img.size
				max_width=max_height=1024
				if w >= max_width or h >= max_height:
					raise forms.ValidationError("照片大小太大")
				if img.format.lower() not in ['jpeg','jpg','png']:
					raise forms.ValidationError('照片格式必须是jpg，png')
				if len(image)>(1*1024*1024):
					raise forms.ValidationError("照片太大，必须小于1m")
		return image
'''
#-*- coding: UTF-8 -*- 

from django import forms
from django.contrib.auth.models import User
import re
from PIL import Image
from home.models import UserProfile

class LoginForm(forms.Form):
	email=forms.EmailField(label="your email",
				required=True,
				error_messages={'required':'请写上你的正确的邮箱'},
				widget=forms.EmailInput(attrs={"class":'form-control',"value":"注册邮箱",'style':'color:#ADADAD'}))
	password=forms.CharField(label="password",
					required=True,
					error_messages={'required':'请写上你正确的密码'},
					widget=forms.TextInput(attrs={"class":'form-control',"value":"密码",'style':'color:#ADADAD'})
				)
		

class RegisterForm(forms.Form):
	name=forms.CharField(label="your name",
				max_length=100,
				required=True,
				error_messages={'required':'请写上名字!'},
				widget=forms.TextInput(attrs={'class':"form-control","value":"写下你的英文名",'style':'color:#ADADAD'}))
	email=forms.EmailField(label="your email",
				required=True,
				error_messages={'required':'请写上正确的邮箱'},
				widget=forms.EmailInput(attrs={"class":'form-control',"value":"写下你的邮箱，邮箱用来登录",'style':'color:#ADADAD'}))
	password1=forms.CharField(label="password",
					required=True,
					error_messages={'required':'请写上你的密码'},
					widget=forms.TextInput(attrs={"class":'form-control',"value":"请输入你的密码",'style':'color:#ADADAD'})
				)
	password2=forms.CharField(label="password",
					required=True,
					error_messages={'required':'请再输入一次'},
					widget=forms.TextInput(attrs={"class":'form-control',"value":"检查一次密码",'style':'color:#ADADAD'})
				)

	def clean_name(self):
		name=self.cleaned_data['name']
		if ' ' in name:
			raise forms.ValidationError('不能有空格')
		if not re.search(r'^\w+$',name):
			raise forms.ValidationError('名字只能是字母或数字')
		try:
			the_name=User.objects.get(username=name)
		except User.DoesNotExist:
			return name
		raise forms.ValidationError("这个用户名被注册了")

		return name

	def clean_password1(self):
		password=self.cleaned_data['password1']
		cha_num=len(password)
		if cha_num<6:
			raise forms.ValidationError("密码应该大于6个字符")
		if not re.search(r'^\w+$',password):
			raise forms.ValidationError('名字只能是字母或数字')
		return password

	def clean_email(self):
		email=self.cleaned_data['email']
		try:
			user=User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('该邮箱已经被注册了')

	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1=self.cleaned_data['password1']
			password2=self.cleaned_data['password2']
			if password1==password2:
				return password2
			raise forms.ValidationError('两次密码输入不一致')
		
SEX=(
	("M","男"),
	("W","女"),
	("U","不明"),
)
JOIN=(
	
	("2","考虑一下"),
	("1","加入"),
)

class CareerForm(forms.Form):
	name=forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你的真实姓名"})
		)

	sex=forms.ChoiceField(
		choices=SEX,
		required=False,
		widget=forms.Select(attrs={'class':"form-control"})
		)

	subject=forms.CharField(
		max_length=200,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你的专业"})
		)

	classname=forms.CharField(
		max_length=200,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你所在的班级"})
		)

	birthday=forms.CharField(
		max_length=200,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你的生日"})
		)

	race=forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你的民族"})
		)


	contact=forms.CharField(
		max_length=400,
		required=False,
		widget=forms.TextInput(attrs={'class':"form-control","placeholder":"请写上你的联系方式"})
		)
	introduction=forms.CharField(
		required=False,
		widget=forms.Textarea(attrs={"class":'form-control',"style":"height:250px;","placeholder":"请对自己进行介绍，越多越好"})
		)
	something=forms.CharField(
		required=False,
		widget=forms.Textarea(attrs={"class":'form-control',"style":"height:250px;","placeholder":"你想对扎堆做什么"})
		)
	make_sure_to_join=forms.ChoiceField(
		choices=JOIN,
		
		widget=forms.Select(attrs={'class':"form-control"})
		)
	team=forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={"class":"form-control","placeholder":"您希望加入的组"})
		)


class PicForm(forms.Form):
	avatar=forms.CharField(
		max_length=200,
		required=True,
		widget=forms.TextInput(attrs={"class":"form-control","style":"display:none;"})
		)

'''
class PicForm(forms.Form):
	avatar=forms.ImageField(

		required=True,

		error_messages={'required':"其他都可不填，但是照片必须填，并且填了就无法修改"},
		
		)
	def clean_avatar(self):
		

		image=self.cleaned_data.get("avatar",None)
		if image:
			if image.content_type not in ['image/jpeg','image/png']:
				raise forms.ValidationError("你传的是照片么")
			else:
				img=Image.open(image)
				w,h=img.size
				max_width=max_height=1024
				if w >= max_width or h >= max_height:
					raise forms.ValidationError("照片大小太大")
				if img.format.lower() not in ['jpeg','jpg','png']:
					raise forms.ValidationError('照片格式必须是jpg，png')
				if len(image)>(1*1024*1024):
					raise forms.ValidationError("照片太大，必须小于1m")
		return image
'''