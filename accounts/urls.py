from django.urls import path
from .views import ProfileUpdateView, SignUpView, StyledLoginView

urlpatterns = [
    path("login/", StyledLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
]