# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Post, Category
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
#
#
# # в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
# @receiver(post_save, sender=Post)
# def notify_category_subscribers(sender, **kwargs):
#     post_category_id = sender.postCategory
#     category_id = Category.objects.get(id=post_category_id).id
#     category_name = Category.objects.get(id=category_id).name
#
#     qs = Category.objects.filter(name=category_name).values('subscribers__username', 'subscribers__email')
#     for subs in qs:
#         subscriber_username = subs.get('subscribers__username')
#         subscriber_email = subs.get('subscribers__email')
#         html_content = render_to_string(
#             'news_updated.html',
#             {
#                 'subscriber_username': subscriber_username,
#                 'new_post': sender
#             }
#         )
#         msg = EmailMultiAlternatives(
#             subject=f'{sender.title}',
#             body=f"Здравствуй, {subscriber_username}. Новая статья в твоём любимом разделе!",
#             from_email='b.kanycty@yandex.ru',
#             to=[subscriber_email],
#         )
#
#         msg.attach_alternative(html_content, "text/html")
#
#         msg.send()
