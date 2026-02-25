from rest_framework import serializers
from .models import Post, PostContent


class PostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostContent
        fields = ['type', 'text', 'image_url', 'image_alt', 'blockquote_footer', 'order']


class PostListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for the homepage post list."""
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'date', 'hero_image', 'hero_image_alt', 'is_new', 'nav_label']


class PostDetailSerializer(serializers.ModelSerializer):
    """Full serializer including post content blocks."""
    content = PostContentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'date', 'hero_image', 'hero_image_alt', 'is_new', 'nav_label', 'content']
