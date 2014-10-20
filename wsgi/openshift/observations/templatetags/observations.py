from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def form_get_app_name(value):
    """Get the app name in the form view"""
    url_parts = value.rsplit('/', 3)
    return url_parts[1]
    
@register.filter
@stringfilter
def list_get_app_name(value):
    """Get the app name in the list view"""
    url_parts = value.rsplit('/', 2)
    return url_parts[1]