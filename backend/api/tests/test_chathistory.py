from api.models import ChatHistory, Document
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

class ChatHistoryAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.chathistory_url = reverse('api:chathistory-list')

    def test_create_chathistory(self):
        data = {'name': 'Test Chat'}
        response = self.client.post(self.chathistory_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatHistory.objects.count(), 1)
        self.assertEqual(ChatHistory.objects.first().user, self.user)

    def test_list_chathistories(self):
        ch = ChatHistory.objects.create(user=self.user, name='List Chat')
        response = self.client.get(self.chathistory_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_chathistory(self):
        ch = ChatHistory.objects.create(user=self.user, name='Retrieve Chat')
        url = reverse('api:chathistory-detail', args=[ch.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['id']), str(ch.id))
        self.assertIn('documents', response.data)

    def test_delete_chathistory(self):
        ch = ChatHistory.objects.create(user=self.user, name='Delete Chat')
        url = reverse('api:chathistory-detail', args=[ch.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ChatHistory.objects.count(), 0)
