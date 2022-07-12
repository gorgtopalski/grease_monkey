from django import template
from django.core.serializers import serialize
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="json")
def json(value):
    return serialize('json', value)