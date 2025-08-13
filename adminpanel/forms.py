from django import forms
from .models import Course, Subject, Notification

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name","description"]

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["course","name","code","teacher"]

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ["title","body","audience"]
