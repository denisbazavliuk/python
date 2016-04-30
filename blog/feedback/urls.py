from django.conf.urls import include, url
from django.contrib import admin
from .views import email, thanks

urlpatterns = [
	url(r'^$', email, name = 'email'),
	url(r'^thanks/$', thanks, name = 'thanks'),
	]