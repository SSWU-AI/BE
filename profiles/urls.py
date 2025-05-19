from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter()
# router.register(r'profiles', ProfileViewSet, basename='profile')  ← 생략해도 됨

urlpatterns = [
    path('profiles/me/', ProfileViewSet.as_view({
        'get': 'retrieve_own_profile',
        'put': 'update_own_profile',
        'patch': 'update_own_profile',
    }), name='profile-me'),
]
