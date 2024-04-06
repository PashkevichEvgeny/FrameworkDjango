from django.urls import path
from .views import TemplateAbout, author_posts, post_full, rand100, head_tails, dice, main

urlpatterns = [
    path('main/', main, name='main'),
    path('about/', TemplateAbout.as_view(), name='about'),
    path('head-tails/<int:throws>', head_tails, name='head_tails'),
    path('dice/<int:throws>', dice, name='dice'),
    path('rand100/<int:throws>', rand100, name='rand100'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),
]