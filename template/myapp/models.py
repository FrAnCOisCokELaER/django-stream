from django.db import models

# Create your models here.
class myappModel(models.Model):
    message = models.CharField(max_length=240)
