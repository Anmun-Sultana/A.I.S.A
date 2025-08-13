from django.db import models
from django.conf import settings
from adminpanel.models import Subject

User = settings.AUTH_USER_MODEL

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"role":"student"})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
    marked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="attendance_marked")

    class Meta:
        unique_together = ("student","subject","date")

    def __str__(self): return f"{self.student} - {self.subject} - {self.date}"
