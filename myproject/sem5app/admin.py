from django.contrib import admin
from sem3app.models import Author, Post, Comment

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'dob']
    ordering = ['surname']
    list_filter = ['dob', 'surname']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'get_summary', 'category', 'number_post_views', 'status']
    ordering = ['-published', 'status']
    list_filter = ['author', 'category', 'status']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'comment']
    ordering = ['-created', 'updated']
    list_filter = ['author', 'post', 'created', 'updated']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
