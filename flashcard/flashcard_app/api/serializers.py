from rest_framework import serializers
from flashcard_app.models import FlashCard

class FlashCardSerializer(serializers.ModelSerializer):
    editor = serializers.StringRelatedField(read_only=True)
    # answer = serializers.CharField(source='answer.answer')
    
    class Meta:
        model = FlashCard
        fields = '__all__'
        
# class AnswerSerializer(serializers.ModelSerializer):
#     question = serializers.CharField(source='question.question')
    
#     class Meta:
#         model = Answer
#         fields = '__all__'