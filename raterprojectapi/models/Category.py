"""Category Model module"""
from django.db import models

class Category(models.Model):
    """Category database model"""
    label = models.models.CharField(max_length=50)