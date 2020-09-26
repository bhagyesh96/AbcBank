from django.db import models
import datetime
from django.contrib.auth.models import User


class Transections(models.Model):
    source = models.ForeignKey(User, related_name='source_user', blank=True, null=True, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver_user', blank=True, null=True, on_delete=models.CASCADE)
    amount = models.FloatField(null=True)
    created_datetime = models.DateTimeField(auto_now_add=True,null=True)
    updated_datetime = models.DateTimeField(auto_now=True,null=True) 

    def __str__(self):
        return str(self.source)

class Profile (models.Model):
    ROLE_CHOICE=[
        (0,'Customer'),
        (1,'Bank')
    ]
    account_number = models.IntegerField()
    balance = models.IntegerField()
    user = models.ForeignKey(User, related_name='satus_user', blank=True, null=True, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE,default=0)

    def __str__(self):
        return str(self.account_number)

