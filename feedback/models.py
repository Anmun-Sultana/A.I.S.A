from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Feedback(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    message = models.TextField()
    reply = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(null=True, blank=True)

    def __str__(self): return f"Feedback by {self.sender.username}"
