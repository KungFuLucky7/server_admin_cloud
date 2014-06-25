from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def form_get_app_name(value):
    url_parts = value.rsplit('/', 3)
    return url_parts[1]
    
@register.filter
@stringfilter
def list_get_app_name(value):
    url_parts = value.rsplit('/', 2)
    return url_parts[1]