from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serializers import CommentSerializer
from .permissions import CommentPermission

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Automatically set the logged-in user
