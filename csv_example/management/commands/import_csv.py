import csv
from decimal import Decimal, InvalidOperation
import os
import re

from django.core.management.base import BaseCommand
from csv_example import models as csv_example_models


def camel_case_to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    s2 = s2.replace('__', '_')
    return s2


def parse_value(key, value):
    # TODO would be nice to generate conversions from the model class
    mappings = {'site_id': int, 'year': int, 'doy': Decimal, 'season': str, 'treatment': str,
                'n_replicates': int, 'r_avg_umol_m2_s': float, 'resp_stdev': float,
                'moist_avg_cm3_cm_3': float, 'moist_stdev': float, 'stemp_avg_c': float,
                'stemp_sd_c': float, 'warming_start': int, 'ecosystem_type': str,
                'sand_pct': Decimal, 'silt_pct': Decimal, 'clay_pct': Decimal}
    try:
        parsed_value = mappings[key](value)
    except (InvalidOperation, ValueError):
        print('Could not convert value {} for key {}'.format(value, key))
        parsed_value = None
    return parsed_value


class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        file_path = os.path.join('data', 'Soil measurements from global warming experiments 1994-2014.csv')
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                kwargs = {}
                for key in row:
                    # Convert CSV column names to model field names
                    transformed_key = camel_case_to_snake_case(key)
                    transformed_key = transformed_key.replace('.', '_')

                    # Parse values into appropriate data type
                    value = row[key]
                    parsed_value = parse_value(transformed_key, value)

                    kwargs[transformed_key] = parsed_value

                # Split out site info from measurement info
                soil_site_keys = ['warming_start', 'ecosystem_type', 'sand_pct', 'silt_pct', 'clay_pct']
                soil_site_kwargs = {key: kwargs.pop(key) for key in soil_site_keys if key in kwargs}
                site_id = kwargs.pop('site_id')

                soil_site, created = csv_example_models.SoilSite.objects.get_or_create(
                    site_id=site_id, defaults=soil_site_kwargs)
                csv_example_models.SoilMeasurement.objects.create(**kwargs, soil_site=soil_site)
