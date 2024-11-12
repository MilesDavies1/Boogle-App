from rest_framework import serializers
from .models import SavedGame

class SavedGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedGame
        fields = ['id', 'player_name', 'words_found', 'remaining_time']
