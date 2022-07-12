from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="line_color")
@stringfilter
def line_color(value):
    bg_color = ''

    if(value=='L11'):
        bg_color = 'bg-l11'
    elif(value=='L11A'):
        bg_color = 'bg-l11a'
    elif(value=='L11B'):
        bg_color = 'bg-l11b'
    elif(value=='L12'):
        bg_color = 'bg-l12 '
    elif(value=='L12A'):
        bg_color = 'bg-l12a'
    elif(value=='L12B'):
        bg_color = 'bg-l12b'
    elif(value=='L13'):
        bg_color = 'bg-l13'
    elif(value=='L14'):
        bg_color = 'bg-l14'
    
    return bg_color