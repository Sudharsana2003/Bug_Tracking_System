# apps/bugs/serializers.py
from rest_framework import serializers
from .models import Bug
from django.contrib.auth import get_user_model

User = get_user_model()

class BugSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')  # Reporter/creator username

    class Meta:
        model = Bug
        fields = [
            'id', 'project', 'title', 'description', 'status', 'priority',
            'severity', 'created_by', 'assigned_to', 'created_at',
            'updated_at', 'due_date'
        ]
        read_only_fields = ('created_by',)

    def validate_assigned_to(self, value):
        user = self.context['request'].user
        # Reporter cannot assign bugs
        if user.groups.filter(name='Reporter').exists() and value is not None:
            raise serializers.ValidationError("Reporters cannot assign bugs.")
        return value

    def validate_status(self, value):
        user = self.context['request'].user
        # Developers cannot change status of bugs not assigned to them
        if user.groups.filter(name='Developer').exists():
            if self.instance and self.instance.assigned_to != user:
                raise serializers.ValidationError("You can only change status for bugs assigned to you.")
        return value

    def validate_priority(self, value):
        user = self.context['request'].user
        if user.groups.filter(name='Developer').exists():
            if self.instance and self.instance.assigned_to != user:
                raise serializers.ValidationError("You can only change priority for bugs assigned to you.")
        return value

    def validate_severity(self, value):
        user = self.context['request'].user
        if user.groups.filter(name='Developer').exists():
            if self.instance and self.instance.assigned_to != user:
                raise serializers.ValidationError("You can only change severity for bugs assigned to you.")
        return value

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        # Prevent reporters from assigning bugs on update
        if user.groups.filter(name='Reporter').exists():
            validated_data.pop('assigned_to', None)
            validated_data.pop('status', None)
            validated_data.pop('priority', None)
            validated_data.pop('severity', None)
            validated_data.pop('due_date', None)
        # Developers can only update assigned bugs fields
        elif user.groups.filter(name='Developer').exists():
            if instance.assigned_to != user:
                # prevent editing anything
                raise serializers.ValidationError("You can only update bugs assigned to you.")
        return super().update(instance, validated_data)
