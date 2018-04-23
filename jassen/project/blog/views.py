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

from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)


class PostView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(status__contains='publish').order_by('-date')
        context = {'post':post,}
        return render(request, "Post_list.html", context)

class PostDetailView(View):
    def get(self, request, post_id, *args, **kwargs):
        post = Post.objects.filter(pk=post_id, status__contains='publish').order_by('-date')
        context = {'post':post,}
        return render(request, "Post_Detail.html", context)