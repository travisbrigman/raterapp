"""GameRating Model module"""
from django.db import models

class GameRating(models.Model):
    """GameRating database model"""
    user = models.ForeignKey("User",  on_delete=models.CASCADE, related_name="registrations")
    game = models.ForeignKey("Game",  on_delete=models.CASCADE)
    user_rating = models.IntegerField
    game_review = models.CharField(max_length=500)