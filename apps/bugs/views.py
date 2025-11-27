# apps/bugs/views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from .models import Bug
from .serializers import BugSerializer
from .permissions import BugPermission

class BugViewSet(ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
    permission_classes = [BugPermission]

    def get_queryset(self):
        user = self.request.user
        # Developers can see all bugs, but can only edit assigned ones
        # Reporters can see all bugs
        return Bug.objects.all()

    def perform_create(self, serializer):
        # Automatically set the creator/reporter
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        user = self.request.user
        instance = self.get_object()

        # Developers can only update bugs assigned to them
        if user.groups.filter(name='Developer').exists() and instance.assigned_to != user:
            raise PermissionDenied("You can only update bugs assigned to you.")

        # Reporters cannot update restricted fields, serializer already handles it
        serializer.save()
