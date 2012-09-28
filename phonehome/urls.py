from django.conf.urls import patterns, url


urlpatterns = patterns(
    'phonehome.views',
    url(r'^$', 'phone'),
)
