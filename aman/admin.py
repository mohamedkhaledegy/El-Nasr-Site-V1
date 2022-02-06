import site
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.site_header = "النصر"
admin.site.site_title = "النصر"

## Store
@admin.register(Store)
class StoreImportExport(ImportExportModelAdmin):
    pass
# Fix
class FixRequestAdmin(admin.ModelAdmin):
    list_display = ('store','short_desc', 'emergency_type','admen_aman')
    ## العواميد اللى بتظهر فى الادمين داشبورد 
admin.site.register(FixRequest, FixRequestAdmin)
 
@admin.register(Item)
class ItemImportExport(ImportExportModelAdmin):
    pass
admin.site.register(AdmenAman)
admin.site.register(Tags)


@admin.register(Visit)
class VisitImportExport(ImportExportModelAdmin):
    pass

admin.site.register(Profile)