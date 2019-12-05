from django.db import models


class NeedsForm(models.Model):
    """
    A single Needs Form
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return self.title