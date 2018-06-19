from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils import translation
from django.conf import settings

register = template.Library()

@register.filter
def price_view(price):
    language_code = translation.get_language()
    price_format = [thing[1] for thing in settings.PRICES if language_code == thing[0]]
    return '%s%s'%(intcomma(price), price_format[0])

