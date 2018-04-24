from django import forms
from .models import Post,Category
 


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user',
        'title',
        'sub_title',
        'banner_photo',
        'body',
        'date',
        'date_modified',
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

class TagForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
        'heading',
        'sub_heading',)

