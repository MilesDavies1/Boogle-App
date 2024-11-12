from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WordsView(APIView):
    def get(self, request):
        # Example: Predefined list of valid words
        valid_words = ["CAT", "DOG", "BAT", "TIGER", "RAT", "BAG", "GAT", "TIER"]
        return Response(valid_words, status=status.HTTP_200_OK)
