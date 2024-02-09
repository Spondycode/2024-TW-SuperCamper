from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Conversation

@login_required
def inbox_view(request):
    conversation = Conversation.objects.first()
    context = {
        "conversation": conversation,
    }
    return render(request, "a_inbox/inbox.html", context)
