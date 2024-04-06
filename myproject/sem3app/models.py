from django.db import models


# Create your models here.
class Author(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField(default=None)
    dob = models.DateField(default=None)

    def full_name(self):
        return f'{self.name} {self.surname}'


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_posts')
    category = models.CharField(max_length=100, default='')
    number_post_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title=}, {self.author.full_name()=}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'
