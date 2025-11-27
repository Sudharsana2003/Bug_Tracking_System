from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Show username instead of ID

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'created_at')  # User is always the logged-in user
