from djongo import models

# Create your models here.

class Posts(models.Model):
    id = models.ObjectIdField()
    author = models.JSONField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=False)
    objects = models.DjongoManager()
    