from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *



# Register your models here.

admin.site.register(Profile)
admin.site.register(Tracker)

class Add_Excel_Admin(ImportExportModelAdmin):
    class meta:
        model = Add_Excel
        list_display = ['income','expenses','income_type']


admin.site.register(Add_Excel,Add_Excel_Admin)
