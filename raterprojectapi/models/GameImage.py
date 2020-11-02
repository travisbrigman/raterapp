"""GameImage Model module"""
from django.db import models

class GameImage(models.Model):
    """GameImage database model"""
    user = models.ForeignKey("User",  on_delete=models.CASCADE, related_name="registrations")
    game = models.ForeignKey("Game",  on_delete=models.CASCADE)
    user_Image = models.ImageField