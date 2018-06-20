from django.apps import AppConfig
from django.utils.translation import ugettext as _

class ShopConfig(AppConfig):
    name = 'shop'
    verbose_name = _('Shop')
    verbose_name_plural = _('Shop')
