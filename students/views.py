from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.decorators import student_required
from staff.models import Attendance
from adminpanel.models import LeaveRequest
from django.contrib import messages
from datetime import date

@login_required
@student_required
def attendance_report(request):
    qs = Attendance.objects.filter(student=request.user).select_related("subject").order_by("-date")
    present = qs.filter(present=True).count()
    total = qs.count() or 1
    percent = round((present/total)*100, 2)
    return render(request, "students/attendance_report.html", {"items": qs, "percent": percent})

@login_required
@student_required
def leave_apply(request):
    if request.method == "POST":
        reason = request.POST.get("reason","").strip()
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")
        if reason and from_date and to_date:
            LeaveRequest.objects.create(applicant=request.user, reason=reason, from_date=from_date, to_date=to_date)
            messages.success(request, "Leave request submitted.")
            return redirect("students:leave_list")
    return render(request, "students/leave_apply.html")

@login_required
@student_required
def leave_list(request):
    items = LeaveRequest.objects.filter(applicant=request.user).order_by("-created_at")
    return render(request, "students/leave_list.html", {"items": items})
