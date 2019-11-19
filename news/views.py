from django.shortcuts import render

# Create your views here.
def news(request):
    """A view that displays the news page"""
    return render(request, "news.html")
    
def looking_for_work(request):
    """A view that displays the news page"""
    return render(request, "looking_for_work.html")
    
def project_complete(request):
    """A view that displays the project_complete page"""
    return render(request, "project_complete.html")
    
def opening(request):
    """A view that displays the opening page"""
    return render(request, "opening.html")