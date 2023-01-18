from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from flashcard_app.models import FlashCard
from flashcard_app.api.serializers import FlashCardSerializer
from flashcard_app.api.permissions import CardOwnerPermission


class CardsList(generics.ListCreateAPIView):
    # queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return FlashCard.objects.filter(editor=user)

    def perform_create(self, serializer):
        editor = self.request.user
        serializer.save(editor=editor)
            
class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    permission_classes = [IsAuthenticated,CardOwnerPermission]