from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from social_auth import urls as social_auth_urls
import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^givenumber/$', views.GiveNumberView, name='givenumber'),
    url(r'^confirmnumber/$', views.ConfirmNumberView, name='confirmnumber'),
    url(r'^tryit/$', views.TryItView, name='tryit'),

    url(r'^birthdays/$', login_required(views.birthdays), name='birthdays'),
    url(r'^social/', include(social_auth_urls)),
    url(r'^phone/', include('phonehome.urls')),
    url(r'^wishes/(?P<id>\d+)/$', views.PlayerView),

    #url(r'^confirmnumber/$', views.ConfirmNumberView.as_view(), name='confirmnumber'),
    #url(r'^schedule/$', views.ScheduleView.as_view(), name='schedule'),
    #url(r'^saveincontacts/$', views.SaveInContactsView.as_view(), name='saveincontacts'),
)

urlpatterns += staticfiles_urlpatterns()
