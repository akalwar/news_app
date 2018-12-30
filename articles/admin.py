from django.contrib import admin
from . import models

class CommentInline(admin.StackedInline):
    model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ CommentInline,]

admin.site.register(models.Article)
admin.site.register(models.Comment)

