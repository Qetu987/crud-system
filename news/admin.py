from django.contrib import admin
from news.models import News, Comments


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'upvotes', 'author']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'new', 'author', 'date', 'contant']
    list_display_links = ['id', 'author']
    search_fields = ['id', 'author', 'new']