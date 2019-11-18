from django.shortcuts import render

# Create your views here.
def news(request):
    """A view that displays the news page"""
    return render(request, "news.html")