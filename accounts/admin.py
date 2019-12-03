from django.contrib import admin
from .models import Testimonial

class Testimonial(admin.ModelAdmin):
        model = Testimonial