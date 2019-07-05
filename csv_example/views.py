import csv
from django.http import HttpResponse

from csv_example import models


def get_field_names(model_class):
    fields = model_class._meta.get_fields()
    field_names = [field.name for field in fields]
    return field_names


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="soil_measurements.csv"'

    writer = csv.writer(response)
    field_names = get_field_names(models.SoilMeasurement)
    data = models.SoilMeasurement.objects.all().order_by('soil_site', 'year', 'doy').values(*field_names)
    writer.writerow(field_names)
    for row in data:
        row_data = [row[field_name] for field_name in field_names]
        writer.writerow(row_data)

    return response
