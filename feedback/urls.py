from django.urls import path
from . import views

urlpatterns = [
    path("", views.feedback_list, name="feedback_list"),
    path("new/", views.feedback_submit, name="feedback_submit"),
]
