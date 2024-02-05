from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from hotel.models import Reservation

#the till for each reservation
class Till(models.Model):
    till_res = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return self.till_res.number


class Item_Till(models.Model):
    item_till = models.ForeignKey(Till, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    observation = models.CharField(max_length=30, null=True, blank=True, default='-')
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.item_till.till_res.number

class Payment(models.Model):
    payment_till = models.ForeignKey(Till, on_delete=models.CASCADE)
    pay_method = models.CharField(max_length=25,)
    amount = models.IntegerField()
    observation = models.CharField(max_length=30, null=True, blank=True, default='-')
    date = models.DateField(auto_now=True, blank=True)


@receiver(pre_save, sender=Payment)
def Negative_Amount(sender, instance, **kwargs):
   negative = instance.amount= -instance.amount
   int(negative)