from django.db.models import Q
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
        queryset = Bug.objects.all()

        # SEARCH SUPPORT
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(status__icontains=search) |
                Q(priority__icontains=search) |
                Q(severity__icontains=search) |
                Q(project__name__icontains=search) |
                Q(created_by__username__icontains=search) |
                Q(assigned_to__username__icontains=search)
            )

        # Developer restriction (Optional)
        if user.groups.filter(name="Developer").exists():
            queryset = queryset.filter(assigned_to=user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        user = self.request.user

        if user.groups.filter(name='Developer').exists() and instance.assigned_to != user:
            raise PermissionDenied("You can only update bugs assigned to you.")

        serializer.save()
