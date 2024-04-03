from django.core.management.base import BaseCommand

from sem2app.models import Post, Author


class Command(BaseCommand):
    help = "Search Posts By Author Name"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name Author Of Posts')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        author = Author.objects.filter(name=name).first()
        posts = Post.objects.filter(author=author).all()
        for post in posts:
            self.stdout.write(f'{post} {post.content=}')
