from django.core.management.base import BaseCommand

from sem2app.models import Post


class Command(BaseCommand):
    help = "Read Post By ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Post ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.filter(pk=pk).first()
        self.stdout.write(f'{post} {post.content=}')
