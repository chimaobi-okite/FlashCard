from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterTestCase(APITestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='example',
                                             email='example@example.com',
                                             password='example1234')
    
    def test_resgister(self):
        data = {'username':'testcase',
                'email':'testcase@examaple.com',
                'password':12345678,
                'confirm_password':12345678}
        response = self.client.post(reverse('register'),data=data,)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_register_password_mismatch(self):
        data = {'username':'testcase',
                'email':'testcase@examaple.com',
                'password':12345678,
                'confirm_password':1234567}
        response = self.client.post(reverse('register'),data=data,)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('error'), "There is a password mismatch, check both passwords")
    
    def test_existing_email(self):
        data = {'username':'testcase',
                'email':'example@example.com',
                'password':12345678,
                'confirm_password':12345678}
        response = self.client.post(reverse('register'),data=data,)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('error'), "Email already exists")
        
            
class TestJwtLogin(APITestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='example',
                                             email='example@example.com',
                                             password='example1234')
        
    def test_get_token(self):
        user = {'username':'example','password':'example1234'}
        response = self.client.post(reverse('token_obtain_pair'), data=user)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
    
    def test_get_refresh_token(self):
        refresh = RefreshToken.for_user(self.user)
        data = {'refresh':str(refresh)}
        response = self.client.post(reverse('token_refresh'), data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)  
        