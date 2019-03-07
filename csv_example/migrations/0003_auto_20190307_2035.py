# Generated by Django 2.1.7 on 2019-03-07 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csv_example', '0002_auto_20190307_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoilSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.IntegerField(unique=True)),
                ('warming_start', models.IntegerField()),
                ('ecosystem_type', models.CharField(choices=[('BorealForest', 'BorealForest'), ('Desert', 'Desert'), ('Meadow', 'Meadow'), ('N_Shrubland', 'N_Shrubland'), ('S_Shrubland', 'S_Shrubland'), ('TemperateAgriculture', 'TemperateAgriculture'), ('TemperateForest', 'TemperateForest'), ('TemperateGrassland', 'TemperateGrassland'), ('WetSedgeTundra', 'WetSedgeTundra')], max_length=15)),
                ('sand_pct', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('silt_pct', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('clay_pct', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='soilmeasurement',
            name='clay_pct',
        ),
        migrations.RemoveField(
            model_name='soilmeasurement',
            name='ecosystem_type',
        ),
        migrations.RemoveField(
            model_name='soilmeasurement',
            name='sand_pct',
        ),
        migrations.RemoveField(
            model_name='soilmeasurement',
            name='silt_pct',
        ),
        migrations.RemoveField(
            model_name='soilmeasurement',
            name='site_id',
        ),
        migrations.RemoveField(
            model_name='soilmeasurement',
            name='warming_start',
        ),
        migrations.AddField(
            model_name='soilmeasurement',
            name='soil_site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='csv_example.SoilSite'),
            preserve_default=False,
        ),
    ]