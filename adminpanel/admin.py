from django.contrib import admin
from .models import Course, Subject, Notification, LeaveRequest

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Notification)
admin.site.register(LeaveRequest)
