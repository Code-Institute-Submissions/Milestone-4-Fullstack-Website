from django.db import models


class NeedsFormModel(models.Model):
    """
    A single Needs Form
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __unicode__(self):
        return self.title