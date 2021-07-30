from django.db import models


# Create your models here.
class Users(models.Model):
    id_int = models.AutoField(primary_key=True)
    users_email = models.CharField(max_length=30)
    users_pwd = models.CharField(max_length=255)
    users_nickname = models.CharField(max_length=30)
    users_subscription = models.CharField(max_length=30, null=True)
    users_skin_type = models.CharField(max_length=30, null=True)

class Board(models.Model):
    id_int=models.AutoField(primary_key=True)
    board_writer = models.CharField(max_length=20)
    board_title = models.CharField(max_length=20)
    board_contents = models.TextField()
    board_views = models.IntegerField(max_length=4)
    board_create_at = models.DateTimeField(auto_now_add=True)
    board_type = models.CharField(max_length=30)   
    board_like = models.IntegerField(4) 

class comment(models.Model):
    comment_int = models.AutoField(primary_key=True)
    id_int = models.AutoField()
    user_nickname = models.CharField(30)
    comment_content = models.CharField(100)
    comment_writer = models.CharField(30)
    board_create_at = models.DateTimeField(auto_now_add=True)