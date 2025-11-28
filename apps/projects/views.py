from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsAdminOrManager


# /api/projects/
class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all().order_by('-created_at')

        # SEARCH SUPPORT
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(created_by__username__icontains=search)
            )

        return queryset

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrManager()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# /api/projects/<id>/
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminOrManager()]
        return [IsAuthenticated()]
