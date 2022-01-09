from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    homepage = models.URLField()
    description = models.TextField()
    release_date = models.DateField()
    runtime = models.IntegerField()
    favorite = models.ManyToManyField(User, related_name='favorite')

    def __str__(self):
        return self.title

    