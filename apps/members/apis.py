from django.contrib.auth import authenticate

from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.snippets.serializers import UserSerializer


class AuthTokenView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # __ 튜플에서 안쓰는 값들을 뺄 때
            token, __ = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
            }
            return Response(data)
        raise AuthenticationFailed()


class ProfileView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request):
        return Response(UserSerializer(request.user).data)
