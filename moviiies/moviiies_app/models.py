from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name