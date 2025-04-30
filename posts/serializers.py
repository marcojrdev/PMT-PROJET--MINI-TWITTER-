from rest_framework import serializers
from .models import Post, Like

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    likes_count = serializers.SerializerMethodField()

class Meta:
    model =  Post
    fields = ['id', 'author', 'author_username', 'content', 'image', 'created_at', 'likes_count']
    read_only_fields = ['author', 'created_at', 'likes_count']

def get_likes_count(self, obj):
    return obj.likes.count()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['user', 'created_at']