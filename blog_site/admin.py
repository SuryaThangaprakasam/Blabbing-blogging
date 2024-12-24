from django.contrib import admin
from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','contact','email','profile_pic','is_blocked')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'last_modified')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'author', 'blog', 'created_at')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)