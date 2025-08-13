from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("staff", "Staff"),
        ("student", "Student"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="student")

    def is_admin(self): return self.role == "admin"
    def is_staff_role(self): return self.role == "staff"   # avoid conflict with built-in is_staff
    def is_student(self): return self.role == "student"
