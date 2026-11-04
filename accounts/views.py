from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from .forms import (
    CustomUserCreationForm,
    StyledAuthenticationForm,
    UserProfileForm,
)
from .models import CustomUser



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


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    template_name = "accounts/profile_form.html"
    success_url = reverse_lazy("dashboard")

    def get_object(self, queryset=None):
        return self.request.user