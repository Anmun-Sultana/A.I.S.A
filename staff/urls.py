from django.urls import path
from . import views

urlpatterns = [
    path("attendance/mark/", views.attendance_mark, name="attendance_mark"),
    path("leaves/review/", views.leave_review_list, name="leave_review_list"),
]
