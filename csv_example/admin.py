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


class SoilSiteAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'warming_start', 'ecosystem_type')
    list_filter = ('ecosystem_type',)
    search_fields = ('site_id',)

    fieldsets = (
        ('Site Information', {
            'fields': ('site_id', 'warming_start', 'ecosystem_type')
        }),
        ('Soil Information', {
            'fields': (('sand_pct', 'silt_pct', 'clay_pct'),),
        }),
    )

    class Media:
        css = {
            "screen": ("csv_example/css/admin.css",)
        }


class SoilMeasurementAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('soil_site', 'year', 'season')
    list_filter = ('year', 'soil_site__ecosystem_type')
    search_fields = ('soil_site__site_id',)

    actions = ["export_as_csv"]

    fieldsets = (
        ('Site Information', {
            'fields': ('soil_site',)
        }),
        ('Reading Information', {
            'fields': ('year', 'season', 'treatment')
        }),
        ('Readings', {
            'fields': (('doy', 'n_replicates'),
                       ('r_avg_umol_m2_s', 'resp_stdev'),
                       ('moist_avg_cm3_cm_3', 'moist_stdev'),
                       ('stemp_avg_c', 'stemp_sd_c')),
        }),
    )

    class Media:
        css = {
            "screen": ("csv_example/css/admin.css",)
        }


# Register your models here.
admin.site.register(models.SoilMeasurement, SoilMeasurementAdmin)
admin.site.register(models.SoilSite, SoilSiteAdmin)
