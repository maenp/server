# from django.db import models

# class UserInfo(models.Model):
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=64)

#     def __str__(self):
#         return self.username

# """
# create table app1_userinfo(
#     id int primary key auto_increment,
#     username varchar(32),
#     password varchar(64)
# );

# 相当于执行了上面这条sql语句，创建了一张表，表名为app1_userinfo，表中有三个字段，分别为id、username、password。
# """