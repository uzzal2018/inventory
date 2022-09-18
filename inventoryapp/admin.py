from django.contrib import admin

# Register your models here.
from .models import Inventoryoff
#class TodoAdmin(admin.ModelAdmin):
 #   list_display = ('text', 'user')

admin.site.register(Inventoryoff)