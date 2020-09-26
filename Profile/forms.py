from django import forms
from . import models



class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = models.Transections
        fields =  "__all__"