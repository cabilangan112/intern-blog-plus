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
    sub_Title = models.CharField(max_length=150)
    banner_photo = models.ImageField(upload_to = 'static/media')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE) 
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag",related_name="tags")
    status = models.CharField(max_length=9, choices=POST_STATUS, blank=True, default=True)
    Comment = models.ManyToManyField("comment",related_name="Comment")
    
    def __str__(self):
        return '{}'.format(self.user.first_name, self.user.last_name)

class Comment(models.Model):
    vote = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.user)

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.title)

class Tag(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.title)
