from django.shortcuts import render

# Create your views here.
    
def work(request):
    """A view that displays the work page"""
    return render(request, "work.html")