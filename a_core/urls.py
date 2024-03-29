"""
URL configuration for a_core project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("bossman/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("inbox/", include("a_inbox.urls")),
    path("", include("a_plot.urls")),
    path("", include("a_users.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)