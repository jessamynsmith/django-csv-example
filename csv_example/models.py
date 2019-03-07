from django.db import models


class SoilSite(models.Model):
    ECOSYSTEM_CHOICES = (
        ('BorealForest', 'BorealForest'),
        ('Desert', 'Desert'),
        ('Meadow', 'Meadow'),
        ('N_Shrubland', 'N_Shrubland'),
        ('S_Shrubland', 'S_Shrubland'),
        ('TemperateAgriculture', 'TemperateAgriculture'),
        ('TemperateForest', 'TemperateForest'),
        ('TemperateGrassland', 'TemperateGrassland'),
        ('WetSedgeTundra', 'WetSedgeTundra'),
    )

    site_id = models.IntegerField(unique=True)
    warming_start = models.IntegerField()
    ecosystem_type = models.CharField(choices=ECOSYSTEM_CHOICES, max_length=15)
    sand_pct = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    silt_pct = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    clay_pct = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return 'Site {} ({})'.format(self.site_id, self.ecosystem_type)


class SoilMeasurement(models.Model):
    SEASON_CHOICES = (
        ('Growing', 'Growing'),
        ('NonGrowing', 'NonGrowing'),
        ('Shoulder', 'Shoulder'),
    )

    soil_site = models.ForeignKey(SoilSite, on_delete=models.CASCADE)
    year = models.IntegerField()
    doy = models.DecimalField(max_digits=4, decimal_places=1)
    season = models.CharField(choices=SEASON_CHOICES, max_length=10)
    treatment = models.CharField(max_length=2)
    n_replicates = models.IntegerField()
    r_avg_umol_m2_s = models.FloatField()
    resp_stdev = models.FloatField(blank=True, null=True)
    moist_avg_cm3_cm_3 = models.FloatField()
    moist_stdev = models.FloatField(blank=True, null=True)
    stemp_avg_c = models.FloatField()
    stemp_sd_c = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '{} ({} - {})'.format(self.soil_site, self.year, self.season)
