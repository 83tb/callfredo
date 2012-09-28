from django.conf.urls import patterns, url


urlpatterns = patterns(
    'phonehome.views',
    url(r'^twiml/(?P<number>\d+)/$$', 'phone'),
    url(r'^call/(?P<number>\d+)/$', 'call', name='call'),
    url(r'^recording/$', 'recording', name='recording'),
)
