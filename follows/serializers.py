from rest_framework import serializers
from .models import Follow

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']
        read_only_fields = ['id', 'created_at', 'follower']


    def validate(self, data):
        user = self.context['request'].user
        if data['following'] == user:
            raise serializers.ValidationError("Você não pode se seguir.")
        return data