from django.db import models

# Create your models here.

class Video(models.model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    notes = models.Charfield(blank=True, null=True)

    def __str__(self):
    # String displayed in the admin console or when printing a Video object
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Notes: {self.notes[:200]}'
