from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Respond
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(post_save, sender=Respond)
def notify_post_creator(sender, instance, created, **kwargs):
    if created:

        receiver_username = instance.post.author.authorUser.username
        receiver_email = instance.post.author.authorUser.email
        receiver_post = instance.post.title
        text = instance.text


        html_content = render_to_string(
            'respond_email.html',
            {
                'receiver_username': receiver_username,
                'new_respond': instance
            }
        )
        msg = EmailMultiAlternatives(
            subject=f'Отклик на ваше объявление ({receiver_post})',
            body=f"{text}",
            from_email='b.kanycty@yandex.ru',
            to=[receiver_email],
        )

        msg.attach_alternative(html_content, "text/html")

        msg.send()


@receiver(post_save, sender=Post)
def notify_respond_creator(sender, instance, **kwargs):

    print(sender, instance, list(dict(**kwargs).values()))
    # post_creator_username = instance.author.authorUser.username
    # receiver_username = instance.author.authorUser.username
    # receiver_email = instance.author.authorUser.email
    # receiver_post = instance.post.text
    # text = f'Пользователь {sender_username} принял ваш отклик на объявление \n {receiver_post}'
    # html_content = render_to_string(
    #     'respond_accepted_email.html',
    #     {
    #         'receiver_username': receiver_username,
    #         'sender_username': sender_username,
    #         'new_respond': instance,
    #         'text': text
    #     }
    # )
    # msg = EmailMultiAlternatives(
    #     subject=f'Ваш отклик был принят',
    #     body=f"{text}",
    #     from_email='b.kanycty@yandex.ru',
    #     to=[receiver_email],
    # )
    #
    # msg.attach_alternative(html_content, "text/html")
    #
    # msg.send()