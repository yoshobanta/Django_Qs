from django import template

# object of template

register = template.Library()

def capt(value):
    return value.capitalize()

register.filter('capt',capt)


def rep(value,s):
    return value.replace(value,s)

register.filter('replace',rep)
