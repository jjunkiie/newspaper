from django.views.generic import ListView, DetailView
from .models import Post, Comment


class NewsList(ListView):
    model = Post
    ordering = '-create_time'
    template_name = 'posts_list.html'
    context_object_name = 'posts'


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'



