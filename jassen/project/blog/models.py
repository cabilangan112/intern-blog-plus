from django.db import models
from django.conf import settings
from django.urls import reverse 
User = settings.AUTH_USER_MODEL

POST_STATUS = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('hidden', 'Hidden'),
)