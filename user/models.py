from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    # 0: 사용자, 1: 사장님, 2: 배달기사
    user_type = models.IntegerField()
