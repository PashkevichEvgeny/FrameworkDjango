from django.db import models

# Create your models here.


class Coin(models.Model):
    """Задача 1"""
    objects = None
    side = models.BooleanField()
    throw_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name_side = 'Выпал ОРЕЛ' if self.side else 'Выпала РЕШКА'
        return f'{name_side}, время подбрасывания монеты {format(self.throw_time, "%m-%d %H:%M")}'

    def __repr__(self):
        return f'Coin({self.side=}, {self.throw_time=})'


class Author(models.Model):
    """## Задание №3
    Создайте модель Автор.
    Модель должна содержать следующие поля:
    - имя до 100 символов
    - фамилия до 100 символов
    - почта
    - биография
    - день рождения
    Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.
    """
    objects = None
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    dob = models.DateField()

    def full_name(self):
        return f'{self.name} {self.surname}'


class Post(models.Model):
    """
    ## Задание №4
    Создайте модель Статья (публикация).
    Авторы из прошлой задачи могут писать статьи.
    У статьи может быть только один автор.
    У статьи должны быть следующие обязательные поля:
    - заголовок статьи с максимальной длиной 200 символов
    - содержание статьи
    - дата публикации статьи
    - автор статьи с удалением связанных объектов при удалении автора
    - категория статьи с максимальной длиной 100 символов
    - количество просмотров статьи со значением по умолчанию 0
    - флаг, указывающий, опубликована ли статья со значением по умолчанию False
    """
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_posts')
    category = models.CharField(max_length=100)
    number_post_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title=}, {self.author.full_name()=}'


class Comment(models.Model):
    """
    ## Задание №6
    Создайте модель Комментарий.
    Авторы могут добавлять комментарии к своим и чужим статьям.
    Т.е. у комментария может быть один автор.
    И комментарий относится к одной статье.
    У модели должны быть следующие поля
    - автор
    - статья
    - комментарий
    - дата создания
    - дата изменения
    """
    objects = None
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_for_post')
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
