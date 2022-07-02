from django.contrib import admin
from .models import MessageModel


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email']
    list_display_links = ['id', 'name']
