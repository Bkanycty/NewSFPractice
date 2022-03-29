from celery import shared_task
from django.template.loader import render_to_string

from .models import Category, Post

from django.core.mail import EmailMultiAlternatives

from .models import Post, Author


@shared_task
def weekly_spammer():
    for category in Category.objects.all():
        qs = Category.objects.filter(name=category.name).values('subscribers__username', 'subscribers__email')
        posts_qs = Post.objects.filter(postCategory=category.id).order_by('-dateCreation')[0:5]
        for subs in qs:
            subscriber_username = subs.get('subscribers__username')
            subscriber_email = subs.get('subscribers__email')
            html_content = render_to_string(
                'news_updated_weekly.html',
                {
                    'subscriber_username': subscriber_username,
                    'posts_qs': posts_qs,
                    'category': category.name
                }
            )

            msg = EmailMultiAlternatives(
                subject=f"Еженедельное издание 'Bkanycty news'",
                body="",
                from_email='b.kanycty@yandex.ru',
                to=[subscriber_email],
            )

            msg.attach_alternative(html_content, "text/html")

            msg.send()
