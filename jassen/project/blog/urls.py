from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('detail/<title>/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/', views.comment, name='post-comment'),
    path('draft/', views.Draft, name='draft'),
    path('hidden/', views.Hidden, name='hidden'),
    path('add/post/', views.PostCreate, name='add-post'),
    path('add/tags/', views.TagCreate, name='add-tags'),
    path('add/blog/', views.BlogCreate, name='add-blog'),
    path('add/category/', views.CategoryCreate, name='add-category'),
]