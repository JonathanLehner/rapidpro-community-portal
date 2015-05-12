from django import template

register = template.Library()

@register.filter
def make_unique(value, unique_var): # Only one argument.
    """Make the queryset unique by unique_var, sort by unique_var"""
    return value.distinct(unique_var).order_by(unique_var)