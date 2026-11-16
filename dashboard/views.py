from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView
from accounts.models import CustomUser


class CustomerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        if request.user.role != CustomUser.Role.CUSTOMER:
            return redirect("admin_dashboard")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["member_count"] = CustomUser.objects.filter(role=CustomUser.Role.CUSTOMER).count()
        context["is_admin"] = False
        return context


class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "dashboard/admin_panel.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        if request.user.role != CustomUser.Role.ADMIN:
            messages.error(request, "You do not have permission to access the admin dashboard.")
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        user = self.request.user
        return user.role == CustomUser.Role.ADMIN

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customer_count"] = CustomUser.objects.filter(role=CustomUser.Role.CUSTOMER).count()
        context["admin_count"] = CustomUser.objects.filter(role=CustomUser.Role.ADMIN).count()
        return context