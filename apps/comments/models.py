import uuid
from django.db import models
from django.contrib.auth import get_user_model
from apps.bugs.models import Bug

User = get_user_model()

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.bug.title}"
