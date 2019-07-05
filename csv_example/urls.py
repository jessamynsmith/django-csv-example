from django.urls import path

from csv_example import views


urlpatterns = [
    path('', views.SoilMeasurementFilterView.as_view(), name='soil_measurements'),
    path('download/', views.download_csv, name='download_csv'),
]
