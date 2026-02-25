from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


@api_view(['GET'])
def post_list(request):
    """Return all posts - used for homepage cards and navbar dropdown."""
    posts = Post.objects.all()
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_detail(request, slug):
    """Return a single post with all its content blocks."""
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PostDetailSerializer(post)
    return Response(serializer.data)
