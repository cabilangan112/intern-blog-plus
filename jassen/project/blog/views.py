from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model
from django.views.generic import (ListView,DetailView,CreateView,UpdateView, View)
from .models import Post,Category,Tag,Blog,Comment
from user.models import User
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)


class PostView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(status__contains='publish').order_by('-date')
        context = {'post':post,}
        return render(request, "Post_list.html", context)

class PostDetailView(View):
    def get(self, request,  title,*args, **kwargs):
        post = Post.objects.filter(title=title, status__contains='publish').order_by('-date')
        context = {'post':post,}
        return render(request, "Post_Detail.html", context)

    def get_object(self):
        title = self.kwargs.get("title")
        if title is None:
            raise Http404
        return get_object_or_404(Post, title__iexact=title)

class UserDetail(View):
    def get(self, last_name, request, *args, **kwargs): 
        query = self.request.GET.get('q')
        user = User.objects.filter(last_name=last_name)
        context = {'user':user,}
        return render(request, "user_detail.html", context)

