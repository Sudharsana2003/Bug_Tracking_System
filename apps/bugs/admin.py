from django.contrib import admin
from .models import Bug

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'created_by', 'assigned_to', 'status', 'priority')

    def get_readonly_fields(self, request, obj=None):
        """
        Make fields read-only based on user role:
        - Admin / Manager: can edit all
        - Developer: can edit status & priority only for assigned bugs
        - Reporter: all fields read-only except title, description, project
        """
        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return []

        readonly = ['created_by', 'assigned_to']  # default readonly for others

        if request.user.groups.filter(name='Developer').exists():
            if obj and obj.assigned_to != request.user:
                # Developer cannot edit other bugs
                readonly += ['title', 'description', 'project', 'status', 'priority']
            else:
                # Developer editing their own bug: only created_by & assigned_to readonly
                readonly += []

        elif request.user.groups.filter(name='Reporter').exists():
            # Reporter cannot edit created_by or assigned_to or status/priority
            readonly += ['status', 'priority']

        return readonly

    def has_change_permission(self, request, obj=None):
        # Admins/Managers can edit all
        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return True

        # Developers can only edit bugs assigned to them
        if obj and request.user.groups.filter(name='Developer').exists():
            return obj.assigned_to == request.user

        # Reporters cannot edit
        if obj and request.user.groups.filter(name='Reporter').exists():
            return False

        return False

    def save_model(self, request, obj, form, change):
        # Automatically set created_by on new bugs
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
