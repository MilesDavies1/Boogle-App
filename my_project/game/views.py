# game/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SavedGame
from .serializers import SavedGameSerializer

# Root view to handle the empty path
def home(request):
    return render(request, 'home.html')  # You can render a simple template here

class WordsView(APIView):
    def get(self, request):
        valid_words = ["CAT", "DOG", "BAT", "TIGER", "RAT", "BAG", "GAT", "TIER"]
        return Response(valid_words, status=status.HTTP_200_OK)

class SavedGameView(APIView):
    def get(self, request):
        saved_games = SavedGame.objects.all()
        serializer = SavedGameSerializer(saved_games, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SavedGameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
