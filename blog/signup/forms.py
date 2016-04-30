#coding=utf-8

from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['email', 'fullname', 'nickname', 'birthday']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_split = email.split('@')
		if email_split[1] != 'gmail.com':
			raise forms.ValidationError(u'Пожалуйста введите правильный email')
		else:
			return email

	def clean_birthday(self):
		birthday = self.cleaned_data.get('birthday')
		birthday = str(birthday)
		if birthday[0:4] > '2016':
			raise forms.ValidationError(u'Пожалуйста введите правильную дату')
		else:
			return birthday
	