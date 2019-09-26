from django import template

register = template.Library()

@register.filter
def cut(value, arg):
    """
    cuts out arg from string
    """
    return value.replace(arg, '')

# register.filter('cut', cut)
