from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.course_list, name="course_list"),
    path("courses/new/", views.course_form, name="course_new"),
    path("courses/<int:pk>/", views.course_form, name="course_edit"),
    path("subjects/new/", views.subject_form, name="subject_new"),
    path("subjects/<int:pk>/", views.subject_form, name="subject_edit"),
    path("notifications/", views.notification_list, name="notification_list"),
    path("notifications/new/", views.notification_form, name="notification_new"),
    path("leaves/review/", views.leave_review_list, name="leave_review_list"),
    path("leaves/review/<int:pk>/<str:action>/", views.leave_review_action, name="leave_review_action"),
]
