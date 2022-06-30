from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.utils.translation import gettext as _  # импортируем функцию для перевода

from rest_framework import viewsets
from rest_framework import permissions

from news.serializers import *
from news.models import *


class NewsViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(categoryType='NW')
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArticlesViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(categoryType='AR')
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Home(TemplateView):
    template_name = 'home.html'


# Create your views here.

class Index(View):
    def get(self, request):
        string = _('Привет мир')

        return HttpResponse(string)
