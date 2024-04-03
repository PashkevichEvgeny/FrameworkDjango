from django.core.management.base import BaseCommand

from sem2app.models import Post, Author


class Command(BaseCommand):
    help = "Create Post"

    # def add_arguments(self, parser):
        # parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        # pk = kwargs.get('pk')
        author = Author.objects.filter(pk=1).first()
        d = {'title': 'Some Title', 'content': 'Some content', 'author': author, 'category': 'Memoir'}
        post = Post(**d)
        post.save()
        self.stdout.write(f'{post}')
