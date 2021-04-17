from django import template

register = template.Library()

@register.filter
def subtract(value, num):
    """Subtracting two numbers together"""
    return value - num

@register.filter
def remainder(value, num):
    """Remainder two numbers together"""
    return value % num
