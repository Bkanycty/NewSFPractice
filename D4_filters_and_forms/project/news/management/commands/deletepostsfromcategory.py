from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category, PostCategory


class Command(BaseCommand):
    help = 'Удаляет все новости выбранной категории'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        parser.add_argument('category')

    def handle(self, category, **options):
        # здесь можете писать любой код, который выполнется при вызове вашей команды
        self.stdout.readable()
        self.stdout.write(
            f'Вы действительно хотите удалить все новости из категории {category}? yes/no')  # спрашиваем пользователя действительно ли он хочет удалить все товары
        answer = input()  # считываем подтверждение

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))

        elif answer == 'yes':
            try:
                Category.objects.get(name=category)
                for pc in PostCategory.objects.all():
                    if Category.objects.get(id=pc.categoryThrough.id).name == category:
                        Post.objects.get(id=pc.postThrough.pk).delete()
                        self.stdout.write(self.style.SUCCESS('Succesfully wiped news!'))

            except Category.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Категории {category} не существует'))