from django.db import models
from django.contrib.auth.models import User

class FlashCard(models.Model):
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    
# class Answer(models.Model):
#     question = models.OneToOneField(Question, on_delete=models.CASCADE)
#     answer = models.CharField(max_length=500)
#     created = models.DateTimeField(auto_now=True, auto_now_add=False)
    
