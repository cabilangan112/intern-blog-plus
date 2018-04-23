from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('post/<int:post_id>/', views.PostDetailView.as_view(), name='detail'),
]