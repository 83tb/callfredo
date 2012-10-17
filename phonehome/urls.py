from django.conf.urls import patterns, url


urlpatterns = patterns(
    'phonehome.views',
    url(r'^twiml/(?P<number>\d+)/$$', 'phone'),
    url(r'^call/(?P<number>\d+)/$', 'call', name='call'),
    url(r'^recording/(?P<id>\d+)/$', 'recording', name='recording'),
    url(r'^press/(?P<id>\d+)/$', 'press', name='press'),
)
