from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'link_site.views.home', name='home'),
    # url(r'^link_site/', include('link_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('myblog.urls')),
    url(r'^links/', include('linkmain.urls')),
    url(r'^$', 'linkmain.views.index'),
    (r'^login/$',
     'django.contrib.auth.views.login',
     {'template_name': 'login.html',
      'redirect_field_name': 'next'}),
    (r'^logout/$',
     'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    (r'^register/$','linkmain.views.register'),
                       
)


