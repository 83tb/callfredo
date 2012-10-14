from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from social_auth import urls as social_auth_urls
from hundredseconds import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^givenumber/$', views.GiveNumberView.as_view(), name='givenumber'),
    url(r'^confirmnumber/$', views.ConfirmNumberView.as_view(), name='confirmnumber'),
    url(r'^schedule/$', views.ScheduleView.as_view(), name='schedule'),
    url(r'^saveincontacts/$', views.SaveInContactsView.as_view(), name='saveincontacts'),
    url(r'^tryit/$', views.TryItView.as_view(), name='tryit'),




    url(r'^social/', include(social_auth_urls)),
    url(r'^phone/', include('phonehome.urls')),
    url(r'^player/', views.PlayerView),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('hundredseconds.accounts.urls', namespace='accounts'))
)

urlpatterns += staticfiles_urlpatterns()
