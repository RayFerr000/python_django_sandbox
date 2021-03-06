from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from User.views import user_signup_save, login,logout
admin.autodiscover()
urlpatterns = patterns('',
    
    url(r'^$', TemplateView.as_view(template_name = 'index.html'), name = 'home'),
    url(r'^signup/', user_signup_save, name="user_signup_save"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login, name = "login"),
    url(r'^logout/', logout, name = "logout")
)