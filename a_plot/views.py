from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Plot, Comment, Reply
# from .forms import PlotAddForm, PlotEditForm, RegisterForm, CommentCreateForm, ReplyCreateForm, PlotReportForm
from django.contrib import messages 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    plots = Plot.objects.all()
    context = {
        'title': 'SuperCamper',
        'plots': plots,
    }
    return render(request, "index.html", context)


