from django.contrib import admin
from .models import Profile,Transections
@admin.register(Transections)
class Transections(admin.ModelAdmin):
    list_display = ('source', 'receiver','created_datetime')
    ordering = ('-id',)

@admin.register(Profile)
class Transections(admin.ModelAdmin):
    list_display = ('account_number', 'balance','role','user')
    ordering = ('-id',)    


