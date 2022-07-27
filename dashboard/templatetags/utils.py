from django import template

register = template.Library()

@register.filter('get_value_from_dict')
def get_value_from_dict(dict_data, key):
    if key:
        return dict_data.get(key)

@register.filter('get_value_from_model')
def get_value_from_dict(model, key):
    if key:
        return model.key

@register.filter('short_shift')
def short_shift(str):
    if str:
        if str == 'Mañana':
            return 'M'
        elif str == 'Tarde':
            return 'T'
        elif str == 'Noche':
            return 'N'
        else:
            return ''

@register.filter('get_fullname')
def get_fullname(usr):
    if usr:
        return usr.get_full_name()