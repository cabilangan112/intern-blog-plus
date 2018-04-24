from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('<title>/', views.PostDetailView.as_view(), name='detail'),
#    path('<last_name>/', views.UserDetail.as_view(), name='user'),
    path('post', views.Post, name='post'),
]