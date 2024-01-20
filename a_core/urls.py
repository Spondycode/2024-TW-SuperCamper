"""
URL configuration for a_core project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("a_plot.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
