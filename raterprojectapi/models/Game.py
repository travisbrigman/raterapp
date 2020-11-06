"""Game Model module"""
from django.db import models
from django.contrib.auth.models import User
class Game(models.Model):
    """Game database model"""
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    release_year = models.IntegerField()
    game_title = models.CharField(max_length=75)
    designer = models.CharField(max_length=75)
    number_of_players = models.IntegerField()
    time_to_play = models.IntegerField()
    age_recommendation = models.CharField(max_length=5)
