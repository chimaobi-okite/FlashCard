from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from flashcard_app.models import FlashCard

class FlashCardTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testcase', password='12345678')
        tokens = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(tokens.access_token))
        cards = [FlashCard(editor = self.user, question= 'new test question 1', answer = 'new test answer 1'),
                 FlashCard(editor = self.user, question= 'new test question 2', answer = 'new test answer 2'),
                 FlashCard(editor = self.user, question= 'new test question 3', answer = 'new test answer 3')]
        FlashCard.objects.bulk_create(cards)
        
        
    
    def test_get_cards(self):
        response = self.client.get(reverse('cards-list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 3)
        
    def test_create_card(self):
        data = {'editor':self.user,'question':"Newly created test question",
                'answer': 'answer to newly created test question'}
        response = self.client.post(reverse('cards-list'), data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data.get('editor'), 'testcase')
        
    def test_get_card(self):
        response = self.client.get(reverse('card-detail', args=(1,)))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('id'), 1)
        self.assertEquals(response.data.get('editor'), 'testcase')
        self.assertEquals(response.data.get('question'), 'new test question 1')
        
    def test_update_card(self):
        data = {'editor':self.user,'question':"Newly created test question 1 update",
                'answer': 'answer to newly created test question'}
        response = self.client.put(reverse('card-detail', args=(1,)), data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('id'), 1)
        self.assertEquals(response.data.get('editor'), 'testcase')
        self.assertEquals(response.data.get('question'), 'Newly created test question 1 update')
        
    def test_delete_card(self):
        response = self.client.delete(reverse('card-detail', args=(1,)))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        
class FlashCardNoAuthTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testcase', password='12345678')
        cards = [FlashCard(editor = self.user, question= 'new test question 1', answer = 'new test answer 1'),
                 FlashCard(editor = self.user, question= 'new test question 2', answer = 'new test answer 2'),
                 FlashCard(editor = self.user, question= 'new test question 3', answer = 'new test answer 3')]
        FlashCard.objects.bulk_create(cards)
        
        
    
    def test_get_cards(self):
        response = self.client.get(reverse('cards-list'))
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_create_card(self):
        data = {'editor':self.user,'question':"Newly created test question",
                'answer': 'answer to newly created test question'}
        response = self.client.post(reverse('cards-list'), data=data)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_get_card(self):
        response = self.client.get(reverse('card-detail', args=(1,)))
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_update_card(self):
        data = {'editor':self.user,'question':"Newly created test question 1 update",
                'answer': 'answer to newly created test question'}
        response = self.client.put(reverse('card-detail', args=(1,)), data=data)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
        
    def test_delete_card(self):
        response = self.client.delete(reverse('card-detail', args=(1,)))
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_not_card_owner_perm(self):
        user = User.objects.create_user(username='testcase2', password='12345678')
        tokens = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(tokens.access_token))
        response = self.client.get(reverse('card-detail', args=(1,)))
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        