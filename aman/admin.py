import site
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Store)
class DeviceImportExport(ImportExportModelAdmin):
    pass


class FixRequestAdmin(admin.ModelAdmin):
    list_display = ('store','short_desc', 'emergency_type','admen_aman')
    ## العواميد اللى بتظهر فى الادمين داشبورد 

admin.site.register(FixRequest, FixRequestAdmin)


class SpareAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand')
    ## العواميد اللى بتظهر فى الادمين داشبورد 

admin.site.register(AdmenAman)
admin.site.register(Tags)