from django.db import models

from django.db import models

class SavedGame(models.Model):
    player_name = models.CharField(max_length=100)
    words_found = models.JSONField()  # Store found words as a list
    remaining_time = models.IntegerField()

    def __str__(self):
        return f"Game of {self.player_name}"
