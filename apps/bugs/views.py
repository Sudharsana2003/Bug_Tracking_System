# apps/bugs/views.py
from rest_framework.viewsets import ModelViewSet
from .models import Bug
from .serializers import BugSerializer
from .permissions import BugPermission

class BugViewSet(ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
    permission_classes = [BugPermission]

    def perform_create(self, serializer):
        # Ensure the creator is always the logged-in user
        serializer.save(created_by=self.request.user)
