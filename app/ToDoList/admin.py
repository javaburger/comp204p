from django.contrib import admin

# Register your models here.

from .models import List, Item

class ListAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'title']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','list', 'content']

admin.site.register(List, ListAdmin)
admin.site.register(Item, ItemAdmin)