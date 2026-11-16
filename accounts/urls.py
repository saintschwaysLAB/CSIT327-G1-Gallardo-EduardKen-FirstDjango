from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView, SignUpView, StyledLoginView, logout_view

urlpatterns = [
    path("login/", StyledLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", logout_view, name="logout"),
    path("profile/", ProfileDetailView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
]