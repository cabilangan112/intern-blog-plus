from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('<int:post_id>/', views.PostDetailView.as_view(), name='detail'),
#    path('<last_name>/', views.UserDetail.as_view(), name='user'),
    path('post/comment/', views.comment_new, name='post-comment'),

]