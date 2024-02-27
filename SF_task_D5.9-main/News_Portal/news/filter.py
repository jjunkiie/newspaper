from django_filters import FilterSet, DateTimeFilter
from .models import Post


class PostFilter(FilterSet):
    class Meta:
       model = Post
       fields = {
           'title_of_post': ['icontains'],
           'author__user': ['exact'],
           'news_or_article': ['exact'],
           'date_of_post': ['gt']
        }
       filter_overrides = {
           DateTimeFilter: {
               'filter_class': DateTimeFilter,
               'extra': lambda f: {
                   'widget': DateTimeFilter,
               },
           },
       }