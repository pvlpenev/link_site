from django.conf.urls.defaults import *

urlpatterns = patterns(
    'linkmain.views',
    (r'^$', 'index'),
    (r'^add/$', 'add'),
)
