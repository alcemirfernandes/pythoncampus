#encoding: utf-8
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^palestras/', include('talks.urls')),
    (r'', include('server.urls')),
)


from lncc import talks as talks_for_lncc
from estacio import talks as talks_for_estacio

urlpatterns+= patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'event.html', 'extra_context': {'talks': talks_for_lncc} }),
    
    (r'^index2/$', 'direct_to_template', {'template': 'index2.html'}),

    (r'^sobre/$', 'direct_to_template', {'template': 'sobre.html'}),

    (r'^about/$', 'direct_to_template', {'template': 'about.html'}),

    (r'^eu-quero-uma-pythoncampus-na-minha-universidade/$',
        'direct_to_template', {'template': 'i-want.html'}),

    (r'^contato/$', 'direct_to_template', {'template': 'contact.html'}),

    (r'^making-of/$', 'direct_to_template', {'template': 'making-of.html'}),

    (r'^dojorio/$', 'direct_to_template', {'template': 'coding-dojo.html'}),

    (r'^oficina/$', 'direct_to_template', {'template': 'oficina.html'}),

    (r'^evento/istcc-p/$', 'direct_to_template', {'template': 'event.html', 'extra_context': {'talks': talks_for_lncc} }),
    (r'^evento/istcc-p/', include('subscription.urls')),

    (r'^evento/estacio/$', 'direct_to_template', {'template': 'event.html', 'extra_context': {'talks': talks_for_estacio} }),
    (r'^evento/estacio/', include('subscription.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

