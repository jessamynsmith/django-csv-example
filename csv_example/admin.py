import csv

from django.contrib import admin
from django.http import HttpResponse

from csv_example import models


# Code from http://books.agiliq.com/projects/django-admin-cookbook/en/latest/export.html
class ExportCsvMixin:
    """ Admin Mixin to export CSV"""
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class SoilMeasurementAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('site_id', 'year', 'season', 'ecosystem_type')
    list_filter = ('year', 'ecosystem_type')
    search_fields = ('site_id',)

    actions = ["export_as_csv"]


# Register your models here.
admin.site.register(models.SoilMeasurement, SoilMeasurementAdmin)
