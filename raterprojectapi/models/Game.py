"""Game Model module"""
from django.db import models

class Game(models.Model):
    """Game database model"""
    created_by = models.ForeignKey("User",  on_delete=models.CASCADE, related_name="registrations")
    release_year = models.IntegerField
    game_title = models.CharField(max_length=50)