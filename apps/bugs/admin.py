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
        'updated_at',
    )

    list_filter = (
        'project',
        'status',
        'priority',
        'assigned_to',
        'created_at',
    )

    search_fields = ('title', 'description')
    ordering = ('-created_at',)

    # ROLE BASED READONLY CONTROL
    def get_readonly_fields(self, request, obj=None):

        # ADMINS & MANAGERS → Full control
        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return ('created_at', 'updated_at')

        # Common readonly
        readonly = ['created_by', 'updated_at', 'created_at']

        # DEVELOPERS
        if request.user.groups.filter(name='Developer').exists():
            if obj and obj.assigned_to != request.user:
                return readonly + [
                    'title', 'description', 'project',
                    'assigned_to', 'status',
                    'priority', 'severity', 'due_date'
                ]

            # Developer editing own bug
            return readonly + ['assigned_to']

        # REPORTERS
        if request.user.groups.filter(name='Reporter').exists():
            return readonly + [
                'assigned_to',
                'status',
                'priority',
                'severity',
                'due_date',
            ]

        return readonly

    # WHO CAN CHANGE BUGS?
    def has_change_permission(self, request, obj=None):

        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return True

        if obj and request.user.groups.filter(name='Developer').exists():
            return obj.assigned_to == request.user

        if obj and request.user.groups.filter(name='Reporter').exists():
            return False

        return False

    # SET CREATED BY AUTOMATICALLY
    def save_model(self, request, obj, form, change):

        if not change:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)
