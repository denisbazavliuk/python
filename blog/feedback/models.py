#coding=utf-8
from __future__ import unicode_literals
from django.db import models


class Email(models.Model):
	from_email = models.EmailField(u'Электронный адрес')
	subject = models.CharField(u'Заголовок', max_length = 150)
	message = models.TextField(u'Текст письма')
	timesend = models.DateTimeField(u'Дата отправки', auto_now = False, auto_now_add = True)

	def __unicode__(self):
		return self.from_email
