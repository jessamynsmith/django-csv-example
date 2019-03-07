from django.contrib import admin

from csv_example import models


class SoilMeasurementAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'year', 'season', 'ecosystem_type')
    list_filter = ('year', 'ecosystem_type')
    search_fields = ('site_id',)


# Register your models here.
admin.site.register(models.SoilMeasurement, SoilMeasurementAdmin)
