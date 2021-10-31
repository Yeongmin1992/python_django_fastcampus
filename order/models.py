from django.db import models

class Shop(models.Model):
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=40)

class Menu(models.Model):
    # menu는 shop에 종속되어 있음으로 Shop의 id를 Foriegn key로 사용, 특정 id를 가진 shop이 사라지면 해당 shop에 종속된 메뉴도 cascade방식으로 함께 사라짐 
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)

class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered')
    address = models.CharField(max_length=40)
    estimated_time = models.IntegerField(default = -1)
    deliver_finish = models.BooleanField(default = 0)


class Orderfood(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)
