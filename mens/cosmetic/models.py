from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
from django.conf import settings

class UserManager(BaseUserManager): 
    def _create_user(self, email, password, **extra_fields): 
        if not email : 
            # 이메일이 없다면 
            raise ValueError('이메일은 필수 요소입니다.') 
        if not password : 
            # # 패스워드가 없다면 
            raise ValueError('패스워드는 필수 요소입니다.') # 이메일 주소를 소문자로 변환하는 과정을 거친 뒤에 저장한다. 
        email = self.normalize_email(email) # 사용자 모델 객체를 생성한다. 
        user = self.model( 
            email = email 
            ) # 사용자 패스워드는 Django에서 제공해주는 해시화 과정(SHA 256)을 거쳐서 저장한다. 
            
        user.set_password(password) # 실제로 DB에 사용자 정보를 저장한다. 
        
        user.save(using=self._db) # 기본적으로 모든 사용자는 일반사용자 권한을 갖게된다. 

        return user # 일반 사용자 생성 

class User(AbstractBaseUser): 
    id = models.BigAutoField(primary_key=True) 
    email = models.EmailField(max_length=254, unique=True) # 이메일 주소 
    secret = models.UUIDField(default=uuid.uuid4) # 사용자 서명용 비밀키
    username = models.CharField(max_length=30 )
    subscription_path = models.CharField(max_length=30)
    skin_type = models.CharField(max_length=30)

    objects = UserManager() # 사용자 정보를 관리하는 클래스는 지정한다. 
    USERNAME_FIELD = 'email' # 사용자 이름으로 사용될 필드의 이름을 지정한다. # 사용자 PK 값을 가져오기위한 함수 
    REQUIRED_FIELDS = ['username']

    def get_id(self): 
        return self.id


class Board(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board_title = models.CharField(max_length=20)
    board_contents = models.TextField()
    board_views = models.IntegerField(default=0)
    board_create_at = models.DateTimeField(auto_now_add=True)
    board_type = models.CharField(max_length=30)
    board_like = models.IntegerField(default=0)

    def __str__(self):
        return self.board_title

    class Meta:
        managed = False
        db_table = 'board'
        ordering = ["-board_create_at"]
    

class comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=200)
    comment_writer = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        managed = False
        db_table = 'comment'
    