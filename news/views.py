from django.shortcuts import render

# Create your views here.
def news(request):
    """A view that displays the news page"""
    return render(request, "news.html")
    
def looking_for_work(request):
    """A view that displays the news page"""
    return render(request, "/news/looking_for_work.html/")