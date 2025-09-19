from rest_framework import permissions, serializers, viewsets
from rest_framework.generics import ListCreateAPIView

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

class ChatHistoryDocumentView(ListCreateAPIView):
	serializer_class = DocumentSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		chathistory_pk = self.kwargs["pk"]
		return Document.objects.filter(user=self.request.user, chathistory_id=chathistory_pk)

	def perform_create(self, serializer):
		chathistory_pk = self.kwargs["pk"]
		chathistory = ChatHistory.objects.filter(id=chathistory_pk, user=self.request.user).first()
		if not chathistory:
			raise serializers.ValidationError("ChatHistory not found or not owned by user.")
		serializer.save(user=self.request.user, chathistory=chathistory)