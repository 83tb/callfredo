from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from hundredseconds.accounts import views

urlpatterns = patterns('',
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^social-error/$', views.SocialErrorView.as_view()),

    url(r'^birthdays/$', login_required(views.birthdays), name='birthdays'),
)
