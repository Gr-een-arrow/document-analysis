from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ChatHistoryViewSet, DocumentViewSet

router = DefaultRouter()
router.register(r'chathistory', ChatHistoryViewSet, basename='chathistory')
router.register(r'document', DocumentViewSet, basename='document')

urlpatterns = [
    path('', include(router.urls)),
]
