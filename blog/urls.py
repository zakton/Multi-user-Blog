from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail'),
    path('create/', views.PostCreateView.as_view(),
        name='post_create'),
    path('<pk>/edit/', views.PostUpdateView.as_view(),
        name='post_edit'),
    path('<pk>/delete/',
        views.PostDeleteView.as_view(),
        name='post_delete'),
]
