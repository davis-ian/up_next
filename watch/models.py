from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    release = models.DateField(null=True)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title
