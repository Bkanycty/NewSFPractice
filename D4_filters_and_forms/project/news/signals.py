from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Category, PostCategory
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(post_save, sender=PostCategory)
def notify_category_subscribers(sender, instance, created, **kwargs):
    if created:

        category_name = instance.categoryThrough
        title = Post.objects.get(id=instance.postThrough.id).title
        qs = Category.objects.filter(name=category_name).values('subscribers__username', 'subscribers__email')
        for subs in qs:
            subscriber_username = subs.get('subscribers__username')
            subscriber_email = subs.get('subscribers__email')
            html_content = render_to_string(
                'news_updated.html',
                {
                    'subscriber_username': subscriber_username,
                    'new_post': Post.objects.get(id=instance.postThrough.id)
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'{title}',
                body=f"Здравствуй, {subscriber_username}. Новая статья в твоём любимом разделе!",
                from_email='b.kanycty@yandex.ru',
                to=[subscriber_email],
            )

            msg.attach_alternative(html_content, "text/html")

            msg.send()
