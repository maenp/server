from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class UserInfo(AbstractUser):
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    reqtime = models.DateTimeField(default=timezone.now, verbose_name='注册时间')

    # 修改反向访问器的related_name参数
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set'
    )

    class Meta:
        db_table = 'user'         # 指定数据表名
        verbose_name = '用户表'    # 在admin站点中显示的名称