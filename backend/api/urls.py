from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter

from .views import ChatHistoryViewSet, DocumentViewSet, ChatHistoryDocumentView, UserCreateAPIView

router = DefaultRouter()
router.register(r'chathistory', ChatHistoryViewSet, basename='chathistory')

urlpatterns = [
    path('', include(router.urls)),
    path('chathistory/<uuid:pk>/documents/', ChatHistoryDocumentView.as_view(), name='chathistory-documents'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('users/', UserCreateAPIView.as_view(), name='user-create'),
]
