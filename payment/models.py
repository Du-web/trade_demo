from django.db import models

# Create your models here.


#   用户表， 存储用户id，用户名，用户邮箱，用户手机号
class User(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'user_db'


#   用户账户表，存储用户的账号，余额
class Accout(models.Model):
    account_num = models.CharField(max_length=50, blank=True, null=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'accout_db'


#   用户交易表，存储所有用户的每一笔交易信息，包括关联的账户，关联的用户，交易金额，交易日期，交易状态（交易中，交易成功，交易失败）
class Trade(models.Model):
    status_choices = (
        (0, '交易中'),
        (1, '交易成功'),
        (2, '交易失败'),
    )
    accout = models.ForeignKey(to=Accout, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    trade_amount = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    trade_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.SmallIntegerField(choices=status_choices, default=0, null=True)

    class Meta:
        db_table = 'trade_db'
