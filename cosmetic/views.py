from django.shortcuts import render
from .serializers import BoardSerializer, UserSerializer, CommentSerializer, RankSerializer
from .models import Board, User, Comment, Rank
from rest_framework import generics, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
class UserCreate(generics.CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class BoardViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class RankViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
