from django.contrib import admin
from .models import UsersDataBase,Notification,Notes,gallery

# Register your models here.

admin.site.register(UsersDataBase)
admin.site.register(Notification)
admin.site.register(Notes)
admin.site.register(gallery)