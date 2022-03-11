from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, upgrade_me, \
    CategoriesList, Celebrities, subscribe_celebrities, Games, subscribe_games, Cooking, subscribe_cooking, News, \
    subscribe_news, Politics, subscribe_politics, Sport, subscribe_sport, Technologies, subscribe_technologies, Humor, \
    subscribe_humor

urlpatterns = [
    path('', NewsList.as_view()),
    path('search/', NewsSearch.as_view()),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),  # Ссылка на детали товара
    path('add/', NewsCreate.as_view(), name='news_create'),  # Ссылка на создание товара
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('categories/', CategoriesList.as_view(), name='category_selection'),
    path('Знаменитости/', Celebrities.as_view(), name='celebrities'),
    path('subscribe_celebrities/', subscribe_celebrities, name='subscribe_celebrities'),
    path('Игры/', Games.as_view(), name='Games'),
    path('subscribe_games/', subscribe_games, name='subscribe_games'),
    path('Кулинария/', Cooking.as_view(), name='cooking'),
    path('subscribe_cooking/', subscribe_cooking, name='subscribe_cooking'),
    path('Новости/', News.as_view(), name='News'),
    path('subscribe_news/', subscribe_news, name='subscribe_news'),
    path('Политика/', Politics.as_view(), name='politics'),
    path('subscribe_politics/', subscribe_politics, name='subscribe_politics'),
    path('Спорт/', Sport.as_view(), name='sport'),
    path('subscribe_Sport/', subscribe_sport, name='subscribe_sport'),
    path('Технологии', Technologies.as_view(), name='technologies'),
    path('subscribe_technologies/', subscribe_technologies, name='subscribe_technologies'),
    path('Юмор/', Humor.as_view(), name='Humor'),
    path('subscribe_humor/', subscribe_humor, name='subscribe_humor'),
]
