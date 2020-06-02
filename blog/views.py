from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, \
                                      DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Post

class AuthorMixin(object):
    def get_queryset(self):
        qs = super(AuthorMixin, self).get_queryset()
        return qs.filter(author=self.request.user)

class AuthorEditMixin(object):
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AuthorEditMixin, self).form_valid(form)

class AuthorPostMixin(AuthorMixin): #, LoginRequiredMixin):
    model = Post
    fields = ['title', 'body', 'status']
    success_url = reverse_lazy('blog:post_list') #('manage_post_list') should be for restricted access

class AuthorPostEditMixin(AuthorPostMixin, AuthorEditMixin):
    #fields = ['title', 'body', 'status']
    #success_url = reverse_lazy('manage_post_list')
    template_name = 'blog/post/createupdate.html'


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

class PostCreateView(AuthorPostEditMixin, CreateView):
    #model = Post
    #fields = ['title', 'body', 'status'] #, 'author']
    #success_url = reverse_lazy('blog:post_list')
    #template_name = 'blog/post/createupdate.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(AuthorPostEditMixin, UpdateView):
    #model = Post
    #fields = ['title', 'body', 'status']
    #success_url = reverse_lazy('blog:post_list')
    #template_name = 'blog/post/createupdate.html'
    pass

class PostDeleteView(AuthorPostMixin, DeleteView):
    #model = Post
    #fields = ['title', 'slug', 'body', 'status', 'author']
    #success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/post/delete.html'
