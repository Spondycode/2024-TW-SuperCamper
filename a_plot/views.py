from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'SuperCamper',
    }
    return render(request, "index.html", context)


