from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from posts.models import Post
from posts.forms import BlogPostForm

    
def work(request):
    """A view that displays the work page"""
    posts = Post.objects.filter(published_date__lte=timezone.now()
    ).order_by('-published_date')
    return render(request, "work.html", {'posts': posts})
    
def storefront_ice(request):
    """A view that displays the storefront_ice page"""
    return render(request, "storefront_ice.html")     
    
def smoking_man_brown(request):
    """A view that displays the smoking_man_brown page"""
    return render(request, "smoking_man_brown.html")   
    
def car_lens_flare_blue(request):
    """A view that displays the car_lens_flare_blue page"""
    return render(request, "car_lens_flare_blue.html")   
    
def city(request):
    """A view that displays the city page"""
    return render(request, "city.html")
    
def house(request):
    """A view that displays the house page"""
    return render(request, "house.html")
    
def hood_grey(request):
    """A view that displays the hood_grey page"""
    return render(request, "hood_grey.html")
    
def protest_target(request):
    """A view that displays the protest_target page"""
    return render(request, "protest_target.html")
    
def censored_green(request):
    """A view that displays the censored_green page"""
    return render(request, "censored_green.html")
    
def girl_with_gun_red(request):
    """A view that displays the girl_with_gun_red page"""
    return render(request, "girl_with_gun_red.html")