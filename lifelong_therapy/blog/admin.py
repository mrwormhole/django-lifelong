from django.contrib import admin
from .models import Author, Post

admin.site.site_header = "Lifelong Admin"
admin.site.site_title = "Lifelong Admin Area"
admin.site.index_title = "Welcome to Lifelong Admin Area"

admin.site.register(Author)
admin.site.register(Post)
