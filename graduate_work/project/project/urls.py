"""project URL Configuration

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
import allauth.urls
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from my_silant import views

from rest_framework import routers
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r'machines', views.MachineListApiView)
router.register(r'maintenances', views.MachineListApiView)
router.register(r'reclamations', views.ReclamationListApiView)

urlpatterns = [
    path('machine_api/', views.MachineListApiView.as_view()),
    path('maintenance_api/', views.MaintenanceListApiView.as_view()),
    path('reclamation_api/', views.ReclamationListApiView.as_view()),
    path('admin/', admin.site.urls),
    path('', include('my_silant.urls')),
    path('accounts/', include('allauth.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('openapi/', get_schema_view(
        title="my_silant",
        description="API for all things …"
    ), name='openapi-schema'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
