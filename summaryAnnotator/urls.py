"""summaryAnnotator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from accounts.views import login_view, logout_view, register_view
from Task.views import article_list_view, article_edit_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', login_view),
    path('login/', login_view, name="loginURL"), 
    path('logout/', logout_view, name="logoutURL"), 
    path('register/', register_view, name="registerURL"),
    path('articles/', article_list_view, name="articlesURL"),
    path('articles/<int:id>/', article_edit_view, name='articleEditURL'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
