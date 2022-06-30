"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from .views import Home, NewsViewset, ArticlesViewset
from django.views.decorators.cache import cache_page
from rest_framework import routers
# from news import views
from project import views

router = routers.DefaultRouter()
router.register(r'News', views.NewsViewset)
router.register(r'Articles', views.ArticlesViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('products/', include('simpleapp.urls')),
    path('news/', include('news.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
    path('', cache_page(5)(Home.as_view())),
    path('i18n/', include('django.conf.urls.i18n'))  # подключаем встроенные эндопинты для работы с локализацией
    # делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py) сами автоматически подключались когда мы их добавим.
]
