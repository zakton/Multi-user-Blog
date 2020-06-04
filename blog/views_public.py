from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, \
                                      DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, \
                                       PermissionRequiredMixin
from django.views.generic.base import RedirectView
from .models import Post

# Notes:
# - LoginRequiredMixin prohibits accessing a page without logging in
# = PermissionRequiredMixin prohibits accessing a page without permission_required

class PostDetailView(DetailView):       # For restricted viewing. Two types of blog for public and restricted.
                                        # Have to create another one for public viewing.
    template_name = 'blog/post/detail.html'

    def get(self, request, year, month, day, post):
        post = get_object_or_404(Post, slug=post,
                                       status='published',
                                       publish__year=year,
                                       publish__month=month,
                                       publish__day=day)
        return self.render_to_response({'post': post})

class PostListView(ListView):           # for restricted viewing
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

class LoginRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.groups.filter(name='Authors').exists():
            return reverse_lazy('blog:manage_post_list')
        else: # must be a subscriber
            print('must be a subscriber')
            return reverse_lazy('blog:subscriber_list')
