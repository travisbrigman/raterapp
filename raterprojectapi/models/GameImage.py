"""GameImage Model module"""
from django.db import models
from django.contrib.auth.models import User

class GameImage(models.Model):
    """GameImage database model"""
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    game = models.ForeignKey("Game",  on_delete=models.CASCADE)
    user_Image = models.ImageField