# all custom tempmplate tags

from django import template

register = template.Library()


def cut(value, arg):

    return value.replace(arg, '')


register.filter('cut', cut)

    # This is a custom template filter called "cut" that takes two arguments -
    # a string value and a substring to remove from the string. The function then
    #  returns the original string with all instances of the substring removed.
    # For example, if you pass the string "hello world" and the substring "l",
    #  the function would return "heo word".