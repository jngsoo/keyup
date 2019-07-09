from django.contrib import admin
from .models import dummy_for_histo_and_cloud,TimeGraph,histo_2

from import_export.admin import ImportExportModelAdmin

class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.register(dummy_for_histo_and_cloud, ViewAdmin)
admin.site.register(TimeGraph)
admin.site.register(histo_2)


