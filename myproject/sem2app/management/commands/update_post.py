from django.core.management.base import BaseCommand

from sem2app.models import Post, Author


class Command(BaseCommand):
    help = "Update Title For Post By ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Enter ID Post')
        parser.add_argument('title', type=str, help='Add new title')

    def handle(self, *args, **kwargs):
        pk, title = kwargs['pk'], kwargs['title']
        post = Post.objects.filter(pk=pk).first()
        post.title = title
        post.save()
        self.stdout.write(f'{post}')
