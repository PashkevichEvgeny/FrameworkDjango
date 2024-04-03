from django.core.management.base import BaseCommand

from sem2app.models import Post, Comment


class Command(BaseCommand):
    help = "Search Comments By Title Post"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Title Post')

    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        post = Post.objects.filter(title=title).first()
        comments = Comment.objects.filter(post=post).all()
        for comment in comments:
            self.stdout.write(f'{comment} {comment.content=}')