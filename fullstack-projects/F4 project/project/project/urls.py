from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from RecipesApp import views
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r'categories', views.CategoriesViewset)
router.register(r'recipes', views.RecipesViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('openapi/', get_schema_view(
        title="Your Project",
        description="API for all things …"
    ), name='openapi-schema'),
]
