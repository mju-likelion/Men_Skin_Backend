from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User, Board, Comment, Rank

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            username = validated_data['username'],
            age = validated_data['age'],
            skin_type = validated_data['skin_type']
        )
        return user
    class Meta:
        model = User
        fields = ['email','password','username','age','skin_type']
    
class BoardSerializer(serializers.ModelSerializer)  :
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Board
        fields = ['user','board_title','board_contents','board_type','board_create_at']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Comment
        fields = '__all__'

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = '__all__'
        