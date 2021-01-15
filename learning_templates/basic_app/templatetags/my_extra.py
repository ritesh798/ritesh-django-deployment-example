from django import template

register = template.Library()

def cut(value,arg):
    """This cuts all values of argsbfrom the string
    """
    return value.replace(arg,'')

register.filter('cut',cut)