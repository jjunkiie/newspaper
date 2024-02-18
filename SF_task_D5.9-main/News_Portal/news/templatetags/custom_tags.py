from django import template

register = template.Library()


@register.simple_tag()
def current_time(date):
    return date.strftime("%d.%m.%Y")