import csv
from decimal import Decimal, InvalidOperation
import os
import re

from django.core.management.base import BaseCommand
from csv_example.models import SoilMeasurement


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
                    transformed_key = camel_case_to_snake_case(key)
                    transformed_key = transformed_key.replace('.', '_')

                    value = row[key]   
                    parsed_value = parse_value(transformed_key, value)

                    kwargs[transformed_key] = parsed_value

                SoilMeasurement.objects.create(**kwargs)
                """
                SiteID,Year,DOY,Season,Treatment,n_Replicates,R_avg_umol.m2.s,Resp_stdev,Moist_avg_cm3.cm.3,Moist_stdev,Stemp_Avg_C,Stemp_SD_C,WarmingStart,EcosystemType,sand_pct,silt_pct,clay_pct

                site_id = models.IntegerField()
    year = models.IntegerField()
    doy = models.DecimalField(max_digits=4, decimal_places=1)
    season = models.CharField(choices=SEASON_CHOICES, max_length=10)
    treatment = models.CharField(max_length=2)
    n_replicates = models.IntegerField()
    r_avg_umol_m2_s = models.FloatField()
    resp_stdev = models.FloatField()
    moist_avg_cm3_cm_3 = models.FloatField()
    moist_stdev = models.FloatField()
    stemp_avg_c = models.FloatField()
    warming_start = models.FloatField()
    ecosystem_type = models.CharField(choices=ECOSYSTEM_CHOICES, max_length=15)
    sand_pct = models.DecimalField(max_digits=3, decimal_places=1)
    silt_pct = models.DecimalField(max_digits=3, decimal_places=1)
    clay_pct"""
