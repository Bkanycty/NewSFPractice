import requests
from django import forms
from django.forms import ModelForm, Form, ModelChoiceField
from .models import Post, Respond
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class PostForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['category', 'title', 'text', 'content']

class RespondForm(ModelForm):
    class Meta:
        model = Respond
        fields = ['text']

class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='registered')
        basic_group.user_set.add(user)
        return user
