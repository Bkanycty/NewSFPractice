import requests
from django_filters import FilterSet, ModelChoiceFilter
from .models import *
from django.contrib.auth.models import User

class RespondsFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах

    class Meta:
        model = Respond
        fields = {
            'post': ['exact']
        }
