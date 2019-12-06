from django.shortcuts import render

# Create your views here.
def home(request):
    """A view that displays the home page"""
    return render(request, "home.html")