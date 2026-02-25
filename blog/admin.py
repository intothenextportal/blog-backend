from django.contrib import admin
from .models import Post, PostContent


class PostContentInline(admin.TabularInline):
    model = PostContent
    extra = 1
    fields = ['order', 'type', 'text', 'image_url', 'image_alt', 'blockquote_footer']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'date', 'is_new']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostContentInline]


@admin.register(PostContent)
class PostContentAdmin(admin.ModelAdmin):
    list_display = ['post', 'type', 'order']
    list_filter = ['post', 'type']
