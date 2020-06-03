from django.urls import path
#from . import views
from . import views_public
from . import views_authors
from . import views_subscribers

app_name = 'blog'
urlpatterns = [

    # Public Views ... views
    path('', views_public.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views_public.PostDetailView.as_view(),
        name='post_detail'),

    # Author Views ... views_author
    path('create/', views_authors.PostCreateView.as_view(),
        name='post_create'),
    path('<pk>/edit/', views_authors.PostUpdateView.as_view(),
        name='post_edit'),
    path('<pk>/delete/',
        views_authors.PostDeleteView.as_view(),
        name='post_delete'),
    path('manage/',
        views_authors.AuthorPostListView.as_view(),
        name='manage_post_list'),

    # Subscriber Views
    path('subscribed/',
        views_subscribers.SubscriberListView.as_view(),
        name='subscriber_list'),
]
