from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ChatHistoryViewSet, DocumentViewSet, ChatHistoryDocumentView

router = DefaultRouter()
router.register(r'chathistory', ChatHistoryViewSet, basename='chathistory')

urlpatterns = [
    path('', include(router.urls)),
    path('chathistory/<uuid:pk>/documents/', ChatHistoryDocumentView.as_view(), name='chathistory-documents'),
]
