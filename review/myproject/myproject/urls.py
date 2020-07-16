"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import blog.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/',blog.views.hello,name = 'hello'),
    path('blog/intro/',blog.views.intro, name = 'intro'),
    path('',blog.views.blog, name = 'blogs'),
    path('blog/new/', blog.views.new, name= 'new'),
    path('blog/create/',blog.views.create, name= 'create'),
    path('blog/<int:blog_id>/update/',blog.views.update, name= 'update'),
    path('blog/<int:blog_id>/delete/',blog.views.delete, name= 'delete'),
    path('blog/<int:blog_id>/', blog.views.detail, name = 'detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
