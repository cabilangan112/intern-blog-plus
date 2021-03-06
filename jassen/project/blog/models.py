from django.db import models
from django.conf import settings
from django.urls import reverse 
User = settings.AUTH_USER_MODEL

POST_STATUS = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('hidden', 'Hidden'),
)
class Blog(models.Model):
    heading = models.CharField(max_length=150)
    sub_heading = models.CharField(max_length=150)
    
    def __str__(self):
        return '{}'.format(self.heading)

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    banner_photo = models.ImageField(upload_to = 'static/media')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE) 
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag",related_name="tags")
    status = models.CharField(max_length=9, choices=POST_STATUS, blank=True, default=True)

    def __str__(self):
        return '{}'.format(self.title)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True) 
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.text)

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.title)

class Tag(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.title)
