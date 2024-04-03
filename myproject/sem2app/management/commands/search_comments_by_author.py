from django.core.management.base import BaseCommand

from sem2app.models import Author, Comment


class Command(BaseCommand):
    help = "Search Comments By Title Post"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name Author')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        author = Author.objects.filter(name=name).first()
        comments = Comment.objects.filter(author=author).all()
        for comment in comments:
            self.stdout.write(f'{comment} {comment.content=}')