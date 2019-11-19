from django.shortcuts import render

# Create your views here.
    
def work(request):
    """A view that displays the work page"""
    return render(request, "work.html")
    
def city(request):
    """A view that displays the city page"""
    return render(request, "city.html")
    
def protest_target(request):
    """A view that displays the protest_target page"""
    return render(request, "protest_target.html")
    
def censored_green(request):
    """A view that displays the censored_green page"""
    return render(request, "censored_green.html")
    
def lady_in_red(request):
    """A view that displays the lady_in_red page"""
    return render(request, "lady_in_red.html")