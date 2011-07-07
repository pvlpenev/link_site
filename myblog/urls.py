from django.conf.urls.defaults import *

urlpatterns = patterns('myblog.views',

    url('^$', 'index'),
    url(r'^(?P<blogpost_id>\d+)/$', 'detail'),
)
