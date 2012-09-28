from django.conf.urls import patterns, include, url
from django.contrib import admin
from social_auth import urls as social_auth_urls
from hundredseconds import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^social/', include(social_auth_urls)),

    url(r'^admin/', include(admin.site.urls)),
)
