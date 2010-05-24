#encoding: utf-8
from django.conf import settings
from django.conf.urls.defaults import *

from lncc import talks as talks_for_lncc
from estacio import talks as talks_for_estacio

urlpatterns = patterns('django.views.generic.simple',
    (r'istcc-p/$', 'direct_to_template', {'template': 'event/lncc.html', 'extra_context': {'talks': talks_for_lncc} }),

    (r'unesa-madureira/$', 'direct_to_template', {'template': 'event/estacio.html', 'extra_context': {'talks': talks_for_estacio} }),

    # subscription
    (r'unesa-madureira/', include('subscription.urls')),
)