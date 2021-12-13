from django.contrib import admin
from .models import *
from import_export import resources
from .resources import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(CompanyInformation, BookAdmin)

class Mr(ImportExportModelAdmin):
    resource_class = MrResource

admin.site.register(Mrcreate, Mr)

class mrcover(ImportExportModelAdmin):
    resources_class=MCcovernot

admin.site.register(MCcovernoteM,mrcover)


admin.site.register(clinetM)



