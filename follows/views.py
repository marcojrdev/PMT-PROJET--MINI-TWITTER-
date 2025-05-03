from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Follow
from .serializers import FollowSerializer
from rest_framework.generics import ListAPIView

class FollowCreateView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user) 

class FollowDeleteView(generics.DestroyAPIView):
    queryset = Follow.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        follower =self.request.user
        following_id = self.kwargs['id']
        return Follow.objects.get(follower=follower, following_id=following_id)
    
class FollowingListView(ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)
    
class FollowerListView(ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)