from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    
    url(r'^$', views.HomeView.as_view(), name='home'),
    
    url(r'^User/', include('User.urls', namespace="User")),
    
    url(r'^admin/', include(admin.site.urls)),
)
