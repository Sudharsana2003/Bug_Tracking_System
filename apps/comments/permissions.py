from rest_framework import permissions

class CommentPermission(permissions.BasePermission):
    """
    Custom permission for Comment:
    - Admin / Manager: can edit/delete all comments
    - User: can edit/delete only their own comments
    - Read access for everyone authenticated
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
            return True

        # Users can update/delete only their own comments
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.user == request.user

        return True  # Read-only allowed for all authenticated
