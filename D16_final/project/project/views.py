from django.views.generic import TemplateView


class Posts(TemplateView):
    template_name = 'posts.html'