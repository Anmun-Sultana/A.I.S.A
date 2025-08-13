from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.decorators import admin_required
from .models import Course, Subject, Notification, LeaveRequest
from .forms import CourseForm, SubjectForm, NotificationForm

@login_required
@admin_required
def course_list(request):
    items = Course.objects.all()
    return render(request, "adminpanel/course_list.html", {"items": items})

@login_required
@admin_required
def course_form(request, pk=None):
    obj = get_object_or_404(Course, pk=pk) if pk else None
    if request.method == "POST":
        form = CourseForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Course saved.")
            return redirect("adminpanel:course_list")
    else:
        form = CourseForm(instance=obj)
    return render(request, "adminpanel/course_form.html", {"form": form})

@login_required
@admin_required
def subject_form(request, pk=None):
    obj = get_object_or_404(Subject, pk=pk) if pk else None
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Subject saved.")
            return redirect("adminpanel:course_list")
    else:
        form = SubjectForm(instance=obj)
    return render(request, "adminpanel/subject_form.html", {"form": form})

@login_required
def notification_list(request):
    # audience filter by role
    role = getattr(request.user, "role", "student")
    qs = Notification.objects.all().order_by("-created_at")
    if role == "student":
        qs = qs.filter(audience__in=["all","students"])
    elif role == "staff":
        qs = qs.filter(audience__in=["all","staff"])
    return render(request, "adminpanel/notification_list.html", {"items": qs})

@login_required
@admin_required
def notification_form(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            messages.success(request, "Notification published.")
            return redirect("adminpanel:notification_list")
    else:
        form = NotificationForm()
    return render(request, "adminpanel/notification_form.html", {"form": form})

@login_required
@admin_required
def leave_review_list(request):
    items = LeaveRequest.objects.all().order_by("-created_at")
    return render(request, "staff/leave_review_list.html", {"items": items})

@login_required
@admin_required
def leave_review_action(request, pk, action):
    lr = get_object_or_404(LeaveRequest, pk=pk)
    if action in ["approved","rejected"]:
        lr.status = action
        lr.reviewed_by = request.user
        lr.save()
    return redirect("adminpanel:leave_review_list")
