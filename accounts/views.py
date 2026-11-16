from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import (
    CustomUserCreationForm,
    StyledAuthenticationForm,
    UserProfileForm,
)
from .models import CustomUser


def logout_view(request):
    logout(request)
    return redirect("login")


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "accounts/profile.html"

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Account created successfully. You can now log in.")
        return response


class StyledLoginView(LoginView):
    form_class = StyledAuthenticationForm
    template_name = "registration/login.html"

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        if user.role == CustomUser.Role.ADMIN:
            return redirect("admin_dashboard")
        return redirect("dashboard")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    template_name = "accounts/profile_form.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user