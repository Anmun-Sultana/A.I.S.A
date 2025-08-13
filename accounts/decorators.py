from django.contrib.auth.decorators import user_passes_test

def role_required(role):
    def check(user):
        return user.is_authenticated and user.role == role
    return user_passes_test(check, login_url="accounts:login")

admin_required = role_required("admin")
staff_required = role_required("staff")
student_required = role_required("student")
