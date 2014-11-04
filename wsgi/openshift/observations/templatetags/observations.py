from django import template
from django.template.defaultfilters import stringfilter
import urllib2

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
    
@register.filter
@stringfilter
def trim_query_string(value):
    """In list view, Quick Start Guide, trim the query string to the correct format"""
    query_string = value
    if 'e=guide&' in value:
        query_string = value.replace('e=guide&', '')
    elif 'e=guide' in value:
        query_string = value.replace('e=guide', '')
    return query_string
    
@register.filter
@stringfilter
def trim_url(value):
    """Trim url for the correct path"""
    url_parts = value.split('/', 4)
    url_parts.remove(url_parts[4])
    url = '/'.join(url_parts)
    return url
    
@register.filter
@stringfilter
def modify_query_string(value):
    """In form view, modify the query string to the correct format"""
    query_string = value
    #if '_changelist_filters=' in value:
        #query_string = value.replace('_changelist_filters=', '')
    return urllib2.unquote(query_string)
