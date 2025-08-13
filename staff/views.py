from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.decorators import staff_required
from adminpanel.models import Subject, LeaveRequest
from accounts.models import User
from .models import Attendance
from django.contrib import messages
from datetime import date

@login_required
@staff_required
def attendance_mark(request):
    subjects = Subject.objects.filter(teacher=request.user)
    students = User.objects.filter(role="student").order_by("username")
    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        the_date = request.POST.get("date") or date.today().isoformat()
        present_ids = request.POST.getlist("present")
        if subject_id:
            subject = Subject.objects.get(pk=subject_id)
            for s in students:
                Attendance.objects.update_or_create(
                    student=s, subject=subject, date=the_date,
                    defaults={"present": str(s.id) in present_ids, "marked_by": request.user}
                )
            messages.success(request, "Attendance saved.")
    return render(request, "staff/attendance_mark.html", {"subjects": subjects, "students": students})

@login_required
@staff_required
def leave_review_list(request):
    items = LeaveRequest.objects.filter(applicant__role__in=["student","staff"]).order_by("-created_at")
    return render(request, "staff/leave_review_list.html", {"items": items})
