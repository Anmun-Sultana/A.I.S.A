from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self): return self.name

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={"role":"staff"})

    class Meta:
        unique_together = ("course", "name")

    def __str__(self): return f"{self.code} - {self.name}"

class Notification(models.Model):
    AUDIENCE_CHOICES = (
        ("all", "All Users"),
        ("students", "Students"),
        ("staff", "Staff"),
    )
    title = models.CharField(max_length=150)
    body = models.TextField()
    audience = models.CharField(max_length=20, choices=AUDIENCE_CHOICES, default="all")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self): return self.title

class LeaveRequest(models.Model):
    STATUS_CHOICES = (("pending","Pending"),("approved","Approved"),("rejected","Rejected"))
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leave_requests")
    reason = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="leave_reviews")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f"{self.applicant.username} ({self.status})"
