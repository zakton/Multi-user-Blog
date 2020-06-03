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

# Notes:
# - LoginRequiredMixin prohibits accessing a page without logging in
# = PermissionRequiredMixin prohibits accessing a page without permission_required

class AuthorMixin(object):
    def get_queryset(self):
        qs = super(AuthorMixin, self).get_queryset()
        return qs.filter(author=self.request.user)

class AuthorEditMixin(object):
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AuthorEditMixin, self).form_valid(form)

class AuthorPostMixin(AuthorMixin, LoginRequiredMixin):
    model = Post
    fields = ['title', 'body', 'status', 'restriction']
    success_url = reverse_lazy('blog:manage_post_list') #('manage_post_list') should be for restricted access

class AuthorPostEditMixin(AuthorPostMixin, AuthorEditMixin):
    #fields = ['title', 'body', 'status']
    #success_url = reverse_lazy('manage_post_list')
    template_name = 'blog/post/createupdate.html'

class PostCreateView(PermissionRequiredMixin, AuthorPostEditMixin, CreateView):
    permission_required = 'blog.add_post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(PermissionRequiredMixin, AuthorPostEditMixin, UpdateView):
    permission_required = 'blog.change_post'


class PostDeleteView(PermissionRequiredMixin, AuthorPostMixin, DeleteView):
    template_name = 'blog/post/delete.html'
    permission_required = 'blog.delete_post'

class AuthorPostListView(PermissionRequiredMixin, AuthorPostMixin, ListView):
    template_name = 'blog/post/managed_list.html'
    permission_required = 'blog.change_post'
