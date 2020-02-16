from django.db import models

# Create your models here.

class Forbidden(models.Model):
    word =  models.CharField(max_length = 255)
