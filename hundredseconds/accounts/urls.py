from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from hundredseconds.accounts import views

urlpatterns = patterns('',
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^social-error/$', views.SocialErrorView.as_view()),

    url(r'^phone/$', login_required(views.PhoneUpdateView.as_view()), name='phone'),
    url(r'^birthdays/$', login_required(views.birthdays), name='birthdays'),
    url(r'^profile/$', login_required(views.LoggedInView.as_view()), name='loggedin'),
)
