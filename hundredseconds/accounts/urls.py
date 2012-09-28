from django.conf.urls import patterns, url
from hundredseconds.accounts import views

urlpatterns = patterns('',
    url(r'^logout/$', django.contrib.auth.views.logout, name='logout'),
    url(r'^social-error/$', views.SocialErrorView.as_view()),
)
