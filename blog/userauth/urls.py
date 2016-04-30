from django.conf.urls import include, url
from django.contrib import admin
from .views import login, logout, register


urlpatterns = [
    url(r'^$', login, name = 'login'),
    url(r'^logout/', logout, name = 'logout'),
    url(r'^register/', register, name = 'register'),
]
