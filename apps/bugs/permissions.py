from rest_framework.permissions import BasePermission, SAFE_METHODS

class BugPermission(BasePermission):
    """
    Custom permission for Bugs according to roles:
    - Superuser: Full access
    - Admin / Manager: Full access
    - Developer: Can view assigned bugs
    - Reporter: Can create bugs and view their own bugs
    """

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        # Superuser full access
        if user.is_superuser:
            return True

        # Admin / Manager full access
        if user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return True

        # Developers can view (list/retrieve) only
        if user.groups.filter(name='Developer').exists():
            if view.action in ['list', 'retrieve']:
                return True
            return False

        # Reporters can create and view list/retrieve their own bugs
        if user.groups.filter(name='Reporter').exists():
            if view.action in ['list', 'retrieve', 'create']:
                return True
            return False

        return False

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Superuser full access
        if user.is_superuser:
            return True

        # Admin / Manager full access
        if user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return True

        # Developer: can view bugs assigned to them
        if user.groups.filter(name='Developer').exists():
            if request.method in SAFE_METHODS:
                return obj.assigned_to == user
            return False  # Developers cannot modify other fields

        # Reporter: can view their own created bugs
        if user.groups.filter(name='Reporter').exists():
            if request.method in SAFE_METHODS:
                return obj.created_by == user
            # Reporter cannot update or assign
            if request.method == 'POST':
                return True
            return False

        return False
