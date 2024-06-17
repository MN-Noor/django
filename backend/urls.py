"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# myapp/urls.py
from django.urls import path
from guide_db.auth import sign_in, sign_up, logout

urlpatterns = [
    path('api/signin/', sign_in, name='sign_in'),
    path('api/signup/', sign_up, name='sign_up'),
    path('api/logout/', logout, name='logout'),
]
