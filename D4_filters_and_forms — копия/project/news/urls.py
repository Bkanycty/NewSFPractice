from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, upgrade_me


urlpatterns = [
    path('', NewsList.as_view()),
    path('search/', NewsSearch.as_view()),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),  # Ссылка на детали товара
    path('add/', NewsCreate.as_view(), name='news_create'),  # Ссылка на создание товара
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
]
