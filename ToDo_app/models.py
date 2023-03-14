from django.db import models

# Create your models here.

class Todo_model(models.Model):
    item = models.CharField(max_length=255)
    time  = models.DateTimeField(auto_now_add=True)
    