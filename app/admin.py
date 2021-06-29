from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Category, Regions, Blog, PicturesFromTheBlog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Regions)
class RegiosnsAdmin(TranslatableAdmin):
    list_display = ('name',)


@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    list_display = ('title', 'category')


# @admin.register(Hashtags)
# class HashtagsAdmin(admin.ModelAdmin):
#     list_display = ('name', )


@admin.register(PicturesFromTheBlog)
class PicturesAdmin(admin.ModelAdmin):
    list_display = ('owner', )
