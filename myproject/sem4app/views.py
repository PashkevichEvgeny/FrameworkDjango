import logging

from django.shortcuts import render, get_object_or_404, redirect

from sem3app.models import Author, Post, Comment
from sem3app.views import head_tails, dice, rand100
from .forms import UserForm, GameForm, AddAuthorForm, AddPostForm, AddCommentForm

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'sem4app/user_form.html', {'form': form})


def game_form(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            name_game = form.cleaned_data['name_game']
            throws = form.cleaned_data['throws']
            match name_game:
                case 'H':
                    return head_tails(request, throws)
                case 'D':
                    return dice(request, throws)
                case 'R':
                    return rand100(request, throws)
            logger.info(f'Получили {name_game=}, {throws=}')
    else:
        form = GameForm()
    return render(request, 'sem4app/game_form.html', {'form': form})


def add_author(request):
    message = ''
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f'Получили {form.cleaned_data=}')
            message = f'Автор {" ".join(map(str, form.cleaned_data.values()))} сохранен'
    else:
        form = AddAuthorForm()
    return render(request, 'sem4app/user_form.html', {'form': form, 'message': message})


def add_post(request):
    message = ''
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = Post(title=form.cleaned_data['title'],
                        content=form.cleaned_data['content'],
                        author=Author.objects.get(pk=form.cleaned_data['author']),
                        category=form.cleaned_data['category'],)
            post.save()

            logger.info(f'Получили {form.cleaned_data=}')
            message = f'Статья {" ".join(map(str, form.cleaned_data.values()))} сохранена'
    else:
        form = AddPostForm()
    return render(request, 'sem4app/user_form.html', {'form': form, 'message': message})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.number_post_views += 1
    post.save()
    comments = Comment.objects.filter(post=post_id).order_by('-created')

    message = ''
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author=Author.objects.get(pk=form.cleaned_data['author']),
                              post=Post.objects.get(pk=post_id),
                              comment=form.cleaned_data['comment'],)
            comment.save()

            logger.info(f'Получили {form.cleaned_data=} {post_id=}')
            return redirect('post_full', post_id)
    else:
        form = AddCommentForm()
    return render(request, 'sem4app/post_full.html', {'post': post,
                                                      'author': post.author,
                                                      'comments': comments,
                                                      'form': form,
                                                      'message': message})

