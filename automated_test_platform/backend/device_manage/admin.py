from django.contrib import admin

# Register your models here.

from .models import DeviceType

class ComputerAdmin(admin.ModelAdmin):
    """
    list
    """
    list_display = ('id', 'serial', 'ip', 'localIP', 'location', 'deviceModel')

class DeviceTypeAdmin(admin.ModelAdmin):
    """
    list
    """
    list_display = ( 'deviceType', 'deviceModel', 'remarks')
    list_filter = ('deviceType', 'remarks')
    search_fields = ['deviceType']

admin.site.register(DeviceType, DeviceTypeAdmin)

