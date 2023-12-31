"""PFE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='http://127.0.0.1:8000/admin/')
def dashadmin(request):
    return render(request,'admin/dashadmin.html')

urlpatterns = [
    path('admin/', admin.site.urls ),
    path('dashboard/admin', dashadmin,name="dashadmin"),
    path('', include('home.urls')),
    path('Inscrire/', include('creer_compte.urls')),
    path('connect/', include('connexion.urls')),
    path('greeneur/', include('user.urls')),
    path('composteur/', include('composteur.urls')),

]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)