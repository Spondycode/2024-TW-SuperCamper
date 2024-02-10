from django.urls import path
from .views import inbox_view, search_users


urlpatterns = [
    path('', inbox_view, name="inbox"),
    path('c/<conversation_id>/', inbox_view, name="inbox"),
    path('search_users/', search_users, name="inbox-searchusers" )
]