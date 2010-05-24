from django.conf.urls.defaults import *


urlpatterns = patterns('server.views',
        (r'^404/$', 'not_found'),
        (r'^500/$', 'server_error'),
)