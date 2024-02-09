from django.contrib import admin
from .models import InboxMessage, Conversation

admin.site.register(InboxMessage)
admin.site.register(Conversation)


