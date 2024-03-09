from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Post, Author, Category
from .filters import PostFilter
from .forms import PostForm

from django.shortcuts import render


class Welcome(LoginRequiredMixin, TemplateView):
    template_name = 'new_welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context




class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostSearch(PostList):
    template_name = 'news_search.html'



class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'

    login_url = '/sign/login/'


class PostUpdate(LoginRequiredMixin,UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'
    login_url = '/sign/login/'

class PostDelete(DeleteView):
    model = Post
    template_name = 'new_delete.html'
    success_url = reverse_lazy('post_list')

@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новых публикаций в категории: '
    return render(request, 'account/subscribe.html', {'category': category, 'message': message})


@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)

    message = 'Вы успешно отписаны от рассылки по категории: '
    return render(request, 'account/unsubscribe.html', {'category': category, 'message': message})