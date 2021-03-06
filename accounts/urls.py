from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^social-error/$', views.SocialErrorView.as_view()),
)
