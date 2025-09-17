import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from api.models import Document

User = get_user_model()

class DocumentAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.document_url = reverse('api:document-list')

    def test_create_document(self):
        file_data = SimpleUploadedFile("test.txt", "Sample File Content".encode("utf-8"), content_type="application/pdf")
        data = {
            'name': 'Test Document',
            'file': file_data,
            'metadata': json.dumps({'author': 'John Doe'})
        }
        
        response = self.client.post(self.document_url, data, format='multipart')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Document.objects.count(), 1)
        self.assertEqual(Document.objects.first().user, self.user)

    def test_list_documents(self):
        Document.objects.create(user=self.user, name='Doc1', file='test_documents/sample1.txt')
        Document.objects.create(user=self.user, name='Doc2', file='test_documents/sample2.txt')
        response = self.client.get(self.document_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_document(self):
        doc = Document.objects.create(user=self.user, name='Doc1', file='test_documents/sample1.txt')
        url = reverse('api:document-detail', args=[doc.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['id']), str(doc.id))

    def test_delete_document(self):
        doc = Document.objects.create(user=self.user, name='Doc1', file='test_documents/sample1.txt')
        url = reverse('api:document-detail', args=[doc.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Document.objects.count(), 0)
