from django.contrib import admin
from .models import Message, Post
# Register your models here.
admin.site.register(Post)
admin.site.register(Message)