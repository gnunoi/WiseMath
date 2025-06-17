from django import template

register = template.Library()

@register.filter
def index(list, index):
    return list[index] if index < len(list) else ''