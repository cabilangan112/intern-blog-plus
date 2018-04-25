from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.generic import (ListView,DetailView,CreateView,UpdateView, View)
from .models import Post,Category,Tag,Blog,Comment
from .forms import PostForm,CommentForm
from user.models import User
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)


class PostView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(status__contains='publish').order_by('-date')
        context = {'post':post,}
        return render(request, "Post_list.html", context)


class PostDetailView(View):
    def get(self, request, title, *args, **kwargs):
        post = get_object_or_404(Post, title=title, status='published')
        comment = post.comment_set.all()
        context = {'post':post,'comment': comment,}
        return render(request, "Post_Detail.html", context)

def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('/')
    else:
        form = CommentForm()
    context = {
        'form': form,
    }
    return render(request, 'post.html', context)


    def get_object(self):
        title = self.kwargs.get("title")
        if title is None:
            raise Http404
        return get_object_or_404(Post, title__iexact=title)


class CreatePostView(View):
    def get(self, request):
        create = Post.objects.all()
        context = {'create' : create,'form' : PostForm,}
        return render(request, "post.html", context)

    def get(self, request):
        form = PostForm(request.POST)
        post = Post.objects.all()
        if form.is_valid():
            form.save()
            return redirect('index')            
        context = {'form' : form,'post' : post,}        
        return render(request, "post.html", context)


class UserDetail(View):
    def get(self, request,  pk, *args, **kwargs): 
        users = User.objects.get(pk=pk)
        post = Post.objects.filter(user=pk)
        context = {'users':users,}
        return render(request, "user_detail.html", context)