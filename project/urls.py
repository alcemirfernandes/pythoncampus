#encoding: utf-8
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.shortcuts import redirect

admin.autodiscover()


urlpatterns = patterns('',
    # Home page
    (r'^$', lambda r: redirect('/evento/istcc-p/')),

    # Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Default error handlers
    (r'', include('server.urls')),

    # Event app
    (r'^evento/', include('event.urls')),

    # Unused talk app
    (r'^palestras/', include('talks.urls')),
)


urlpatterns+= patterns('django.views.generic.simple',
    (r'^index2/$', 'direct_to_template', {'template': 'index2.html'}),

    (r'^sobre/$', 'direct_to_template', {'template': 'sobre.html'}),

    (r'^about/$', 'direct_to_template', {'template': 'about.html'}),

    (r'^eu-quero-uma-pythoncampus-na-minha-universidade/$',
        'direct_to_template', {'template': 'i-want.html'}),

    (r'^contato/$', 'direct_to_template', {'template': 'contact.html'}),

    (r'^making-of/$', 'direct_to_template', {'template': 'making-of.html'}),

    (r'^dojorio/$', 'direct_to_template', {'template': 'coding-dojo.html'}),

    (r'^oficina/$', 'direct_to_template', {'template': 'oficina.html'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

