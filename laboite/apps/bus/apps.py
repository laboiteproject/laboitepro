from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppBusConfig(AppConfig):
    name = label = 'laboite.apps.bus'
    verbose_name = _('App : Bus')
