#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from signup.models import SignUp


# Create your models here.

class Post(models.Model):
	title = models.CharField(u'Заголовок', max_length = 120)
	content = models.TextField(u'Текст статьи')
	timestamp = models.DateTimeField(u'Дата создания', auto_now = False, auto_now_add = True)
	updated = models.DateTimeField(u'Дата последнего изменения', auto_now = True, auto_now_add = False)
	# author = models.ForeignKey(User)


	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', kwargs = {'id': self.id})

	class Meta:
		ordering = ['-timestamp', '-updated']


