# apps/bugs/admin.py
from django.contrib import admin
from .models import Bug

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project',
        'created_by',
        'assigned_to',
        'status',
        'priority',
        'severity',
        'due_date',
        'created_at',
        'updated_at',  # <--- Add this line
    )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return []

        readonly = ['created_by', 'assigned_to', 'created_at', 'updated_at']

        if request.user.groups.filter(name='Developer').exists():
            if obj and obj.assigned_to != request.user:
                readonly += ['title', 'description', 'project', 'status', 'priority', 'severity', 'due_date']
        elif request.user.groups.filter(name='Reporter').exists():
            readonly += ['status', 'priority', 'severity', 'due_date']

        return readonly

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return True
        if obj and request.user.groups.filter(name='Developer').exists():
            return obj.assigned_to == request.user
        if obj and request.user.groups.filter(name='Reporter').exists():
            return False
        return False

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
