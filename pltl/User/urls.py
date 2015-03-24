from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from User import views

urlpatterns = patterns('',
    url(r'^$', views.user_signup_save, name = 'user_signup_save'))