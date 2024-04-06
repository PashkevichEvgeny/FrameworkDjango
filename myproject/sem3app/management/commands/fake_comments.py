import random
from random import choices

from django.core.management.base import BaseCommand
from sem3app.models import Author, Post, Comment


def text_comment():
    LOREM = """Lorem ipsum dolor sit amet, consectetur adipisicing elit.
               Accusamus accusantium aut beatae consequatur consequuntur cumque, delectus et illo iste maxime
               nihil non nostrum odio officia, perferendis placeat quasi quibusdam quisquam quod sunt
               tempore temporibus ut voluptatum? A aliquam culpa ducimus, eaque eum illo mollitia nemo
               tempore unde vero! Blanditiis deleniti ex hic, laboriosam maiores odit officia praesentium
               quae quisquam ratione, reiciendis, veniam. Accusantium assumenda consectetur consequatur
               consequuntur corporis dignissimos ducimus eius est eum expedita illo in, inventore 
               ipsum iusto maiores minus mollitia necessitatibus neque nisi optio quasi quo quod,
               quos rem repellendus temporibus totam unde vel velit vero vitae voluptates."""
    t = []
    flag = False
    for word in choices(LOREM.split(), k=16):
        if word[-1] in '.!?':
            flag = True
        elif flag:
            flag = False
            t.append(word.title())
        t.append(word)
    t[0], t[-1] = t[0].title(), t[-1] + '.'
    t[-1] = t[-1].replace('.,', '.')
    return t


class Command(BaseCommand):
    help = "Generate fake comments."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Enter number comments.')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        posts = Post.objects.all()
        authors = Author.objects.all()
        for post in posts:
            for _ in range(random.randint(1, count + 1)):
                comment = Comment(author=random.choice(authors),
                                  post=post,
                                  comment=" ".join(text_comment()))
                self.stdout.write(f'{comment}')
                comment.save()
