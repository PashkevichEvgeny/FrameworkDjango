import random

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView


# Create your views here.

# view as a function
from sem3app.models import Author, Post, Comment


def main(request):
    context = {"name": "John"}
    return render(request, "sem3app/index.html", context)


# view as a class
class TemplateAbout(TemplateView):
    template_name = "sem3app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Python'
        context['number'] = 'трех'
        return context


def games(throws, size, message) -> dict:
    return {'results': [f'{message} - {random.randint(*size)}' for _ in range(throws)]}


def head_tails(request, throws):
    context = games(throws, (0, 1), 'На монетке')
    context.update({'title': 'Орел-Решка'})
    return render(request, "sem3app/games.html", context)


def dice(request, throws):
    context = games(throws, (1, 6), 'Вам выпало')
    context.update({'title': 'Кости'})
    return render(request, "sem3app/games.html", context)


def rand100(request, throws):
    context = games(throws, (0, 100), 'Случайное число')
    context.update({'title': 'Случайное число от 0 до 100'})
    return render(request, "sem3app/games.html", context)


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')
    return render(request, 'sem3app/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.number_post_views += 1
    post.save()
    comments = Comment.objects.filter(post=post_id).order_by('created')
    return render(request, 'sem3app/post_full.html', {'post': post, 'author': post.author, 'comments': comments})
