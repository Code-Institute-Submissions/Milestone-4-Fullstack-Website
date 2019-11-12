from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")

def about(request):
    """A view that displays the about page"""
    return render(request, "about.html")
    
def news(request):
    """A view that displays the news page"""
    return render(request, "news.html")
    
def products(request):
    """A view that displays the products page"""
    return render(request, "products.html")
    
