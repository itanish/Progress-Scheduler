import random

from django import template

register = template.Library()

classList = [
    'bg-success', 'bg-danger', 'bg-warning', 'bg-info',

]


@register.filter
def random_css(a):
    return random.choice(classList)
