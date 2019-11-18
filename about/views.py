from django.shortcuts import render

# Create your views here.
def about(request):
    """A view that displays the about page"""
    return render(request, "about.html")