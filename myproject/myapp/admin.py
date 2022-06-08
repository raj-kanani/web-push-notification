from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'address']

@admin.register(BroadcastNotification)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'broadcast_on', 'sent']


@admin.register(Child)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'weight']
