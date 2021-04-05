from django.core.management import BaseCommand
from user.models import NoteUser
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = u'Создание случайного пользователя'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')
        parser.add_argument('-p', '--prefix', type=str, help='Префикс для username')

    def handle(self, *args, **kwargs):
        prefix = kwargs['prefix']
        total = kwargs['total']
        for i in range(total):
            if prefix:
                username = f'{prefix}_{get_random_string()}'
            else:
                username = get_random_string()
            NoteUser.objects.create(username=get_random_string(), email=get_random_string())
