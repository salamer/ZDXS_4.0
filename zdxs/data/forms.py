 # -*- coding:utf-8 -*- 

from django import forms

class DataForm(forms.Form):
	title=forms.CharField(label="your title",
				required=True,
				error_messages={'required':'请写一个正确的主题'},
				widget=forms.TextInput(attrs={"class":'form-control',"placeholder":"写下你的资料主题"}))
	data=forms.CharField(label="body",
					required=True,
					error_messages={'required':'请写下一个正确的资料'},
					widget=forms.Textarea(attrs={"class":'form-control',"placeholder":"请写下你的资料",})
				)
	summury=forms.CharField(label="summury",
					required=True,
					error_messages={'required':'简要是必要的哦'},
					widget=forms.Textarea(attrs={"class":'form-control',"placeholder":"请写下你的简要","style":"height:200px;"})
				)
	category=forms.CharField(label="your category",
				required=True,
				error_messages={'required':'分类是最重要的哦'},
				widget=forms.TextInput(attrs={"class":'form-control',"placeholder":"分类是必要的，且最好不要重复"}))


	def cleaned_body(self):
		body=self.cleaned_data['body']
		lgt=len(body)
		if lgt<15:
			raise forms.ValidationError("资料必须要超过15个字符")
		return body
	
	def cleaned_categoy(self):
		category=self.cleaned_data['category']
		if " " in category:
			raise forms>ValidationError("分类里面不能有空格哦")
		return category
		

class DataCommentForm(forms.Form):
	comment=forms.CharField(label="comment",
					required=True,
					error_messages={'required':'不能是空评论哦'},
					widget=forms.Textarea(attrs={"class":'form-control',"placeholder":"写下的你疑问和不解，以及对这个资料的优化","style":"height:150px;"})
				)


	def cleaned_comment(self):
		body=self.cleaned_data['comment']
		lgt=len(body)
		if lgt<5:
			raise forms.ValidationError("必须要超过5个字符")
		return body
