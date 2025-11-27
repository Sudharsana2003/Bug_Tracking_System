# apps/bugs/serializers.py
from rest_framework import serializers
from .models import Bug
from django.contrib.auth import get_user_model

User = get_user_model()

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = '__all__'
        read_only_fields = ('created_by',)  # Ensure reporters can't override

    def validate_assigned_to(self, value):
        user = self.context['request'].user
        # Reporter cannot assign bugs
        if user.groups.filter(name='Reporter').exists():
            if value is not None:
                raise serializers.ValidationError("Reporters cannot assign bugs.")
            return None
        return value

    def create(self, validated_data):
        # Automatically set the reporter/creator
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        # Prevent reporters from assigning bugs on update
        if user.groups.filter(name='Reporter').exists():
            validated_data.pop('assigned_to', None)
        return super().update(instance, validated_data)
