from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Существующее представление для списка постов
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

# НОВОЕ представление для одного поста
class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer