#encoding: utf-8
from django.conf import settings
from django.conf.urls.defaults import *

from lncc import talks as talks_for_lncc
from unesa import talks as talks_for_unesa

urlpatterns = patterns('django.views.generic.simple',
    (r'istcc-p/$', 'direct_to_template', {'template': 'event/lncc.html', 'extra_context': {'talks': talks_for_lncc} }),

    (r'unesa-madureira/$', 'direct_to_template', {'template': 'event/unesa.html', 'extra_context': {'talks': talks_for_unesa} }),

    # subscription
    (r'unesa-madureira/', include('subscription.urls')),
)