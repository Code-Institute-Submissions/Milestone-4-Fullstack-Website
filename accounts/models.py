from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name