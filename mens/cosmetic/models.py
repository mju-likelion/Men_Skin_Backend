from django.db import models

class User_info(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.EmailField(max_length=30 ,verbose_name='사용자 이메일')
    user_pwd = models.CharField(max_length=255 ,verbose_name='사용자 비밀번호')
    user_nickname = models.CharField(max_length=30 ,verbose_name='사용자 닉네임')
    user_subscription = models.CharField(max_length=30, null=True ,verbose_name='사용자 가입경로')
    users_skin_type = models.CharField(max_length=30, null=True ,verbose_name='사용자 피부톤')

    class Meta:
        managed = False
        db_table = 'user_info'

class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User_info', on_delete=models.CASCADE, db_column='user_id')
    board_title = models.CharField(max_length=20 ,verbose_name='게시판 제목')
    board_contents = models.TextField(verbose_name='내용')
    board_views = models.IntegerField(default=0 ,verbose_name='조회수')
    board_create_at = models.DateTimeField(auto_now_add=True ,verbose_name='날짜')
    board_type = models.CharField(max_length=30 ,verbose_name='게시판 타입')
    board_like = models.IntegerField(default=0, verbose_name='추천수')

    def __str__(self):
        return self.board_title
    
    class Meta:
        managed = False
        db_table = 'board'
        ordering = ["-board_create_at"]

class Comment(models.Model):
    comment_int = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User_info', on_delete=models.CASCADE, db_column='user_id')
    board_id = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='board_id')
    comment_content = models.CharField(max_length=100 ,verbose_name='댓글 내용')
    comment_writer = models.CharField(max_length=30 ,verbose_name='댓글 작성자')
    board_create_at = models.DateTimeField(auto_now_add=True ,verbose_name='작성 날짜')

    class Meta:
        managed = False
        db_table = 'comment'
