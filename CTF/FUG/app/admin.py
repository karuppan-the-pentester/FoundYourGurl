from django.contrib import admin
from .models import UsersDataBase,Notification

# Register your models here.

admin.site.register(UsersDataBase)
admin.site.register(Notification)