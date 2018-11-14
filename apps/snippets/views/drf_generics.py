from django.contrib.auth.models import User
from rest_framework import generics, permissions

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserDetailSerializer

from ..permissions import IsOwnerOrReadOnly


# create 하기 전에 한번 살펴보기
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(onwer=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
