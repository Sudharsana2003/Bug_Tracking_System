from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('bug', 'user', 'content', 'created_at')
    list_filter = ('bug', 'user')
    search_fields = ('content',)

    def has_change_permission(self, request, obj=None):
        # Admin / Manager -> Full change rights
        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return True

        # Developer / Reporter -> Only own comments
        if obj and obj.user == request.user:
            return True

        # Others -> no change
        return False

    def has_delete_permission(self, request, obj=None):
        # Admin / Manager -> delete allowed
        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return True

        # Developer / Reporter -> cannot delete
        return False

    def get_readonly_fields(self, request, obj=None):
        # Admin / Manager → No restriction
        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return []

        # Developer / Reporter editing own comment
        if obj and obj.user == request.user:
            return ['bug', 'user', 'created_at']

        # Developer / Reporter on other users' comment → View-only
        return ['bug', 'user', 'content', 'created_at']

    def has_add_permission(self, request):
        # Everyone can add comment
        return True

    def save_model(self, request, obj, form, change):
        # Force ownership on create
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)
