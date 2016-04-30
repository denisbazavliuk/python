#coding=utf-8


from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class SignUp(models.Model):	 
	email = models.EmailField(u'Электронный адрес', help_text = u'Только домены gmail.com') 
	fullname = models.CharField('Имя', blank = False, null = True, max_length = 120)
	nickname = models.CharField(u'Никнейм', blank = False, null = True, max_length = 120)
	birthday = models.DateField(u'Дата рождения', blank = False, null = True)
	timestamp = models.DateTimeField(u'Дата создания', auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(u'Дата обновления', auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return self.email




