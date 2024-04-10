from django.contrib import admin
from sem3app.models import Author, Post, Comment
from hw3app.models import Client, Product, Order
# Register your models here.

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
