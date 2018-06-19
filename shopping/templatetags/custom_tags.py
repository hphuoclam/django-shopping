from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def price_view(price):
    return '%s%s'%(intcomma(price), '₫')

