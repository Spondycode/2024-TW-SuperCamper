from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from a_users.models import Profile
from django.http import HttpResponse, Http404
from django.db.models import Q
from.models import InboxMessage, Conversation

@login_required
def inbox_view(request, conversation_id=None):
    my_conversations = Conversation.objects.filter(participants=request.user)
    if conversation_id:
        conversation = get_object_or_404(my_conversations, id=conversation_id)
    else:
        conversation = None
    context = {
        "conversation": conversation,
        "my_conversations": my_conversations,
    }
    return render(request, "a_inbox/inbox.html", context)

def search_users(request):
    letters = request.GET.get("search_user")
    if request.htmx:
        if len(letters) > 0:
            profiles = Profile.objects.filter(realname__icontains=letters).exclude(realname=request.user.profile.realname)
            users_id = profiles.values_list("user", flat=True)
            users = User.objects.filter(
                Q(username__icontains=letters) | Q(id__in=users_id)
            ).exclude(username=request.user.username)
            return render(request, "a_inbox/list_searchuser.html", {"users": users})
        else:
            return HttpResponse("")
    else:
        raise Http404("Page not found")
