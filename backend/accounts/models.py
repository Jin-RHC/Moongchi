from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.
class User(AbstractUser):
    nickname_validator = UnicodeUsernameValidator()
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    nickname = models.CharField(
        default = 2,
        max_length=30,
        unique=True,
        help_text= '필수 항목이며 중복은 불가능합니다. 글자, 숫자, @/./+/-/_만 사용 가능합니다.',
        validators=[nickname_validator],
        error_messages={
            'unique': "이미 해당 별명을 가진 사용자가 존재합니다.",
        },
    )
    def __str__(self): 
        return f'{self.username}, {self.nickname}'