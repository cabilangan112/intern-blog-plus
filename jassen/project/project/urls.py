"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from user.views import RegisterView
from blog.views import UserDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls', namespace='blog')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', RegisterView.as_view(), name='register'),
    path('<int:pk>',UserDetail.as_view(), name='user'),    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
