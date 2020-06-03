from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, \
                                      DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, \
                                       PermissionRequiredMixin
from .models import Post

class SubscriberDetailView(DetailView):       # For restricted viewing. Two types of blog for public and restricted.
                                        # Have to create another one for public viewing.
    template_name = 'blog/post/detail.html'

    def get(self, request, year, month, day, post):
        post = get_object_or_404(Post, slug=post,
                                       status='published',
                                       publish__year=year,
                                       publish__month=month,
                                       publish__day=day)
        return self.render_to_response({'post': post})

class SubscriberListView(LoginRequiredMixin, ListView):           # for restricted viewing
    #queryset = Post.restricted.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/subscribers/list.html'

    def get_queryset(self):
        return Post.objects.filter(status='published', restriction='restricted', subscribers__username=self.request.user)
