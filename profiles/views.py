from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(responses={200: ProfileSerializer})
    @action(detail=False, methods=['get'], url_path='me')
    def retrieve_own_profile(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    @swagger_auto_schema(
        method='put',
        request_body=ProfileSerializer,
        responses={200: ProfileSerializer, 400: '잘못된 요청'}
    )
    @swagger_auto_schema(
        method='patch',
        request_body=ProfileSerializer,
        responses={200: ProfileSerializer, 400: '잘못된 요청'}
    )
    @action(detail=False, methods=['put', 'patch'], url_path='me')
    def update_own_profile(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
