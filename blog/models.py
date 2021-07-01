from djongo import models
from django.urls import reverse

# Create your models here.

class Posts(models.Model):
    id = models.ObjectIdField()
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    objects = models.DjongoManager()

    