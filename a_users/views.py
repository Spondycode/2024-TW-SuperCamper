from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from a_plot.views import Plot
from .forms import ProfileAddForm
from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404
from django.http import Http404
# from django.contrib.auth.models import User
from django.contrib.auth.models import User




# View the profile of the logged in user and show plots created by the user
def profile_view(request):
    if request.user.is_authenticated:
        plots = Plot.objects.filter(owner=request.user)  # Fetch plots created by the logged in user
        profile = request.user.profile  
        context = {
            "plots": plots,
            "profile": profile,
        }
        return render(request, "a_users/profile.html", context)
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")






    

# Edit the profile of the logged in user
@login_required()
def profile_edit_view(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        form = ProfileAddForm(instance=profile)
        context = {
            "form": form,
            "profile": profile,
        }
        if request.method == "POST":
            form = ProfileAddForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully")
                return redirect("profile")
        return render(request, "a_users/profile_edit.html", context)
        
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")
    
    
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
