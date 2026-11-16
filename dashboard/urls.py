from django.urls import path
from .views import CustomerDashboardView, AdminDashboardView


urlpatterns = [
    path("", CustomerDashboardView.as_view(), name="dashboard"),
    path("admin-dashboard/", AdminDashboardView.as_view(), name="admin_dashboard"),
]