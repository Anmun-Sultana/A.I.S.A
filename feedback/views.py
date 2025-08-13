from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import FeedbackForm
from .models import Feedback

@login_required
def feedback_submit(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.sender = request.user
            fb.save()
            messages.success(request, "Feedback submitted.")
            return redirect("feedback:feedback_list")
    else:
        form = FeedbackForm()
    return render(request, "feedback/feedback_submit.html", {"form": form})

@login_required
def feedback_list(request):
    if request.user.role == "admin":
        items = Feedback.objects.all().order_by("-created_at")
    else:
        items = Feedback.objects.filter(sender=request.user).order_by("-created_at")
    return render(request, "feedback/feedback_list.html", {"items": items})
