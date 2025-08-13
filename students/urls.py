from django.urls import path
from . import views

urlpatterns = [
    path("attendance/", views.attendance_report, name="attendance_report"),
    path("leave/apply/", views.leave_apply, name="leave_apply"),
    path("leave/", views.leave_list, name="leave_list"),
]
