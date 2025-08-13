from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm

@login_required
def route_dashboard(request):
    role = getattr(request.user, "role", "student")
    if role == "admin":
        return redirect("accounts:dashboard_admin")
    elif role == "staff":
        return redirect("accounts:dashboard_staff")
    return redirect("accounts:dashboard_student")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("accounts:route_dashboard")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        user = authenticate(request, username=uname, password=pwd)
        if user:
            login(request, user)
            return redirect("accounts:route_dashboard")
        messages.error(request, "Invalid credentials")
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile.html", {"form": form})

@login_required
def dashboard_admin(request):
    return render(request, "accounts/dashboard_admin.html")

@login_required
def dashboard_staff(request):
    return render(request, "accounts/dashboard_staff.html")

@login_required
def dashboard_student(request):
    return render(request, "accounts/dashboard_student.html")
