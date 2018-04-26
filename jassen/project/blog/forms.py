from django import forms
from .models import Post,Category,Tag,Blog,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)
        fields = ('user',
        'title',
        'sub_title',
        'banner_photo',
        'body',
        'blog',
        'category',
        'tags',
        'status',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
        'title',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = (
        'title',)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
        'heading',
        'sub_heading',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post','author',)
        fields = (
        'post',
        'text',
        'author',)
    
