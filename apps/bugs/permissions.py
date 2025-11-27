from rest_framework.permissions import BasePermission, SAFE_METHODS

class BugPermission(BasePermission):
    """
    Custom permission for Bugs according to roles:

    - Superuser: Full access
    - Admin / Manager: Full access
    - Developer: Can view all bugs, update only assigned bugs
    - Reporter: Can create bugs, view all bugs, cannot update assigned_to
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

        # Developers: can list and retrieve all bugs
        if user.groups.filter(name='Developer').exists():
            if view.action in ['list', 'retrieve']:
                return True
            # PUT/PATCH handled in object permission
            if view.action in ['update', 'partial_update']:
                return True
            return False

        # Reporter: can list/retrieve and create
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

        # Developer: can view all, update only assigned bugs
        if user.groups.filter(name='Developer').exists():
            if request.method in SAFE_METHODS:
                return True  # can view all
            # For unsafe methods (PUT/PATCH), allow only if assigned
            return obj.assigned_to == user

        # Reporter: view all, can create only
        if user.groups.filter(name='Reporter').exists():
            if request.method in SAFE_METHODS:
                return True  # can view all
            if request.method == 'POST':
                return True
            return False  # cannot PUT/PATCH/DELETE

        return False
