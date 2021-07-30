from django.db import models

class Users(models.Model):
    id_int = models.AutoField(primary_key=True)
    users_email = models.EmailField(max_length=30, verbose_name='사용자 이메일')
    users_pwd = models.CharField(max_length=255, verbose_name='사용자 비밀번호')
    users_nickname = models.CharField(max_length=30, verbose_name='사용자 닉네임')
    users_subscription = models.CharField(max_length=30, null=True, verbose_name='사용자 가입경로')
    users_skin_type = models.CharField(max_length=30, null=True, verbose_name='사용자 피부톤')

class Board(models.Model):
    id_int=models.AutoField(primary_key=True)
    board_writer = models.CharField(max_length=20, verbose_name='작성자')
    board_title = models.CharField(max_length=20, verbose_name='게시판 제목')
    board_contents = models.TextField(verbose_name='내용')
    board_views = models.IntegerField(max_length=4, verbose_name='조회수')
    board_create_at = models.DateTimeField(auto_now_add=True, verbose_name='작성 날짜')
    board_type = models.CharField(max_length=30, verbose_name='게시판 타입')   
    board_like = models.IntegerField(max_Lenght=4, verbose_name='추천수') 

    def __str__(self):
        return self.board_title
    
    class Meta:
        ordering = ["board_create_at"]

class comment(models.Model):
    comment_int = models.AutoField(primary_key=True)
    id_int = models.AutoField(fk)
    user_nickname = models.CharField(fk,게시판 작성자)
    comment_content = models.CharField(100, verbose_name='댓글내용')
    comment_writer = models.CharField(30, verbose_name='댓글 작성자')
    board_create_at = models.DateTimeField(auto_now_add=True , verbose_name='작성 날짜')
