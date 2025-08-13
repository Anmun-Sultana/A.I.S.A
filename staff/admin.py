from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student","subject","date","present","marked_by")
    list_filter = ("subject","date","present")
