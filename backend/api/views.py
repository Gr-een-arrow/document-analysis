from rest_framework import permissions, viewsets

from .models import ChatHistory, Document
from .serializers import ChatHistorySerializer, DocumentSerializer


class ChatHistoryViewSet(viewsets.ModelViewSet):
	serializer_class = ChatHistorySerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return ChatHistory.objects.filter(user=self.request.user)
	

class DocumentViewSet(viewsets.ModelViewSet):
	serializer_class = DocumentSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return Document.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)