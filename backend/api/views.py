from rest_framework import permissions, viewsets

from .models import ChatHistory
from .serializers import ChatHistorySerializer


class ChatHistoryViewSet(viewsets.ModelViewSet):
	serializer_class = ChatHistorySerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return ChatHistory.objects.filter(user=self.request.user)