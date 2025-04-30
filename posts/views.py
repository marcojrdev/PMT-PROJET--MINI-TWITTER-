from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Like
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')
    
class LikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete()
            return Response({'status': 'Post descurtido'}, status=status.HTTP_200_OK)
        return Response({'status': 'Post curtido'}, status=status.HTTP_201_CREATED)