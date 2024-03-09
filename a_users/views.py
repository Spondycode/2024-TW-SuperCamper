from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from a_plot.views import Plot
from .forms import ProfileAddForm
from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from allauth.account.utils import send_email_confirmation
from django.urls import reverse
from a_inbox.forms import InboxNewMessageForm
from django.core.paginator import Paginator




# View the profile of the logged in user and show plots created by the user
def profile_view(request):
    if request.user.is_authenticated:
        plots = Plot.objects.filter(owner=request.user)  # Fetch plots created by the logged in user
        profile = request.user.profile
        
        paginator = Paginator(plots, 24)  # Show 12 plots per page
        page = int(request.GET.get('page', 1))
        plots = paginator.page(page)
        
        context = {
            "plots": plots,
            "profile": profile,
            'page': page,
            
        }
        return render(request, "a_users/profile.html", context)
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")



# View the profile of an owner os a plot and show plots created by the user
def user_profile_view(request, username):
    try:
        user = User.objects.get(username=username)
        plots = Plot.objects.filter(owner=user)  # Fetch plots created by the logged in user
        profile = user.profile
        
        paginator = Paginator(plots, 24)  # Show 12 plots per page
        page = int(request.GET.get('page', 1))
        plots = paginator.page(page)
        
        new_message_form = InboxNewMessageForm() # form to send a message to the user from the profile page
        
        context = {
            "plots": plots,
            "profile": profile,
            "new_message_form": new_message_form,
            "page": page,
        }
        return render(request, "a_users/user_profile.html", context)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    except Plot.DoesNotExist:
        raise Http404("Plot does not exist")






@login_required
def profile_edit_view(request):
    form = ProfileAddForm(instance=request.user.profile)
    
    if request.method == "POST":
        form = ProfileAddForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
        
    if request.path == reverse("profile-onboarding"):
        template = 'a_users/profile_onboarding.html'
    else:
        template = 'a_users/profile_edit.html'
        
    return render(request, template, {"form": form})





    #create a view to create a profile
def profile_create_view(request):  # Create a new profile
    if request.user.is_authenticated:
        form = ProfileAddForm()
        context = {
            "form": form,
        }
        if request.method == "POST":
            form = ProfileAddForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                messages.success(request, "Profile created successfully")
                return redirect("profile")
        return render(request, "a_users/profile_create.html", context)
        
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")
    
    
# Delete a Profile
@login_required()
def profile_delete_view(request):
    user = request.user
    
    if request.method == "POST":
        # profile = request.user.profile
        logout(request)
        user.delete()
        messages.success(request, "Profile deleted successfully")
        return redirect("home")
            
    return render(request, "a_users/profile_delete.html")
    
    
def profile_delete_confirm_view(request):
    if request.user.is_authenticated:
        return render(request, "a_users/profile_delete_confirm.html")
        
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")


def profile_verify_email(request):
    send_email_confirmation(request, request.user)
    return redirect("profile")