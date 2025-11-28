from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied

from .models import Comment
from .serializers import CommentSerializer
from .permissions import CommentPermission


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]

    def get_queryset(self):
        user = self.request.user
        queryset = Comment.objects.all().order_by('-created_at')

        # 🔍 SEARCH SUPPORT
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(content__icontains=search) |
                Q(user__username__icontains=search) |
                Q(bug__title__icontains=search)
            )
        return queryset
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        user = self.request.user

        # Users can edit ONLY their own comments
        if instance.user != user:
            raise PermissionDenied("You can update only your own comments.")

        serializer.save()
