from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, \
                                      DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Post

class PostDetailView(DetailView):
    template_name = 'blog/post/detail.html'

    def get(self, request, year, month, day, post):
        post = get_object_or_404(Post, slug=post,
                                       status='published',
                                       publish__year=year,
                                       publish__month=month,
                                       publish__day=day)
        return self.render_to_response({'post': post})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'body', 'status'] #, 'author']
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/post/postform.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body', 'status']
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/post/postform.html'

class PostDeleteView(DeleteView):
    model = Post
    fields = ['title', 'slug', 'body', 'status', 'author']
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/post/postdeleteform.html'
