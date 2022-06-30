from .models import *
from rest_framework import serializers


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [ 'author_id', 'id', 'categoryType', 'dateCreation', 'title', 'text', 'rating']
