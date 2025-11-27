# apps/comments/admin.py
from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('bug', 'user', 'content', 'created_at')
    list_filter = ('bug', 'user', 'created_at')
    search_fields = ('content', 'user__username')
    ordering = ('-created_at',)

    readonly_fields = ('created_at',)

    # --------------------------------
    # ADD PERMISSION
    # --------------------------------
    def has_add_permission(self, request):
        # Everyone can add comment
        return True

    # --------------------------------
    # CHANGE PERMISSION
    # --------------------------------
    def has_change_permission(self, request, obj=None):

        # Admin & Manager → Full access
        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return True

        # ADD PAGE → allow access
        if obj is None:
            return True

        # Developer & Reporter → Only their own comments
        if obj.user == request.user:
            return True

        # Others → No edit
        return False

    # --------------------------------
    # DELETE PERMISSION
    # --------------------------------
    def has_delete_permission(self, request, obj=None):

        # Only Admin & Manager can delete comments
        return request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists()

    # --------------------------------
    # FIELD LOCKING
    # --------------------------------
    def get_readonly_fields(self, request, obj=None):

        # ADD PAGE → No readonly fields
        if obj is None:
            return []

        # Admin & Manager → Editable all
        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return []

        # Developer & Reporter editing OWN comment
        if obj.user == request.user:
            return ['bug', 'user', 'created_at']

        # Viewing OTHER users' comment
        return ['bug', 'user', 'content', 'created_at']

    # --------------------------------
    # AUTO OWNER SET
    # --------------------------------
    def save_model(self, request, obj, form, change):

        # Auto assign owner on create
        if not change:
            obj.user = request.user

        super().save_model(request, obj, form, change)
