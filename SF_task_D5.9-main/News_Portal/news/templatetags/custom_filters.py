from django import template
from django_filters import FilterSet


register = template.Library()

FORBIDDEN_WORDS = ["редиска", "Редиска","Дебил" , "дебил" ]    # обойдемся без мата :)


@register.filter()
def censor(text):
    for word in FORBIDDEN_WORDS:
        text = text.replace(word, word[0] + "*" * (len(word) - 1))
    return text
